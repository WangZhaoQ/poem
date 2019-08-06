import re
import time

# github1里的近代和现代合并为一个朝代
def join_xiandai_jindai():
    file_list = [
        r'E:\practice\Poems\my_handle\finally_csv\近代.csv',
        r'E:\practice\Poems\my_handle\finally_csv\现代.csv'
    ]
    a =0
    for file in file_list:
        with open(file,'r+',encoding='utf-8') as f1:
            lines = f1.readlines()
            for line in lines:
                a+=1
                print('正在读入第%s行'%a)
                new_line = re.split(r',', line)
                title = re.sub('"', '', new_line[0])
                # dynasty = re.sub('"','',new_line[1])
                dynasty = '近现代'
                writer = re.sub('"', '', new_line[2])
                content_1 = re.sub('"', '', new_line[3])
                content = re.sub(r'\n', '', str(content_1))
                type = str(re.sub('"','',new_line[4]))
                remark = str(re.sub('"','',new_line[5]))
                shangxi = str(re.sub('"','',new_line[6]))
                translation = str(re.sub('"','',new_line[7]))
                dynasty = re.sub('"','',new_line[1])
                with open(r'E:\practice\Poems\my_handle\finally_csv\近现代.csv','a',encoding='utf-8') as f2:
                    f2.write(
                    '"' + title + '"' + ',' + '"' + dynasty + '"' + ',' + '"' + writer + '"' + ',' + '"' + content + '"' +
                    ',' + '"' + type + '"' + ',' + '"' + remark + '"' + ',' + '"' + shangxi + '"' + ',' + '"' + translation + '"' + '\n')

special_file_list = [
    '元末明初',
    '先秦',
    '唐末宋初',
    '宋末元初',
    '宋末金初',
    '明末清初',
    '清末民国初',
    '清末近现代初',
    '辽',
    '近现代末当代初',
    '金末元初',
    '隋末唐初',
    '魏晋末南北朝初',
]

def handle_special_dynasty():
    a = 0
    e = 0
    data = []
    for path in special_file_list:
        with open(r'E:\practice\Poems\my_handle\git3_csv\%s.csv'% path,'r',encoding='utf-8') as f1:
            lines = f1.readlines()
            for line in lines:
                try:
                    a+=1
                    print('正在读入第%s行'%a)
                    new_line = re.split(r',', line)
                    title = re.sub('"', '', new_line[0])
                    dynasty = re.sub('"','',new_line[1])
                    writer = re.sub('"', '', new_line[2])
                    content_1 = re.sub('"', '', new_line[3])
                    content = re.sub(r'\n', '', str(content_1))
                    with open(r'E:\practice\Poems\my_handle\git3_special_dynasty\%s.csv'%dynasty,'a+',encoding='utf-8') as f2:
                        f2.write(
                                     '"' + title + '"' + ',' + '"' + dynasty + '"' + ',' + '"' + writer + '"' + ',' + '"' + content + '"' +
                                     ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + '\n')
                    print('写入')
                except:
                    e+=1
                    print(e)
                    time.sleep(3)
                    continue


def handle_git23_same_dynasty(path1, path2):
    data_poem_1 = []
    a = 0
    for path in path1:
        with open(path, 'r', encoding='utf-8') as f1:
            lines = f1.readlines()
            for line in lines:
                try:
                    a += 1
                    print('正在读入第%s行' % a)
                    new_line = re.split(r',', line)
                    title_new = re.sub('"', '', new_line[0])
                    writer_new = re.sub('"', '', new_line[2])
                    content_1 = re.sub('"', '', new_line[3])
                    content = re.sub(r'\n', '', str(content_1))
                    #看情况是否代
                    dynasty = re.sub('"','',new_line[1])
                    # dynasty = re.sub('"', '', new_line[1])
                    # print(line)
                    # time.sleep(3)
                    data_poem_dict = {'title': title_new, 'writer': writer_new, 'content': content,
                                      'dynasty': dynasty, 'type': '', 'remark': '', 'shangxi': '', 'translation': ''}
                    data_poem_1.append(data_poem_dict)
                except Exception as e:
                    print(e)
                    continue


    data_poem_2 = []
    b = 0
    with open(path2, 'r', encoding='utf-8') as f2:
        lines = f2.readlines()
        for line in lines:
            try:
                b += 1
                print('正在进入第%s个文件' % b)
                new_line = re.split(r',', line)
                title_new = re.sub('"', '', new_line[0])
                writer_new = re.sub('"', '', new_line[2])
                content_new = re.sub('"', '', new_line[3])
                # title  dynasty  writer  content  type  remark  shangxi  translation
                data_poem_dict = {'title': title_new, 'writer': writer_new, 'content': content_new,
                                  'dynasty': '', 'type': '', 'remark': '', 'shangxi': '', 'translation': ''}
                data_poem_2.append(data_poem_dict)
            except Exception as e:
                print(e)
                continue
    repeat_poem = []
    n = 0
    # 由汉向两汉文件里插入
    for i1 in data_poem_1:
        title1 = i1.get('title')
        writer1 = i1.get('writer')
        content1 = i1.get('content')
        dynasty1 = i1.get('dynasty')
        # print(i1)
        # time.sleep(2)
        for i2 in data_poem_2:
            title2 = i2.get('title')
            writer2 = i2.get('writer')
            content2 = i2.get('content')
            if title1 == title2:
                if content1 == content2:
                    # print('重复的诗为：%s' %title1)
                    repeat_poem.append(title1)
        if title1 not in repeat_poem:
            n += 1
            print('插入数量:%s' % n)
            print('插入唐诗为:%s' % title1)
            with open(path2, 'a',encoding='utf-8') as f3:
                f3.write(
                    '"' + title1 + '"' + ',' + '"' + dynasty1 + '"' + ',' + '"' + writer1 + '"' + ',' + '"' + content1 + '"' +
                    ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + ',' + '"' + '' + '"' + '\n')
