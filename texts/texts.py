import glob

files = glob.glob('*.txt')
file_dict = dict()

for file in files:
    with open(file) as f:
        lines = 0
        for line in f:
            lines += 1
    file_dict.update({lines: file})

dict_sorted = sorted(file_dict)

with open('result.txt', 'w') as result:
    for str_len in dict_sorted:
        text_sorted = file_dict[str_len]
        with open(text_sorted) as f:
            result.write("Дан файл " + str(text_sorted) + ', \n' + "в котором количество строк: " + str(str_len) + '\n' + f.read() + '\n' + '\n')
