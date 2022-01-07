# Boss-zhiping-Data
爬取Boss直聘数据 + Python + Pyqt
@[toc]
###  步骤
#### 方法1：
使用resquest 获取不到网页的源码：

后来有的网友说要登录才能爬取，就想试一下登录：
![在这里插入图片描述](https://img-blog.csdnimg.cn/f301e092ed174e36b4b271acc317ab86.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBASnVjd2F5,size_20,color_FFFFFF,t_70,g_se,x_16)看来没法登录也解决不了！！！

#### 方法2：

尝试使用无头浏览器进行爬取，还好能够爬取到信息！
接下来定位需要的信息就可以！！！



最后，由于直接进行测试，导致IP被反爬识别访问异常了！！！~~kule~~
IP 尝试多次被封！！！
![在这里插入图片描述](https://img-blog.csdnimg.cn/f73d739dd9114a618e36127df22a3925.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBASnVjd2F5,size_20,color_FFFFFF,t_70,g_se,x_16)手动验证
![在这里插入图片描述](https://img-blog.csdnimg.cn/f9b9dfa1491d424ba41bd730bf4d9aef.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBASnVjd2F5,size_20,color_FFFFFF,t_70,g_se,x_16)

+ 下次使用代理IP

#### 爬取结果
![在这里插入图片描述](https://img-blog.csdnimg.cn/9fd6271250cf4abaacdb2606bf33a7ab.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBASnVjd2F5,size_20,color_FFFFFF,t_70,g_se,x_16)
#### 代码
考试之后再贴上......初步代码，持续更新.......
[数据爬取](https://github.com/jucway/Boss-zhiping-Data)
#### 更新...
1. 添加gui界面
python GUI 第一次写，先打一个最简单的设计。。。。
![在这里插入图片描述](https://img-blog.csdnimg.cn/267c70d88b2d48edae9b207508fde304.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBASnVjd2F5,size_20,color_FFFFFF,t_70,g_se,x_16)初步

2. 输入城市名，输入职位名称，文件命名，点击保存格式。。。。
![在这里插入图片描述](https://img-blog.csdnimg.cn/5ddef9deb64e4f3abcc80f70b74953fb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBASnVjd2F5,size_20,color_FFFFFF,t_70,g_se,x_16)
初步封装成类：
+ 总结：
>  self.button.clicked.connect(self.paqu) 绑定按钮
>  citys = self.CityEdit.toPlainText() 获取输入框的文本，这个函数没有text()函数
>  self.button = QPushButton('确定',self) self 是将按钮添加到当前窗口上这是一个继承父类的窗口
>          self.FileNEdit.move(280, 160) 布局，相对于父窗口的起点位置



首发：博客园地址: https://www.cnblogs.com/Jucw/p/15752474.html
        self.FileNEdit.resize(130, 30) 自身窗口的大小
