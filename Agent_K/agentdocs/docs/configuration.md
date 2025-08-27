# 🔁 Reproducing Results
Here are some guidelines to reproduce the results from the paper. Below the commands, there is a table of values that were used to produce the results in the paper.

**⚠️ Note: If values for some arguments are not provided, it’s up to the user to define them — they do not impact the final results.**

* Each of the experiments were run for two attempts.
* For Agent K non tabular classification competition were run with class imabalance and once without class imbalance.

## 🤖 Agent K Runs
For Agent K total 81 competitions were run. The list of competitions can be seen on the [Benchmark set](benchmark.md).
Here are the details about the configuration of the Agent K runs.
### 📊 Tabular Tasks
Around 55% of the total tasks are tabular tasks. In the [Benchmark table](benchmark.md) these tasks are the ones with only "Tab" in the modality column.
Each task was run with a maximum time limit of 24 hours on 8 cpus. Here is how to run the tabular tasks.

```bash
ALT_RAW_DATA_ROOT=... 
CPU_RANGE=...  # we used 8 cpus for our experiments
TASK_ID=... 
ATTEMPT=... 
WORKSPACE_NAME=... 
TIME_LIMIT_SECONDS=86400
MODEL_ID=qwen2.5-72b 
taskset -c $CPU_RANGE python run_complete_pipeline.py \
  --task_id $TASK_ID \
  --prep_task data_preprocessing \
  --prep_method data-prep-flow \
  --ds_method agent-k-solve \
  --llm $MODEL_ID \
  --code-llm $MODEL_ID \
  --total_time $TIME_LIMIT_SECONDS \
  --tabular-task \
  --attempt $ATTEMPT \
  --max_cpu 8 \
  --workspace_name $WORKSPACE_NAME
```

🖼️📚 Running Non-Tabular (CV/NLP/Multimodal) Competitions
```bash
MAX_TIME_PER_SUBMISSION_SECONDS=... 
ALT_RAW_DATA_ROOT=... 
TASK_ID=... 
ATTEMPT_SPEC=... 
ATTEMPT=... 
TIME_LIMIT_SECONDS=172800
MODEL_ID=qwen2.5-72b
BLEND_AFTER_N=3
python run_complete_pipeline.py \
  --task_id=$TASK_ID \
  --prep_task=data_preprocessing \
  --prep_method=data-prep-flow \
  --ds_method=agent-k-solve \
  --llm=$MODEL_ID \
  --code-llm=$MODEL_ID \
  --total_time=$TIME_LIMIT_SECONDS \
  --attempt_spec=$ATTEMPT_SPEC \
  --attempt=$ATTEMPT \
  --alt_raw_data_root=$ALT_RAW_DATA_ROOT \
  --max_time_per_submission=$MAX_TIME_PER_SUBMISSION_SECONDS \
  --blend_after_n=$BLEND_AFTER_N

```
**Note: To run with class imbalance use flag `--use_ci_handling`**

## 🦾 ReAct Agent Runs

