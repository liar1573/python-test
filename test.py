#encoding='utf-8'
"""Python绘制语谱图"""
"""Python绘制时域波形"""

# 导入相应的包
import numpy, wave
import matplotlib.pyplot as plt
import numpy as np
import os

# filepath = 'G:/实战培训/Python生成语谱图/ReNoise/Prim10/'  # 添加路径
# 这里示例用的是绝对路径，看看能不能改成相对路径，把音频文件放在当前目录的子目录下
filepath = 'data/'
filename = os.listdir(filepath)  # 得到文件夹下的所有文件名

plt.figure()

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=0.5)


for i in range(len(filename)):
    f = wave.open(filepath + filename[i], 'rb')  # 调用wave模块中的open函数，打开语音文件。
    params = f.getparams()  # 得到语音参数
    nchannels, sampwidth, framerate, nframes = params[:4]  # nchannels:音频通道数，sampwidth:每个音频样本的字节数，framerate:采样率，nframes:音频采样点数
    strData = f.readframes(nframes)  # 读取音频，字符串格式
    wavaData = np.fromstring(strData, dtype=np.int16)  # 得到的数据是字符串，将字符串转为int型
    wavaData = wavaData * 1.0/max(abs(wavaData))  # wave幅值归一化
    wavaData = np.reshape(wavaData, [nframes, nchannels]).T  # .T 表示转置
    f.close()

    #（1）绘制语谱图
    # plt.figure()
    plt.subplot(2, 2, i + 1)
    plt.specgram(wavaData[0], Fs=framerate, scale_by_freq=True, sides='default')  # 绘制频谱
    plt.xlabel('Time(s)')
    plt.ylabel('Frequency')
    plt.title("Spectrogram_{}".format(i+1))
    # plt.savefig('G:/实战培训/Python生成语谱图/语谱图/{}.jpg'.format(filename[i][:-4]))
    plt.savefig('{}.png'.format(filename[i][:-4]))
    # ValueError: Format 'jpg' is not supported (supported formats: eps, pdf, pgf, png, ps, raw, rgba, svg, svgz) 现在的图片格式都不支持jpg了吗。。。
    # 尝试通过使用subplot函数把几张子图放在一张图中进行对比
    # plt.subplot(2, 2, i+1)
    #plt.show()

plt.show()

    #（2）绘制时域波形
    # time = np.arange(0, nframes) * (1.0 / framerate)
    # time = np.reshape(time, [nframes, 1]).T
    # plt.plot(time[0, :nframes], wavaData[0, :nframes], c="b")
    # plt.xlabel("time(seconds)")
    # plt.ylabel("amplitude")
    # plt.title("Original wave")
    # # plt.savefig('G:/实战培训/Python生成语谱图/语谱图/{}_.png'.format(filename[i][:-4]))  # 保存绘制的图形
    # plt.savefig('{}_.png'.format(filename[i][:-4]))
    # plt.show()

# Python绘制语谱图+时域波形