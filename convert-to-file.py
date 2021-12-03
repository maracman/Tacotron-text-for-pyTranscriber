import os
from operator import itemgetter

folder_loc = str(input("enter pyTransciber output location (containing your .txt files): "))
new_file = str(folder_loc) + "/combined.txt"
name_content = []
for filename in os.listdir(folder_loc):
    if filename.endswith('.txt'):
        file = open(os.path.join(folder_loc, filename))
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        new_line = ' '.join(lines)
        print(new_line)
        wav_file = str(os.path.splitext(filename)[0])
        name_content.append([str(new_line), wav_file])

name_content = sorted(name_content, key = itemgetter(1))

with open(new_file, 'w') as f:
    for line in name_content:
        wav_file = str(line[1]) + '.wav'
        f.write('wavs/' + wav_file + '|' + str(line[0]) + '.\n')


