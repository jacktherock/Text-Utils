# I have created this file - abhijeet

from django.http import HttpResponse
from django.shortcuts import render

def index(request):     # index() is a function
    return render(request, 'index.html')

def about(request):     # about() is a function
    return render(request, 'about.html')
    # return HttpResponse("About Page <a href='/'>Home</a>")

def contact(request):     # about() is a function
    return render(request, 'contact.html')
    # return HttpResponse("About Page <a href='/'>Home</a>")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    # print(removepunc)
    # print(djtext)

    # Check with checkbox is on
    if removepunc == "on":
        # analyzed = djtext
        punctuations = ''':()-[]{};'"\,<>./?@#$%^&*_~!`+'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        dict1 = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', dict1)

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        dict1 = {'purpose':'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        dict1 = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        dict1 = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if(charcounter == "on"):
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        dict1 = {'purpose': 'Count Characters', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcounter != "on"):
        return HttpResponse("Please Select Any Operation and Try Again !!")
    
    return render(request, 'analyze.html', dict1)

