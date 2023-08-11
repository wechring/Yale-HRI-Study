from django.shortcuts import render
from yaleapp.models import Survey

# Create your views here.
def yaleview(request):
    return render(request, "video.html")

def insert_data(request):
    if request.method == 'POST':
        Q1 = request.POST["beginning"]
        Q2 = request.POST["middle"]
        Q3 = request.POST["end"]
        data = Survey(Q1=Q1, Q2=Q2, Q3=Q3,)
        data.save()
        return render(request, "actionpage.html")
    else:
        return render(request, "video.html")


def actionpage(request):
    return render(request, "actionpage.html")
