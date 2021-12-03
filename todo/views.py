from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import card
# Create your views here.


def home(request):
    cards=card.objects.all().order_by('-id')[0:4]
    try:
      if request.method=="POST":
         nom=request.POST.get('name')
         image=request.FILES['image']
         carte_obj=card.objects.create(nom=nom,image=image)
         print(carte_obj)
         return redirect('/')
    except Exception as e:
      print(e)
    return render(request,'todo/index.html',{'cards':cards})

def delete_card(request,id):
    card_obj=card.objects.get(id=id)
    try:
        card_obj.delete()
    except Exception as e:
        print(e)  
    return redirect("home")