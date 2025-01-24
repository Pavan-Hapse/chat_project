# chat/views.py

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import ChatMessage
from django.contrib import messages
from django.contrib.auth.models import User


@login_required  # Ensure the user is logged in
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

@login_required
def index(request):
    return render(request, 'chats/welcome.html', {})

# chat/views.py

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in after signup
            return redirect('index')  # Redirect to the index page after signup
    else:
        form = UserCreationForm()
    return render(request, 'chats/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the index page after login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'chats/login.html')