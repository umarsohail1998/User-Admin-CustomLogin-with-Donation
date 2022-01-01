from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Account

from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
# from blog.models import BlogPost

def index(request):
    return render(request, 'account/index.html')

def donate_view(request):
    if request.POST:
        dt = dict(request.POST)
        request.user.Donate += int(dt['amount'][0])
        Account.objects.filter(id = request.user.id).update(Donate = request.user.Donate)
        return HttpResponse("Pass")
    else:
	    # return render(request, 'account/home.html')
    	return render(request, 'account/Donate.html')

def home(request):
    context = {}
    context['Username'] = request.user.username
    context['Email'] = request.user.email
    context['Donate'] = request.user.Donate    
    lt = Account.objects.all()
    total = 0
    for x in lt:
        total += x.Donate
    context['Total'] = total
    return render(request, 'account/home.html', context = context)

def registration_view(request):
    
	context = {}
    
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)


def logout_view(request):
	logout(request)
	return redirect('/')


def login_view(request):
    
	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)


def account_view(request):

	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
				}
			)

	context['account_form'] = form

	blog_posts = BlogPost.objects.filter(author=request.user)
	context['blog_posts'] = blog_posts

	return render(request, "account/account.html", context)


def must_authenticate_view(request):
	return render(request, 'account/must_authenticate.html', {})


