import tensorflow as tf

with tf.Session() as sess:
	new_saver = tf.train.import_meta_graph('my_test_model-1.meta')
	new_saver.restore(sess)
	print(sess.run('w1:0'))