# gettag说明
### 功能
此脚本可以遍历文件夹下的指定类型文件，提取出文件中stag和etag两种标记间的文本，以一定的格式加入新的文件中

可用于提取代码的所有注释，或者提取html文件中的特定标签，或者提取自己在代码中做标记的部分。我个人用于提取阅读md文件时画的重点还有自己留下的笔记。
### 例子
例如：

    <tag> my note </tag>

最终可以将my note 部分 提取出来，以简单格式插入新的markdown文件中
用这个脚本生成的文件参考：[我的js学习笔记](https://gitlab.com/Oxlouis/my-learning-blog/blob/master/my_javascript_note.md)

### 调用方法

调用方法: python gettag.py /提取文件路径/ [/存储文件路径/[文件名]] [all]

默认存储文件路径为gettag.py文件所在目录，默认文件名为default.md, all标记用于选择是否包括子目录下的文件。

### 手动修改
脚本中还有一些可调整部分没有提供接口，可以在代码中自行修改，比如说get函数传入的stag,etag，还有读入文件的后缀可以不只是.md文件。