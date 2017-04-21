import tensorflow as tf
import numpy as np

test=[[1,2,3],[4,5,6],[7,8,9]]
test2=[1,2,3,4]
print(tf.argmax(test,1))

sess=tf.Session()

result=sess.run(tf.argmax(test,1))
result2=sess.run(tf.argmax(test2,0))

print(result)

print(result2)
