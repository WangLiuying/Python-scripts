# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 17:32:12 2018

@author: Liuying Wang
"""

import input_data
mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)
#%%
#训练集x&y
mnist.train.images
mnist.train.labels

#%%占位符 参数变量设置 soft回归模型设置

import tensorflow as tf
xs = tf.placeholder('float',[None,784])
ys = tf.placeholder('float',[None,10])

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(xs,W)+b)

#%%交叉熵 
cross_entropy = -tf.reduce_sum(ys*tf.log(y))

#%%GD training
train = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#%%initialization
init = tf.global_variables_initializer()

#%%session run 与评估
sess = tf.Session()
sess.run(init)
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train, feed_dict={xs: batch_xs, ys: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(ys,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

print(sess.run(accuracy, feed_dict={xs: mnist.test.images, ys: mnist.test.labels}))
sess.close()


#%% interactive session的用法
"""
它能让你在运行图的时候，插入一些计算图，这些计算图是由某些操作(operations)构成的。
这对于工作在交互式环境中的人们来说非常便利，比如使用IPython。
如果你没有使用InteractiveSession，那么你需要在启动session之前构建整个计算图，
然后启动该计算图。
"""


import tensorflow as tf
sess = tf.InteractiveSession()

#%%输入设置

xs = tf.placeholder('float',[None,784])
ys = tf.placeholder('float',[None,10])


W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))


#%%interactive session 的图中计算

init = tf.global_variables_initializer()
sess.run(init)

#%% 类别预测和损失函数

y = tf.nn.softmax(tf.matmul(xs,W)+b)
cross_entropy = -tf.reduce_sum(ys*tf.log(y))

#%%训练
#op有run method

train = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

for i in range(1000):
    xs_batch, ys_batch = mnist.train.next_batch(100)
    train.run(feed_dict={xs:xs_batch,ys:ys_batch})
    
#%%评估
#tensor 有 eval method

correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(ys,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,'float'))

accuracy.eval(feed_dict={xs:mnist.test.images,ys:mnist.test.labels})

sess.close()
