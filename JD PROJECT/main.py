from covid import Covid
from django.http import HttpResponse
virus = Covid()
x = input('enter the country name : ')
cases = virus.get_status_by_country_name(x)
for x in cases:
    print(x, ':', cases[x])
