from django.shortcuts import render
from datetime import datetime
# Create your views here.

def birthday(request):
    day = datetime.now().day
    month = datetime.now().month
    is_it_my_birthday =  (int(day) == 20) and (int(month) == 6)
    return render(request, "birthday/index.html", {
        "is_birthday": is_it_my_birthday
    })