# Marconi benchmark commands

These are the exact commands used to benchmark the `Qwen/Qwen3-Next-80B-A3B-Instruct` setup via the autoresearch harness.

Note: replace `<YOUR_HF_TOKEN>` with your own Hugging Face token before running.

## Main branch baseline

This uses the separate main worktree at `/workspace/sglang-main` and forces plain LRU eviction.

```bash
cd /workspace/autoresearch && \
HF_TOKEN='<YOUR_HF_TOKEN>' \
HUGGING_FACE_HUB_TOKEN='<YOUR_HF_TOKEN>' \
SGLANG_REPO=/workspace/sglang-main \
MARCONI_MODEL_PATH='Qwen/Qwen3-Next-80B-A3B-Instruct' \
MARCONI_TP_SIZE=4 \
MARCONI_MIN_GPUS=4 \
MARCONI_EVAL_MODE=full \
MARCONI_CONTEXT_LENGTH=32768 \
MARCONI_RESULTS_DIR=/workspace/autoresearch/results \
MARCONI_RADIX_EVICTION_POLICY=lru \
/venv/main/bin/python train.py
```

## Marconi with autotune enabled

This uses the `marconi-eviction` branch at `/workspace/sglang` and leaves autotune enabled.

```bash
cd /workspace/autoresearch && \
HF_TOKEN='<YOUR_HF_TOKEN>' \
HUGGING_FACE_HUB_TOKEN='<YOUR_HF_TOKEN>' \
SGLANG_REPO=/workspace/sglang \
MARCONI_MODEL_PATH='Qwen/Qwen3-Next-80B-A3B-Instruct' \
MARCONI_TP_SIZE=4 \
MARCONI_MIN_GPUS=4 \
MARCONI_EVAL_MODE=full \
MARCONI_CONTEXT_LENGTH=32768 \
MARCONI_RESULTS_DIR=/workspace/autoresearch/results \
/venv/main/bin/python train.py
```

## Marconi with autotune disabled

### Fixed `eff_weight=1.0`

```bash
cd /workspace/autoresearch && \
HF_TOKEN='<YOUR_HF_TOKEN>' \
HUGGING_FACE_HUB_TOKEN='<YOUR_HF_TOKEN>' \
SGLANG_REPO=/workspace/sglang \
MARCONI_MODEL_PATH='Qwen/Qwen3-Next-80B-A3B-Instruct' \
MARCONI_TP_SIZE=4 \
MARCONI_MIN_GPUS=4 \
MARCONI_EVAL_MODE=full \
MARCONI_CONTEXT_LENGTH=32768 \
MARCONI_RESULTS_DIR=/workspace/autoresearch/results \
MARCONI_EXTRA_SERVER_ARGS='--marconi-eff-weight 1.0 --disable-marconi-autotune' \
/venv/main/bin/python train.py
```

### Fixed `eff_weight=0.5`

```bash
cd /workspace/autoresearch && \
HF_TOKEN='<YOUR_HF_TOKEN>' \
HUGGING_FACE_HUB_TOKEN='<YOUR_HF_TOKEN>' \
SGLANG_REPO=/workspace/sglang \
MARCONI_MODEL_PATH='Qwen/Qwen3-Next-80B-A3B-Instruct' \
MARCONI_TP_SIZE=4 \
MARCONI_MIN_GPUS=4 \
MARCONI_EVAL_MODE=full \
MARCONI_CONTEXT_LENGTH=32768 \
MARCONI_RESULTS_DIR=/workspace/autoresearch/results \
MARCONI_EXTRA_SERVER_ARGS='--marconi-eff-weight 0.5 --disable-marconi-autotune' \
/venv/main/bin/python train.py
```
