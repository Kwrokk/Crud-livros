from flask import Flask, render_template, request, redirect
import sqlite3 as sql
app = Flask(__name__) 

livros = []

@app.route('/') #rota raiz
def index ():
    return render_template('index.html', livros=livros)

@app.route('/segpag') #rota pra segunda pagina
def segpag (livros):
    return render_template('segpag.html', livros=livros)

@app.route('/terpag') #rota pra terceira pagina
def terpag ():
    return render_template('terpag.html', livros=livros)


@app.route('/criar', methods=['POST']) #rota/criar
def create():
    livro = {
        'titulo': request.form['nome'],
        'autor': request.form['autor'],
        'paginas': request.form['paginas'],
        'sinopse': request.form['sinopse']
    }

    livros.append(livro)
    
    return redirect('/')

@app.route('/alterar', methods=['POST']) #rota/alterar
def update():
    old_titulo = request.form['old_titulo']
    new_titulo = request.form['new_titulo']
    if old_titulo in livros:
        index = livros.index(old_titulo)
        livros[index] = new_titulo

    print(livros)

    old_autor = request.form['old_autor']
    new_autor = request.form['new_autor']
    if old_autor in livros:
        index = livros.index(old_autor)
        livros[index] = new_autor
    return redirect('/')    

@app.route('/apagar', methods=['POST']) #Rota/apagar
def delete():
    nome = request.form['nome']
    if nome in livros:
        livros.remove(nome)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)