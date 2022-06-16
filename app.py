from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    {
        "id":0,
        "author": "william shakespear",
        "lang": "english",
        "title": "Remeo and juliet",
    },
    {
        "id":1,
        "author": "R. Giridharan",
        "lang": "english",
        "title": "Right Under Our Nose",
    },
    {
        "id":2,
        "author": "Priyanka Chopra Jonas",
        "lang": "english",
        "title": "Unfinished",
    },
    {
        "id":3,
        "author": "Samir Soni",
        "lang": "english",
        "title": "My Experiment with Silence",
    }
]
@app.route('/books', methods=['GET','POST'])
def books():
    if request.method =='GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Nothing found', 404
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        id = bookd_list[-1]['id']+1

        new_obj = {
            'id': id,
            'author': new_author,
            'lang' : new_lang,
            'title' : new_title

        }
        books_list.append(new_obj)
        return jsonify(books_list),201

@app.route('/books/<int:id>', methods=['GET','PUT','DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
            pass
    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['author']=request.form['author']
                book['language']=request.form['language']
                book['title']=request.form['title']
                updated_book = {
                    'id': id,
                    'author':book['author'],
                    'language' : book['language'],
                    'title' : book['title'],
                }
                return jsonify(updated_book)
    if request.method == 'DELETE':
        for index, book in ennumerate(book_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)


    if __name__ == '__main__':
        app.run()