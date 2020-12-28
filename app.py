import train
import settings,utils
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import threading
import os
import time

def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


def get_path():
    file_path = filedialog.askopenfilename()
    return file_path


def show_jpg():
    global suit_content, content_path,content_size, photo, imglabel
    settings.CONTENT_IMAGE_PATH = get_path()
    content_path = settings.CONTENT_IMAGE_PATH
    img = Image.open(content_path)  # 打开图片
    img1 = img.resize((int(img.size[0] * 500 / img.size[1]), 500), Image.ANTIALIAS)
    content_size = img.size
    settings.HEIGHT = content_size[1]  # 传递输出尺寸给settings
    height.delete(0, 10)
    height.insert(0,settings.HEIGHT)
    settings.WIDTH = content_size[0]
    width.delete(0,10)
    width.insert(0,settings.WIDTH)
    suit_content = ImageTk.PhotoImage(img1)  # 用PIL模块的PhotoImage打开
    imglabel.grid_forget()  # 隐藏窗口本身的画板
    imglabel = tk.Label(root, image=suit_content, width=510, height=600, bg='AntiqueWhite')
    # label中图像参数必须是全局变量
    imglabel.grid(column=0, row=1, rowspan=30, sticky='w')      # column是列，row是行，rowspan代表占用多少行
    label = tk.Label(text=('内容图片路径:', content_path), wraplength=400)  # 打印文件的路径,wraplength单行长度
    label.grid(column=0, row=31)


def show_style():
    global style_img, style_path, imglabel1
    settings.STYLE_IMAGE_PATH = get_path()
    style_path = settings.STYLE_IMAGE_PATH
    img = Image.open(style_path)  # 打开图片
    img1 = img.resize((int(img.size[0] * 500 / img.size[1]), 500), Image.ANTIALIAS)
    style_img = ImageTk.PhotoImage(img1)  # 用PIL模块的PhotoImage打开
    imglabel1.grid_forget()
    imglabel1 = tk.Label(root, image=style_img, width=510, height=600, bg='AntiqueWhite')  # label中图像参数必须是全局变量
    imglabel1.grid(column=1, row=1, rowspan=30, sticky='W')
    label = tk.Label(text=('风格图片:', style_path), wraplength=400)  # 打印文件的路径
    label.grid(column=1, row=31)


def fuse():
    settings.EPOCHS = int((int(times.get())/100))   # 获取文本框内训练次数传给settings
    settings.WIDTH = int(width.get())
    utils.width = int(width.get())
    settings.HEIGHT = int(height.get())
    utils.height = int(height.get())
    thread_it(train.train)
    os.startfile(settings.OUTPUT_DIR)      # 打开输出文件夹


def output_path():
    settings.OUTPUT_DIR = filedialog.askdirectory()
    out_path.delete(0, 100)
    out_path.insert(index=0, string=settings.OUTPUT_DIR)


def update(idx):    # 更新gif显示
    frame = frames[idx]
    idx += 1
    decolabel.configure(image=frame)
    root.after(200, update, idx%numIdx)


def update_progress_bar():
    while settings.had_trained<=(100*settings.EPOCHS):
        green_length = int(sum_length * (settings.had_trained % 100) / 100)  # 绿条长度
        canvas_progress_bar.coords(canvas_shape, (0, 0, green_length, 25))  # 更新两个坐标给shape
        canvas_progress_bar.itemconfig(canvas_text, text='当前第 %02d 轮(100次一轮)' % (settings.had_epoched + 1))
        var_progress_bar_percent.set('%0.2f  %%' % (settings.had_trained % 100))        # %表示格式化输出
        time.sleep(1)
    canvas_progress_bar.itemconfig(canvas_text, text='训练结束')
    canvas_progress_bar.coords(canvas_shape, (0, 0, 300, 25))  # 更新两个坐标给shape


def update_progress_bar_sum():
    while settings.had_epoched < settings.EPOCHS:
        settings.timed += 1
        hour = int(settings.timed / 3600)
        minute = int(settings.timed / 60) - hour * 60
        second = settings.timed % 60
        green_length = int(sum_length * settings.had_epoched / settings.EPOCHS)  # 绿条长度
        canvas_progress_bar_sum.coords(canvas_shape, (0, 0, green_length, 25))  # 更新两个坐标给shape
        canvas_progress_bar_sum.itemconfig(canvas_text, text='%02d:%02d:%02d' % (hour, minute, second))
        var_progress_bar_percent_sum.set('%0.2f  %%' % (settings.had_epoched*100/settings.EPOCHS))
        time.sleep(1)
    canvas_progress_bar_sum.coords(canvas_shape, (0, 0, 300, 25))  # 更新两个坐标给shape
    var_progress_bar_percent_sum.set('100.00%')

def run():
    th = threading.Thread(target=fuse)
    th.setDaemon(True)
    th.start()
    th = threading.Thread(target=update_progress_bar)
    th.setDaemon(True)
    th.start()
    th_sum = threading.Thread(target=update_progress_bar_sum)
    th_sum.setDaemon(True)
    th_sum.start()


