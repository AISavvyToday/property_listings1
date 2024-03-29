from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor 
from listings.choices import price_choices, bedroom_choices, town_choices



# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-listing_date').filter(is_published=True)[:3]
    
    context ={
        'listings': listings,
        'town_choices':town_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors=Realtor.objects.order_by('-hire_date')[:3]

    mvr_realtors=Realtor.objects.all().filter(is_mvr=True)

    context= {
        'realtors':realtors,
        'mvr_realtors':mvr_realtors
    }


    return render(request, 'pages/about.html', context)
