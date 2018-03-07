# -*- coding: utf-8 -*-
"""
Tensor flow learning

Created on Sun Feb 11 16:35:07 2018

@author: Liuying Wang
"""
import tensorflow as tf

#%%示范session的用法

a = tf.constant([3,4,6])
b = tf.constant([1,2,3])
c = a * b

with tf.Session() as sess:
    print(sess.run(c))

#%%矩阵乘法
    
mat1 = tf.constant([[3.0,3.0]])
mat2 = tf.constant([[1.0],[2.0]])
product = tf.matmul(mat1,mat2)

with tf.Session() as sess:
    print(sess.run(product))
    
#%%counter示例

counter = tf.Variable(0,'counter')
one = tf.constant(1)
add = tf.add(counter,one)
update = tf.assign(counter,add)
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)
for i in range(3):
    result = sess.run(update)
    print(result)
sess.close()

#%%placeholder
    
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
multiple = tf.multiply(a,b)

sess = tf.Session()
result = sess.run(multiple,feed_dict= {a:[1],b:[3]})
print(result)
sess.close()
    

#%%拟合一元线性方程
import numpy as np
import tensorflow as tf

x_data = (np.random.rand(1000)).astype(np.float32)
y_data = x_data*0.1+0.3+np.random.rand(1000)
print(x_data,y_data)
#%%
weights = tf.Variable(tf.random_uniform([1],-0.2,0.2))
bias = tf.Variable(tf.zeros([1]))

y = weights * x_data + bias
loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

#%%
sess = tf.Session()
sess.run(init)
for i in range(200):
    sess.run(train)
    if i % 20 == 0:
        print(sess.run([weights,bias]))
sess.close()


#%% 单层神经网络 实现

import numpy as np
import tensorflow as tf

#false data
x_data = np.random.rand(1000)[:,np.newaxis]
y_data = x_data**2*0.5 + 0.3 + np.random.normal(0,0.5,x_data.shape)

#%%udf:add_layer

def add_layer(in_data,insize,outsize,activation=None):
    weights = tf.Variable(np.random.normal(size = (insize,outsize)))
    bias = tf.Variable(np.zeros(shape = (1,outsize)))
    zhat = tf.matmul(in_data,weights)+bias
    if activation is None:
        output = zhat
    else:
        output = activation(zhat)
    return output

#%% 1-hidden-layer nn

xs = tf.placeholder(tf.float64,shape = [None,1])
ys = tf.placeholder(tf.float64,shape = [None,1])

l1 = add_layer(xs,1,10,tf.nn.relu)
l2 = add_layer(l1,10,1)

loss = tf.reduce_mean(tf.square(ys - l2))
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
init = tf.global_variables_initializer()
#%%运行1000次
sess = tf.Session()
sess.run(init)
for i in range(1000):
    sess.run(train,feed_dict={xs:x_data,ys:y_data})
    if i % 100 == 0:
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
sess.close()


