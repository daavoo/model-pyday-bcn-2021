import pickle
from pathlib import Path

import fire
import numpy as np
import yaml

from datasets import load_metric
from dvclive.huggingface import DvcLiveCallback
from loguru import logger
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset


metric = load_metric("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)


@logger.catch(reraise=True)
def train(input_folder, output_folder):
    with open("params.yaml") as f:
        params = yaml.safe_load(f)["train"]

    raw_datasets = load_dataset("json", 
        data_files={
            "train": str(Path(input_folder) / "train.json"), 
            "val": str(Path(input_folder) / "val.json")
        },
        field="data"
    )

    tokenizer = AutoTokenizer.from_pretrained(params["pretrained_model"])

    def tokenize_function(example):
        return tokenizer(example["text"], truncation=True, padding="max_length")

    tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)

    model = AutoModelForSequenceClassification.from_pretrained(
        params["pretrained_model"],
        num_labels=len(params["labels"]),
        id2label={n: x for n, x in enumerate(params["labels"])},
        label2id={x: n for n, x in enumerate(params["labels"])}
    )

    training_arguments = TrainingArguments(
        output_dir=output_folder,
        num_train_epochs=params["epochs"],
        per_device_train_batch_size=params["train_batch_size"],
        per_device_eval_batch_size=params["eval_batch_size"],
        evaluation_strategy="epoch",
        learning_rate=params["learning_rate"]
    )

    trainer = Trainer(
        model=model,
        args=training_arguments,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["train"],
        compute_metrics=compute_metrics,
        tokenizer=tokenizer
    )

    trainer.add_callback(DvcLiveCallback(model_file=params["output_folder"]))
    trainer.train()

    predictions = trainer.predict(tokenized_datasets["train"])

    with open(Path(output_folder) / "predictions.pkl", "wb") as f:
        pickle.dump(predictions, f)

if __name__ == "__main__":
    fire.Fire(train)
