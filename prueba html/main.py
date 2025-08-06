from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/validar', methods=['POST'])
def validar():
    usuario = request.form['usuario']
    password = request.form['password']

    # Validación simple
    if usuario == 'admin' and password == '123':
        return redirect(url_for('ruta_osos'))
    else:
        error = "Usuario o contraseña incorrectos"
        return render_template('login.html', error=error)

@app.route('/animales')
def ruta_osos():
    return render_template('index.html')

@app.route('/osos')
def ruta_o():
    return render_template('osos.html')

@app.route('/polar')
def ruta_polar():
    return render_template('oso-polar.html')

@app.route('/panda')
def ruta_panda():
    return render_template('oso-panda.html')

@app.route('/grizzly')
def ruta_grizzly():
    return render_template('oso-grizzly.html')





@app.route('/elefantes')
def ruta_elefantes():
    ahora = datetime.now()
    estreno = ahora + timedelta(hours=3)
    tiempo_restante = estreno - ahora

    horas, resto = divmod(tiempo_restante.total_seconds(), 3600)
    minutos, segundos = divmod(resto, 60)

    return render_template(
        'elefantes.html',
        horas=int(horas),
        minutos=int(minutos),
        segundos=int(segundos)
    )

if __name__ == '__main__':
    app.run(debug=True)
