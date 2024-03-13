
from django.db.models import Q
from .models import Profiles







def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')


    profiles = Profiles.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(username__icontains=search_query) 
    )

    return profiles, search_query
