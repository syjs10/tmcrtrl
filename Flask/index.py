from flask import Flask, url_for, request
app = Flask(__name__)
import lib.database
@app.route('/')
def index():
    datas = lib.database.getData()
    return datas
@app.route('/get/<tmp>')
def gettmp(tmp):
    datas = lib.database.getNewData()
    return "ok"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)
