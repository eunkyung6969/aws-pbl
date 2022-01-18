from flask import Flask

app = Flask(__name__)

@app.route('/')
def hell():
    return "<h1> hellow flask. 드디어 된다아아아아아앙. 이길은 어디로 가는지 알순없지마아안 알순없지마마망ㄴ~  <h1>"

@app.route('/test')
def test():
    return "test"

if __name__ == '__main__':
    app.run("0.0.0.0",port =8080)