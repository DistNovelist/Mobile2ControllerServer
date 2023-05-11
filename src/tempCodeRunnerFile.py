import requests

url = 'http://127.0.0.1:8080/' # WebhookのURLを入力してください
data = {'key': 'value'} # POSTデータを辞書型で定義してください
response = requests.post(url, json=data)

print(response.status_code) # レスポンスコードを表示
