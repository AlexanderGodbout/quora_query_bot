import tensorflow as tf 
import tensorflow_datasets as tfds


print(tf.__version__)

msg1 = tf.constant('Hello, TensorFlow!')
msg2 = tf.constant('How are you!')
msg3 = msg1 + msg2 
tf.print(msg3)
print(msg3)


DATA_DIR = '/data'
NUM_STEPS = 1000  
MINIBATCH_SIZE = 100 

dataset = tfds.load(name="mnist", split=tfds.Split.TRAIN)

#x = tf.placeholder(tf.float32, [None, 784])
x = tf.random.normal(shape=(10, 784))
W = tf.Variable(tf.random.normal(shape=(784,10)), name = 'weight')
#W = tf.Variable(tf.zeros([784, 10]))
y_true = tf.random.normal(shape=(10,10))



@tf.function
def cost(): 
        y_pred = tf.matmul(x, W)
        #error = tf.reduce_mean(tf.square(y_pred))
        #error = tf.reduce_mean(tf.square(y_true - y_pred))
        #return error 

        cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
                logits=y_pred, labels=y_true))
        return cross_entropy 

optimizer = tf.optimizers.SGD(learning_rate = 0.5)
gd_step = optimizer.minimize(cost, var_list=[W])

correct_mask = tf.equal(tf.argmax(tf.matmul(x, W), 1), tf.argmax(y_true, 1))
print(y_true)
print(tf.argmax(y_true, 1))
accuracy = tf.reduce_mean(tf.cast(correct_mask, tf.float32))

print('correct mask')
print(correct_mask)

#for _ in range(NUM_STEPS):








