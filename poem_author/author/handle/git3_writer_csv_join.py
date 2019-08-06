import os,re

#想法，将对应的朝代的诗人和不对应的朝代的诗人分成两拨
#对应的可以统一一起判断如何插入
#不对应的可以单独直接处理，直接写入
def git3_join_git2(path_list):
    #将特殊朝代的csv单独处理
    a = 0
    for file in path_list:
        with open(r'E:\practice\Poems\my_handle\author\git3\git3_special_poet\%s'%file,'r',encoding='utf-8') as  f:
            lines = f.readlines()
            for line in lines:
                a += 1
                print('正在处理%s文件第%s行'%(file,a))
                new_line = re.split(r',', line)
                writer_new = re.sub('"', '', new_line[2])
                dynasty_new = re.sub('"', '', new_line[1])
                simpleIntro_new = ''
                detailIntro_new = ''
                headImageUr_new = ''
                # title  dynasty  writer  content  type  remark  shangxi  translation
                # data_writer_dict = {'writer': writer_new, 'dynasty': dynasty_new, 'simpleIntro': simpleIntro_new,
                #                     'detailIntro': detailIntro_new, 'headImageUrl': headImageUr_new}
                # data_writer_1.append(data_writer_dict)
                with open(r'E:\practice\Poems\my_handle\author\git3\git3_special_poet_csv\%s'%file,'a',encoding='utf-8') as f2:
                    f2.write(
                        '"' + writer_new + '"' + ',' + '"' + dynasty_new + '"' + ',' + '"' + simpleIntro_new +
                        '"' + ',' + '"' + detailIntro_new + '"' + ',' + '"' + headImageUr_new + '"' + '\n')


def git3_join_git2_same_dynasty(path_list):
    a = 0
    data1 = []
    for file in path_list:  #git12  少
        with open(r'E:\practice\Poems\my_handle\author\git3\git2\%s' % file, 'r', encoding='utf-8') as  f:
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
        with open(r'E:\practice\Poems\my_handle\author\git3\git3_join_git_12\%s' % file,'r',encoding='utf-8') as f2:
            lines = f2.readlines()
            for line in lines:
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
                    print('在%s文件中插入诗人为:%s  插入数量:%s' % (file,writer1,n))
                    with open(r'E:\practice\Poems\my_handle\author\git3\git2\%s' % file, 'a',
                              encoding='utf-8') as f3:
                        f3.write(
                            '"' + writer1 + '"' + ',' + '"' + dynasty1 + '"' + ',' + '"' + simpleIntro1 +
                            '"' + ',' + '"' + detailIntro1 + '"' + ',' + '"' + headImageUrl + '"' + '\n')

if __name__ == '__main__':

    # path =os.listdir( r'E:\practice\Poems\my_handle\author\git3\git3_special_poet')
    # git3_join_git2(path)
    path = os.listdir(r'E:\practice\Poems\my_handle\author\git3\git2')
    git3_join_git2_same_dynasty(path)