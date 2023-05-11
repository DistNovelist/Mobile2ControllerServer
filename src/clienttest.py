import requests

url = 'http://192.168.2.108:8080' # WebhookのURLを入力してください
data = {'key': 'value', 'test':'hoge'} # POSTデータを辞書型で定義してください
response = requests.post(url, json=data)

print(response.status_code) # レスポンスコードを表示
