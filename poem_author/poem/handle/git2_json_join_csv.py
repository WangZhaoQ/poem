import json
import time
import os
import re

#唐代 csv 里的每一条数据以字典形式放入列表中
data_poem_1 = []
with open(r'E:\practice\Poems\my_handle\csv_file\唐代.csv','r',encoding='utf-8') as f2:
    lines = f2.readlines()
    for line in lines:
        new_line = re.split(r',', line)
        title_new = re.sub('"', '', new_line[0])
        writer_new = re.sub('"', '', new_line[2])
        content_new = re.sub('"', '', new_line[3])
        # title  dynasty  writer  content  type  remark  shangxi  translation
        data_poem_dict = {'title':title_new,'writer':writer_new,'content':content_new,
                          'dynasty':'','type':'','remark':'','shangxi':'','translation':''}
        data_poem_1.append(data_poem_dict)
#
n = len(data_poem_1)
files_path = os.listdir(r'E:\practice\Poems\my_handle\tang_json_new')
data_poem_2 = []
a = 0
for i in files_path:
    a+=1
    print('正在进入第%s个文件'% a)
    path = r'E:\practice\Poems\my_handle\tang_json_new\%s'% i
    with open(path,'r',encoding='utf-8') as f:
        file = json.load(f)
        b = 0
        for item in file: #json文件
            b += 1
            print('正在进入第%s个文件第%s行' % (a, b))
            author1 = item.get('author')
            title1 = item.get('title')
            content_list = item.get('paragraphs')
            content1 = ''.join(content_list)
            data_poem_dict = {'title': title1, 'writer': author1, 'content': content1,
                              'dynasty': '', 'type': '', 'remark': '', 'shangxi': '', 'translation': ''}
            data_poem_2.append(data_poem_dict)
repeat_poem = []
n = 0
for i1 in data_poem_2:
    title1 = i1.get('title')
    writer1 = i1.get('writer')
    content1 = i1.get('content')
    for i2 in data_poem_1:
        title2 = i2.get('title')
        writer2 = i2.get('writer')
        content2 = i2.get('content')
        if title1 ==  title2 :
            if content1 == content2:
                repeat_poem.append(title1)
    if title1 not in repeat_poem:
        n += 1
        print('插入数量:%s' % n)
        print('插入唐诗为:%s'%title1)
        with open(r'E:\practice\Poems\my_handle\csv_file\唐代.csv', 'a',
                  encoding='utf-8') as f3:
            f3.write(
                '"' + title1 + '"' + ',' + '"' + '' + '"' + ',' + '"' + writer1 + '"' + ',' + '"' + content1 + '"' +
                ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + '\n')