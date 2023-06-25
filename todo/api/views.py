from django.shortcuts import render, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import TodoItem_form
from .models import TodoItem_model
from django.views.decorators.csrf import csrf_protect


# Renders the welcome page when you run the server
def welcome_view(request):
    print(request.headers)
    return render(request,"api/welcome.html",{})

# Renders the login page where user can login to an existing account
def login_view(request):
	print(request.headers)
	return render(request, "api/login.html",{})

# Renders the signup page where user can create a new account
def signup_view(request):
	print(request.headers)
	return render(request,"api/signup.html",{})

# Renders the form to create a new task.
def create_view(request):
    print(request.headers)
    return render(request,'api/todo_create.html',{})


def todo(request):
    print(request.headers)
    todo = TodoItem_model.objects.filter(user=request.user)
    return render(request,'api/todo.html',{'todo' : todo})


# login view is for signing into an existing user.
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None: # If authentication is successful
            login(request, user)
            # Redirect to a success page.
            return redirect('todo')   

        else: # If authentication fails
            # Return an error message  the login credentials are incorrect.
            error_message = 'Invalid username or password.'
            return render(request, 'api/login.html', {'error_message': error_message})
    else:
        return redirect('login_view')


#signup view is for creating a new user account.
def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']  # Get the username from the POST data

        # If the user already exists
        if User.objects.filter(username=username).exists():
            user_exists = True
            return render(request, 'api/signup.html', {'user_exists': user_exists})
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:  # Check if the two passwords match
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save() # Save the new user account to the database
            return redirect('login_view')
    return render(request, 'signup.html')


def create(request):
    if request.method=='POST': # Create a form instance with POST data
        form = TodoItem_form(request.POST) # Check if the form is valid
        if form.is_valid():
            task = form.cleaned_data['task']
            description = form.cleaned_data['description']
            deadline = form.cleaned_data['deadline']

            # Save the form data to create a new instance of the TodoItem_model
            new_TodoItem_model = form.save(commit=True)

            # Assign the current user to the 'user' field of the new TodoItem_model instance
            new_TodoItem_model.user = request.user
            new_TodoItem_model.save() # Save the new TodoItem_model instance to the database

            return redirect('todo')
        else:
            form = TodoItem_form(request.POST)
            print(form.errors)
    else:
        return render(request,'api/todo_create.html',{})

@csrf_protect
def delete(request, task):
    try:
        task_to_delete = TodoItem_model.objects.get(pk=task, user=request.user)
    except TodoItem_model.DoesNotExist:
        raise Http404("Task does not exist or does not belong to user.")
    task_to_delete.delete() # Delete the task from the database
    return redirect('todo')

def log_out(request):
    logout(request)  # Log out the user
    return redirect('welcome_view')

def completed_task(request,task_id):
    todo_item = get_object_or_404(TodoItem_model, pk=task_id)
    todo_item.completed = True # Mark the todo item as completed
    todo_item.save() # Save the changes to the todo item in the database


    return redirect('todo')