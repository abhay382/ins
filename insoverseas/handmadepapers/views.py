from django.shortcuts import render
from.models import Contact
# Create your views here.
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'index.html')

def Gallery (request):
    return render(request,'gallery.html')


def about (request):
    return render(request,'about.html')



def contact (request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'index.html', {'thank': thank})



def query (request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        query = Query(name=name, email=email, desc=desc)
        query.save()
        thank = True
    return render(request, 'pop.html', {'thank': thank})











def seed (request):
    return render(request,'seedpapers.html')



def Leatherjournal (request):
    return render(request,'Leatherjournal.html')





def christ (request):
    return render(request,'Christmasornaments.html')





def bag (request):
    return render(request,'papersbags.html')



def handmade (request):
    return render(request,'handmadepaper.html')



def plantable (request):
    return render(request,'plantablepaper.html')



def lamp (request):
    return render(request,'paperlamps.html')



def boxes (request):
    return render(request,'boxes.html')




def gift (request):
    return render(request,'giftstar.html')




def cards (request):
    return render(request,'cards.html')




def fatory (request):
    return render(request,'factorytour.html')



def Lbags (request):
    return render(request,'Lbags.html')
