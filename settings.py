# 内容特征层及loss加权系数
CONTENT_LAYERS = {'block4_conv2': 0.5, 'block5_conv2': 0.5}
# 风格特征层及loss加权系数
STYLE_LAYERS = {'block1_conv1': 0.2, 'block2_conv1': 0.2, 'block3_conv1': 0.2, 'block4_conv1': 0.2,
                'block5_conv1': 0.2}
# 内容图片路径
CONTENT_IMAGE_PATH = r'J:\workspace\卒業デザイン\DeepLearningExamples-master\tf2-neural-style-transfer\images\content.jpg'
# 风格图片路径
STYLE_IMAGE_PATH = r'J:\workspace\卒業デザイン\DeepLearningExamples-master\tf2-neural-style-transfer\images\style.jpg'
# 生成图片的保存目录
OUTPUT_DIR = 'J:/workspace/卒業デザイン/DeepLearningExamples-master/tf2-neural-style-transfer/output'

# 内容loss总加权系数
CONTENT_LOSS_FACTOR = 1
# 风格loss总加权系数
STYLE_LOSS_FACTOR = 100

# 图片宽度
WIDTH = 100
# 图片高度
HEIGHT = 100
# 训练epoch数
EPOCHS = 20
# 每个epoch训练多少次
STEPS_PER_EPOCH = 100
# 学习率 作用：决定梯度下降最大误差值
LEARNING_RATE = 0.03

had_trained = 0
had_epoched = 0
timed = 0
