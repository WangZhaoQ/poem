import jsonlines,time,os
import re

data1 = []
writer_data1 = []
writer_data_dict1 = {}
files1 = os.listdir(r'E:\practice\Poems\my_handle\author\git1_writer')

a = 0
for file in files1:
    # print(file)
    a+=1
    print('正在读取文件%s'% file)
    path = r'E:\practice\Poems\my_handle\author\git1_writer\%s'% file
    a += 1
    with open(path, "r+", encoding="utf8") as f:
        for item in jsonlines.Reader(f):
            # new_item = re.sub(r'\\N', '""',item)
            # i = re.sub(r'\\N', '""', item)
            data1.append(item)
    length_data = len(data1)
    print(length_data)
    b = 0
    for i in data1:
        b += 1
        # i = re.sub(r'\\N', '""', i2)
        print('正在载入第%s个文件第%s行.....' % (a,b))
        name = str(i.get('name'))
        headImageUrl = str(i.get('headImageUrl'))
        simpleIntro = str(i.get('simpleIntro'))
        detailIntro = re.sub(r'\\n','',re.sub(r'\n', '',str(i.get('detailIntro'))))
        # simple_intro = re.sub(r'\.', '。', re.sub(r',', '，', re.sub(r'\\n','',str(i.get('simpleIntro')))))
        # simple_intro_new = re.sub(r'\u3000','',re.sub('▲','',re.sub('')))
        # detailIntro = re.sub(r'\.', '。', re.sub(r',', '，', re.sub(r'\\n','',str(i.get('detailIntro')))))
        if headImageUrl == 'None':
            headImageUrl = ''
        if simpleIntro == 'None':
                simple_intro = ''
        if detailIntro == 'None':
            detailIntro = ''
        writer_data_dict1 = {'name':name,
                                  'dynasty':'',
                                  'headImageUrl':headImageUrl,
                                  'simpleIntro':simpleIntro,
                                  'detailIntro':detailIntro}
        writer_data1.append(writer_data_dict1)
        # print(writer_data1)
        # time.sleep(3)



# for i in writer_data1:
    # print(i.get('name'))/

#多的,有dynsaty
data2 = []
writer_data2 = []
writer_data_dict2 = {}
files2 = os.listdir(r'E:\practice\Poems\my_handle\author\git1_gushi_writer_csv')
a = 0
for file in files2:
    # print(file)
    a+=1
    print('正在读取文件%s'% file)
    path = r'E:\practice\Poems\my_handle\author\git1_gushi_writer_csv\%s'% file
    a += 1
    with open(path,'r',encoding='utf-8') as f2:
        lines = f2.readlines()
        for line in lines:
            new_line = re.split(r',', line)
            name = re.sub('"', '', new_line[0])
            dynasty = re.sub('"', '', new_line[1])

            writer_data_dict2 = {'name':name,'dynasty':dynasty,
                                 'headImageUrl': '',
                                 'simpleIntro': '',
                                 'detailIntro': ''
                                 }
            writer_data2.append(writer_data_dict2)



no_need_join = []
a = 0
data2_len = len(writer_data2)
for i1 in writer_data2:
    a+=1
    print('正在读取列表writer_data2第%s项------%s'%(a,data2_len))
    name1 = i1.get('name')
    dynasty1 = re.sub(r'\n','',i1.get('dynasty'))
    headImageUrl1 = i1.get('headImageUrl')
    simpleIntro1 = i1.get('simpleIntro')
    detailIntro1 = i1.get('detailIntro')
    b = 0
    for i2 in writer_data1:
        # b += 1
        # print('a:%s,b:%s'%(a,b))
        name2 = i2.get('name')
        dynasty2 = re.sub(r'\n', '', i2.get('dynasty'))
        headImageUrl2 = i2.get('headImageUrl')
        simpleIntro2 = i2.get('simpleIntro')
        detailIntro2 = i2.get('detailIntro')
        # print(simpleIntro2)
        # time.sleep(3)
        if name1 == name2:
            i2['dynasty'] = dynasty1
            no_need_join.append(name1)
    if name1 not in no_need_join:
        writer_data1.append(i1)
        # print(i1)
        # time.sleep(3)
c = 0
writer_data1_len = len(writer_data1)

for i3 in writer_data1:
    c+=1
    print('正在读取列表writer_data1第%s项------%s'%(c,writer_data1_len))
    name = i3.get('name')
    dynasty = re.sub(r'\n','',i3.get('dynasty'))
    headImageUrl1 = i3.get('headImageUrl')
    simpleIntro1 = i3.get('simpleIntro')
    detailIntro1 = i3.get('detailIntro')
    if dynasty == '' or dynasty == 'None':
        dynasty = '未知'
    with open(r'E:\practice\Poems\my_handle\author\git1_writer_finally_csv\%s.csv'% dynasty,'a',encoding='utf-8') as f:
        f.write(
            '"' + name + '"' + ',' + '"' + dynasty + '"' + ',' + '"' + simpleIntro1 + '"' + ',' + '"' + detailIntro1 + '"' +
            ',' + '"' + headImageUrl1 + '"'  + '\n'
        )
    # print(name)
    # print(dynasty)
    # print(headImageUrl)
    # print(simpleIntro)
    # print(detailIntro)
    # print(i3)
    # time.sleep(3)








# files2 = os.listdir(r'E:\practice\Poems\chinese-gushiwen\guwen')
# c = 0
# for file in files2:
#     # print(file)
#     a+=1
#     print('正在读取文件%s'% file)
#     path = r'E:\practice\Poems\chinese-gushiwen\guwen\%s'% file
#     a += 1
#     with open(path, "r+", encoding="utf-8") as f:
#         for item in jsonlines.Reader(f):
#             # new_item = re.sub(r'\\N', '""',item)
#             # i = re.sub(r'\\N', '""', item)
#             data2.append(item)
#     length_data = len(data1)
#     print(length_data)
#     b = 0
#     for i in data2:
#         b += 1
#         # i = re.sub(r'\\N', '""', i2)
#         print('正在载入第%s个文件第%s行.....' % (c,b))
#         name = str(i.get('name'))
#         dynasty = str(i.get('dynasty'))
#         writer_data_dict2 = {'name': name,
#                              'dynasty': dynasty,
#                              }
#         writer_data2.append(writer_data_dict2)
# for i in writer_data2:
#     print(i.get('name'))
#     print(i.get('dynasty'))
#     time.sleep(1)

