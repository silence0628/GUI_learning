### # GUI学习

* 毕设相关软件20190501

* GUI_4文件夹

  主要包括名为“基于深度学习平台的核素识别系统”，利用QT designer 和 Python结合在一起，制作一款简易式可操作的友好用户界面：该软件集成了三种方法：基于一维卷积神经网络、基于二维卷积神经网络以及基于奇异值分解和支持向量机的核素识别方法。界面简单，可操作性强。
  
  ![](<https://github.com/silence0628/GUI_learning/blob/master/GUI_4/imgs/software-1.png>)

以及第二版本

​		![](<https://github.com/silence0628/GUI_learning/blob/master/GUI_4/imgs/software-2.png>)

，后续会将识别算法植入进去，

主要功能：

* 1 导入待测样本txt（Cs137-1.txt）
* 2 进行数据可视化，绘制一维能谱波形图和二维空间映射图
* 3 选择识别算法（此处为已经训练好的模型）
* 4 特征可视化分析，展现不同网络层的输出特征图
* 5 识别结果（以不同大小的概率进行计算，得出识别结果）