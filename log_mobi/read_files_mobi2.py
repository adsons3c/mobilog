import sqlite3
import os.path, time
import datetime


'''Obtendo data do arquivo'''
def file_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


date_file = file_date('envio-notificacao-semob-detran-2018-11-20.txt').strftime('%d-%m-%Y')
file = open("envio-notificacao-semob-detran-2018-11-20.txt", "r")
texto = file.readlines()
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
# cursor.execute("""
# CREATE TABLE envio_notificacao (
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         AUTO TEXT NOT NULL,
#         codigo_returno INTEGER,
#         mensagem_retorno TEXT,
#         hora TEXT NOT NULL,
#         mensagem_envio TEXT NOT NULL,
#         date_file TEXT NOT NULL,
#         proprietario TEXT
#
# );
#  """)
for e in texto:
    if e[90:93].startswith('99'):
        # print(e[93:])
        # print(e[0:8])
        # print(e[13:89])
        AUTO = e[35:45]
        codigo_returno = e[90:93]
        mensagem_retorno = e[93:]
        hora = e[0:8]
        mensagem_envio = e[13:89]

        try:
            cursor.execute("""
            INSERT INTO log_envio_notificacao (AUTO, codigo_returno, mensagem_retorno, hora, mensagem_envio, date_file)
            VALUES (?,?,?,?,?,?)
            """, (AUTO, codigo_returno, mensagem_retorno, hora, mensagem_envio, date_file))
            conn.commit()

        except Exception as erro:
            print(erro)

    else:
        print(e[90:130]) # codigo de retorno
        print(e[35:45]) # AUTO
        print(e[130:170]) # proprietario
        AUTO = e[35:45]
        codigo_returno = e[90:130]
        hora = e[0:8]
        proprietario = e[130:170]
        mensagem_envio = e[13:89]

        try:
            cursor.execute("""
            INSERT INTO log_envio_notificacao (AUTO, codigo_returno, proprietario, hora, mensagem_envio, date_file)
            VALUES (?,?,?,?,?,?)
            """, (AUTO, codigo_returno, proprietario, hora, mensagem_envio, date_file))
            conn.commit()

        except Exception as erro:
            print(erro)


conn.close()
