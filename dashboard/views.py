from django.shortcuts import render

def sansa_esg_dashboard(request):
    return render(request, "dashboard/index.html")
