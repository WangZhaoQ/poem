import re

def join_xiandai_jindai():
    file_list = [
        r'E:\practice\Poems\my_handle\author\git1_gushi_writer_csv\近代.csv',
        r'E:\practice\Poems\my_handle\author\git1_gushi_writer_csv\现代.csv'
    ]
    a =0
    for file in file_list:
        with open(file,'r+',encoding='utf-8') as f1:
            lines = f1.readlines()
            for line in lines:
                a+=1
                print('正在读入第%s行'%a)
                new_line = re.split(r',', line)
                # title = re.sub('"', '', new_line[1])
                # dynasty = re.sub('"','',new_line[1])
                dynasty = '近现代'
                writer = re.sub('"', '', new_line[0])
                # content_1 = re.sub('"', '', new_line[3])
                # content = re.sub(r'\n', '', str(content_1))
                # type = str(re.sub('"','',new_line[4]))
                # remark = str(re.sub('"','',new_line[5]))
                # shangxi = str(re.sub('"','',new_line[6]))
                # translation = str(re.sub('"','',new_line[7]))
                # dynasty = re.sub('"','',new_line[1])
                with open(r'E:\practice\Poems\my_handle\author\git1_gushi_writer_csv\近现代.csv','a',encoding='utf-8') as f2:
                    f2.write(
                    '"' + writer + '"' + ',' + '"' + dynasty + '"' + '\n')

if __name__ == '__main__':
    join_xiandai_jindai()