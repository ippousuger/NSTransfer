# -*- coding: utf-8 -*-
# @File    : train.py
# @Author  : AaronJny
# @Time    : 2020/03/13
# @Desc    :
import os
import numpy as np
from tqdm import tqdm
import tensorflow as tf
from model import NeuralStyleTransferModel
import settings
import utils



def _compute_content_loss(noise_features, target_features):
    """
    计算指定层上两个特征之间的内容loss
    :param noise_features: 噪声图片在指定层的特征矩阵
    :param target_features: 内容图片在指定层的特征矩阵
    """
    # reduce_sum应该理解为压缩求和，用于降维
    content_loss = tf.reduce_sum(tf.square(noise_features - target_features))   # square计算平方。
    # 计算系数
    x = 2. * M * N
    content_loss = content_loss / x
    return content_loss


def compute_content_loss(noise_content_features):
    """
    计算当前图片的内容loss，即进行每层的权值计算并进行∑
    :param noise_content_features: 噪声图片的内容特征
    """
    # 初始化内容损失
    content_losses = []
    # 加权计算内容损失，用for循环是因为对矩阵中每个像素进行计算
    # zip()将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
    for (noise_feature, factor), (target_feature, _) in zip(noise_content_features, target_content_features):
        layer_content_loss = _compute_content_loss(noise_feature, target_feature)
        content_losses.append(layer_content_loss * factor)
    return tf.reduce_sum(content_losses)


def gram_matrix(feature):
    """
    计算给定特征的格拉姆矩阵
    """
    # 先交换维度，把channel维度提到最前面
    x = tf.transpose(feature, perm=[2, 0, 1])   # transpose(perm=[2,0,1]) 比如原数组是3*4*5会转换成5*3*4
    # reshape，压缩成2d
    x = tf.reshape(x, (x.shape[0], -1))     # reshape(x,(x.shape[0],-1)) -1代表系统自己计算得到参数 5*3*4的列表转换成5*12
    # 计算x和x的转置的乘积 @表示矩阵的乘积
    return x @ tf.transpose(x)      # x已转换为二阶矩阵，调用transpose直接求转置


def _compute_style_loss(noise_feature, target_feature):
    """
    计算指定层上两个特征之间的风格loss
    :param noise_feature: 噪声图片在指定层的特征
    :param target_feature: 风格图片在指定层的特征
    """
    noise_gram_matrix = gram_matrix(noise_feature)
    style_gram_matrix = gram_matrix(target_feature)
    style_loss = tf.reduce_sum(tf.square(noise_gram_matrix - style_gram_matrix))
    # 计算系数
    x = 4. * (M ** 2) * (N ** 2)
    return style_loss / x


def compute_style_loss(noise_style_features):
    """
    计算并返回图片的风格loss
    :param noise_style_features: 噪声图片的风格特征
    """
    style_losses = []
    for (noise_feature, factor), (target_feature, _) in zip(noise_style_features, target_style_features):
        layer_style_loss = _compute_style_loss(noise_feature, target_feature)
        style_losses.append(layer_style_loss * factor)
    return tf.reduce_sum(style_losses)


def total_loss(noise_features):
    """
    计算总损失
    :param noise_features: 噪声图片特征数据
    """
    content_loss = compute_content_loss(noise_features['content'])
    style_loss = compute_style_loss(noise_features['style'])
    return content_loss * settings.CONTENT_LOSS_FACTOR + style_loss * settings.STYLE_LOSS_FACTOR


# 使用tf.function加速训练
@tf.function
def train_one_step():
    """
    一次迭代过程
    """
    # 求loss
    with tf.GradientTape() as tape:
        noise_outputs = model(noise_image)      # 把噪声图像传入网络获得噪声特征矩阵
        loss = total_loss(noise_outputs)
    # 求梯度(gradient) 表示某一函数在该点处的方向导数沿着该方向取得最大值
    grad = tape.gradient(loss, noise_image)     # y:loss,x:noise_image
    # 梯度下降，更新噪声图片
    optimizer.apply_gradients([(grad, noise_image)])    # 将极值点作为输入参数对variable进行更新。
    return loss


def train():
    global content_image,style_image,M,N,noise_image,model,target_content_features,target_style_features,optimizer
    # 创建模型
    model = NeuralStyleTransferModel()      # 将定义好的网络结构封装成一个对象用于训练

    # 加载内容图片
    content_image = utils.load_images(settings.CONTENT_IMAGE_PATH)
    # 风格图片
    style_image = utils.load_images(settings.STYLE_IMAGE_PATH)

    # 计算出目标内容图片的内容特征备用
    # **注目**个人理解，model后的参数是call中的input，最后return出字典格式的特征
    target_content_features = model([content_image, ])['content']
    # 计算目标风格图片的风格特征
    target_style_features = model([style_image, ])['style']

    M = settings.HEIGHT * settings.WIDTH
    N = 3

    # 定义优化器，在tran_one_step中调用优化
    # 使用Adma优化器。动态梯度学习
    optimizer = tf.keras.optimizers.Adam(settings.LEARNING_RATE)

    # 基于内容图片随机生成一张噪声图片。np.random.uniform从[-0.2,0.2]中随机采样，第三个是输出样本数目
    noise_image = tf.Variable((content_image + np.random.uniform(-0.2, 0.2, (1, settings.HEIGHT, settings.WIDTH, 3))) / 2)

    # 创建保存生成图片的文件夹
    if not os.path.exists(settings.OUTPUT_DIR):
        os.mkdir(settings.OUTPUT_DIR)

    for epoch in range(settings.EPOCHS):
        # 使用tqdm提示训练进度
        with tqdm(total=settings.STEPS_PER_EPOCH, desc='Epoch {}/{}'.format(epoch + 1, settings.EPOCHS)) as pbar:
            # ↑↑动态监控迭代对象进度tqdm(total进度条总数，desc进度条名字，iterable迭代对象)，
            # '{}'.format()把()内参数放到{}内
            for step in range(settings.STEPS_PER_EPOCH):
                settings.had_trained += 1
                _loss = train_one_step()
                pbar.set_postfix({'loss': '%.4f' % float(_loss)})   # 在进度条后显示损失值
                pbar.update(1)
            utils.save_image(noise_image, 'output/{}.jpg'.format(epoch + 1))
        settings.had_epoched += 1