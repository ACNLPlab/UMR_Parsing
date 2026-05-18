# UMR_Parsing

Best BiBL checkpoint: https://drive.google.com/file/d/1eoxzvzaRXxgC79mCXmb_W6sfcCYFKZyo/view
Best T5 checkpoint: https://drive.google.com/drive/folders/1f3wrRA7HciQSr3OUHyPGYK0avZcGRiPY?usp=sharing

## How to use our best model:
To begin, either download the BiBL repo (https://github.com/KHAKhazeus/BiBL) or our BiBL directory from this repo.
First, download the checkpoint from the link  and move it to BiBL/best_ckpt.
Then, create a conda env using BiBl/bibl_env.yml or the .yml from BiBL's repo.
Next, create a test file in the format found in test.txt.
Finally, run bibl_inf.sh to genreate UMR graphs. Remember to change it to point to your files and the correct checkpoint.

## How to use our T5 model:
To use our T5 model, first download the UD-to-UMR pipeline repo (https://github.com/fjambe/UD2UMR). 
Then, follow this repo's guidelines to create partial UMRs.
Now, dowload our model checkpoint from the Google Drive link above and our code from our T5 directory.
Next, use our file test_ckpt.py to generate the completed versions of these UMRs.



