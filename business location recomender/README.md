# business location recomender

Project created with MLOps-Template cookiecutter. For more info: https://mlopsstudygroup.github.io/mlops-guide/


## 📋 Requirements

* DVC
* Python3 and pip
* Access to IBM Cloud Object Storage

## 🏃🏻 Running Project


pip install -r requirements.txt


### 🔑 Setup IBM Bucket Credentials for IBM COS

#### MacOS and Linux
Setup your credentials on ```~/.aws/credentials``` and ```~/.aws/config```. DVC works perfectly with IBM Obejct Storage, although it uses S3 protocol, you can also see this in other portions of the repository.


~/.aws/credentials

```credentials
[default]
aws_access_key_id = {Key ID}
aws_secret_access_key = {Access Key}
```


### ✅ Pre-commit Testings

In order to activate pre-commit testing you need ```pre-commit```

Installing pre-commit with pip
```
pip install pre-commit
```

Installing pre-commit on your local repository. Keep in mind this creates a Github Hook.
```
pre-commit install
```

Now everytime you make a commit, it will run some tests defined on ```.pre-commit-config.yaml``` before allowing your commit.

**Example**
```
$ git commit -m "Example commit"

black....................................................................Passed
pytest-check.............................................................Passed
```


### ⚗️ Using DVC

Download data from the DVC repository(analog to ```git pull```)
```
dvc pull
```

Reproduces the pipeline using DVC
```
dvc repro
```

```
Запуск проекта:
```

1. В папку src.data забросить интересы пользователей по интересуемому городу
