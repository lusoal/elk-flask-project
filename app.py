from flask import Flask, render_template, request, session, send_file
import pickle
import os
import json

from controller.user_controller import UsuarioController 
from model.usuario import Usuario
from controller.elk import Elk

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def defineCreds():
    usuario = request.form['usuario']
    senha = request.form['senha']
    cliente = request.form['cliente']

    new_user = Usuario(usuario, senha, cliente)
    
    #coloca nome no cliente dentro do metodo
    user = UsuarioController(new_user)
    if user.get_credentials():
        cliente = json.dumps(new_user.__dict__)
        
        cliente = json.loads(cliente)
        session['cliente'] = cliente['cliente']
        session['login'] = cliente['login']
        return render_template("dashboard.html", cliente = session['cliente'])
    else:
        print "retornar para index"

@app.route('/listLogs', methods=['POST', 'GET'])
def listLogs():
    if(session['cliente']):
        print "entrei"
        print session['cliente']
        elk = Elk(str(session['cliente']))
        dias = request.form['dias']
        logs = elk.get_logs_today(int(dias))

        lists = zip(logs[0], logs[1])
        return render_template("logs_cliente.html", lista = lists )
        
@app.route('/returnDash', methods=['GET'])
def return_to_dash():
    return render_template("dashboard.html", cliente = session['cliente'])

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    print session['cliente']
    print session['login']
    session.pop('cliente', None)
    session.pop('login', None)
    return render_template("index.html")

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)