import sqlite3
import os.path, time
import datetime


'''Obtendo data do arquivo'''
def file_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

date_file = file_date('envio-registro-pagamento-aits-semob-detran-2018-10-31.txt').strftime('%d-%m-%Y')
file = open("envio-registro-pagamento-aits-semob-detran-2018-10-31.txt", "r")
texto = file.readlines()
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
# cursor.execute("""
# CREATE TABLE registro_pagamento (
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         AUTO TEXT NOT NULL,
#         codigo_returno INTEGER,
#         mensagem_retorno TEXT NOT NULL,
#         hora TEXT NOT NULL,
#         mensagem_envio TEXT NOT NULL,
#         date_file TEXT NOT NULL,
#         CONSTRAINT unique_date UNIQUE (hora)
#
# );
#  """)
for e in texto:
    AUTO = e[42:52]
    codigo_returno = e[104:107]
    mensagem_retorno = e[107:]
    hora = e[0:8]
    mensagem_envio = e[13:103]

    try:
        cursor.execute("""
        INSERT INTO log_registro_pagamento (AUTO, codigo_returno, mensagem_retorno, hora, mensagem_envio, date_file)
        VALUES (?,?,?,?,?,?)
        """, (AUTO, codigo_returno, mensagem_retorno, hora, mensagem_envio, date_file))
        conn.commit()

    except Exception as erro:
        print(erro)


conn.close()
