import os
downloaded_files = os.listdir("./vids")
for i in range(12):
	fpath = "ava_file_names_trainval_v2.1_{}.txt".replace("{}", str(i))
	lines = []
	with open(fpath) as fr:
		for l in fr:
			if l.strip() not in downloaded_files:
				lines.append(l)
	with open(fpath.replace(".txt", ".2.txt"), "w") as fw:
		fw.writelines(lines)