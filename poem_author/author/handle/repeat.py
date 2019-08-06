import os
import time

def handle_repeat_poem(path_list):

    for file in path_list:
        data1 = []
        data2 = []
        a = 0
        print('正在处理--%s---文件' % file)
        path = r'E:\practice\Poems\my_handle\author\git3_finally_csv\%s' % file
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
        time.sleep(10)
        for line2 in data2:
            with open(r'E:\practice\Poems\my_handle\author\writer_finally_csv\%s'% file,'a',encoding='utf-8') as f2:
                f2.write(line2)



if __name__ == '__main__':
    # path_list = os.listdir(r'E:\practice\Poems\my_handle\author\git3_finally_csv')
    # handle_repeat_poem(path_list)
#  两汉.csv文件转换前后的长度：536----127
#五代.csv文件转换前后的长度：58----14
#元代.csv文件转换前后的长度：37514----1265
#元末明初.csv文件转换前后的长度：15736----79
#先秦.csv文件转换前后的长度：798----42
#南北朝.csv文件转换前后的长度：4764----473
#唐代.csv文件转换前后的长度：85558----8681
#宋代.csv文件转换前后的长度：455875----22286

#宋末元初.csv文件转换前后的长度：12055----41
#当代.csv文件转换前后的长度：28127----191
#明代.csv文件转换前后的长度：236947----4616
#明末清初.csv文件转换前后的长度：17700----176
#未知.csv文件转换前后的长度：6077----2060
#清代.csv文件转换前后的长度：90588----9052
#清末民国初.csv文件转换前后的长度：15367----99
#清末近现代初.csv文件转换前后的长度：12464----48
#秦.csv文件转换前后的长度：2----2
#辽.csv文件转换前后的长度：22----7
#近现代.csv文件转换前后的长度：28318----984
#近现代末当代初.csv文件转换前后的长度：3426----23
#金末元初.csv文件转换前后的长度：3019----17
#隋末唐初.csv文件转换前后的长度：472----40
#魏晋末南北朝初.csv文件转换前后的长度：1----1
 # 金朝.csv文件转换前后的长度：1745 - ---257
#隋代.csv文件转换前后的长度：1092----88
#魏晋.csv文件转换前后的长度：2017----265
