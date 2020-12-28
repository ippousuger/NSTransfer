# -*- coding: utf-8 -*-
# @File    : model.py
# @Author  : AaronJny
# @Time    : 2020/03/13
# @Desc    :
import typing
import tensorflow as tf
import settings


def get_vgg19_model(layers):
    """
    创建并初始化vgg19模型
    :return:
    """
    # 加载imagenet上预训练的vgg19
    vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
    '''
    include_top: 是否包含最后的3个全连接层
    weights： 定义为‘imagenet’，表示加载在imagenet数据库上训练的预训练权重，定义为None则不加载权重，参数随机初始化
    '''
    # 提取需要被用到的vgg的层的output
    # 在keras中,要想获取层的输出的各种信息,可以先获取层对象,再通过层对象的属性output或者output_shape获取层输出的其他特性.
    outputs = [vgg.get_layer(layer).output for layer in layers]
    model = tf.keras.Model([vgg.input, ], outputs)
    # 锁死权重，不进行训练
    model.trainable = False
    return model


# Keras Model Subclassing 子类方式自定义模型
# 使用这种方式构建模型，有个特点，就是在模型类中必须手工重载实现其call()方法
# 换句话来说，就是call()方法的参数training必须由自己来管理
class NeuralStyleTransferModel(tf.keras.Model):     # 括号内是父类名

    def __init__(self, content_layers: typing.Dict[str, float] = settings.CONTENT_LAYERS,
                 style_layers: typing.Dict[str, float] = settings.STYLE_LAYERS):
        # 在 __init__ 方法中创建层并将它们设置为类实例的属性
        # 此处添加初始化代码（包含call方法中会用到的层）
        # 函数参数中的冒号是类型限定，若不是要求类型会警告但不会报错。typing类型检查
        # Dict[str,float]字典中key是str类型，value是float类型
        super(NeuralStyleTransferModel, self).__init__()    # 为成功继承父类的属性需用super().__init__
        # 内容特征层字典 Dict(dictionary)[层名,加权系数]
        self.content_layers = content_layers
        # 风格特征层
        self.style_layers = style_layers
        # 提取需要用到的所有vgg层，.keys返回字典的键即是层名，并转换为list列表类型。+是连接
        layers = list(self.content_layers.keys()) + list(self.style_layers.keys())  # .keys返回字典的键。字典是[keys：values]
        # 创建layer_name到output索引的映射
        # dict()创建字典，可以传入元组列表创建字典，也可以通过zip得到元组列表后来创建字典
        # zip()可以将两个可迭代对象中的对应元素打包成一个个元组，然后返回这些元组组成的列表
        # 语义为，创建字典keys是layers中的元组，value是他们的索引
        self.outputs_index_map = dict(zip(layers, range(len(layers))))
        # 创建并初始化vgg网络
        self.vgg = get_vgg19_model(layers)

    # 此处添加模型调用的代码（处理输入并返回输出）
    def call(self, inputs, training=None, mask=None):   # 类中方法的参数必须有self，调用时不必为其赋值，为对象本身
        """
        前向传播//指对神经网络沿着输入层到输出层的顺序，依次计算并存储模型中的中间变量
        :return
            typing.Dict[str,typing.List[outputs,加权系数]]
        """
        outputs = self.vgg(inputs)  # 输出使用vgg(输入)
        # 分离内容特征层和风格特征层的输出，方便后续计算 typing.List[outputs,加权系数]
        content_outputs = []
        for layer, factor in self.content_layers.items():   # layer,factor为for循环中两个变量参数
            # items() 方法以列表返回可遍历的(键, 值) 元组数组。
            content_outputs.append((outputs[self.outputs_index_map[layer]][0], factor))
        style_outputs = []
        for layer, factor in self.style_layers.items():
            style_outputs.append((outputs[self.outputs_index_map[layer]][0], factor))
        # 以字典的形式返回输出，字典中的值是列表
        return {'content': content_outputs, 'style': style_outputs}
