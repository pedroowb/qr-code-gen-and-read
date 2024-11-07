import qrcode
import os
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="db_computadores"
)

cursor = conexao.cursor()
cursor.execute("SELECT numero_serie, novo_nome, nome_maquina, numero_serie, modelo, andar, setor, localidade, observacoes, ip, patrimonio FROM computadores")

if not os.path.exists("qrcodes"):
    os.makedirs("qrcodes")

for linha in cursor:
    numero_serie = linha[0]
    url_completa = f"http://localhost:5000/computador/{numero_serie}"

    qr = qrcode.make(url_completa)

    nome_arquivo = f"{numero_serie}.png"
    caminho_arquivo = os.path.join("qrcodes", nome_arquivo)

    qr.save(caminho_arquivo)

cursor.close()
conexao.close()
