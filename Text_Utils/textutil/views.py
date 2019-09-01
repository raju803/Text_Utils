from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('Home')
    #parms={'raju':'Kamrul Islam Raju'}
    return render(request,'index.html')

# def analyze(request):
#     # Get the text
#     djtext =request.GET.get('text','default')
#     removepunc =request.GET.get('removepunc','off')
#     print(djtext)
#     print(removepunc)
#     if removepunc=='on':
#         #analyzed=djtext
#         punctuations ='''!()-[]{};:'"\,<>.+/?@#$%^&*_'''
#         analyzed=""
#         for char  in djtext:
#             if char not in punctuations:
#                 analyzed=analyzed + char
#         parms={'purpose':'Remove Punctions','analyze_text':analyzed}
#         return render(request,'analyze.html',parms)
#     else:
#         return HttpResponse('<h1>Error</h1>')


def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("<h1>Error</h1>")