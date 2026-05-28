#!/bin/bash

# Common variables
PROJECT_ROOT="/home/felix_jaspersen/Repositories/HEBO/MCBO" 
PARTITION="oahu"
CONDA_DIR="/home/felix_jaspersen/miniconda3/etc/profile.d/conda.sh"
CONDA_ENV="mcbo_env" 
LOG_DIR="${PROJECT_ROOT}/slurm_logs"
RESULT_DIR="${PROJECT_ROOT}/results"

# Experiment variables
SEEDS="42 43 44"
# TASKS=("ackley-53" "svm_opt" "xgboost_opt" "aig_optimization_hyp")
TASKS=("Func3C")

for task in "${TASKS[@]}"; do
    # BO methods
    for model in gp_to ; do
        for acq_opt in is ; do
            acq_func="ei"
            for tr in "basic" ; do
                opt_id="${model}__${acq_opt}__${acq_func}__${tr}"

                JOB_NAME="mcbo_${task}_${tr}"
                echo "Queuing experiment: $JOB_NAME with opt_id: $opt_id"

                sbatch <<EOF
#!/usr/bin/bash
#SBATCH -J $JOB_NAME
#SBATCH -p $PARTITION
#SBATCH -c 4
#SBATCH -t 04:00:00
#SBATCH --gres=gpu:1
#SBATCH --mem=8gb
#SBATCH --output=${LOG_DIR}/%J-${JOB_NAME}.out

source $CONDA_DIR
conda activate $CONDA_ENV

cd $PROJECT_ROOT

# The native script handles the looping over seeds internally!
# The -u unbuffered flag lets you see print statements in the live slurm logs.
python -u experiments/run_task_exps.py \\
    --task_id $task \\
    --optimizers_ids $opt_id \\
    --seeds $SEEDS \\
    --result_dir ${RESULT_DIR} \\
    --verbose 2
EOF

            done
        done
    done

    # Non-BO methods
    # for opt_id in ga sa rs hc; do
    #     cmd="python ./experiments/run_task_exps.py --device_id 0 --task_id $task --optimizers_ids $opt_id --seeds $SEEDS"
    #     $cmd
    # done
done
