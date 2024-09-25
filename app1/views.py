from django.shortcuts import render


def main_page(request):
    return render(request, "index.html")


def about_page(request):
    return render(request, "about.html")