### 🤖 ReAct Agent (No RAG) 
```bash
TASK_ID=... 
TOP_N=... 
MIN_EXEC_TIME_SECONDS=... 
TIME_LIMIT_SECONDS=172800 (Tabular), 345600 (CV/NLP)
TIME_OUT_SECONDS=32400 (Tabular), 64800 (CV/NLP)
WORKSPACE_DIR=... 
MODEL_ID=Qwen/Qwen2.5-72B-Instruct 
DATA_DIR=... 
TOKENIZERS_PARALLELISM=False aide \
      data_dir=${DATA_DIR}/${TASK_ID} \
      exp_name="${TASK_ID}" \
      top_n="${TOP_N}" \
      agent.time_limit="${TIME_LIMIT_SECONDS}" \
      agent.min_exec_time="${MIN_EXEC_TIME_SECONDS}" \
      exec.timeout="${TIME_OUT_SECONDS}" \
      copy_data=false \
      workspace_dir="${WORKSPACE_DIR}" \
      agent.code.model="${MODEL_ID}" \
      agent.feedback.model="${MODEL_ID}" \
      agent.use_rag=False
```
### 📚 ReAct Agent + RAG
```bash
TASK_ID=... 
TOP_N=... 
MIN_EXEC_TIME_SECONDS=... 
TIME_LIMIT_SECONDS=172800 (Tabular), 345600 (CV/NLP)
TIME_OUT_SECONDS=32400 (Tabular), 64800 (CV/NLP)
WORKSPACE_DIR=... 
MODEL_ID=Qwen/Qwen2.5-72B-Instruct  
DATA_DIR=... 
TOKENIZERS_PARALLELISM=False aide \
      data_dir=${DATA_DIR}/${TASK_ID} \
      exp_name="${TASK_ID}" \
      top_n="${TOP_N}" \
      agent.time_limit="${TIME_LIMIT_SECONDS}" \
      agent.min_exec_time="${MIN_EXEC_TIME_SECONDS}" \
      exec.timeout="${TIME_OUT_SECONDS}" \
      copy_data=false \
      workspace_dir="${WORKSPACE_DIR}" \
      agent.code.model="${MODEL_ID}" \
      agent.feedback.model="${MODEL_ID}" \
      agent.use_rag=True
```

### 💡 ReAct Agent from COT
```bash
TASK_ID=... 
TOP_N=... 
MIN_EXEC_TIME_SECONDS=... 
TIME_LIMIT_SECONDS=172800 (Tabular), 345600 (CV/NLP)
TIME_OUT_SECONDS=32400 (Tabular), 64800 (CV/NLP)
WORKSPACE_DIR=... 
MODEL_ID=Qwen/Qwen2.5-72B-Instruct 
DATA_DIR=... 
$USE_AGENT_K_WARM_START=...
$AGENT_K_SUBMISSIONS=...
TOKENIZERS_PARALLELISM=False aide \
      data_dir=${DATA_DIR}/${TASK_ID} \
      exp_name="${TASK_ID}" \
      top_n="${TOP_N}" \
      agent.time_limit="${TIME_LIMIT_SECONDS}" \
      agent.min_exec_time="${MIN_EXEC_TIME_SECONDS}" \
      exec.timeout="${TIME_OUT_SECONDS}" \
      copy_data=false \
      workspace_dir="${WORKSPACE_DIR}" \
      agent.code.model="${MODEL_ID}" \
      agent.feedback.model="${MODEL_ID}" \
      agent.use_agent_k_warm_start=$USE_AGENT_K_WARM_START \
      agent.agent_k_submissions=$AGENT_K_SUBMISSIONS \
      agent.use_rag=False
```

### ⚡ ReAct Agent (DeepSeek)
From your `Project Root` and inside the `reactagent` environment
```bash
TASK_ID=... 
TOP_N=... 
MIN_EXEC_TIME_SECONDS=... 
TIME_LIMIT_SECONDS=172800 (Tabular), 345600 (CV/NLP)
TIME_OUT_SECONDS=32400 (Tabular), 64800 (CV/NLP)
WORKSPACE_DIR=... 
MODEL_ID=deepseek-reasoner 
DATA_DIR=... 
DEEPSEEK_API_KEY=<your-api-key> TOKENIZERS_PARALLELISM=False aide \
      data_dir=${DATA_DIR}/${TASK_ID} \
      exp_name="${TASK_ID}" \
      top_n="${TOP_N}" \
      agent.time_limit="${TIME_LIMIT_SECONDS}" \
      agent.min_exec_time="${MIN_EXEC_TIME_SECONDS}" \
      exec.timeout="${TIME_OUT_SECONDS}" \
      copy_data=false \
      workspace_dir="${WORKSPACE_DIR}" \
      agent.code.model="${MODEL_ID}" \
      agent.feedback.model="${MODEL_ID}" \
      agent.use_rag=False
```


For descriptions of each of the variables and arguments and additional information refer to [running ReAct](reactagent.md).