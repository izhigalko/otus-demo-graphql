from collections import defaultdict

from promise import Promise
from promise.dataloader import DataLoader

from .books.models import Book


class AuthorsBooksDataLoader(DataLoader):

    def batch_load_fn(self, author_ids):
        query = Book.objects.filter(author_id__in=author_ids)
        books = defaultdict(list)

        for book in query.iterator():
            books[book.author_id].append(book)

        return Promise.resolve(books.values())


author_books_data_loader = AuthorsBooksDataLoader()
