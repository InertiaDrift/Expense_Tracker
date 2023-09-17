from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user

#class User(models.Model):
  #firstname = models.CharField(max_length=255)
  #lastname = models.CharField(max_length=255)

  #def __str__(self):
    #return f"{self.firstname} {self.lastname}"


class Categories(models.Model):
  category = models.CharField(max_length=100)
  class Meta:
        app_label = 'tracker'
  def __str__(self):
        return self.category
  

class Tags (models.Model):
  tag = models.CharField(max_length=100)
  class Meta:
        app_label = 'tracker'
  def __str__(self):
        return self.tag


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.notes

