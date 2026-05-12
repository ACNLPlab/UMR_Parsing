#! /bin/sh

#SBATCH --job-name=bibl-train
#SBATCH --partition gpu-a100-q
#SBATCH --gres=gpu:a100:1
#SBATCH --cpus-per-task=16
#SBATCH --mem=80G
#SBATCH --output %j.out
#SBATCH --error %j.err

source /cm/shared/apps/amh-conda/etc/profile.d/conda.sh
conda activate base
conda activate /home/common/ACNLP/conda_envs/conda-spring

# Clear any existing Python path and set only the correct directory
export PYTHONPATH=/home/common/ACNLP/umr_parsing/BiBL
cd /home/common/ACNLP/umr_parsing/BiBL/

python -u bin/train.py --config configs/config.yaml --direction amr --save_dir runs_umr2
