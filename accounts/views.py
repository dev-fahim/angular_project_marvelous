from django.shortcuts import render

# Create your views here.


def qrCode(request):
	return render(request, 'login/login.html', {})
