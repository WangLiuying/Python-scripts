# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 19:44:41 2018

@author: Liuying Wang
"""
import tensorflow as tf
#%%
def weight_var(shape):
    weight = tf.truncated_normal(shape, stddev = 1.0, dtype = tf.float32)
    return tf.Variable(weight)

def bias_var(shape):
    bias = tf.constant(0,shape = shape, dtype = tf.float32)
    return tf.Variable(bias)

#%%
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides = [1,1,1,1], padding = 'SAME')

def max_pool(x):
    return tf.nn.max_pool(x, ksize = [1,2,2,1], strides = [1,2,2,1], padding = 'SAME')
    
#%%
import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
x = tf.placeholder(tf.float32, [None,784])
y = tf.placeholder(tf.float32, [None,10])

#%%第一层

x_image = tf.reshape(x,[-1,28,28,1])

W_conv1 = weight_var([5,5,1,32])
#[filter_height, filter_width, in_channels, out_channels]
b_conv1 = bias_var([32])
z_conv1 = conv2d(x_image, W_conv1)+b_conv1
a_conv1 = tf.nn.relu(z_conv1)

a_pool1 = max_pool(a_conv1)

#%%第二层

W_conv2 = weight_var([5,5,32,64])
b_conv2 = bias_var([64])
z_conv2 = conv2d(a_pool1, W_conv2)+b_conv2
a_conv2 = tf.nn.relu(z_conv2)

a_pool2 = max_pool(a_conv2)

#%%第三层

a_flat = tf.reshape(a_pool2,[-1,7*7*64])

W_fc3 = weight_var([7*7*64,1024])
b_fc3 = bias_var([1024])
z_fc3 = tf.matmul(a_flat, W_fc3)+b_fc3
a_fc3 = tf.nn.relu(z_fc3)

#%%dropout

keepprob = tf.placeholder(tf.float32)
a_fc3_drop = tf.nn.dropout(a_fc3, keepprob)

#%%softmax层

W_fc4 = weight_var([1024,10])
b_fc4 = bias_var([10])

z_fc4 = tf.matmul(a_fc3_drop, W_fc4)+b_fc4
yhat = tf.nn.softmax(z_fc4)

#%%训练

cross_entropy = -tf.reduce_sum(y*tf.log(yhat))
optimizer = tf.train.AdamOptimizer(0.0001)
train_step = optimizer.minimize(cross_entropy)
correct_predict = tf.equal(tf.argmax(y,1), tf.argmax(yhat,1))
accuracy = tf.reduce_mean(tf.cast(correct_predict, tf.float32))

initial = tf.global_variables_initializer()

sess = tf.Session()
sess.run(initial)
#%%
for itertime in range(10000):
    batch = mnist.train.next_batch(64)
    if itertime%100==0:
        training_accuracy = sess.run(accuracy, 
                                     feed_dict={x:batch[0], y:batch[1],keepprob:1.0})
        print('The training at step %d accuracy is %g' % (itertime,
                                                          training_accuracy))
    sess.run(train_step, feed_dict={x:batch[0], y:batch[1],keepprob:0.5})
print('The test accuracy is %g' %
      sess.run(accuracy, feed_dict={x:mnist.test.images, y:mnist.test.labels,keepprob:1.0}))