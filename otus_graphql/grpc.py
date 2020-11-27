from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

from .books import models
from .books_pb2 import Author, Book
from .books_pb2_grpc import BooksServiceServicer, add_BooksServiceServicer_to_server


def grpc_hook(server):
    add_BooksServiceServicer_to_server(BooksService(), server)


class BooksService(BooksServiceServicer):

    @staticmethod
    def to_protobuf_author(author: models.Author) -> Author:
        birthday = Timestamp()
        birthday.FromDatetime(datetime.combine(author.birthday, datetime.min.time()))
        return Author(name=author.name, birthday=birthday)

    def GetBooks(self, request, context):
        books = models.Book.objects.select_related('author').all()
        for book in books:
            author = self.to_protobuf_author(book.author)
            yield Book(title=book.title, description=book.description, author=author)
