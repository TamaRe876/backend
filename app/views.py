from django.shortcuts import render
from .forms import PersonForm

def index(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonForm()
    return render(request, 'app/index.html', {'form': form})
