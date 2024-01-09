from datasets import load_dataset

dataset = load_dataset("ajinkyakolhe112/pizza_vs_steak_classification")
dataset = dataset.with_format("tf")

print(dataset.shape, dataset.features)
"""
    `datasets.Dataset.filter()`
    `datasets.Dataset.to_tf_dataset`
"""

tf_train_data = dataset["train"].to_tf_dataset(
   shuffle=True,
   batch_size=16,
)
tf_valid_data = dataset["test"].to_tf_dataset(
   shuffle=True,
   batch_size=16,
)

