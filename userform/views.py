from django.shortcuts import render

from .forms import UserEntryForm
from .models import UserEntry
from django.http import JsonResponse

# Create your views here.
def home(request):
    data = {"uuid":""}
    if request.method == "POST":
        form = UserEntryForm(request.POST or None, request.FILES or None)
        if request.is_ajax():
            if form.is_valid():
                form.save()
                data['header'] = form.cleaned_data['header']
                data['uuid'] = form.cleaned_data['uuid']
                data['status'] = "success"
    else:
        form = UserEntryForm()
    context={
        'form': form,
        'uuid': data['uuid']
    }
    return render(request, 'userform/home.html', context)

def search(request):
    result = ""
    if 'q' in request.GET:
        search = request.GET['q']
        if search:
            result = UserEntry.objects.get(uuid=search)
            print(UserEntry.objects.get(uuid=search))
    context = {
        'result': result,
    }

    return render(request, "userform/search.html", context)

