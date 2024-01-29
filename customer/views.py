from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'customer/home.html')

def signup(request):
    return render(request, 'customer/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pwd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'customer/login.html')
    else:
        return render(request, 'customer/login.html')

def dashboard(request):
    return render(request, 'customer/dashboard.html')

def restaurant_registration(request):
    return render(request, 'restaurant_partner/restaurant_registration.html')

def restaurant_login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pwd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('restaurant_dashboard')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'restaurant_partner/login.html')
    else:
        return render(request, 'restaurant_partner/restaurant_login.html')

def restaurant_dashboard(request):
    return render(request, 'restaurant_partner/restaurant_dashboard.html')

def delivery_signup(request):
    return render(request, 'delivery_partner/delivery_signup.html')

def delivery_login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pwd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('delivery_dashboard')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'delivery_partner/login.html')
    else:
        return render(request, 'delivery_partner/login.html')
    
def delivery_dashboard(request):
    return render(request, 'delivery_partner/dashboard.html')