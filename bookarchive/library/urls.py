from django.urls import path
from .views import (
    HomeView,
    BookListView, BookCreateView, BookUpdateView, BookDeleteView,
    PersonListView, PersonCreateView, PersonUpdateView, PersonDeleteView,
    LoanListView, LoanCreateView, LoanUpdateView, LoanDeleteView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    path("books/", BookListView.as_view(), name="book_list"),
    path("books/add/", BookCreateView.as_view(), name="book_add"),
    path("books/<int:pk>/edit/", BookUpdateView.as_view(), name="book_edit"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),

    path("persons/", PersonListView.as_view(), name="person_list"),
    path("persons/add/", PersonCreateView.as_view(), name="person_add"),
    path("persons/<int:pk>/edit/", PersonUpdateView.as_view(), name="person_edit"),
    path("persons/<int:pk>/delete/", PersonDeleteView.as_view(), name="person_delete"),

    path("loans/", LoanListView.as_view(), name="loan_list"),
    path("loans/add/", LoanCreateView.as_view(), name="loan_add"),
    path("loans/<int:pk>/edit/", LoanUpdateView.as_view(), name="loan_edit"),
    path("loans/<int:pk>/delete/", LoanDeleteView.as_view(), name="loan_delete"),
]