from django.shortcuts import render

# Create your views here.


def people(request):
    return render(request, 'audit/index.html', {'people': Person.objects.all()})
