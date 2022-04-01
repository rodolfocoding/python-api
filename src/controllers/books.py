from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

bookst_db = [
    {
        'id': 1, 'title': 'War and peace'
    },
    {
        'id': 2, 'title': 'Harry Potter'
    },
    {
        'id': 3, 'title': 'Pai rico, Pai pobre'
    },
    {
        'id': 4, 'title': 'A arte da guerra'
    }
]


@api.route('/books')
class BookList(Resource):
    def get(self,):
        return bookst_db

    def post(self,):
        response = api.payload
        bookst_db.append(response)
        return response, 200