# simple_file_list = [
#     '元' 1
#     '南北朝'1
#     '唐' 1
#     '宋' 1
#     '当代'1
#     '明' 1
#     '汉' 1
#     '清' 1
#     '先秦'1
#     '辽' 1
#     '近现代'1
#     '金'1
#     '隋'1
#     '魏晋'1
# ]
if __name__ == '__main__':
    # handle_special_dynasty()
    # path_list = [
    #     'E:\practice\Poems\my_handle\git3_csv\明_1.csv',
    #     'E:\practice\Poems\my_handle\git3_csv\明_2.csv',
    #     'E:\practice\Poems\my_handle\git3_csv\明_3.csv',
    #     'E:\practice\Poems\my_handle\git3_csv\明_4.csv',
    # ]
    # path = r'E:\practice\Poems\my_handle\finally_csv\明代.csv'

    # path_list = [
    #     'E:\practice\Poems\my_handle\git3_csv\宋_1.csv',
    #     'E:\practice\Poems\my_handle\git3_csv\宋_2.csv',
    #     'E:\practice\Poems\my_handle\git3_csv\宋_3.csv',
    #     'E:\practice\Poems\my_handle\git3_csv\宋_4.csv',
    # ]
    # path = r'E:\practice\Poems\my_handle\finally_csv\宋代.csv'
    # path_list = [
    #          'E:\practice\Poems\my_handle\git3_csv\清_1.csv',
    #          'E:\practice\Poems\my_handle\git3_csv\清_2.csv',
    #      ]
    # path = r'E:\practice\Poems\my_handle\finally_csv\清代.csv'
    #
    # path_list = [
    #     'E:\practice\Poems\my_handle\git3_csv\元.csv',
    # ]
    # path = r'E:\practice\Poems\my_handle\finally_csv\元代.csv'
    #
    # path_list = [
    #     'E:\practice\Poems\my_handle\git3_csv\南北朝.csv',
    # ]
    # path = r'E:\practice\Poems\my_handle\finally_csv\南北朝.csv'
    #
    # path_list = [
    #     'E:\practice\Poems\my_handle\git3_csv\唐.csv',
    # ]
    # path = r'E:\practice\Poems\my_handle\finally_csv\唐代.csv'
    #
    # path_list = [
    #     'E:\practice\Poems\my_handle\git3_csv\当代.csv',
    # ]
    # path = r'E:\practice\Poems\my_handle\finally_csv\当代.csv'
    #
    # path_list = [
    #     'E:\practice\Poems\my_handle\git3_csv\汉.csv',#运行时注意改一下dynasty
    # ]
    # path = r'E:\practice\Poems\my_handle\finally_csv\两汉.csv'
    #
    # path_list = [
    #     'E:\practice\Poems\my_handle\git3_csv\先秦.csv'    #改朝代
    # ]
    # path = r'E:\practice\Poems\my_handle\finally_csv\先秦.csv'
    #
    # path_list=['E:\practice\Poems\my_handle\git3_csv\金.csv'] #改朝代
    # path = r'E:\practice\Poems\my_handle\finally_csv\金朝.csv'
    #
    # path_list = ['E:\practice\Poems\my_handle\git3_csv\近现代.csv']
    # path = r'E:\practice\Poems\my_handle\finally_csv\近现代.csv'

    # path_list = ['E:\practice\Poems\my_handle\git3_csv\辽.csv']
    # path = r'E:\practice\Poems\my_handle\finally_csv\辽.csv'

    # path_list = ['E:\practice\Poems\my_handle\git3_csv\隋.csv']
    # path = r'E:\practice\Poems\my_handle\finally_csv\隋代.csv'

    path_list = ['E:\practice\Poems\my_handle\git3_csv\魏晋.csv']
    path = r'E:\practice\Poems\my_handle\finally_csv\魏晋.csv'
    handle_git23_same_dynasty(path_list,path)
