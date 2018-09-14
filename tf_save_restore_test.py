# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 13:09:45 2018

@author: Lin Daiwei
"""
import os
import tensorflow as tf
from baselines.ddpg.models import *
import numpy as np


def save(data):
    """
    Create a network and save it to SAVE_PATH
    """
    
    
    DATA_SIZE = 100
    SAVE_PATH = 'D:\\V-REP-simulator\V-REP-Simulator\save'
    EPOCHS = 50
    LEARNING_RATE = 0.01
    MODEL_NAME = 'test'
    
    
    tf.reset_default_graph()

    x = tf.placeholder(tf.float32, shape=[None, 2], name='inputs')
    y = tf.placeholder(tf.float32, shape=[None, 1], name='targets')
    
    net = tf.layers.dense(x, 16, activation=tf.nn.relu)
    net = tf.layers.dense(net, 16, activation=tf.nn.relu)
    pred = tf.layers.dense(net, 1, activation=tf.nn.sigmoid, name='prediction')
    
    loss = tf.reduce_mean(tf.squared_difference(y, pred), name='loss')
    train_step = tf.train.AdamOptimizer(0.01).minimize(loss)
    
    checkpoint = tf.train.latest_checkpoint("D:\\V-REP-simulator\V-REP-Simulator\save")
    should_train = checkpoint == None
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        sess.graph.finalize()
        if should_train:
            print("Training")
            saver = tf.train.Saver()
            for epoch in range(EPOCHS):
                _, curr_loss = sess.run([train_step, loss], feed_dict={x: data[0], y: data[1]})
                print('EPOCH = {}, LOSS = {:0.4f}'.format(epoch, curr_loss))
            path = saver.save(sess, SAVE_PATH + '\\' + MODEL_NAME + '.ckpt')
            print("saved at {}".format(path))
#        else:
#            print("Restoring")
#            graph = tf.get_default_graph()
#            saver = tf.train.import_meta_graph(checkpoint + '.meta')
#            saver.restore(sess, checkpoint)
#    
#            loss = graph.get_tensor_by_name('loss:0')
#    
#            test_loss = sess.run(loss, feed_dict={'inputs:0': test[0], 'targets:0': test[1]})
#            print(sess.run(pred, feed_dict={'inputs:0': np.random.rand(10,2)}))
#            print("TEST LOSS = {:0.4f}".format(test_loss))
    
    
#    # Create some variables.
#    v1 = tf.get_variable("v1", shape=[3], initializer = tf.zeros_initializer)
#    v2 = tf.get_variable("v2", shape=[5], initializer = tf.zeros_initializer)
#    
#    inc_v1 = v1.assign(v1+1)
#    dec_v2 = v2.assign(v2-1)
#    
#    # Add an op to initialize the variables.
#    init_op = tf.global_variables_initializer()
#    
#    # Add ops to save and restore all the variables.
#    saver = tf.train.Saver()
#    # Later, launch the model, initialize the variables, do some work, and save the
#    # variables to disk.
#    with tf.Session() as sess:
#      sess.run(init_op)
#      # Do some work with the model.
#      inc_v1.op.run()
#      dec_v2.op.run()
#      # Save the variables to disk.
#      save_path = saver.save(sess, "D:/V-REP-simulator/V-REP-Simulator/tmp/model.ckpt")
#      print("Model saved in path: %s" % save_path)

def restore(data):
    """
    Create a network and restore from previous trained models
    """
    tf.reset_default_graph()

    x = tf.placeholder(tf.float32, shape=[None, 2], name='inputs')
    y = tf.placeholder(tf.float32, shape=[None, 1], name='targets')
    
    net = tf.layers.dense(x, 16, activation=tf.nn.relu)
    net = tf.layers.dense(net, 16, activation=tf.nn.relu)
    pred = tf.layers.dense(net, 1, activation=tf.nn.sigmoid, name='prediction')
    
    loss = tf.reduce_mean(tf.squared_difference(y, pred), name='loss')
    train_step = tf.train.AdamOptimizer(0.01).minimize(loss)
#    checkpoint = tf.train.latest_checkpoint("D:\\V-REP-simulator\V-REP-Simulator\save")
    
    
#    # Create some variables.
#    v1 = tf.get_variable("v1", shape=[3], initializer = tf.zeros_initializer)
#    v2 = tf.get_variable("v2", shape=[5], initializer = tf.zeros_initializer)
#    init_op = tf.global_variables_initializer()
#    # Add ops to save and restore all the variables.
#    saver = tf.train.Saver()
#    
#    # Later, launch the model, use the saver to restore variables from disk, and
#    # do some work with the model.
    
    saver = tf.train.Saver()
    with tf.Session() as sess:
        
        sess.run(tf.global_variables_initializer())
        
        print("Before restore:")
        _, curr_loss = sess.run([train_step, loss], feed_dict={x: data[0], y: data[1]})
        print('EPOCH = {}, LOSS = {:0.4f}'.format(0, curr_loss))
        
        # Restore variables from disk
        path = os.path.join(os.path.abspath('..'),'V-REP-Simulator\save','test.ckpt')
        print(type(path))
        saver.restore(sess, path)
        print("Model restored.")
        _, curr_loss = sess.run([train_step, loss], feed_dict={x: data[0], y: data[1]})
        print('EPOCH = {}, LOSS = {:0.4f}'.format(0, curr_loss))

        
if __name__ == '__main__':
    tf.reset_default_graph()
    DATA_SIZE = 100
    data = (np.random.rand(DATA_SIZE, 2), np.random.rand(DATA_SIZE, 1))
    
    
    save(data)
    restore(data)