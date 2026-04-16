from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Book, Person, Loan
from .forms import BookForm, PersonForm, LoanForm


class HomeView(TemplateView):
    template_name = "library/home.html"

# CRUD BOOK
class BookListView(ListView):
    model = Book
    template_name = "library/book_list.html"
    context_object_name = "books"

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "library/form.html"
    success_url = reverse_lazy("book_list")

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "library/form.html"
    success_url = reverse_lazy("book_list")

class BookDeleteView(DeleteView):
    model = Book
    template_name = "library/confirm_delete.html"
    success_url = reverse_lazy("book_list")

# CRUD Person
class PersonListView(ListView):
    model = Person
    template_name = "library/person_list.html"
    context_object_name = "persons"

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "library/form.html"
    success_url = reverse_lazy("person_list")

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "library/form.html"
    success_url = reverse_lazy("person_list")

class PersonDeleteView(DeleteView):
    model = Person
    template_name = "library/confirm_delete.html"
    success_url = reverse_lazy("person_list")

# CRUD Loan
class LoanListView(ListView):
    model = Loan
    template_name = "library/loan_list.html"
    context_object_name = "loans"

class LoanCreateView(CreateView):
    model = Loan
    form_class = LoanForm
    template_name = "library/form.html"
    success_url = reverse_lazy("loan_list")

class LoanUpdateView(UpdateView):
    model = Loan
    form_class = LoanForm
    template_name = "library/form.html"
    success_url = reverse_lazy("loan_list")

class LoanDeleteView(DeleteView):
    model = Loan
    template_name = "library/confirm_delete.html"
    success_url = reverse_lazy("loan_list")