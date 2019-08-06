import json
import time
import os
import re

#唐代 csv 里的每一条数据以字典形式放入列表中
data_poem_1 = []
data_poem_dict_1 = {}
with open(r'E:\practice\Poems\my_handle\csv_file\test\唐代.csv','r',encoding='utf-8') as f2:
    lines = f2.readlines()
    for line in lines:
        new_line = re.split(r',', line)
        title = re.sub('"', '', new_line[0])
        writer = re.sub('"', '', new_line[2])
        content = re.sub('"', '', new_line[3])
        data_poem_1.append(title)
        data_poem_dict_1[title] = {'writer':writer,'content':content}
n = len(data_poem_1)
data_poem_2 = []
data_poem_dict_2 = {}
files_path = os.listdir(r'E:\practice\Poems\my_handle\tang_json_new')
repeat_poem = []
for i in files_path:
    # a+=1
    # print('正在进入第%s个文件'% a)
    path = r'E:\practice\Poems\my_handle\tang_json_new\%s'% i
    with open(path,'r',encoding='utf-8') as f:
        file = json.load(f)
        b = 0
        for item in file: #json文件
            author = item.get('author')
            title = item.get('title')
            content_list = item.get('paragraphs')
            content = ''.join(content_list)
            data_poem_2.append(title)
            data_poem_dict_2[title] = {'writer':writer,'content':content}
    for title in data_poem_1:
        if title  in data_poem_2 and data_poem_dict_1[title]['content'] == data_poem_dict_2[title]['content']:
            if title not in repeat_poem:
                repeat_poem.append(title)
                with open(r'E:\practice\Poems\my_handle\1-2repeat.txt','a',encoding='utf-8') as f:
                    f.write(title+'\n')
            continue
        else:
            continue

