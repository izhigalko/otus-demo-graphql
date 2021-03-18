import graphene
import datetime
from graphene_django import DjangoObjectType
from .loaders import author_books_data_loader

from .books.models import Author, Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ("id", "name", "birthday", "books")


class AuthorNPlus1Type(AuthorType):
    class Meta:
        model = Author
        fields = ("id", "name", "birthday", "books")

    def resolve_books(root, info, **kwargs):
        return author_books_data_loader.load(root.id)


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "description", "author")


class Query(graphene.ObjectType):
    books = graphene.List(BookType, description="Get all books",
                          limit=graphene.Int())
    author = graphene.Field(AuthorType, description="Get author",
                            id=graphene.ID(required=True))
    select_n_plus_1 = graphene.List(AuthorType,
                                    description="Select n + 1 problem representation",
                                    author_ids=graphene.List(graphene.ID, required=True))
    resolved_n_plus_1 = graphene.List(AuthorNPlus1Type,
                                      description="Select n + 1 resolved problem representation",
                                      author_ids=graphene.List(graphene.ID, required=True))

    def resolve_books(root, info, limit=None):
        query = Book.objects.select_related('author').all()

        if limit:
            query = query[:limit]

        return query

    def resolve_author(root, info, id):
        return Author.objects.get(pk=id)

    def resolve_select_n_plus_1(root, info, author_ids):
        return Author.objects.filter(pk__in=author_ids).all()

    def resolve_resolved_n_plus_1(root, info, author_ids):
        return Author.objects.filter(pk__in=author_ids).all()


class CreateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(root, info, name):
        author = Author(name=name, birthday=datetime.date.today())
        author.save()
        return CreateAuthor(author=author)


class Mutations(graphene.ObjectType):
    create_author = CreateAuthor.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
