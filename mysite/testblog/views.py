from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Hello

# Create your views here.
def Hello_list(request):
    what = Hello.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    how = Hello.objects.all()
    return render(request, 'world.html',{'whatsup':what, 'howsup':how})

def Hello_detail(request, wow):
    why = get_object_or_404(Hello, pk=wow)
    return render(request, 'world_detail.html', {'whyup':why})