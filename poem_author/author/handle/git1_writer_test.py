import jsonlines,json,time,re


writer_data = []
writer_data_dict = {}
with open(r"E:\practice\Poems\my_handle\author\git1_writer\writer0-1000.json", "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
         print(item)
         print(type(item))
         time.sleep(3)