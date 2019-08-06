import jsonlines,time
import re

data = []
dynasty_list = []
path_list = [
            "E:\practice\Poems\chinese-gushiwen-1\guwen\guwen0-1000.json",
            "E:\practice\Poems\chinese-gushiwen-1\guwen\guwen1001-2000.json",
            "E:\practice\Poems\chinese-gushiwen-1\guwen\guwen2001-3000.json",
            "E:\practice\Poems\chinese-gushiwen-1\guwen\guwen3001-4000.json",
            "E:\practice\Poems\chinese-gushiwen-1\guwen\guwen4001-5000.json",
            "E:\practice\Poems\chinese-gushiwen-1\guwen\guwen5001-6000.json",
            "E:\practice\Poems\chinese-gushiwen-1\guwen\guwen6001-7000.json",
            "E:\practice\Poems\chinese-gushiwen-1\guwen\guwen7001-8000.json",
            "E:\practice\Poems\chinese-gushiwen-1\guwen\guwen8001-9000.json",
            "E:\practice\Poems\chinese-gushiwen-1\guwen\guwen9001-10000.json"
]
a = 0
for path in path_list:
    a += 1
    with open(path, "r+", encoding="utf8") as f:
        for item in jsonlines.Reader(f):
            # new_item = re.sub(r'\\N', '""',item)
            data.append(item)
    length_data = len(data)
    print(length_data)
    b = 0
for i in data:
    b += 1
    print('正在载入第%s文件第%s行.....' % (a,b))
    title = str(i.get('title'))
    dynasty = str(i.get('dynasty'))
    writer = str(i.get('writer'))
    content = re.sub(r'\n', '',str(i.get('content')))
    type_list = i.get('type')
    type = re.sub(r'\n', '',str('，'.join(type_list)))
    remark = re.sub(r'\n','',str(i.get('remark')))
    translation = re.sub(r'\n','',str(i.get('translation')))
    shangxi = re.sub(r'\n','',str(i.get('shangxi')))
    if type == 'None':
        type = ''
    if remark == 'None':
            remark = ''
    if translation == 'None':
        translation = ''
    if shangxi == 'None':
        shangxi = ''

    dynasty_list = ['唐代', '宋代', '魏晋', '近代', '南北朝', '先秦', '元代', '五代', '两汉', '现代', '清代', '明代', '金朝', '未知', '隋代', '当代']

    # with open(r'E:\practice\Poems\my_handle\finally_csv\%s.csv'% dynasty, 'a+',encoding='utf-8') as f:
        # f.write(
        #             '"' + title + '"' + ',' + '"' + dynasty + '"' + ',' + '"' + writer + '"' + ',' + '"' + content + '"' +
        #             ',' + '"' + type + '"' + ',' + '"' + remark + '"' + ',' + '"' + shangxi + '"' + ',' + '"' + translation + '"' +'\n')
        #
    with open(r'E:\practice\Poems\my_handle\author\git1_gushi_writer_csv\%s.csv'% dynasty, 'a+',encoding='utf-8') as f:

        f.write(
            '"' + title + '"' + ',' + '"' + dynasty + '"' + ',' + '"' + writer + '"' +  '\n')
