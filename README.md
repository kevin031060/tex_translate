1、把tex文件放到file文件夹，比如main.tex
更改fromtex2txt.py 里filename = "file/main.tex"
2、运行fromtex2txt.py
如果文件很长，一般会生成main_0.txt, main_1.txt（谷歌翻译有字数限制）
也会生成一个main.txt，删除里面所有的内容就行。
3、打开谷歌翻译--文档翻译，翻译main_0.txt，结果复制到main.txt，再翻译main_1.txt，复制到main.txt拼起来
4、运行txt2tex.py，修改里面filename = "file/main.txt"

运行中的问题：
1、如果tex正文里有“[0,1]”这种中括号，会报错complicted，手动删掉所有这种中括号，根据报错信息删除就行了

2、tex里面如果有不常见的\{}命令，例如

\paragraph{asdijajklsdjsakdjlaksdja}

会有问题，会导致"{"后面的无法翻译。把\paragraph删掉就行。{}没关系不用删

还有其他的，类似于\textit{}这种