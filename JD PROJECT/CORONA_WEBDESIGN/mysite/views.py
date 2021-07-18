from django.shortcuts import render

# Create your views here.
from covid import Covid
from django.http import HttpResponse
virus = Covid()
def index(request):
    if request.method == "POST":
        country = request.POST["country"]
        print(country)
        cases = virus.get_status_by_country_name(country)


        return render(request,"index.html",{"cases":cases})

    # cases = virus.get_status_by_country_name(x)
    # for x in cases:
    #     print(x, ':', cases[x])
    return render(request,"index.html")