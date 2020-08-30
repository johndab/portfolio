from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CvRowForm
from .models import CvRow

def cv(request):
    rows = CvRow.objects.all()
    return render(request, 'cv/cv.html', {'rows': rows})

def form(request):
    if request.method == "POST":
        form = CvRowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cv')
    else:
        form = CvRowForm()

    return render(request, 'cv/form.html', {'form': form})