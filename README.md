# Cloud Runデプロイ用Tacotron変換スクリプト

## Commands

```
パッケージ書き出し
pip freeze > requirements.txt
パッケージインストール
pip install -r requirements.txt
デプロイ(hey-abeはプロジェクト名)
gcloud builds submit --tag gcr.io/hey-abe/convert-tacotron --project hey-abe
```

## Request

```
// curl
curl -X POST -H "Content-Type: application/json; charset=utf-8" -d '{"data":"あなたは安倍晋三ですか"}' https://convert-tacotron-omc3n2et7a-an.a.run.app

// axios
const res = await axios.post(
	'https://convert-tacotron-omc3n2et7a-an.a.run.app',
	{data: 'あなたは安倍晋三ですか'},
	{
		headers: {
			"Content-Type" : "application/json; charset=utf-8"
		}
	}
)
const { converted, origin } = res.data
```

## Response

```
{
	"converted": "a n a t a w a a b e sh i N z o o d e s U k a",
	"origin": "あなたは安倍晋三ですか"
}
```