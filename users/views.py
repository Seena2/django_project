from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method== 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            # save the form, this will also authomatically hash the password
            form.save()
            # parse the form data
            userName=form.cleaned_data.get('username')
            messages.success(request,f' Your account has been created, you can able to login now')
            # return redirect('blog_home') #the name 'blog_home' is define in blog/urls
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method== 'POST':
        # Create instance of the forms and populate them with current user data and POST form data
        uu_form=UpdateUserForm( request.POST, instance=request.user)
        up_form=UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        # Validate the forms and save data, send flash msg and redirect user 
        if uu_form.is_valid() and up_form.is_valid():
            uu_form.save()
            up_form.save()
            messages.success(request,f' Your account has been updated!')
            return redirect('profile')
    else:
         # Create instance of the forms and populate them with current user data
        uu_form=UpdateUserForm( instance=request.user)
        up_form=UpdateProfileForm(instance=request.user.profile)

    context={
        'uu_form':uu_form,
        'up_form':up_form
    }
    return render(request,'users/profile.html',context)

