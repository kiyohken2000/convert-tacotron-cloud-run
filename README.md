# Cloud Runデプロイ用Tacotron変換スクリプト

```
パッケージ書き出し
pip freeze > requirements.txt
パッケージインストール
pip install -r requirements.txt

gcloud builds submit --tag gcr.io/hey-abe/convert-tacotron --project hey-abe
```