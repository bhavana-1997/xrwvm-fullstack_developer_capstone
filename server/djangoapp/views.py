# Uncomment the required imports before adding the code

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
#from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime

from django.http import JsonResponse

from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
# from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    try:
# Load JSON data from request body      
            data = json.loads(request.body)
            username = data.get("userName")  # Use .get() to avoid KeyError
            password = data.get("password")

            # Validate if username or password is missing
            if not username or not password:
                return JsonResponse({"error": "Username and password are required."}, status=400)

            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Log in the user
                return JsonResponse({"userName": username, "status": "Authenticated"}, status=200)
            else:
                return JsonResponse({"error": "Invalid username or password"}, status=401)

    except json.JSONDecodeError:  # Ensure this is aligned with 'try'
        return JsonResponse({"error": "Invalid JSON data"}, status=400)

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...

# Create a `registration` view to handle sign up request
# @csrf_exempt
# def registration(request):
# ...

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
# ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request):
# ...
