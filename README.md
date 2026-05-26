# YoloSmartStick

#### 介绍
本文档主要是教你们如何使用git，还有怎么安装模型、跑模型

#### 软件架构
软件说明

- Anaconda是一个环境隔离的软件，可以理解为做不同的菜(不同项目)需要不同的锅(不同环境)
- labelimg就是打标签用的软件，安装需要用到Anaconda
- yolo是一个训练了一半的模型，我们只需要让他学会识别我们的东西就已经完成了一大半了

# git的使用
##### 关于绑定用户名和密码，按照以下步骤
1. 打开终端，输入命令
```bash
git config --global credential.helper store
```
2. 执行命令之后的第一次推送代码时，还会问你要账号密码，输入，以后就不用了，他已经记住了

##### 日常工作流
**提交仓库前先pull一下，万一别人修改了**
```bash
git pull origin main
```

**添加修改到暂存区**
```bash
git add .
```
**提交修改** 此时你的修改还是在本地的，你们在VSCode里面输入了描述再按提交就是做到了这一步
```bash
git commit -m "你的描述"
```
**将修改上传** 此步骤等效于你们在VSCode里面点击"同步更改"
```bash
git push origin main
```

# YOLO使用到的软件
1. Python集成开发环境：**miniconda**
2. **CUDA、cuDNN**：英伟达提供的针对英伟达显卡的运算平台。用来提升神经网络的运行效率，如果电脑显卡不满足要求也是可以不用安装，使用cpu来进行运算。
3. 深度学习库：**PyTorch**
4. 开发工具：VSCode

# YOLO安装步骤
## miniconda
> Miniconda 是**轻量级 conda 发行版**，只含 conda、Python 和基础依赖，**极小安装包、跨平台、能创建隔离环境、按需装包**，安装miniconda即可，不需要安装完整的Anaconda。
> **Conda** 是一个**跨平台的环境管理器 + 包管理器**。~~就相当于一个`可以帮厨师创建不同的锅防止菜串味的工具`+`菜市场`~~

