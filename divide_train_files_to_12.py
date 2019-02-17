file_path = "/home/bassel/PycharmProjects/ava-dataset-tool/video/trainval/ava_file_names_trainval_v2.1.txt"

with open(file_path) as fr:
    lines = fr.readlines()

nThreads=12
bSize = int(len(lines)/nThreads)

file_name = "/home/bassel/PycharmProjects/ava-dataset-tool/video/trainval/ava_file_names_trainval_v2.1_##.txt"
for i in range(nThreads):
    start = bSize*i
    end = start+bSize

    if i == nThreads-1:
        end = len(lines)

    with open(file_name.replace("##", str(i)), 'w') as fw:
        fw.writelines(lines[start:end])

