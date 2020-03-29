# I have created this file
#   code for personal navigator
#def index(request):
   # return  HttpResponse('''<h1>Hi Vinay</h1> <a href="https://www.youtube.com/?reload=9" >Direct Path To Youtube </a>''')

#def about(request):
   # return  HttpResponse("In about function")

from django.http import HttpResponse
from django.shortcuts import render

# Code of laying pipeline
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')

def index(request):
    #vinay = {'name':'vinay','place':'nanded'}
    #return render(request,'index.html',vinay)
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
 #check checkbox is on
    if removepunc=="on":
        punctuations= '''!()-[]{};:"'\,<>./?@#$%^&*_~'''
        analyzed=""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i

        vinay= {'purpose':'Remove punctuations','analyzed_text':analyzed}
        #analyze the text
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        vinay={'purpose':'Change To Upper Case','analyzed_text':analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        vinay = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed


    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        vinay = {'purpose': 'Extra space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == "on"):
        count=0
        for char in djtext:
            count+=1
        vinay = {'purpose': 'Number of characters', 'analyzed_text': count}

    if (removepunc!="on" and charcount!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("Please Select Any Operation ..")

    return render(request, 'analyze.html', vinay)


#def capfirst(request):
 #   return HttpResponse("capitalize first <a href='/'>Back</a>")

#def newlineremove(request):
    #return HttpResponse("newlineremove <a href='/'>Back</a>")
#def spaceremove(request):
    #return HttpResponse("spaceremove <a href='/'>Back</a>")
#def charcount(request):
    #return HttpResponse("charcount <a href='/'>Back</a>")