#### 下载miniconda
点击[网址](https://www.anaconda.com/download/success?reg=skipped)进入下载页面，或者点击[此处]下载，当然也可以通过镜像站下载
#### 安装miniconda
![图一|450|450x350](https://blog.seamoonsbird.top/usr/uploads/2026/04/miniconda_1.png)
![图二|450](https://blog.seamoonsbird.top/usr/uploads/2026/04/miniconda_2.png)
![图三|450|450x348](https://blog.seamoonsbird.top/usr/uploads/2026/04/miniconda_3.png)
注意：更改目录的时候一定要放在空的文件夹，而且路径中不能有中文和空格**包括`program files`中的空格**，否则会报错。
![图四|450](https://blog.seamoonsbird.top/usr/uploads/2026/04/miniconda_4.png)
此处建议勾选1 3 4选项，如果你安装过python就不用勾第三个
![图五|450](https://blog.seamoonsbird.top/usr/uploads/2026/04/miniconda_5.png)

#### 添加环境变量
`win`+`r`调出运行窗口，输入`sysdm.cpl`，依次点击"高级"，"环境变量"，双击"系统变量"中的"Path"，点击"添加"，将以下几个环境变量添加进去。
```txt
D:\miniconda_env_pkg 
D:\miniconda_env_pkg\Scripts  
D:\miniconda_env_pkg\Library\mingw-w64\bin  
D:\miniconda_env_pkg\Library\bin
```
> **注意：，我因为将miniconda安装在了`D:\miniconda_env_pkg `，所以我的路径才是这个，需要根据实际情况找到这几个文件夹，做调整后再加进去。例如：你把Anaconda安装到了E盘中名为`Python`的文件夹，那么你的格式为`E:\Python\Library\mingw-w64\bin`其余三个类同，只需修改前面的内容即可。

![图一|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/Env_Variables_1.png)
![图二|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/Env_Variables_2.png)
![图三|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/Env_Variables_3.png)
![图四|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/Env_Variables_4.png)
![图五|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/Env_Variables_5.png)

#### 测试安装是否成功
- 点击`win`搜索`Anaconda Prompt`，打开。
- 会弹出一个命令行窗口，在里面输入`conda info`。
应该会输出类似如下：
![图一|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/conda_test_1.png)
- 再输入`conda -V`查看版本号
应该会输出类似如下：
![图二|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/conda_test_2.png)
> 如果输出`conda不是内部或外部命令`那就意味着，anaconda没有配置好环境变量。重新配置以下环境变量

#### 更换conda源
##### 换源说明：
前面提到过，conda就是个巨大的菜市场，但是国内访问速度较慢，可以更换使用镜像站提升速度。
- 如果是在学校，可以看看自己学校有没有镜像站，有的话用校园网会很快，比如我是用的是本校的OSA镜像站。
- 如果不在校园或者学校没有镜像站，那么就使用`中科大源`或者`清华源`等。

##### 换源步骤：
1. 还是利用上一步的方法打开`Anaconda Prompt`，输入命令以### 创建.condarc文件(配置文件)
```bash
conda config --set show_channel_urls yes
```
2. 在C盘的用户文件夹目录下面找到.condarc文件，用记事本打开
**不管你把miniconda装在了哪一个盘，都是在这个目录里面找**
**如果你安装了VSCode，那么就可以输入命令`code .condarc`直接用VSCode打开并进行编辑**
3. 在文件中输入
```condarc
channels:

  - defaults

show_channel_urls: true

default_channels:

  - https://mirrors.osa.moe/anaconda/pkgs/main

  - https://mirrors.osa.moe/anaconda/pkgs/r

  - https://mirrors.osa.moe/anaconda/pkgs/msys2

custom_channels:

  conda-forge: https://mirrors.osa.moe/anaconda/cloud

  pytorch: https://mirrors.osa.moe/anaconda/cloud
```
如果是其他镜像站，可以在他们的镜像站里面的使用教程找到命令，比如[ 清华大学开源软件镜像站 ](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)就写
```condarc
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```
4. 使用下列命令清除索引缓存，并安装常用包测试一下。
```bash
conda clean -i
conda create -n myenv numpy
```

#### 更改虚拟环境存放路径
- 还是打开刚才的`.condarc`文件，在最后添加
```condarc
envs_dirs:
  - D:\Miniconda3\envs
pkgs_dirs:
  - D:\Miniconda3\pkgs
```
这里面的`D:\Miniconda`是你安装miniconda的路径，如果里面没有envs的文件夹，那么就创建一个文件夹并修改文件夹权限。右键文件夹，点击“属性”，点击“安全”，点击“高级”，点击“选择主体”，点击“高级”，点击“立即查找”，选择Users，再勾选所有权限的选项，即可。
![图一|300|300x400](https://blog.seamoonsbird.top/usr/uploads/2026/04/power_1.png)
![图二|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/power_2.png)
![图三|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/power_3.png)
![图四|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/power_4.png)
![图五|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/power_5.png)
![图六|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/power_6.png)
![图七|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/power_7.png)
![图八|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/power_8.png)
![图九|300](https://blog.seamoonsbird.top/usr/uploads/2026/04/power_9.png)
然后一路点确定即可。pkg文件夹同理

## 更新NVIDIA显卡驱动
- 点击托盘，打开NVIDIA驱动程序
- 点击左侧的驱动程序，再在右上角点击studio驱动程序，更新

## 安装CUDA
- 在终端输入`nvidia-smi`，查看自己的CUDA版本，如图所示
右上角有CUDA版本号，去[官网](https://developer.nvidia.com/cuda-downloads)下载CUDA并安装，下载的CUDA不可高于输出的版本号，也最好不要过低。
- 在终端输入`nvcc -V`查看是否安装成功

## 安装cuDNN
根据CUDA版本去[官网](https://developer.nvidia.com/cudnn-downloads)下载对应的cudnn并进行安装，一般9.2.x对应的CUDA版本就是12.x/13.x

## 创建、激活虚拟环境
- 创建
在Anaconda prompt里面输入
```bash
conda create -n xxx python=3.9  #xxx是你自己给这个环境取的名字
```
即可创建一个带有3.9版本的python的虚拟环境.建议python版本不要选太高，否则可能出现安装labelimg(标注工具)的时候由于python版本太高，导致自动安装的pyqt5版本太高，高版本的pyqt5接受整型数据，而labelimg发出浮点型数据，最终导致闪退的尴尬现象~~别问我怎么知道的~~

- 激活
在命令行中输入
```bash
conda activate xxx
```
> 完成改步骤后会在命令行的前面出现(xxx),若出现(base)则是没有成功激活。

## 安装带有CUDA库的PyTorch
打开[官网](https://pytorch.org/get-started/locally/)，选择自己适合的版本，复制图中的命令行，然后输进刚才的命令行。**一定要在xxx环境中**
*下载速度取决于网络情况*
> 验证方法：
> 在命令行中输入`python`
> 然后依次输入以下命令
> `import torch`
> `print(torch.__version__) #查看pytorch版本`
> `print(torch.cuda.is_available()) #查看cuda是否可用 输出为True 或者False`
> `print(torch.backends.cudnn.version()) #查看cudnn是否可用，输出为版本号`

## 安装Labelimg标注工具
在刚才的命令行以及环境中输入以下命令
```bash
pip install PyQt5 pyqt5-tools lxml labelImg
```


## 安装并验证YOLO
- 在刚才的命令行及环境中输入
```bash
pip install ultralytics
```
*下载速度取决于网络情况*

- 输入
```bash
pip show ultralytics
```

## VSCode的配置
- 打开VSCode
- 打开一个你要训练模型的目录，新建一个python程序，空白的就行。
- 右下角选择环境与解释器**注意，要选两次，一次是选解释器，一次是选环境**
如果这一步出现不能使用脚本之类的提示，那就要以管理员身份打开终端，输入下面的命令以临时放宽权限
```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
如果出现要进行`conda init`的提示，那就输入这条命令

# YOLO使用步骤
## 数据集结构说明
```txt
data/
├── train/                # 训练集
│   ├── images/        # 其他场景图片
│   └── labels/           #放打出来的标注         
│
├── val/                  # 验证集 要求不能与训练集重复
│   ├── images/
│   └── labels/
│
└── test/                 # 测试集 测试效果的，也不能与训练集、验证集重复
    └── images/
```

## 使用Labelimg
- 点击 **Open Dir**，选择 `train/images` 或者`val/images`图片文件夹
- 点击 **Change Save Dir**，选择 `train/labels` 或者`val/labels`标签保存文件夹
- 左上角切换标注格式：**Pascal VOC 改为 YOLO**
- 开启自动保存（再也不用 Ctrl+S）
	1. 顶部菜单栏点击：**View**
	2. 勾选 **Auto Save mode**
- 常用快捷键
	- `W`：开始绘制标注框
	- `A`：上一张图片
	- `D`：下一张图片（自动保存）
	- `Del`：删除选中的标注框
- 标签文件说明
	每张图片会生成**同名 `.txt` 标签**，为 YOLO 标准格式：
```plaintext
类别ID 归一化中心x 归一化中心y 归一化宽度 归一化高度
```

## 初体验YOLO
在VSCode的终端中输入
```bash
yolo predict model=yolo11n.pt source=https://ultralytics.com/images/bus.jpg save=True
```
*下载速度取决于网络情况*
然后你就可以在run/detect/predict里面看见一张识别了人、车的图片了

## YOLO的训练
> 此步骤需要有打好标签的数据集,且确保进入环境

##### yolo简述
yolo 有四种运行模式、四种任务模式
###### 四大任务模式
1. **Detect 目标检测**（最常用）
2. **Segment 语义分割**
3. **Classify 图像分类**
4. **Pose 姿态估计**

###### YOLO 四种运行模式(动作)
1. **predict** 推理预测（日常跑图、跑视频、摄像头）
2. **train** 训练（自己数据集炼丹）
3. **val** 验证（看模型精度 mAP、准确率）
4. **export** 导出模型（转 ONNX/TensorRT/onnxruntime 部署）

##### 训练模型
- 新建一个`data.yaml`配置文件，输入以下内容：
```yaml
# 训练、验证、测试集路径（用相对路径）
train: ./data/train/images
val: ./data/val/images
test: ./data/test/images  # 没有测试集可以删掉这行

# 类别数和类别名
nc: 1
names: ['tactile']  # 和 classes.txt 里的类别名保持一致就行
```
- 输入命令
命令模板为
```bash
yolo 任务 动作 model=权重.pt source=输入 其他参数
```
参数解释
```bash
model=xxx.pt # 选用的模型权重
source=xxx # 输入：图片/视频/摄像头/文件夹
conf=0.5 # 置信度阈值，低于0.5不显示
save=True # 保存结果
show=True # 弹出窗口实时看画面
device=0 # 用GPU 0；device=cpu 用CPU
```
一般我们直接输入
```bash
yolo detect train model=yolo11n.pt data=data.yaml epochs=100 imgsz=640 device=0
```
意思是用`yolo11n.pt`模型进行训练，数据集按照`data.yaml`里面的来，训练100轮(每一轮都会在`train`里面找图片学习，在`val`里面验证)，并且要求使用显卡。

- 得到的结果放在`run/任务/动作-x/`文件夹下，比如训练好的模型(用于目标检测)就在`runs\detect\train-x\weights\best.pt`
- **如果出现训练到一半中止了，可以将命令中的`model=`后面的改为最新的`run/detect/train-x/weights/last.pt`继续训练**
- 如果还是不行，那就加上`batch=8 workers=0`，这是减少同时训练的照片数量和减少线程


> 文 / [Seamoonsbird](https://blog.seamoonsbird.top), 2026-04-29
```
