from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Quote, Favorite

import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    # User.objects.all().delete()
    return render(request, "register_app/index.html")

def register(request):
    if request.method == "GET":
        return redirect('/')
    #variables for form information
    fname = request.POST['first_name'].lower()
    lname = request.POST['last_name'].lower()
    email = request.POST['email'].lower()
    password = request.POST['password'].encode()
    confirm_password = request.POST['confirm_password'].encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    #registration validaation. try to break the registration process and add more validations
    wrong = False
    if len(fname) < 1:
        wrong = True
        messages.warning(request, "First name cannot be blank!")
    if not fname.isalpha():
        wrong = True
        messages.warning(request, "First name cannot contain numbers!")
    if len(lname) < 1:
        wrong = True
        messages.warning(request, "Last name cannot be blank!")
    if not lname.isalpha():
        wrong = True
        messages.warning(request, "Last name cannot contain numbers!")
    if len(email) < 1:
        wrong = True
        messages.warning(request, "Email cannot be blank!")
    if not EMAIL_REGEX.match(email):
        wrong = True
        messages.warning(request, "Emails are not valid!")
    email_list = User.objects.filter(email=email)
    if email_list:
        wrong = True
        messages.warning(request, "Email is already registered! ")
    if len(password) < 1 or len(password) < 8:
        wrong = True
        messages.warning(request, "Password cannot be blank and atleast 8 characters!")
    if confirm_password != password:
        wrong = True
        messages.warning(request, "Passwords must match!")
    if not password == password:
        wrong = True
        messages.warning(request, "Passwords do not match!")
    if wrong:
        return redirect('/')

    else:
        messages.success(request, "Congratulations you passed the registration process DOOFUS!")
        User.objects.create(first_name=request.POST['first_name'], last_name= request.POST['last_name'], email= request.POST['email'], password= hashed)
        print fname
        print lname
        print email
        print password
        print confirm_password
        print hashed
        return redirect('/quotes')





def login(request):
    user_email=request.POST['user_email']
    email_list = User.objects.filter(email=user_email)
    password = request.POST['password']
    # password_list = User.objects.filter(password=password)
    num_results = len(email_list)
    print num_results
    if num_results == 0:
        messages.warning(request, "Email does not exist!")
        return redirect('/')
    if email_list:
        hashed = email_list[0].password
        print hashed
        #grabs hashed variable(holding our email_list[0].password) and compares it to the database pw
        if bcrypt.hashpw(password.encode(), hashed.encode()) == hashed.encode():
            request.session['id'] = email_list[0].id
            request.session['first_name'] = email_list[0].first_name
            user_id = request.session['first_name']
            print "Logged in!"
            print request.session['id']
            return redirect('/quotes')
        else:
            print "Wrong PW"
            return redirect('/')

# submit quote to login page.
# need to link id to user and quote
def submit(request):
    quotedby = request.POST['person']
    quote = request.POST['message']
    # Quote.objects.all().delete()

    if len(quotedby) < 3:
        messages.warning(request, "-Quoted by is less than 3 characters!")
        # return redirect('/quotes')
    if len(quote) < 10:
        messages.warning(request, "-Quote cannot be less than 10 characters!")
        return redirect('/quotes')
    else:
        print quotedby
        print quote
        quote_list = Quote.objects.all()
        user = request.session['first_name']
        # user_list = User.objects.filter(user=user)

        Quote.objects.create(author=quotedby, quote=request.POST['message'])
        # user_list = Quote.objects.get(id=id)


        return redirect('/quotes')

# to add quote to favorite list. Need to figure out how to grab the id
def favorite(request, id):
    # fave = Quote.objects.get(id=id)
    # if request.method == "GET":
    #     return render(request, "register_app/login.html", {"quote": fave})
    # fave.create()
    return redirect('/quotes')

# login/registration successful. will display all quotes
def success(request):
    context = {
    "quotes" : Quote.objects.all()
    }
    return render(request, "register_app/login.html", context)

# up click of user, will redirect to user page that displays info
def users(request):
    # print len(Quote.objects.all())
    count = len(Quote.objects.all())
    request.session['count'] = count
    context = {
        "quotes" : Quote.objects.all()
    }
    return render(request, "register_app/users.html", context)

def logout(request):
    if request.method == "GET":
        return redirect('/')
    request.session.pop("id")
    request.session.pop("first_name")
    return redirect('/')
