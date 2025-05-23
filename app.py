from flask import Flask, render_template, request
import math
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

def f_senb(x):
    try:
        cos_val = math.cos(math.pi * x / 2)
        if cos_val == 0:
            return float('inf')
        return math.sqrt(1 / cos_val) * (1.99 - x * (1 - x) * (2.15 - 3.93 * x + 2.7 * x**2))
    except:
        return float('inf')

def g(a, K, sigma, W):
    pi_val = math.pi
    f_val = f_senb(a / W)
    if f_val == 0:
        return float('inf')
    return (K / (sigma * math.sqrt(pi_val) * f_val)) ** 2

def punto_fijo(K, sigma, W, a0, tol=1e-6, max_iter=100):
    iteraciones = [a0]
    a = a0
    for _ in range(max_iter):
        a_new = g(a, K, sigma, W)
        iteraciones.append(a_new)
        if abs(a_new - a) < tol:
            break
        a = a_new
    return a_new, iteraciones

@app.route('/')
def home():
    return render_template('main.html', resultado=None)

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        K = float(request.form['K'])
        sigma = float(request.form['sigma'])
        W = float(request.form['W'])
        a0 = float(request.form['a0'])

        raiz, valores = punto_fijo(K, sigma, W, a0)

        # Graficar
        plt.figure()
        plt.plot(range(len(valores)), valores, marker='o', color='blue')
        plt.title("Iteraciones del método de punto fijo")
        plt.xlabel("Iteración")
        plt.ylabel("a (longitud de grieta)")
        plt.grid(True)
        os.makedirs("static", exist_ok=True)
        plt.savefig("static/iteraciones.png")
        plt.close()

        return render_template("main.html", resultado=round(raiz, 6), imagen="iteraciones.png")
    except Exception as e:
        return render_template("main.html", resultado=f"Error: {e}", imagen=None)

if __name__ == '__main__':
    app.run(debug=True)
