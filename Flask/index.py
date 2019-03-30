from flask import Flask, url_for, request, make_response
app = Flask(__name__)
import lib.database
@app.route('/', methods=['GET', 'POST'])
def index():
    datas = lib.database.getData()
    rst = make_response(datas)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst
@app.route('/get/<tmp>')
def gettmp(tmp):
    datas = lib.database.getNewData()
    return "ok"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)
