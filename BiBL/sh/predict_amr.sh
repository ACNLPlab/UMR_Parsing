#!/bin/sh
rm -rf /home/common/ACNLP/umr_generation/BiBL/predict_amr.log; CUDA_VISIBLE_DEVICES=0 python -u /home/common/ACNLP/umr_parsing/BiBL/bin/predict_amrs.py \
    --datasets /home/common/ACNLP/umr_parsing/umr_data/test_sentences/gt_eng_test_bibl2.txt \
    --gold-path /home/common/ACNLP/umr_parsing/umr_data/test_sentences/gt_eng_test_bibl2.txt \
    --pred-path /home/common/ACNLP/umr_parsing/BiBL/pred.txt \
    --checkpoint /home/common/ACNLP/umr_parsing/BiBL/bibl_checkpoints/amr3_text.pt \
    --beam-size 5 \
    --batch-size 500 \
    --device cuda \
    --penman-linearization --use-pointer-tokens > ./predict_amr.log 2>&1
