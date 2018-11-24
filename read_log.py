# import sqlite3
#
# conn = sqlite3.connect('log_mobi.db')
# cursor = conn.cursor()
#
# # lendo os dados
# cursor.execute("""
# SELECT * FROM log_mobi;
# """)
#
# for linha in cursor.fetchall():
#     print(linha)
#
# conn.close()
# file = open("envio-registro-pagamento-aits-semob-detran-2018-10-31.txt", "r")
# texto = file.readlines()
# for e in texto:
#     print(e[13:103])
#     print(e[0:8])
#     print(e[42:52])
#     print(e[104:107])
#     print(e[107:])
cont = 0
texto = '2205100091549DET123H050000165A021060211518528146340000140690015618201810300011618720181101'
for e in texto:
    cont = cont + 1
print(cont)
# import datetime
# import os.path, time
#
# def file_date(filename):
#     t = os.path.getmtime(filename)
#     return datetime.datetime.fromtimestamp(t)
#
# # data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
# data_atual = '2018-11-20'
# print(type(data_atual))
#
# diretorio = '/home/adson/Documentos/python/mobi/'
# def selecionar_file(diretorio):
#     list_dir = os.listdir(diretorio)
#     for file in list_dir:
#         f = file_date(diretorio + file).strftime('%Y-%m-%d')
#         if file.startswith('envio-notificacao'):
#             if f == data_atual:
#                 print(diretorio + file)
# selecionar_file(diretorio)
# # print(teste)
