import codecs

import fire
from loguru import logger
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline


@logger.catch(reraise=True)
def inference(model_folder, title, body):

    model = AutoModelForSequenceClassification.from_pretrained(model_folder)
    tokenizer = AutoTokenizer.from_pretrained(model_folder)

    pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer)

    sequences = [codecs.unicode_escape_decode(f"{title}\n{body}")[0]]

    return pipeline(sequences)


if __name__ == "__main__":
    fire.Fire(inference)
