#! /bin/bash

#SBATCH --job-name=ckpt
#SBATCH --partition=gpu-a100-q
#SBATCH --gres=gpu:a100:1
#SBATCH --cpus-per-task=16
#SBATCH --mem=80G
#SBATCH --output=%j.out
#SBATCH --error=%j.err

# Load conda
source /cm/shared/apps/amh-conda/etc/profile.d/conda.sh
conda activate base
conda activate /home/common/ACNLP/conda_envs/conda-bibl-ft

# Optional: cd to BiBL root if needed
cd /home/common/ACNLP/umr_parsing/BiBL

# Run the training script
bash sh/train_amr-g_1-r_0_5.sh

