import jsonlines,json,time,re


writer_data = []
writer_data_dict = {}
with open(r"E:\practice\Poems\my_handle\author\git2_writer_jianti\authors_song.json", "r+", encoding="utf8") as f:
    # for item in jsonlines.Reader(f):
    #      print(item)
    file = json.load(f)
    for i in file:
        # print(i)
        # print(type(i))
        name = str(i.get('name'))
        headImageUrl = str(i.get('headImageUrl'))
        # simpleIntro = str(i.get('simpleIntro'))
        # detailIntro = re.sub(r'\n', '',str(i.get('detailIntro')))
        simple_intro = re.sub(r'\.', '。', re.sub(r',', '，', re.sub(r'\\n', '', str(i.get('simpleIntro')))))
        detailIntro = re.sub(r'\.', '。', re.sub(r',', '，', re.sub(r'\\n', '', str(i.get('detailIntro')))))
        print(simple_intro)
        print(detailIntro)

        time.sleep(3)