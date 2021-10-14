from django.shortcuts import render
from .forms import UserEntryForm

# Create your views here.
def home(request):
    form = UserEntryForm(request.POST)
    context={
        'form': form
    }
    return render(request, 'userform/home.html', context)