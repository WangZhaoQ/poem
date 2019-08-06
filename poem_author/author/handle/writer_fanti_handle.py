import json,jsonlines,csv,time,os
import zhconv

files = os.listdir(r'E:\practice\Poems\my_handle\author\git2_writer')

a = 0
for file in files:
    # print(file)
    a+=1
    print('正在转换第%s个文件'% a)
    # path = r'E:\\practice\Poems\chinese-poetry\test\%s'% file
    path = r'E:\practice\Poems\my_handle\author\git2_writer\%s'% file



    with open(path,'r',encoding='utf-8') as f:
        content = f.read()
        content_new = zhconv.convert(content, 'zh-cn')
    path_new = r'E:\practice\Poems\my_handle\author\git_writer_jianti\%s' % file
    with open(path_new, 'w', encoding='utf-8') as f:
        f.write(content_new)


