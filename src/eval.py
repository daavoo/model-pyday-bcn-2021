import json
import pickle
from pathlib import Path

import fire
from loguru import logger


@logger.catch(reraise=True)
def eval(input_folder, output_folder):
    with open(Path(input_folder) / "predictions.pkl", "rb") as f:
        predictions = pickle.load(f)

    output = []
    for scores, label in zip(predictions.predictions, predictions.label_ids):
        output.append(
            {
                "actual": int(label),
                "predicted": int(scores.argmax())
            }
        )
    Path(output_folder).mkdir(exist_ok=True, parents=True)
    with open(Path(output_folder) / "confusion.json", "w") as f:
        json.dump(output, f)

if __name__ == "__main__":
    fire.Fire(eval)
