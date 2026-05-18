from transformers import pipeline
import json
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments
from datasets import Dataset, load_dataset
import os

# 1. Load your fine-tuned model
checkpoint_path = "/home/common/ACNLP/umr_parsing/ud2umr/UD2UMR/output/umr_t5_output/checkpoint-30070"  # or your checkpoint directory
tokenizer = T5Tokenizer.from_pretrained(checkpoint_path)
model = T5ForConditionalGeneration.from_pretrained(checkpoint_path)

# 2. Create pipeline
umr_pipeline = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    device=0 if torch.cuda.is_available() else -1
)

# 3. Load test data
with open("t5_test_data.json") as f:
    test_data = json.load(f)

# 4. Generate predictions
results = []
for example in test_data:
    try:
        output = umr_pipeline(
            example["input"],
            max_length=1024,
            num_beams=3,  # Better quality than greedy search
            early_stopping=True
        )[0]["generated_text"]
        
        results.append({
            "input": example["input"],
            "prediction": output,
            "target": example.get("target", "")
        })
    except Exception as e:
        print(f"Error processing: {example['input']}")
        print(f"Error: {str(e)}")
        results.append({
            "input": example["input"],
            "prediction": "ERROR",
            "target": example.get("target", "")
        })

# 5. Save results
with open("t5_test_results.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"Saved predictions to t5_test_results_10epochs.json")
