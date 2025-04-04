from datasets import load_dataset
from pathlib import Path

dataset = load_dataset(path="dvilasuero/finepersonas-v0.1-tiny", split="train")

Path("llamaindex/data").mkdir(parents=True, exist_ok=True)
for i, persona in enumerate(dataset):
    with open(Path("llamaindex/data") / f"persona_{i}.txt", "w") as f:
        f.write(persona["persona"])

