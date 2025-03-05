from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    word = request.GET.get('word', '')

    filtered_books_by_word = Book.objects.filter(title__icontains=word).count()
    filtered_genres_by_word = Genre.objects.filter(name__icontains=word).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'filtered_books_by_word': filtered_books_by_word,
        'filtered_genres_by_word': filtered_genres_by_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# book list class view
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'book_list.html'
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

# author list class view
class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'author_list.html'
    paginate_by = 10

    def get_queryset(self):
        """Return the list of authors."""
        authors = super().get_queryset()
        print(f"Number of authors retrieved: {authors.count()}")  # Debug statement
        return authors

# author detail class view
class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
