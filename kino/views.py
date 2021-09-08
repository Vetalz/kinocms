from django.shortcuts import render


def index(request):
    context = {
        'title': 'KinoCMS'
    }
    return render(request, 'kino/index.html', context)
