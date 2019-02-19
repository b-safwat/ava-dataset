def generate_sbatch(size, num):

    for i in range(num):
        start = i * size
        end = start + size

        print("sbatch run_extract_frames.sh {} {} ava_val_v2.1.csv".format(start, end))

generate_sbatch(59285, 4)