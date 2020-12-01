from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from grpc_reflection.v1alpha import reflection

from .books import models
from .books_pb2 import Author, Book, DESCRIPTOR
from .books_pb2_grpc import BooksServiceServicer, add_BooksServiceServicer_to_server


def grpc_hook(server):
    add_BooksServiceServicer_to_server(BooksService(), server)
    reflection.enable_server_reflection((
        DESCRIPTOR.services_by_name['BooksService'].full_name,
        reflection.SERVICE_NAME
    ), server)


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
