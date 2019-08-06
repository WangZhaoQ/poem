import re
import time
#
# def handle_git23_same_dynasty(pathlist1,path2):
#     data_poem_1 = []
#     a = 0
#     with open(r'E:\practice\Poems\my_handle\git3_csv\魏晋.csv','r',encoding='utf-8') as f1:
#         lines = f1.readlines()
#         for line in lines:
#             a+=1
#             print('正在读入第%s行'%a)
#             new_line = re.split(r',', line)
#             title_new = re.sub('"', '', new_line[0])
#             writer_new = re.sub('"', '', new_line[2])
#             content_1 = re.sub('"', '', new_line[3])
#             content = re.sub(r'\n', '', str(content_1))
#             # dynasty = re.sub('"','',new_line[1])+'代'
#             dynasty = re.sub('"','',new_line[1])
#             # print(line)
#             # time.sleep(3)
#             data_poem_dict = {'title': title_new, 'writer': writer_new, 'content': content,
#                               'dynasty': dynasty, 'type': '', 'remark': '', 'shangxi': '', 'translation': ''}
#             data_poem_1.append(data_poem_dict)
#
#     data_poem_2 = []
#     b = 0
#     with open(r'E:\practice\Poems\my_handle\csv_file\魏晋.csv','r',encoding='utf-8') as f2:
#         lines = f2.readlines()
#         for line in lines:
#             b += 1
#             print('正在进入第%s个文件' % b)
#             new_line = re.split(r',', line)
#             title_new = re.sub('"', '', new_line[0])
#             writer_new = re.sub('"', '', new_line[2])
#             content_new = re.sub('"', '', new_line[3])
#             # title  dynasty  writer  content  type  remark  shangxi  translation
#             data_poem_dict = {'title': title_new, 'writer': writer_new, 'content': content_new,
#                               'dynasty': '', 'type': '', 'remark': '', 'shangxi': '', 'translation': ''}
#             data_poem_2.append(data_poem_dict)
#     repeat_poem = []
#     n = 0
#     #由汉向两汉文件里插入
#     for i1 in data_poem_1:
#         title1 = i1.get('title')
#         writer1 = i1.get('writer')
#         content1 = i1.get('content')
#         dynasty1 = i1.get('dynasty')
#         # print(i1)
#         # time.sleep(2)
#         for i2 in data_poem_2:
#             title2 = i2.get('title')
#             writer2 = i2.get('writer')
#             content2 = i2.get('content')
#             if title1 ==  title2 :
#                 if content1 == content2:
#                     # print('重复的诗为：%s' %title1)
#                     repeat_poem.append(title1)
#         if title1 not in repeat_poem:
#             n += 1
#             print('插入数量:%s' % n)
#             print('插入唐诗为:%s'%title1)
#             with open(r'E:\practice\Poems\my_handle\csv_file\魏晋.csv', 'a',
#                       encoding='utf-8') as f3:
#                 f3.write(
#                     '"' + title1 + '"' + ',' + '"' + dynasty1 + '"' + ',' + '"' + writer1 + '"' + ',' + '"' + content1 + '"' +
#                     ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + '\n')
# # print(repeat_poem)
#先秦，辽
path_list = 'E:\practice\Poems\my_handle\git3_csv\辽.csv'

a = 0
e = 0
# with open(r'E:\practice\Poems\my_handle\git3_csv\秦.csv', 'r', encoding='utf-8') as f1:
with open(path_list, 'r', encoding='utf-8') as f1:

    lines = f1.readlines()
    for line in lines:
        try:
            a += 1
            print('正在读入第%s行' % a)
            new_line = re.split(r',', line)
            title = re.sub('"', '', new_line[0])
            dynasty = re.sub('"', '', new_line[1])
            writer = re.sub('"', '', new_line[2])
            content_1 = re.sub('"', '', new_line[3])
            content = re.sub(r'\n', '', str(content_1))
            with open(r'E:\practice\Poems\my_handle\git3_special_dynasty\辽.csv' , 'a+',
                      encoding='utf-8') as f2:
                f2.write(
                    '"' + title + '"' + ',' + '"' + dynasty + '"' + ',' + '"' + writer + '"' + ',' + '"' + content + '"' +
                    ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + '\n')
            print('写入')
        except:
            e += 1
            print(e)
            time.sleep(3)
            continue

