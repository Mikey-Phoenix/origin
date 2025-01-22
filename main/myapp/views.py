from django.shortcuts import render, redirect
from .models import ArtWork
from .forms import BidForm
from django.http import HttpResponseRedirect

# Create your views here.
# def all_artworks(request):

def home(request):
    submitted = False
    arts = ArtWork.objects.all()
    # selectedArt = ArtWork.objects.get(id)
    # if request.method == 'POST':
    #     form = BidForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/home?submitted=True')
    # else:
    #     form = BidForm
    #     if 'submitted' in request.GET:
    #         submitted = True
    
    return render(request, 'myapp/index.html',
                  {'arts': arts,
                #    'form': form,
                   'submitted': submitted})
    # return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def gallery(request):
    arts = ArtWork.objects.all()
    return render(request, 'myapp/gallery.html',
                  {'arts': arts})

def bids(request):
    arts = ArtWork.objects.all()
    return render(request, 'myapp/bids.html',
                  {'arts': arts})

def make_bid(request, art_id):
    # submitted = False
    arts = ArtWork.objects.all()
    selected_art = ArtWork.objects.get(pk=art_id)
    form = BidForm(request.POST or None, instance=selected_art)
    # if request.method == 'POST':
    #     form = BidForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/home?submitted=True')
    # else:
    #     form = BidForm
    #     if 'submitted' in request.GET:
    #         submitted = True
    if form.is_valid():
        form.save()
        # return redirect('home')
    return render(request, 'myapp/make_bid.html',
                  {'arts': arts,
                   'form': form,
                   'selected_art': selected_art,
                #    'submitted': submitted,
                   })