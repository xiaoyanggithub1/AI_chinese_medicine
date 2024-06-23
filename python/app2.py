from flask import Flask, request, make_response
from flask_cors import CORS


from chatbot_graph import ChatBotGraph
import json

handler = ChatBotGraph()
app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/query', methods=['POST'])
def query():
    datas = request.get_json()
    # print(datas)
    # 处理数据代码
    data = datas['search']
    # print(type(data))
    answer = handler.chat_main(data)
    # print(answer)
    answer1 = json.loads(answer)
    # 解决ajax请求跨域问题
    res = make_response(answer1)
    # res.headers['Access-Control-Allow-Origin'] = '*'
    return res

if __name__ == '__main__':
    # app.run()
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True, port=5009, host='0.0.0.0')  # 指定端口,host,0.0.0.0代表不管几个网卡，任何ip都可访问
