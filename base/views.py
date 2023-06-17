from django.shortcuts import render,redirect
from .models import Carousel, Bloodreq,Program,News,Explore,Fests,BloodDonation,BloodDonatedStudents
from .forms import BloodDonationForm, Bloodreqform ,UserForm
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def loginPage(request):
    form = UserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('blood-donation-admin')
        else:
            return redirect('loginpage')
            
    context = {'form':form}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def creators(request):
    context = {}
    return render(request, 'creators.html' ,context)

def home(request):
    carousels = Carousel.objects.all()
    blood_req = Bloodreq.objects.all()
    events = Program.objects.order_by('date')
    newses = News.objects.order_by('-created')[0:3]  #limits the news to 5
    explores = Explore.objects.all()
    fests = Fests.objects.all()

    for event in events:
        # deletes the event when the time is up 0 for events
        due_date_events = datetime.combine(date=event.date, time=event.time)
        if due_date_events <= datetime.now():
            event.delete()


    context={'carousels':carousels, 
             'blood_req':blood_req, 
             'events':events, 
             'newses':newses, 
             'explores':explores,
             'fests':fests}
    return render(request,'home.html',context)

def news(request, pk):
    news = News.objects.get(id=pk)
    context = {'news':news}
    return render(request,'news.html',context)


def explore(request, pk):
    explore = Explore.objects.get(id=pk)
    context = {'explore':explore}
    return render(request,'explore.html',context)

def fests(request, pk):
    fests = Fests.objects.get(id=pk)
    context = {'fests':fests}
    return render(request,'fests.html',context)

def donateBlood(request):
    form = BloodDonationForm()
    if request.method == 'POST':
        form = BloodDonationForm(request.POST)
        if form.is_valid():
            # Save the modified form data
            bloodDonation = form.save()
            bloodDonation.save()
            return redirect('blood-donation-response')

    context = {'form':form}
    return render(request,'blood_donation_form.html',context)

def donateBloodRes(request):
    return render(request, 'blood_donation_response.html')

def program(request, pk):
    program_details = Program.objects.get(id=pk)
    context={
        'program_details': program_details
    }
    return render(request,'news.html',context)

@login_required(login_url='loginpage')
def donateBloodAdmin(request):
    form = Bloodreqform()
    bloodDonors = BloodDonation.objects.all()
    bloodreqs = Bloodreq.objects.all()
    bloodDonatedStudents = BloodDonatedStudents.objects.all()

    if request.method == 'POST':
        form = Bloodreqform(request.POST)
        if form.is_valid():
            bloodreq = form.save()
            bloodreq.save()
            return redirect('blood-donation-admin')
            
    context = {
        'form':form, 
        'bloodDonors':bloodDonors, 
        'bloodreqs':bloodreqs,
        'bloodDonatedStudents':bloodDonatedStudents}
    return render(request,'blood_donation_admin.html',context)


@login_required(login_url='loginpage')
def bloodDonatedAdd(request,pk):
    bloodDonor = BloodDonation.objects.get(id=pk)
    newDonation = BloodDonatedStudents()
    newDonation.name = bloodDonor.name
    newDonation.blood_type = bloodDonor.blood_type
    newDonation.roll_no = bloodDonor.roll_no
    newDonation.phone = bloodDonor.phone
    newDonation.save()
    bloodDonor.delete()
    return redirect('blood-donation-admin')


@login_required(login_url='loginpage')
def bloodreqDel(request, pk):
    bloodreq = Bloodreq.objects.get(id=pk)
    bloodreq.delete()
    return redirect('blood-donation-admin')






