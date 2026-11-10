from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Booking
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Booking, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


def home(request):
    return render(request, 'index.html')


@csrf_exempt
def send_alert(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print("Received:", data)
        return JsonResponse({'message': 'Alert received!'})
def book_helper(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tier = data.get('tier')
            start_time = data.get('start_time')
            route = data.get('route')

            if not tier or not start_time or not route:
                return JsonResponse({'status': 'error', 'message': 'Missing required fields'}, status=400)

            booking = Booking.objects.create(
                user=request.user,
                tier=tier,
                start_time=start_time,
                route=route
            )
            return JsonResponse({'status': 'success', 'booking_id': booking.id})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'}, status=405)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            UserProfile.objects.create(
                user=user,
                gender=request.POST.get('gender'),
                location=request.POST.get('location')
            )

            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'mobility_app/register.html', {
        'form': form
    })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('home')

        return render(request, 'mobility_app/login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'mobility_app/login.html')


def user_logout(request):
    if request.method == 'POST':
        logout(request)

    return redirect('home')