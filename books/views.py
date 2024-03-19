from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from .models import Good
from .forms import SampleModelForm, RegisterForm
from django.views.generic import DetailView

def index(request):
    return render(request, 'books.html')

def indeе(request):
    qwer = Good.objects.all()
    return render(request, 'books2.html', {'qwer': qwer})

@method_decorator(login_required, name='dispatch')
class NewDetailView(DetailView):
    model = Good
    template_name = 'books2.html'
    context_object_name = 'book'

@login_required
def create(request):
    if request.method =='POST':
        form = SampleModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boot')
    else:
        form = SampleModelForm()

    return render(request, 'forms.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def setcookie(request):
    html = HttpResponse("<h1>Hello</h1>")
    html.set_cookie('CookieName',
        'Hello this is your Cookies', max_age = None)
    return html
def set_cookie(request):
    html = HttpResponse("<h1>Мой сайт</h1>")
    if request.COOKIES.get('visit_count'):
        visit_count = int(request.COOKIES.get('visit_count')) + 1
    else:
        visit_count = 1
    html.set_cookie('visit_count', str(visit_count))
    return html

def deletercooike(request):
    html = HttpResponse('<h1>Cookie Deleter</h1>')
    html.delete_cookie('CookieName')
    return html