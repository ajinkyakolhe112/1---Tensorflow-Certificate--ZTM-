
#%%
import datasets as huggingface_datasets

dataset_splits = huggingface_datasets.load_dataset("ajinkyakolhe112/pizza_vs_steak_classification")
dataset_training, dataset_validation = dataset_splits['train'], dataset_splits['test']

huggingface_datasets.get_dataset_split_names("ajinkyakolhe112/pizza_vs_steak_classification")
print( dataset_splits.shape, dataset_splits['train'].features )

#%%
import tensorflow as tf
def processing_func(examples_batch: dict):

    examples_batch['image_float32'] = []
    
    for image_PIL in examples_batch['image']:
        print(image_PIL)
        image_converted = tf.convert_to_tensor(image_PIL, dtype=tf.float32)
        examples_batch['image_float32'].append(image_converted)
    
    return examples_batch

dataset_training.set_transform(processing_func)
dataset_validation.set_transform(processing_func)

assert dataset_training[0]['image_float32'].shape.__len__() == 3 # FORMAT: Length = 3. [1_Height, 2_Width, 3_Channels]

#%%
# !IMP: Pytorch Dataloader is better. This DOESN"T WORK.
training_dataset_tf   = dataset_training.to_tf_dataset  (columns=["image_float32"], label_cols=["label"], batch_size=4, shuffle=True)
validation_dataset_tf = dataset_validation.to_tf_dataset(columns=["image_float32"], label_cols=["label"], batch_size=4, shuffle=True)

