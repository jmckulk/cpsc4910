from django.shortcuts import render
from .models import Account

def login(request):
    log_in = Account.objects
    return render(request, 'login/login.html', {
        'login': log_in
    })
	
def checkLogin(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			username = request.POST.get("username", "")
			password = request.POST.get("password", "")
			user = authenticate(username=username, password=password)
			
			if user is not None:
				login(request, user)
