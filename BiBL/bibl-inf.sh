#!/bin/sh
#SBATCH --job-name=bibl_generator
#SBATCH --output=bibl_generator_%j.out
#SBATCH --error=bibl_generator_%j.err
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G

source /cm/shared/apps/amh-conda/etc/profile.d/conda.sh
conda activate base
conda activate BIBL

unset PYTHONPATH

#INPUT_FILE="/home/common/ACNLP/umr_parsing/umr_data/test_sentences/gt_eng_test_bibl.txt"
#INPUT_FILE="/home/common/ACNLP/umr_parsing/data4pipe/data/eng-umr1-FULL.txt"
INPUT_FILE="/home/common/ACNLP/eng2nav/chrf_bibl_sents.txt"

filename=$(basename "$INPUT_FILE")
dataset_name=$(echo "$filename")  

OUTPUT_FILE="/home/common/ACNLP/eng2nav/chrf_eng_umrs.txt"

GOLD_FILE="/home/common/ACNLP/umr_parsing/BiBL/gold-file.txt"

python /home/common/ACNLP/umr_parsing/BiBL/bin/predict_amrs.py \
    --datasets "$INPUT_FILE" \
    --gold-path "$GOLD_FILE" \
    --pred-path "$OUTPUT_FILE" \
    --checkpoint /home/common/ACNLP/umr_parsing/BiBL/runs/10/best-smatch_checkpoint_2_0.3371.pt \
    --beam-size 3 \
    --batch-size 100 \
    --device cuda \
    --penman-linearization --use-pointer-tokens


