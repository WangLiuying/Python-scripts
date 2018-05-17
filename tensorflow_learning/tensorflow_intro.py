# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:15:47 2017

@author: Liuying Wang

此脚本为自学tensorflow，内容来自中文社区官方文档
"""

import tensorflow as tf
import numpy as np

# 使用 NumPy 生成假数据(phony data), 总共 100 个点.
x_data = np.float32(np.random.rand(2, 100)) # 随机输入
y_data = np.dot([0.100, 0.200], x_data) + 0.300

# 构造一个线性模型
# 
b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(W, x_data) + b

# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化变量
init = tf.initialize_all_variables()

# 启动图 (graph)
sess = tf.Session()
sess.run(init)

# 拟合平面
for step in range(0, 201):
    sess.run(train)
    if step % 20 == 0:
        print (step, sess.run(W), sess.run(b))

# 得到最佳拟合结果 W: [[0.100  0.200]], b: [0.300]
        
#%%
hello = tf.constant('Hello Tensorflow!')
sess = tf.Session()
print(sess.run(hello))

#%%
a = tf.constant(32)
b = tf.constant(20)
sess.run(a+b)

#%%
import tensorflow as tf

#%%基本步骤

##构建图
matrix1 = tf.constant([[3.,3.]])##1x2矩阵

matrix2 = tf.constant([[2.],[2.]])##2x1矩阵

product = tf.matmul(matrix1, matrix2)

##启动会话
sess = tf.Session()

result = sess.run(product)##自动触发关联op的计算、传输

print(result)

##关闭会话释放资源
sess.close()

#%%使用with 可以更加智能地开启、关闭sess

with tf.Session() as sess:
    result = sess.run(product)
    print(result)
    
#%%指派CPU

with tf.Session() as sess:
    with tf.device('/cpu:0'):
        matrix1 = tf.constant([[3.,3.]])
        matrix2 = tf.constant([[2.],[2.]])
        product = tf.matmul(matrix1,matrix2)
        print(sess.run(product))
    
#%%使用交互式的tensorflow会话
        
sess = tf.InteractiveSession()

x = tf.Variable([1.0,2.0])
a = tf.constant([3.0,3.0])

x.initializer.run()

sub = x - a
sub.eval()

print(sub.eval())


#%%变量的用法
# 创建一个变量, 初始化为标量 0.
state = tf.Variable(0, name="counter")

# 创建一个 op, 其作用是使 state 增加 1

one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# 启动图后, 变量必须先经过`初始化` (init) op 初始化,
# 首先必须增加一个`初始化` op 到图中.
init_op = tf.initialize_all_variables()

# 启动图, 运行 op
with tf.Session() as sess:
  # 运行 'init' op
  sess.run(init_op)
  # 打印 'state' 的初始值
  print(sess.run(state))
  # 运行 op, 更新 'state', 并打印 'state'
  for _ in range(3):#更新了三次
    sess.run(update)
    print(sess.run(state))
    
#%%fetch操作：使用run
    #如上文中各处sess.run
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
intermed = tf.add(input2, input3)
mul = tf.multiply(input1, intermed)

with tf.Session() as sess:
  result = sess.run([mul, intermed])
  print(result)
    
#%%feed操作
    
import tensorflow as tf
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:
  print(sess.run([output], feed_dict={input1:[8.], input2:[2.]}))