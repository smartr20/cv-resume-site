from django.shortcuts import render

# Create your views here.
def index_view(request):
    profile={'name': 'Reza', 'family_name': 'Moradi', 'phone': '+98912-353-2287', 'email':'smartr20@gmail.com', 'website': 'khane-shabake.com'}
    return render(request,'website/index.html', profile)