from django.shortcuts import render

def index(request):
    context = {
        'judul' : 'HOME',
        'subjudul' : 'ALBAR',
        'nav' : [
            ['/','home'],
            ['/blog','blog'],
        ]
    }
    return render(request, 'index.html', context)