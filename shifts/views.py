from django.shortcuts import render
from django.http import HttpResponse

from .models import Shift_view
def index(request):
    shifts = Shift_view.objects.all()
    return render(request, 'index.html',
                  {'shifts': shifts})

# from .models import Shift
# def index(request):
#    shifts = Shift.objects.all()
#    return render(request, 'index.html',
#                 {'shifts': shifts})


