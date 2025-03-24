from ninja import NinjaAPI, Schema
from pydantic import Field
from django.shortcuts import get_object_or_404
from catalog.models import Author, Genre
from datetime import date

api = NinjaAPI()


# Genre API CRUD endpoints
class GenreSchema(Schema):
    id: int
    name: str

@api.post("/genres", response=GenreSchema)
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

@api.put("/genres/{genre_id}", response=GenreSchema)
def update_genre(request, genre_id: int, genre: GenreSchema):
    genre_instance = get_object_or_404(Genre, id=genre_id)
    for attr, value in genre.dict().items():
        setattr(genre_instance, attr, value)
    genre_instance.save()
    return genre_instance

@api.delete("/genres/{genre_id}")
def delete_genre(request, genre_id: int):
    genre_instance = get_object_or_404(Genre, id=genre_id)
    genre_instance.delete()
    return {"success": True}

# Language API CRUD endpoints
class LanguageSchema(Schema):
    id: int
    name: str

@api.post("/languages", response=LanguageSchema)
def create_language(request, language: LanguageSchema):
    language_instance = Language.objects.create(**language.dict())
    return language_instance

@api.get("/languages", response=list[LanguageSchema])
def list_languages(request):
    languages = Language.objects.all()
    return languages

@api.get("/languages/{language_id}", response=LanguageSchema)
def get_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    return language

@api.put("/languages/{language_id}", response=LanguageSchema)
def update_language(request, language_id: int, language: LanguageSchema):
    language_instance = get_object_or_404(Language, id=language_id)
    for attr, value in language.dict().items():
        setattr(language_instance, attr, value)
    language_instance.save()
    return language_instance

@api.delete("/languages/{language_id}")
def delete_language(request, language_id: int):
    language_instance = get_object_or_404(Language, id=language_id)
    language_instance.delete()
    return {"success": True}
class AuthorSchema(Schema):
    id: int
    first_name: str
    last_name: str
    date_of_birth: date = Field(default=None)
    date_of_death: date = Field(default=None)

@api.post("/authors", response=AuthorSchema)
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

@api.put("/authors/{author_id}", response=AuthorSchema)
def update_author(request, author_id: int, author: AuthorSchema):
    author_instance = get_object_or_404(Author, id=author_id)
    for attr, value in author.dict().items():
        setattr(author_instance, attr, value)
    author_instance.save()
    return author_instance

@api.delete("/authors/{author_id}")
def delete_author(request, author_id: int):
    author_instance = get_object_or_404(Author, id=author_id)
    author_instance.delete()
    return {"success": True}
