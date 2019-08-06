import os


def handle_repeat_poem(path_list):

    for file in path_list:
        data1 = []
        data2 = []
        a = 0
        print('正在处理--%s---文件' % file)
        path = r'E:\practice\Poems\my_handle\finally_csv\%s' % file
        with open(path,'r',encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                a += 1
                print('正在读取%s文件的第%s行'% (file,a))
                data1.append(line)
        for i in data1:
            if i not in data2:
                data2.append(i)
        print('%s文件转换前后的长度：%s----%s' % (file,len(data1),len(data2)))
        for line2 in data2:
            with open(r'E:\practice\Poems\my_handle\finally_csv_after_repeat\%s'% file,'a',encoding='utf-8') as f2:
                f2.write(line2)



if __name__ == '__main__':
    path_list = os.listdir(r'E:\practice\Poems\my_handle\finally_csv')
    handle_repeat_poem(path_list)
    #宋代.csv文件转换前后的长度：445189----445125
    #明代.csv文件转换前后的长度：236051----236037
    #清代.csv文件转换前后的长度：89758 - ---89747
    #清末民国初.csv文件转换前后的长度：15367----15367
    #清末近现代初.csv文件转换前后的长度：12464----12464
    #近现代.csv文件转换前后的长度：28430----28145

