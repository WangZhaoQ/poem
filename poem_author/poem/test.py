


csvfile = open(r'E:\practice\mayun_project\poem_author_handle\poem_author\poem\poem_finally_csv_after_repeat\宋代.csv', 'r',encoding='utf-8').readlines()
filename = 1
for i in range(len(csvfile)):
    if i % 250000 == 0:
        open(str(filename) + '.csv', 'a+',encoding='utf-8').writelines(csvfile[i:i+250000])
        filename += 1