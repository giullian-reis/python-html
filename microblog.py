from flask import Flask
app = Flask("microblog")
#programa que vai ficar ligado na internet
#ouvindo requisicoes e ele precisa ter rotas
#flask faz ligacao entre url e funcoes do python

#chama o app e faz alguma coisa com ele com a funcao que ta em baixo
@app.route("/")#se entrar no site e tiver barra ele vai fazer o que a função faz
def index():
    return "Hello World"

app.run()