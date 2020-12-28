# -*- coding: utf-8 -*-
# @File    : utils.py
# @Author  : AaronJny
# @Time    : 2020/03/13
# @Desc    :
import tensorflow as tf
import settings

# 我们准备使用经典网络在imagenet数据集上的与训练权重，所以归一化时也要使用imagenet的平均值和标准差
image_mean = tf.constant([0.485, 0.456, 0.406])
image_std = tf.constant([0.299, 0.224, 0.225])
width=settings.WIDTH
height=settings.HEIGHT

def normalization(x):
    """
    使用深度学习在进行图像分类或者对象检测时候，首先需要对图像做数据预处理
    对输入图片x进行归一化，返回归一化的值
    """
    return (x - image_mean) / image_std


def load_images(image_path):
    """
    加载并处理图片
    :param image_path:　图片路径
    :param width: 图片宽度
    :param height: 图片长度
    :return:　一个张量
    """
    # 加载文件
    x = tf.io.read_file(image_path)
    # 解码图片
    # 将图像使用JPEG的格式解码从而得到图像对应的三维矩阵。Tensorflow还提供了 tf.image.decode_png函数对png格式的图像进行编码。
    # 解码之后的结果为一个张量， 在使用他的取值之前需要明确调用运行的过程。
    x = tf.image.decode_jpeg(x, channels=3)
    # 修改图片大小
    x = tf.image.resize(x, [height, width])
    x = x / 255.
    # 归一化
    x = normalization(x)
    # tf.reshape(tensor, shape, name=None)
    # 函数的作用是将tensor重塑维度。其中shape为一个列表形式↓
    x = tf.reshape(x, [1, height, width, 3])    # 参数为x：张量，[1张图，高度，宽度，三维]
    # 返回结果
    return x


def save_image(image, filename):
    # seq[start:end:step]   从start开始到end结束，每隔step输出一次，省略为默认
    x = tf.reshape(image, image.shape[1:])  # shape[]:0-高度 1-宽度 2-通道数:彩色图是RGB格式，结果就为3.如果是灰度图，结果为1
    x = x * image_std + image_mean
    x = x * 255.
    # tf.cast(x, dtype, name=None)x：输入 dtype：转换目标类型.name：名称.返回：Tensor
    # 此函数是类型转换函数,将x的数据格式转化成dtype
    x = tf.cast(x, tf.int32)
    # 可以将一个张量中的数值限制在一个范围之内。
    # （可以避免一些运算错误:可以保证在进行log运算时，不会出现log0这样的错误或者大于1的概率）
    x = tf.clip_by_value(x, 0, 255)
    x = tf.cast(x, tf.uint8)    # 8位无符号整型
    # 将表示一张图像的三维矩阵重新按照jpeg格式编码并存入文件中。
    x = tf.image.encode_jpeg(x)
    tf.io.write_file(filename, x)