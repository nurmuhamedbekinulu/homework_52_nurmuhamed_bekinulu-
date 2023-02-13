from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from webapp.cat import Cat
from static.classes.static import Static


def index_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'index.html')
    print(request.POST)
    Static.cat.name = request.POST.get('name')
    context = {
        'name': Static.cat.name,
        'age': Static.cat.age,
        'satiety': Static.cat.satiety,
        'happines': Static.cat.happines,
        'awake_status': Static.cat.awake_status,
        'actions': Static.actions
    }
    return render(request, 'cat_stats.html', context=context)

def cat_stats_view(request: WSGIRequest):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'play':
            Static.cat.play()
        elif action == 'feed':
            Static.cat.feed()
        else:
            Static.cat.sleep()
            print(Static.cat.awake_status)
        context = {
            'name': Static.cat.name,
            'age': Static.cat.age,
            'satiety': Static.cat.satiety,
            'happines': Static.cat.happines,
            'awake_status': Static.cat.awake_status,
            'actions': Static.actions
        }
        return render(request, 'cat_stats.html', context=context)