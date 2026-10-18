# 🚀 Agent Post-Training Pipeline

End-to-end SFT and DPO training scripts optimized for multi-turn reasoning and structured tool use. This repository includes synthetic trajectory generators that intentionally inject edge cases (like malformed JSON and missing parameters) to bulletproof your agents against real-world errors.

## 🛠️ What's Inside
- **`synthetic_generator.py`**: Builds multi-turn reasoning traces (`Reason -> Action -> Observation`) with built-in edge cases for robust error-recovery training.
- **`train_dpo.py`**: Direct Preference Optimization setup to penalize hallucinations, infinite loops, and parameter guessing while rewarding efficient execution.

## 📦 Quickstart

1. Clone the repo and install dependencies:
   ```bash
   git clone [https://github.com/1994-munk/agent-post-training-pipeline.git](https://github.com/1994-munk/agent-post-training-pipeline.git)
   cd agent-post-training-pipeline
   pip install -r requirements.txt
