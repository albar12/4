from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'BLOG',
        'subjudul' : 'ALBAR',
        'nav' : [
            ['/','home'],
            ['/blog','blog'],
            ['/blog/cerita','cerita'],
        ]
    }
    return render(request, 'blog\index.html', context)

def cerita(request):
    context = {
        'judul' : 'CERITA',
        'subjudul' : 'ALBAR',
        'badan' : 'lorem',
        'nav' : [
            ['/blog','blog'],
            ['/blog/cerita','cerita'],
        ]
    }
    return render(request, 'blog\index.html', context)
