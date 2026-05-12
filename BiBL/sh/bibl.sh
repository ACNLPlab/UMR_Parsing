#!/bin/sh
#SBATCH --job-name=bibl_inference
#SBATCH --output=bibl_inference_%j.out
#SBATCH --error=bibl_inference_%j.err
#SBATCH --cpus-per-task=30

DATASET_FOLDER="/home/common/ACNLP/umr_parsing/umr_data/test_sentences"

for input_file in ${DATASET_FOLDER}/*.txt; do
    filename=$(basename "$input_file")
    dataset_name=$(echo "$filename" | grep -oP "test-\K[^_]+")
    output_file="/home/common/ACNLP/umr_parsing/BiBL/outputs/${dataset_name}.txt"

    srun python /home/common/ACNLP/umr_parsing/BiBL/bin/predict_amrs.py \
        --datasets "$input_file" \
        --gold-path gold-file.txt \
        --pred-path "$output_file" \
        --checkpoint /home/common/ACNLP/umr_parsing/BiBL/bibl_checkpoints/amr3_text.pt \
        --beam-size 5 \
        --batch-size 500 \
        --device cpu \
        --penman-linearization --use-pointer-tokens
done

wait
