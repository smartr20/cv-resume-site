from django.shortcuts import render

# Create your views here.
def index_view(request):
    profile={'name': 'Reza', 'family_name': 'Moradi', 'phone': '098912-353-2287', 'email':'smartr20@gmail.com'}
    return render(request,'website/index.html', profile)