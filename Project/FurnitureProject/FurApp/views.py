from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Chair

# Create your views here.

"""    option1 = Chair()
    option1.name = "Wooden Chair"
    option1.img = "arrivals1.png"
    option1.price = 800
    option1.offer = True

    option2 = Chair()
    option2.name = "Wooden ArmChair"
    option2.img = "arrivals3.png"
    option2.price = 400
    option2.offer = False

    option3 = Chair()
    option3.name = "Modern Chair"
    option3.img = "arrivals2.png"
    option3.price = 950
    option3.offer = True

    option4 = Chair()
    option4.name = "Modern Chair"
    option4.img = "arrivals2.png"
    option4.price = 950
    option4.offer = False

    options = [option1, option2, option3, option4]"""




def index(request):
    options = Chair.objects.all()

    return render(request, 'index.html', {'options': options})

