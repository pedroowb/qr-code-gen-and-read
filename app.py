from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


@app.route("/computador/<numero_serie>")
def computador(numero_serie):
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="db_computadores"
        )

        if conexao.is_connected():
            cursor = conexao.cursor()

            try:
                cursor.execute(
                    "SELECT novo_nome, nome_maquina, numero_serie, modelo, andar, setor, localidade, observacoes, ip, patrimonio FROM computadores WHERE numero_serie = %s",
                    (numero_serie,))
                dados = cursor.fetchone()
            except Error as e:
                print(f"Erro ao executar consulta: {e}")
                return "Erro ao buscar dados do computador."

            finally:
                cursor.close()

        if dados:
            return render_template("formulario.html", dados=dados)
        else:
            return "Computador não encontrado."

    except Error as e:
        print(f"Erro na conexão com o banco de dados: {e}")
        return "Erro ao conectar ao banco de dados."

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()


if __name__ == "__main__":
    app.run(debug=True)
