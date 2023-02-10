from django.shortcuts import  render, redirect
from .forms import NewUserForm,studentForm
from django.contrib.auth import login
from django.contrib import messages
from .models  import student1
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})


def signup (request ):
    form= studentForm()
    return render(request,"main/signup.html",{'form':form})


def signupaction (request ):
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            name= form.changed_data['name']
            id = form.changed_data['studentid']
            email = form.changed_data['email']
            password =form.changed_data['password']
            stu =student1(name=name,id=id,email=email,password=password)
            stu.save()
            return render(request,"signup.html",{'form':form})
            
    return render(request,"signup.html",{'form':form})