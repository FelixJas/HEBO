# 🧠 Installing Agent K

Clone the Agent K repository:

    ```bash
    git clone --depth=1 --branch ajar https://gitlab-uk.rnd.huawei.com/ai-uk-team/reinforcement_learning_london/pangu-agent/agent.git
    cd agent
    ```

### 📦 Creating the Environment

1. Create an environment named `agent`.

    ```bash
    conda create -n agent python=3.11
    ```

2. Save Python executable path.

    ```bash
    conda activate agent
    which python > ./third_party/agent_k_python_path.txt
    ```

3. Install the required packages.

    ```bash
    pip install -e .[datascience]
    pip install -e ./third_party/ds-agent/
    ```

Packages required for running tabular tasks.

1. Installing ramp-hyperopt

   ```bash
    pip install git+https://rnd-gitlab-eu.huawei.com/Noahs-Ark/libraries/ramp-hyperopt.git@fe
   ```

2. Installing ramp-workflow

    ```bash
    pip install git+https://rnd-gitlab-eu.huawei.com/Noahs-Ark/libraries/ramp-workflow.git@generative_regression_clean
    ```

Installing geckodriver

- Download a release of geckodriver using the following command.

`wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz`

- unzip the file using the following command.

`tar -xvzf geckodriver-v0.32.0-linux64.tar.gz`

- set the path in your .bashrc file

`export PATH=$PATH:/path/to/your/geckodriverdirectory/geckodriver*`

### 🏅 Setting Up Kaggle

1. install kaggle in your environment
   `pip install kaggle`.
2. Create an API Token on https://www.kaggle.com/<username>/account. This will trigger download for kaggle.json file.
3. Place this file in the appropriate directory depending on your operating system. For linux the default path is
   `~/.config/kaggle/kaggle.json`.
4. For more follow the steps in installation and API credentials section
   on https://github.com/Kaggle/kaggle-api/tree/main/docs.

   #### 🔐 Adding Login Details
   Inside `./third_party/data_preprocessing` create a json file named `kaggle_login_details.json` in the following
   format.

    ```
    {
       "username": "",
       "email": "",
       "pwd": ""
    }
    ```

### 📂 Setting Up Raw Data Paths

This is the directory where when trying a new competition Agent K downloads the raw data for the competition.
This data will be later used during the setup stage and in the main pipeline.

- create a file in `/path/to/your/agent_k_directory` named `root_path_to_raw_ds_data.txt` fill it with the path to the
  directory where you want your raw data to be saved.

```shell
RAW_DATA_PATH=...
echo $RAW_DATA_PATH > ./root_path_to_raw_data.txt
```
