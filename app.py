from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

CSV_URL = 'https://raw.githubusercontent.com/GabrielOliveira7/displaycsv/refs/heads/main/playlist.csv'

@app.route('/')
def index():
    """
    Esta função é chamada quando alguém acessa a página principal.
    Ela lê os dados do CSV a partir da URL e exibe na página
    """
    try:
        # O pandas lê o CSV diretamente da URL
        # O separador do CSV gerado pelo Azure é a vírgula (,)
        df = pd.read_csv(CSV_URL, delimiter=',')
        
        # O template 'display.html' já existe no repositório e será usado aqui
        # 'index=False' evita que o número da linha do pandas apareça na tabela
        return render_template('display.html', tables=[df.to_html(classes='data', index=False)], titles=df.columns.values)
    except Exception as e:
        # Se algo der errado (URL errada, etc.), uma mensagem de erro será exibida
        return f"Ocorreu um erro ao ler o CSV: <br>{e}"

if __name__ == '__main__':
    app.run(debug=True)
