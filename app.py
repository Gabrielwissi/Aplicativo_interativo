import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

def load_model():
    return "Modelo carregado (mock)"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analisar', methods=['POST'])
def analisar_lote():

    return jsonify({
        'resultado': 1,
        'probabilidade': 0.8,
        'mensagem_area': "",
        'mensagem_testada': "",
        'resumo': {
            'area_total': 500.0,
            'testada_calculo': 12.0,
            'zona': "ZM",
            'Valor_m2_comercial': 2000.0,
            'Valor_comercial': 1000000.0,
        }
    })

@app.route('/resultado')
def resultado():
   
    resultado = request.args.get('resultado', 0, type=int)
    probabilidade = request.args.get('probabilidade', 0, type=float)
    resumo = request.args.get('resumo', '{}')
    
    return render_template(
        'resultado.html',
        resultado=resultado,
        probabilidade=probabilidade,
        resumo=eval(resumo) 
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
