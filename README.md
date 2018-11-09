# cookiecutter-kaggle

- Kaggle用テンプレート

## ディレクトリ構成

```
{{cookiecutter.project_name}}
├── Dockerfile
├── README.md
├── requirements.txt
└── src
    ├── conf
    │   ├── logging.conf
    │   └── my_package.cfg.org
    ├── run.py
    ├── tests
    └── {{cookiecutter.project_name}}
        ├── __init__.py
        ├── api
        │   ├── __init__.py
        │   ├── classes
        │   │   └── users.py
        │   ├── func1.py
        │   ├── func2.py
        │   └── users.py
        ├── app.py
        ├── config.py
        └── models
            ├── __init__.py
            └── users.py
```
