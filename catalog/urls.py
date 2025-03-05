from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # path for list of authors
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    # the detail view for the specific author with a primary key field named <id>
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]