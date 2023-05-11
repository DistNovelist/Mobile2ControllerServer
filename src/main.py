from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_webhook():
    """
    Webhookを処理する関数
    """
    if request.method == 'POST':
        data = request.get_json() # POSTされたJSONデータを取得

        print(data)
        print(request.remote_addr) # JSONデータと送信元IPアドレスを表示
        print(data['key'])
        if('test' in data):
            print(data['test'])
        return 'success',200
    else:
        abort(400)

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
