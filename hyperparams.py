# -*- coding: utf-8 -*-

## 这个是配置文件的放置目录

'''
By kyubyong park. kbpark.linguist@gmail.com. 
https://www.github.com/kyubyong/tacotron
'''


class Hyperparams:
    '''Hyper parameters'''

    # pipeline
    prepro = False  # if True, run `python prepro.py` first before running `python train.py`.

    vocab = "PE abcdefghijklmnopqrstuvwxyz'.?"  # P: Padding E: End of Sentence

    # data
    data = "/data/LJSpeech-1.1"
    # data = "/data/private/voice/nick"
    test_data = 'harvard_sentences.txt'
    max_duration = 10.0

    # signal processing
    # 信号处理时候的参数
    sr = 22050  # Sample rate.  频率
    n_fft = 2048  # fft points (samples) 采样个数
    frame_shift = 0.0125  # seconds
    frame_length = 0.05  # seconds
    hop_length = int(sr * frame_shift)  # samples.
    win_length = int(sr * frame_length)  # samples.
    n_mels = 80  # Number of Mel banks to generate
    power = 1.2  # Exponent for amplifying the predicted magnitude
    n_iter = 50  # Number of inversion iterations
    preemphasis = .97  # or None  预加重系数
    max_db = 100  # 声音最大分贝数
    ref_db = 20   # 相对分贝数

    # model
    embed_size = 256  # alias = E
    encoder_num_banks = 16
    decoder_num_banks = 8
    num_highwaynet_blocks = 4
    r = 5  # Reduction factor. Paper => 2, 3, 5  减少因子
    dropout_rate = .5    #

    # training scheme
    lr = 0.001  # Initial learning rate.
    logdir = "models_pre/LJ"   # 需要修改的文件地址 这个放置的是模型的存放地址
    sampledir = 'samples'  # 合成语音的文件地址
    batch_size = 32        # 如果是训练，样本的大小
