import json
import time
import os
import re
#
# #唐代 csv 里的每一条数据以字典形式放入列表中
# data_writer_1 = []
# with open(r'E:\practice\Poems\my_handle\author\git1_writer_finally_csv\唐代.csv','r',encoding='utf-8') as f2:
#     lines = f2.readlines()
#     for line in lines:
#         new_line = re.split(r',', line)
#         writer_new = re.sub('"', '', new_line[0])
#         dynasty_new = re.sub('"', '', new_line[1])
#         simpleIntro_new = re.sub('"', '', new_line[2])
#         detailIntro_new = re.sub('"', '', new_line[3])
#         headImageUr_new = re.sub('"', '', new_line[3])
#         # title  dynasty  writer  content  type  remark  shangxi  translation
#         data_writer_dict = {'writer':writer_new,'dynasty':dynasty_new,'simpleIntro':simpleIntro_new,
#                           'detailIntro':detailIntro_new,'headImageUrl':headImageUr_new}
#         data_writer_1.append(data_writer_dict)
# #
# n = len(data_writer_1)
# # print(n) 3816
# data_writer_2 = []
# path = r'E:\practice\Poems\my_handle\author\git2_writer_jianti\authors_tang.json'
# with open(path,'r',encoding='utf-8') as f:
#     file = json.load(f)
#     b = 0
#     for item in file: #json文件
#         b += 1
#         print('正在进入文件第%s行' %  b)
#         writer = item.get('name')
#         simpleIntro = item.get('desc')
#         data_writer_dict = {'writer': writer, 'dynasty': '唐代', 'simpleIntro': simpleIntro,
#                             'detailIntro': '', 'headImageUrl': ''}
#         data_writer_2.append(data_writer_dict)
# repeat_poem = []
# n = 0
# for i1 in data_writer_2:
#     writer1 = i1.get('writer')
#     dynasty1= i1.get('dynasty')
#     simpleIntro1 = i1.get('simpleIntro')
#     detailIntro1 = i1.get('detailIntro')
#     headImageUrl = i1.get('headImageUrl')
#     for i2 in data_writer_1:
#         writer2 = i2.get('writer')
#         dynasty2 = i2.get('dynasty')
#         simpleIntro2 = i2.get('simpleIntro')
#         m = len(simpleIntro2)
#         detailIntro2 = i2.get('detailIntro')
#         headImageUr2 = i2.get('headImageUrl')
#         if writer1 == writer2 :
#             if len(simpleIntro1)<=len(simpleIntro2):
#                 simpleIntro1 = simpleIntro2
#                 repeat_poem.append(writer1)
#
#     if writer1 not in repeat_poem:
#         n += 1
#         print('插入数量:%s' % n) #250715
#         print('插入诗人为:%s'% writer1)
#         with open(r'E:\practice\Poems\my_handle\author\git2_join_git_1_writer\唐代.csv', 'a',
#                   encoding='utf-8') as f3:
#             f3.write(
#                     '"' + writer1 + '"' + ',' + '"' + dynasty1 + '"' + ',' + '"' + simpleIntro1 +
#                     '"' + ',' + '"' + detailIntro1 + '"' + ',' + '"' + headImageUrl + '"' + '\n')
#
#
#
path_list = [
    r'E:\practice\Poems\my_handle\author\git3\git2\近现代.csv'
]
a = 0
data1 = []
for file in path_list:  # git12  少
    with open(file, 'r', encoding='utf-8') as  f:
        lines = f.readlines()
        for line in lines:
            a += 1
            print('正在处理%s文件第%s行' % (file, a))
            new_line = re.split(r',', line)
            writer_new = re.sub('"', '', new_line[2])
            dynasty_new = re.sub('"', '', new_line[1])
            simpleIntro_new = ''
            detailIntro_new = ''
            headImageUr_new = ''
            data_dict1 = {'writer': writer_new, 'dynasty': dynasty_new, 'simpleIntro': simpleIntro_new,
                          'detailIntro': detailIntro_new, 'headImageUrl': headImageUr_new}
            data1.append(data_dict1)
    data2 = []
    with open(r'E:\practice\Poems\my_handle\author\git3\git3_join_git_12\近现代.csv', 'r', encoding='utf-8') as f2:
        lines = f2.readlines()

        for line in lines:
            try:
                a += 1
                print('正在处理%s文件第%s行' % (file, a))
                new_line = re.split(r',', line)
                writer_new = re.sub('"', '', new_line[2])
                dynasty_new = re.sub('"', '', new_line[1])
                simpleIntro_new = ''
                detailIntro_new = ''
                headImageUr_new = ''
                data_dict2 = {'writer': writer_new, 'dynasty': dynasty_new, 'simpleIntro': simpleIntro_new,
                              'detailIntro': detailIntro_new, 'headImageUrl': headImageUr_new}
                data2.append(data_dict2)
            except:
                continue
    repeat_poem = []
    n = 0
    for i1 in data2:
        writer1 = i1.get('writer')
        dynasty1 = i1.get('dynasty')
        simpleIntro1 = i1.get('simpleIntro')
        detailIntro1 = i1.get('detailIntro')
        headImageUrl = i1.get('headImageUrl')
        for i2 in data1:
            writer2 = i2.get('writer')
            dynasty2 = i2.get('dynasty')
            simpleIntro2 = i2.get('simpleIntro')
            detailIntro2 = i2.get('detailIntro')
            headImageUr2 = i2.get('headImageUrl')
            if writer1 == writer2:
                repeat_poem.append(writer1)
        if writer1 not in repeat_poem:
            n += 1
            # print('插入数量:%s' % n)  # 250715
            print('在%s文件中插入诗人为:%s  插入数量:%s' % (file, writer1, n))
            with open(file, 'a',
                      encoding='utf-8') as f3:
                f3.write(
                    '"' + writer1 + '"' + ',' + '"' + dynasty1 + '"' + ',' + '"' + simpleIntro1 +
                    '"' + ',' + '"' + detailIntro1 + '"' + ',' + '"' + headImageUrl + '"' + '\n')
