from django.shortcuts import render

def people(request):
    return render(request, 'people.html', {'people': Person.objects.all()})
