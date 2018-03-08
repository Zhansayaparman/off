from django.shortcuts import render

from .models import Workers, Admin, Office

def index(request):

    num_works = Workers.objects.all().count()
    num_admin=Admin.objects.count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'index.html',
        context={'num_works':num_works,'num_admin':num_admin,
            'num_visits':num_visits}, # num_visits appended
    )