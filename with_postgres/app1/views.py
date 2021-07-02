from django.shortcuts import render
from .models import User
def table(request):
    model=User.objects.all()
    ctx={
        "model":model
    }
    return render(request,"index.html", ctx)
