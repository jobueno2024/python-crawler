# 構成
- クローリングされるサイト: Flaskを使ったシンプルなWebサイト
- クローリングするアプリ: PythonのrequestsとBeautifulSoupを使ったクローラー

# ディレクトリ構造
```text
project/
├── docker-compose.yml
├── crawler/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── crawler.py
└── website/
    ├── Dockerfile
    ├── requirements.txt
    └── app.py
```
