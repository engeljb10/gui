from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'audit/index.html',{})

def people(request):
    return render(request, 'audit/index.html', {'people': Person.objects.all()})
