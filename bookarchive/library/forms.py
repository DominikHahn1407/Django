from django import forms
from .models import Book, Person, Loan


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "available"]

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["surename", "birthdate"]
        widgets = {
            "birthdate": forms.DateInput(attrs={"type": "date"})
        }

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ["book", "person", "lent_at", "returned_at"]
        widgets = {
            'lent_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'returned_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }