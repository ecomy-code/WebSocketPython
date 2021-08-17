#codigo python agosto 2021 semana de websockets
#pip install "Werkzeug>=2.0.0rc3"
#linux  FLASK_APP=websocket.py flask run
#connect un host       wscat --connect http://localhost:5000/revertir_oracion  y escriba algo para revertir

#pip install gunicorn  Multiples conecciones
#gunicorn -b :5000 --workers 4 --threads 100 websocket:app

from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@sock.route('/revertir_oracion')
def revertir (ws):
  while True:
    texto = ws.receive()
    ws.send(texto[::-1])

