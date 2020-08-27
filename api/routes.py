from flask import Flask, jsonify, request, abort, make_response
from api import app

# jsonify mandar como um json
# request tem funcoes exemplo, get_json

books = [
    {'id': 0, 'title':'Python Fluente', 'author':'Luciano Ramalho', 'read': False},
    {'id': 1, 'title':'Pense em Python', 'author':'Luciano Ramalho', 'read': True},
    {'id': 2, 'title':'Flask Web Framework', 'author':'Luciano Ramalho', 'read': False}
]


@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})


@app.errorhandler(404)
def not_found(error):
    print('error', error)
    return jsonify({'error': 'Not found'}), 404

@app.route('/api/books/<int:book_id>')
def get_book(book_id):
    selected = [book for book in books if book['id'] == book_id]
    if len(selected) > 0:
        return jsonify({'book': selected[0]})
    else:
        abort(404)

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    books.pop(book_id)
    return jsonify({"ok":"apagado com sucesso"}), 201

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
        data = request.get_json(book_id)
        title  = data['title']
        author  = data['author']
        read = data['read']
        status=False
        if read==False:
             status=False
        else:
            status=True
        
        return jsonify({'title': title, 'author': author, 'read':status,"modificado":"modificado com sucesso"}),201

@app.route("/api/books", methods=['POST'])
def create_book():
    if request.method == 'POST':
        data = request.get_json()
        id = data['id']
        title = data['title']
        author = data['author']
        read = data['read']
        status=False
        if read==False:
             status=False
        else:
            status=True
        
        return jsonify({'id':id,'title':title, 'read':status,'author':author,'ok':'Criado com sucesso'}),201
