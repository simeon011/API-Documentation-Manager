from django.shortcuts import render

from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def dashboard(reqeust):
    return render(reqeust, 'common/dashboard.html')
