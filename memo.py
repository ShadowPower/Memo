#! python3
#coding:utf-8

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import json
import database, helper

app = Flask(__name__)

######## DATABASE ########

@app.before_request
def before_request():
    g.db = database.connect_db()
    g.cursor = g.db.cursor()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

######## DATABASE ########



######## WEB ########

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/edit/<int:id>/<token>')
def edit(id=None,token=None):
    return render_template('edit.html', id=id,token=token)

@app.errorhandler(404)
def page_not_found(error):
    return '这里没有网页啦'

######## WEB ########



######## API ########

# 创建便笺
@app.route('/api/create')
def create():
    token = helper.token_generator(10)
    g.cursor.execute('INSERT INTO memo (id, token) VALUES (NULL, ?)', (token,))
    # 取得刚才insert产生的id
    id = g.cursor.lastrowid
    g.db.commit()
    result = {'id':id, 'token':token}
    return json.dumps(result)

# 更新便笺
@app.route('/api/update', methods=['POST'])
def update():
    id = request.form['id']
    token = request.form['token']
    text = request.form['text']
    g.db.execute('UPDATE memo SET text = ? WHERE id=? AND token=?', (text, id, token))
    g.db.commit()
    return 'ok'

# 获取便笺内容
@app.route('/api/memo/<int:id>/<token>')
def memo(id, token):
    g.cursor.execute('SELECT text FROM memo WHERE id=? AND token=?', (id, token))
    result = g.cursor.fetchone()
    return result;

######## API ########

app.secret_key = 'u0R8irlYjpdszxZyg3Aam6qL'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
