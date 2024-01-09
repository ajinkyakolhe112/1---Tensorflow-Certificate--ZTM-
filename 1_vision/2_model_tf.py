
#%%
import keras

"""
3 Ways of Creating Keras Model
    1. Sequential doesn't allow debugging & internal layer output. This format does.
    2. Functional API can't be debugged. 
    3. Overriding keras.model is **BEST**. Easy to debug when needed.
"""

class BaselineModel (keras.Model):
    def __init__(self, num_classes=1000):
        super().__init__()
        self.model = keras.models.Sequential([
            keras.layers.Conv2D        (filters= 10, kernel_size=(3,3), activation="relu", input_shape=(224, 224, 3)), 
            keras.layers.Conv2D        (filters= 10, kernel_size=(3,3), activation="relu"),
            keras.layers.MaxPool2D     (pool_size=(2,2), padding="valid"),

            keras.layers.Conv2D        (filters= 10, kernel_size=(3,3), activation="relu"),
            keras.layers.Conv2D        (filters= 10, kernel_size=(3,3), activation="relu"), 
            keras.layers.MaxPool2D     (pool_size=(2,2)),
            
            keras.layers.Flatten(),
            keras.layers.Dense         (units= 1) # !IMP: NO ACTIVATION. Logits is pre-activation function.
        ])

        self.layers_list = self.model.layers # !IMP: model.layers gives you list of all the layers. 

    def call(self, input_batch):
        # !IMP: LOGITS = pre activation function result. 
        output_logits       = self.model(input_batch)
        output_activations  = keras.activation.sigmoid(output_logits)

        try: # Code Block for debugging
            prev_output = input_batch
            for current_layer in self.layers_list:
                intermediate_output      = current_layer(prev_output)
                prev_output = intermediate_output
            
            assert output_logits == prev_output
        except:
            pass

        return output_logits                                 # type:ignore
    
model = BaselineModel()
# Compile the model
model.compile(
    loss="binary_crossentropy",
    optimizer=keras.optimizers.Adam(),
    metrics=["accuracy"])

