
arquivo = open("Legenda.srt","w+")
arquivo.writelines("rafael bonitao\n")
texto = "você"
arquivo.writelines("i'm your father""\n")
arquivo.writelines("oh no\n")
arquivo.write(texto.replace("ê","e"))

arquivo.close()


arquivoler = open("Legenda.srt","r")
leitura = arquivoler.read()
print(leitura.title())
print(leitura.find("f")) 
print(len(leitura))