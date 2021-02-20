import os
import tensorflow as tf


# Turn off TensorFlow warning messages in program output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Define computational grph
X = tf.placeholder(tf.float32, nme='X')
Y = tf.placeholder(tf.float32, nme='Y')

addition = tf.add(X, Y, name='addition')

with tf.Session() as session:
    result = session.run(addition, feed_dict={X: [1,1,2], Y:[4,2,3]})
    print(result)