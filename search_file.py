import os, fnmatch


# for files in os.walk("/home/adson/Documentos/estudo/script-log-mobi"):
#     for filename in files:
#         print(filename)
directory = os.listdir('/home/adson/Documentos/estudo/script-log-mobi')
extencao = "*.txt"
for files in directory:
    if fnmatch.fnmatch(files, extencao):
        print(files)
