from django.shortcuts import render
from django.http import HttpResponse 
import pyrebase
# Create your views here.

config = {
"apiKey": "AIzaSyA56YYkVbejh60dVQmmffqgGexjEqyqigk",
"authDomain": "mysaveings-653ed.firebaseapp.com",
"databaseURL":"https://mysaveings-653ed-default-rtdb.firebaseio.com/",
"projectId": "mysaveings-653ed",
"storageBucket": "mysaveings-653ed.appspot.com",
"messagingSenderId": "326121323200",
"appId": "1:326121323200:web:6bae0ee48ce5bc360b8b25"
}
firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
# user = auth.sign_in_with_email_and_password(email, password)


#signup
def login(request):
    email =request.POST.get('email')
    print(email)
    password =request.POST.get('password')
    auth.create_user_with_email_and_password(email,password)
    return render(request, 'index.html', {'email':email})
def home(request):
    return render(request, 'home.html',{'name':'venkat'})
# def signup(request):
#     return render(request, 'signup.html',{'name':'venkat'})