global imglabel, imglabel1
imglabel = None
content_size = None
style_path = None
content_path = None
root = tk.Tk()
root.state("zoomed")
root.iconbitmap(r"C:\Users\王浩华\Desktop\favicon.ico")

addr = tk.StringVar(value='2000')
defalut_path = tk.StringVar(value= settings.OUTPUT_DIR)
times = tk.Entry(root, textvariable=addr, width=6)
out_path = tk.Entry(root, textvariable=defalut_path, width=35)
width = tk.Entry(root, width=6)
height = tk.Entry(root, width=6)
content = tk.Button(root, text='原始图像', command=show_jpg)  # command 点击事件命令没有括号
style = tk.Button(root, text='目标风格', command=show_style)  # 要传参用command=lambda :
output = tk.Button(root, text='选择输出路径', command=output_path, width=10, height=2)    # 要传参用command=lambda :
imglabel = tk.Label(root, height=40, width=70, bg='AntiqueWhite')
imglabel1 = tk.Label(root, height=40, width=70, bg='AntiqueWhite')
timeslabel = tk.Label(root, text='请输入想要训练的次数(100的倍数)：')
trainbar_label = tk.Label(root, text='当前轮次进度:')
sumbar_label = tk.Label(root, text='总训练进度:')
widlabel = tk.Label(root, text='图像宽度:')
heilabel = tk.Label(root, text='图像高度:')
content.grid(column=0, row=0, sticky='w')
imglabel.grid(column=0, row=1, rowspan=30, sticky='n')
imglabel1.grid(column=1, row=1, rowspan=30, sticky='n')
timeslabel.grid(column=2, row=0, sticky='n', columnspan=3)
out_path.grid(column=2, row=2, sticky='n', columnspan=4)
output.grid(column=2, row=3, sticky='n', columnspan=4)
width.grid(column=3, row=4, sticky='n')
height.grid(column=5, row=4, sticky='n')
widlabel.grid(column=2, row=4, sticky='n')
heilabel.grid(column=4, row=4, sticky='n')

numIdx = 6     # gif的帧数
frames = [tk.PhotoImage(file=r'C:\Users\王浩华\Desktop\20150920130356_PAriW.gif', format='gif -index %i' %(i))
          for i in range(numIdx)]
decolabel = tk.Label(root)
decolabel.grid(column=2, row=6, sticky='w', columnspan=4, rowspan=15)
root.after(0, update, 0)

style.grid(column=1, row=0, sticky='w')
times.grid(column=5, row=0, sticky='n')


# 进度条
sum_length = 300
canvas_progress_bar = tk.Canvas(root, width=sum_length, height=23,bg='#7A7A7A')
canvas_shape = canvas_progress_bar.create_rectangle(0, 0, 0, 25, fill='green')  # 前两参数是左上角坐标，后两参数是右下角坐标
canvas_text = canvas_progress_bar.create_text(150, 13, anchor=tk.CENTER)    # text坐标取画布的横纵各一半，northwest=NW
canvas_progress_bar.itemconfig(canvas_text, text='')    # 修改图形属性，第一个参数为图形的ID，后边为想修改的参数；
var_progress_bar_percent = tk.StringVar()
var_progress_bar_percent.set('00.00  %')    # 实时更新
label_progress_bar_percent = tk.Label(root, textvariable=var_progress_bar_percent)
canvas_progress_bar.grid(column=3, row=22, columnspan=10, sticky='w')
trainbar_label.grid(column=2, row=22)
label_progress_bar_percent.grid(column=13, row=22)
# 总进度条
sum_length = 300
canvas_progress_bar_sum = tk.Canvas(root, width=sum_length, height=23,bg='#7A7A7A')
canvas_shape_sum = canvas_progress_bar_sum.create_rectangle(0, 0, 0, 25, fill='green')  # 前两参数是左上角坐标，后两参数是右下角坐标
canvas_text_sum = canvas_progress_bar_sum.create_text(150, 13, anchor=tk.CENTER)    # text坐标取画布的横纵各一半，northwest=NW
canvas_progress_bar_sum.itemconfig(canvas_text_sum, text='00:00:00')    # 修改图形属性，第一个参数为图形的ID，后边为想修改的参数；
var_progress_bar_percent_sum = tk.StringVar()
var_progress_bar_percent_sum.set('00.00  %')
label_progress_bar_percent_sum = tk.Label(root, textvariable=var_progress_bar_percent_sum)
canvas_progress_bar_sum.grid(column=3,row=23,columnspan=10, sticky='w')
sumbar_label.grid(column=2, row=23)
label_progress_bar_percent_sum.grid(column=13,row=23)


# 按钮
button_start = tk.Button(root, text='开始融合', fg='#F5F5F5', bg='#7A7A7A', command=run, height=1, width=15, relief=tk.GROOVE, bd=2,
                      activebackground='#F5F5F5', activeforeground='#535353')
button_start.grid(column=4,row=21)
namephoto = tk.PhotoImage(file=r"C:\Users\王浩华\Desktop\名字.png")  # file：t图片路径
namelabel = tk.Label(root,image=namephoto)  # 把图片整合到标签类中
namelabel.grid(column=2,row=24,columnspan=12)


root.mainloop()

