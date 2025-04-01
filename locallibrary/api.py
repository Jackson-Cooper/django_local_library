from ninja import NinjaAPI, Schema
from ninja.security import django_auth
from pydantic import Field
from django.shortcuts import get_object_or_404
from catalog.models import Author, Genre, Book, BookInstance
from datetime import date

api = NinjaAPI()


# Genre API CRUD endpoints
class GenreSchema(Schema):
    id: int
    name: str

@api.post("/genres", response=GenreSchema, auth=django_auth)
def create_genre(request, genre: GenreSchema):
    genre_instance = Genre.objects.create(**genre.dict())
    return genre_instance

@api.get("/genres", response=list[GenreSchema])
def list_genres(request):
    genres = Genre.objects.all()
    return genres

@api.get("/genres/{genre_id}", response=GenreSchema)
def get_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    return genre

@api.put("/genres/{genre_id}", response=GenreSchema, auth=django_auth)
def update_genre(request, genre_id: int, genre: GenreSchema):
    genre_instance = get_object_or_404(Genre, id=genre_id)
    for attr, value in genre.dict().items():
        setattr(genre_instance, attr, value)
    genre_instance.save()
    return genre_instance

@api.delete("/genres/{genre_id}", auth=django_auth)
def delete_genre(request, genre_id: int):
    genre_instance = get_object_or_404(Genre, id=genre_id)
    genre_instance.delete()
    return {"success": True}

# Book API CRUD endpoints
class BookSchema(Schema):
    id: int
    title: str
    author_id: int
    summary: str
    isbn: str
    genre_ids: list[int]

@api.post("/books", response=BookSchema, auth=django_auth)
def create_book(request, book: BookSchema):
    book_instance = Book.objects.create(**book.dict())
    return book_instance

@api.get("/books", response=list[BookSchema])
def list_books(request):
    books = Book.objects.all()
    return books

@api.get("/books/{book_id}", response=BookSchema)
def get_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book

@api.put("/books/{book_id}", response=BookSchema, auth=django_auth)
def update_book(request, book_id: int, book: BookSchema):
    book_instance = get_object_or_404(Book, id=book_id)
    for attr, value in book.dict().items():
        setattr(book_instance, attr, value)
    book_instance.save()
    return book_instance

@api.delete("/books/{book_id}", auth=django_auth)
def delete_book(request, book_id: int):
    book_instance = get_object_or_404(Book, id=book_id)
    book_instance.delete()
    return {"success": True}

# Author API CRUD endpoints
class AuthorSchema(Schema):
    id: int
    first_name: str
    last_name: str
    date_of_birth: date = Field(default=None)
    date_of_death: date = Field(default=None)

@api.post("/authors", response=AuthorSchema, auth=django_auth)
def create_author(request, author: AuthorSchema):
    author_instance = Author.objects.create(**author.dict())
    return author_instance

@api.get("/authors", response=list[AuthorSchema])
def list_authors(request):
    authors = Author.objects.all()
    return authors

@api.get("/authors/{author_id}", response=AuthorSchema)
def get_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    return author

@api.put("/authors/{author_id}", response=AuthorSchema, auth=django_auth)
def update_author(request, author_id: int, author: AuthorSchema):
    author_instance = get_object_or_404(Author, id=author_id)
    for attr, value in author.dict().items():
        setattr(author_instance, attr, value)
    author_instance.save()
    return author_instance

@api.delete("/authors/{author_id}", auth=django_auth)
def delete_author(request, author_id: int):
    author_instance = get_object_or_404(Author, id=author_id)
    author_instance.delete()
    return {"success": True}

# BookInstance API CRUD endpoints
class BookInstanceSchema(Schema):
    id: str
    book_id: str  # Assuming book is referenced by ID
    imprint: str
    due_back: date = Field(default=None)
    borrower_id: str = Field(default=None)  # Assuming borrower is referenced by ID
    status: str
    language_id: str = Field(default=None)  # Assuming language is referenced by ID

@api.post("/bookinstances", response=BookInstanceSchema, auth=django_auth)
def create_book_instance(request, book_instance: BookInstanceSchema):
    book_instance_obj = BookInstance.objects.create(**book_instance.dict())
    return book_instance_obj

@api.get("/bookinstances", response=list[BookInstanceSchema])
def list_book_instances(request):
    book_instances = BookInstance.objects.all()
    return book_instances

@api.get("/bookinstances/{book_instance_id}", response=BookInstanceSchema)
def get_book_instance(request, book_instance_id: str):
    book_instance = get_object_or_404(BookInstance, id=book_instance_id)
    return book_instance

@api.put("/bookinstances/{book_instance_id}", response=BookInstanceSchema, auth=django_auth)
def update_book_instance(request, book_instance_id: str, book_instance: BookInstanceSchema):
    book_instance_obj = get_object_or_404(BookInstance, id=book_instance_id)
    for attr, value in book_instance.dict().items():
        setattr(book_instance_obj, attr, value)
    book_instance_obj.save()
    return book_instance_obj

@api.delete("/bookinstances/{book_instance_id}", auth=django_auth)
def delete_book_instance(request, book_instance_id: str):
    book_instance_obj = get_object_or_404(BookInstance, id=book_instance_id)
    book_instance_obj.delete()
    return {"success": True}