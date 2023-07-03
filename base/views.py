from django.shortcuts import render,redirect
from .models import Carousel, Bloodreq,Program,News,Explore,Fests,BloodDonation,BloodDonatedStudents,Community,Exploreimg
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


def home(request):
    carousels = Carousel.objects.all()
    blood_req = Bloodreq.objects.all()
    events = Program.objects.order_by('date')
    newses = News.objects.order_by('-created')[0:4]  #limits the news to 4 accending order by created
    explores = Explore.objects.all()
    fests = Fests.objects.all()
    communities = Community.objects.all() 

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
             'fests':fests,
             'communities':communities}
    return render(request,'home.html',context)


# program details page render 
def programDetails(request, pk):
    program = Program.objects.get(id=pk)
    context = {'program':program}
    return render(request,'users/program-details.html',context)

# news details page render 
def newsDetails(request, pk):
    news = News.objects.get(id=pk)
    context = {'news':news}
    return render(request,'users/news-details.html',context)

# explore details page render 
def exploreDetails(request, pk):
    explore = Explore.objects.get(id=pk)
    images = Exploreimg.objects.filter(explore=pk) 
    context = {'explore':explore, 'images':images}
    return render(request,'users/explore-details.html',context)

# fest details page render 
def festDetails(request, pk):
    fest = Fests.objects.get(id=pk)
    context = {'fest':fest}
    return render(request,'users/fest-details.html',context)

# fest details page render 
def communityDetails(request, pk):
    community = Community.objects.get(id=pk)
    context = {'community':community}
    return render(request,'users/fest-details.html',context)

# blood donation page renders and save the user data 
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
    return render(request,'users/blood_donation_form.html',context)

# if the blood donation form is submitted suceessfully 
def donateBloodRes(request):
    return render(request, 'blood-donation-response.html')




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


@login_required()
def bloodDonatedAdd(request,pk):
    bloodDonor = BloodDonation.objects.get(id=pk)
    newDonation = BloodDonatedStudents()
    newDonation.name = bloodDonor.name
    newDonation.blood_type = bloodDonor.blood_type
    newDonation.roll_no = bloodDonor.roll_no
    newDonation.phone = bloodDonor.phone
    newDonation.save()
    bloodDonor.delete()
    return None


@login_required(login_url='loginpage')
def bloodreqDel(request, pk):
    bloodreq = Bloodreq.objects.get(id=pk)
    bloodreq.delete()
    return redirect('blood-donation-admin')






