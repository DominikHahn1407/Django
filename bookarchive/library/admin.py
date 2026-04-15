from django.contrib import admin
from .models import Book, Person, Loan

admin.site.register(Book)
admin.site.register(Person)
admin.site.register(Loan)