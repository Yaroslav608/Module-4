from django.shortcuts import render
from .models import Advertisement


def index(request):
    Advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render (request, 'top-sellers.html')

def advertisemet_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST,  request.FILES)
        if form.is_valid():
            new_advertisemet = form.save(commit=False)
            new_advertisemet.user = request.user
            new_advertisemet.save()
            url = reverse('main-page')
            return redirect(url)
        
    else:
        form = AdvertisementForm()
    context = {'form' : form}
    return render(request, 'advertisement-post.html', context)
