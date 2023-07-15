from django.shortcuts import render,redirect
from .models import *
from .forms import BloodDonationForm
from datetime import datetime



def home(request):
    carousels = Carousel.objects.all()
    blood_req = Bloodreq.objects.all()
    events = Program.objects.order_by('date')
    newses = News.objects.order_by('-created')[0:4]  #limits the news to 4 accending order by created
    explores = Explore.objects.all()
    fests = Fests.objects.all()
    communities = Community.objects.all() 
    clubs = Clubs.objects.all()

    for event in events:
        # deletes the event when the time is up 0 for events
        due_date_events = datetime.combine(date=event.date, time=event.time)
        if due_date_events <= datetime.now():
            event.delete()


    context={'carousels':carousels, 
             'blood_req':blood_req, 
             'events':events, 
             'clubs':clubs,
             'newses':newses, 
             'explores':explores,
             'fests':fests,
             'communities':communities}
    return render(request,'home.html',context)


# program details page render 
def programDetails(request, pk):
    program = Program.objects.get(slug=pk)
    context = {'program':program}
    return render(request,'users/program-details.html',context)

# news details page render 
def newsDetails(request, pk):
    news = News.objects.get(slug=pk)
    context = {'news':news}
    return render(request,'users/news-details.html',context)

# explore details page render 
def exploreDetails(request, pk):
    explore = Explore.objects.get(slug=pk)
    # images = Exploreimg.objects.filter(explore=pk) 
    context = {'explore':explore}
    return render(request,'users/explore-details.html',context)

# fest details page render 
def festDetails(request, pk):
    fest = Fests.objects.get(slug=pk)
    context = {'fest':fest}
    return render(request,'users/fest-details.html',context)

# fest details page render 
def communityDetails(request, pk):
    community = Community.objects.get(slug=pk)
    context = {'community':community}
    return render(request,'users/community-details.html',context)

# fest details page render 
def clubDetails(request, pk):
    club = Clubs.objects.get(slug=pk)
    context = {'club':club}
    return render(request,'users/club-details.html',context)

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










