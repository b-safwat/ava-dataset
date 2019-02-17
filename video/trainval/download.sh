#!/bin/sh

#SBATCH --job-name=download_ava
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=20:15:00


ava_url="https://s3.amazonaws.com/ava-dataset/trainval/"

while read p; do
  echo $p
  echo $ava_url$p -O;
  curl $ava_url$p -O;
done <$1