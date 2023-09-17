from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Expense
from .forms import ExpenseForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user after registration
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard or any other page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

#def dashboard(request):
  #template = loader.get_template('dashboard.html')
  #return HttpResponse(template.render())

def add_expense(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        Expense = form.save(commit=False)
        Expense.user = request.user
        form.save()
         
    context['form']= form
    return render(request, "add_expense.html", context)


@login_required
class ExpenseListView(ListView):
    model = Expense
    template_name = 'dashboard.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        # Retrieve expenses for the current user
        return Expense.objects.filter(user=self.request.user)


def dashboard(request):
    if request.user.is_authenticated:
        # Retrieve expenses associated with the current user
        expenses = Expense.objects.filter(user=request.user)

        return render(request, 'dashboard.html', {'expenses': expenses})
    else:
        # Redirect to the login page or any other appropriate page
        return redirect('login')  # Replace 'login' with the actual URL name of your login page  
