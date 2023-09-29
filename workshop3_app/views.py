from django.shortcuts import render
from .models import movie,Attend
from django.http import HttpResponseRedirect, HttpResponse
import json

# Create your views here.
def homepage(request):
    context = {
        'var1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)

def movie_list(request):
    #qs = PlayVideo.objects.all()
    list = [{'movie id': x.movie_id,
             'title': x.movie_name,
             'year': x.year,
             'genre': x.genre,
         }
            for x in movie.objects.order_by('movie_id')]
    #qs_json = serializers.serialize('json', list)
    qs_json = json.dumps(list)
    return HttpResponse(qs_json, content_type='application/json')


def movie_detail(request):
    movie_name = request.GET.get('movie_name')
    this_movie = movie()

    for x in movie.objects.filter(movie_name=movie_name):
        this_movie = x

    list = [{
        'movie_id': this_movie.movie_id,
        'movie_name': this_movie.movie_name,
        'year': this_movie.year,
        'genre': this_movie.genre,
    }]
    qs_json = json.dumps(list[0])
    return HttpResponse(qs_json, content_type='application/json')

def attend(request):
    attn_number = request.GET.get('attn_number')
    this_number = Attend()

    for x in Attend.objects.filter(attn_number=attn_number):
        this_number = x

    this_number.attend_info = True
    this_number.save()


    list = [{
    'attn_numbe': this_number.attn_number,
    'movie_name': this_number.movie_name,
    'seat_number': this_number.seat_number,
    'show_time': this_number.show_time,
    'attend_info': this_number.attend_info,
    }]
    qs_json = json.dumps(list[0])
    return HttpResponse(qs_json, content_type='application/json')



def attend_summary(request):
    list = [{'attn_numbe': x.attn_number,
            'movie_name': x.movie_name,
            'seat_number': x.seat_number,
            'show_time': x.show_time,
            'attend_info': x.attend_info,
             }
            for x in Attend.objects.order_by('attn_number')]
    # qs_json = serializers.serialize('json', list)
    qs_json = json.dumps(list)
    return HttpResponse(qs_json, content_type='application/json')