# -*- coding: utf-8 -*-

'''
By kyubyong park. kbpark.linguist@gmail.com.
https://www.github.com/kyubyong/tacotron
'''

from __future__ import print_function

from hyperparams import Hyperparams as hp
import tqdm
from data_load import load_data
import tensorflow as tf
from train import Graph
from utils import spectrogram2wav
from scipy.io.wavfile import write
import os
import numpy as np

import time

import collections
import threading


def synthesize():
    if not os.path.exists(hp.sampledir): os.mkdir(hp.sampledir)

    start = time.time()

    # Load graph
    g = Graph(mode="synthesize")
    print("Graph loaded")

    # Load data
    texts = load_data(mode="synthesize")

    print(texts.shape)

    time_time_1 = time.time()

    print("第一个时间点", time_time_1 - start)

    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess, tf.train.latest_checkpoint(hp.logdir))
        print("Restored!")

        print("第二个时间点", time.time() - start)

        # Feed Forward  这个很耗时间 ，
        ## mel
        y_hat = np.zeros((texts.shape[0], 200, hp.n_mels * hp.r), np.float32)  # hp.n_mels*hp.r

        print(y_hat.shape)  # 数据当前模型的数组

        print("第2.5 个时间点", time.time() - start)

        # todo 使用多线程加速处理速度

        thread_list = []

        for j in tqdm.tqdm(range(200)):
            t1 = threading.Thread(target=xiancheng, args=(g, j, sess, texts, y_hat,))
            t1.start()
            thread_list.append(t1)

        # for t in thread_list:
        #     t.setDaemon(True)
        #     t.start()

        for t in thread_list:
            t.join()

            # xiancheng(g, j, sess, texts, y_hat)
        ## mag

        print("第三个时间点", time.time() - start)

        print(y_hat)

        mags = sess.run(g.z_hat, {g.y_hat: y_hat})

        print("第四个时间点", time.time() - start)

        for i, mag in enumerate(mags):
            print("File {}.wav is being generated ...".format(i + 1))
            audio = spectrogram2wav(mag)
            write(os.path.join(hp.sampledir, '{}.wav'.format(i + 1)), hp.sr, audio)

            print("第五个时间点", time.time() - start)


def xiancheng(g, j, sess, texts, y_hat):
    _y_hat = sess.run(g.y_hat, {g.x: texts, g.y: y_hat})
    y_hat[:, j, :] = _y_hat[:, j, :]


###################################
#
# cldas_sum = collections.deque()
#
# class MyThread(threading.Thread):
#     def __init__(self, func, args, name=''):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.func = func
#         self.args = args
#         self.result = self.func(*self.args)
#
#     def get_result(self):
#         try:
#             return self.result
#         except Exception:
#             return None
#
# def loop(nloop):
#     # for j in t_list:
#     #     cldas_values = []
#     #     for k in range(4):
#     #         cldas_value = nloop + str(k)
#     #         cldas_values.append(cldas_value)
#     #     cldas_values.append(j)
#     #     cldas_values.append(nloop)
#     #     cldas_sum.append(cldas_values)
#     #     print(id(cldas_values))
#     # print(cldas_sum)
#     return cldas_sum
#
#         ###########################


synthesize()
#
# if __name__ == '__main__':
#     synthesize()
#     print("Done")
