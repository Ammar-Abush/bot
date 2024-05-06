from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.cache import never_cache
from .FacultyGPT.manager.chat_manager import ChatManager
from django.http import JsonResponse
from .models import User, Chat
from  .FacultyGPT.provider import english_provider
from django.utils import timezone




def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            prompt = request.POST["userinput"]
            response = english_provider.Prompt(prompt, request.user.chat_manager)
            print(request.user.username, request.user.chat_manager)
            chat = Chat(owner = request.user, message = prompt, response = response, created_at = timezone.now())
            chat.save()
            print(response)

            #return JsonResponse({'prompt': prompt, 'response': response})
            return render(request, "csbot/index.html")
        else:
            return render(request, "csbot/index.html")
    else:
        return redirect('login') 
        
def history(request):
    if request.user.is_authenticated:

        chats = Chat.objects.filter(owner = request.user)
        '''chats_data = [
            {"message": chat.message, "response": chat.response} 
            for chat in chats
        ]
        return JsonResponse({"chats": chats_data})'''
        return render(request, "csbot/history.html", {
            "chats": chats
        })
    else:
        return redirect('login') 
          
def login_view(request):
    if request.method == "POST":
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

       
        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "csbot/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "csbot/login.html")


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "csbot/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "csbot/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "csbot/register.html")
