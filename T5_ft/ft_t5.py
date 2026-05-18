import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments
from datasets import Dataset, load_dataset
import json
import os

os.environ["WANDB_DISABLED"] = "true"

# 1. Load and prepare dataset
def load_umr_dataset(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return {"input": [x["input"] for x in data], 
            "target": [x["target"] for x in data]}

# 2. Initialize model and tokenizer
model_name = "t5-base"  # or "t5-base", "t5-large" based on your resources
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# 3. Dataset preprocessing
def preprocess_function(examples):
    model_inputs = tokenizer(
        examples["input"],
        max_length=1024,
        truncation=True,
        padding="max_length"
    )
    
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(
            examples["target"],
            max_length=1024,
            truncation=True,
            padding="max_length"
        )
    
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# 4. Load datasets
train_data = load_umr_dataset("t5_train_data.json")
val_data = load_umr_dataset("t5_dev_data.json")

train_dataset = Dataset.from_dict(train_data).map(preprocess_function, batched=True)
val_dataset = Dataset.from_dict(val_data).map(preprocess_function, batched=True)

# 5. Training arguments
training_args = TrainingArguments(
    output_dir="./umr_t5_output",
    evaluation_strategy="epoch",
    learning_rate=4e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=10,
    weight_decay=0.01,
    save_total_limit=3,
    logging_dir='./logs',
    logging_steps=100,
    save_strategy="epoch",
    load_best_model_at_end=True
)

# 6. Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer
)

# 7. Start training
trainer.train()

# 8. Save the model
model.save_pretrained("./umr2_t5_final")
tokenizer.save_pretrained("./umr2_t5_final")
