import os
import tensorflow as tf


# Turn off TensorFlow warning messages in program output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Define computational grph
X = [1,1,2]
Y = [4,2,3]

addition = tf.add(X, Y)

print(addition)