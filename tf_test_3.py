import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


model = keras.Sequential( 
    [ 
         keras.input(shape=(4,))
        ,layers.Dense(2, activation='relu', name="layer1")
        ,layers.Dense(3, activation='relu', name="layer2")
        ,layers.Dense(4, name="layer3")
    ]
)

x = tf.ones((4,4))
y = model(x)

print(model.layers[0].weights)
print(x)
print(y)
print(model.weights)
model.summary()