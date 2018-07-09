#coding:utf-8
import os
import sys
import re

def get(text,wfile,stag,etag,only=0,title='',line=''):
    if only:
        pat = re.compile(stag +'(.*?)' + etag)
        pos = re.search(pat,text)
        wfile.write('## '+pos.group(1)+'\n')
    else:
        pat = re.compile(stag+'(.*?)'+etag,re.S)
        wfile.write('### '+title+'\n')
        lc = 1
        cps = 0
        for x in pat.finditer(text):
            lc = lc + text[cps:x.start()].count('\n')
            cps = x.start()
            flag = False
            for y in x.group(1).split('\n'):
                if len(y)==0:
                    continue
                tail  = '\n' if flag else '--'+str(lc) +'\n' 
                flag = True
                wfile.write(line+ y +tail)

def dealwith(fname,wname):
    print('dealing with '+fname)
    with open(wname,'a+') as w:
        with open(fname,'r') as f :
            txt = f.read()
            get(txt,w,'\\ntitle: ','\\n',1,)
            get(txt,w,'<tag>','</tag>',0,'重点摘抄','* ')
            get (txt,w,'<my>','</my>',0,'我的笔记','* ')
            get(txt,w,'<my note>','</my note>',0,'我的总结')

def dfs(rootDir,sp,all = False):
    for lists in os.listdir(rootDir):
        fp = os.path.join(rootDir,lists)
        if fp[-3:] == '.md':
            dealwith(fp,sp)
        if all and os.path.isdir(fp):
            dfs(fp,sp,all)

if __name__ =='__main__':
    if len(sys.argv) <= 1 or not os.path.exists(sys.argv[1]):
        pass
    else:
        saveDir = ""
        if len(sys.argv) <=2:
            saveDir = os.getcwd()
        sp = os.path.join(saveDir,'default.md') if os.path.isdir(saveDir) else saveDir
        all = 1 if len(sys.argv) > 3 else 0
        with open(sp,'a') as w:
            w.write('# js笔记\n')
        dfs(sys.argv[1],sp,all)

# 此脚本可以遍历文件夹下的指定类型文件，提取出md文件中stag和etag两种标记间的文本，以一定的格式加入新的md文件中
# 可用于提取代码的所有注释，或者提取html文件中的特定标签，或者提取自己在代码中做标记的部分
# 例如：
# <tag> my note </tag>
# 最终可以将my note 部分 提取出来，以简单格式插入新的markdown文件中
# 调用方法: python gettag.py /提取文件路径/ [/存储文件路径/[文件名]] [all]
# 默认存储文件路径为gettag.py文件所在目录，默认文件名为default.md, all标记用于选择是否包括子目录下的文件。