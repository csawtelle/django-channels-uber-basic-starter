from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def userLogin(request, user=''):
  if request.method == 'POST':
    user = authenticate(
			username=request.POST['username'].lower(), 
			password=request.POST['password1']
		)
    if user is None:
      return render(request, 'accounts/login.html', {'error': 'User doesn\'t exist or password doesn\'t match.'})
    else:
      login(request, user)
      return redirect('/')
  if request.method == 'GET':
      return render(request, 'login.html')

def userLogout(request, user=''):
  logout(request)
  return redirect('/')
