from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Album, Song

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums,})

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album': album,})

def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        pk_val = request.POST['song']
        selected_song = album.song_set.get(pk=pk_val)
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail/html', {
            'error_message':"You did not select a valid song",
            'album': album
        })
    else:
        selected_song.is_favourite=True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album,})


# Create your views here.
