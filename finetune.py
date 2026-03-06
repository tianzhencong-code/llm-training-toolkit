# StarCoder Fine-tuning Script
# ============================
# This file is sourced from the bigcode-project/starcoder repository.
#
# Original location:
#   https://github.com/bigcode-project/starcoder/blob/main/finetune/finetune.py
#
# To get the full original script, run:
#   curl -O https://raw.githubusercontent.com/bigcode-project/starcoder/main/finetune/finetune.py
#
# About StarCoder:
#   StarCoder is a code generation model developed by the BigCode project.
#   The fine-tuning script demonstrates how to adapt the model for specific
#   coding tasks using techniques like LoRA and PEFT.
#
# Dependencies (from the starcoder repo requirements.txt):
#   - transformers
#   - datasets
#   - peft
#   - accelerate
#   - torch
#
# Usage:
#   python finetune.py \
#     --model_path="bigcode/starcoder" \
#     --dataset_name="your-dataset" \
#     --output_dir="./checkpoints" \
#     --num_train_epochs=3
#
# For more information, visit: https://github.com/bigcode-project/starcoder
