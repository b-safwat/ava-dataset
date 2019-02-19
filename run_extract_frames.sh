#!/bin/sh

#SBATCH --job-name=extract_ava_frames
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=20:15:00

python extract_keyframe.py --video_dir video/trainval/vids
