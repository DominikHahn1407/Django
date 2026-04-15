from django.db import models
from django.utils import timezone


class Person(models.Model):
    pid = models.AutoField(primary_key=True)
    surename = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.surename
    
class Book(models.Model):
    bnr = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    timestampe = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="loans")
    lent_at = models.DateTimeField(default=timezone.now)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.book} -> {self.person}"
    
    @property
    def is_active(self):
        return self.returned_at is None