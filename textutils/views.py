# this file is created by myself--Rohit
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # getting text and responses of our checkboxes in below lines
    djtext = request.POST.get('text', 'default')
    remove_punc = request.POST.get('remove_punc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    wordcount = request.POST.get('wordcount', 'off')
    new_line_remover = request.POST.get('new_line_remover', 'off')
    space_remover = request.POST.get('space_remover', 'off')

    print(djtext, remove_punc)

    # checking whether our checkbox is checked or not
    # if checked then apply some functioning on our data using the operations below
    if remove_punc == 'on':
        # code to remove punctuations from our text
        punctuations = '''!()[]-{};:'"=+`,\<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'Message': 'Your required functionality is applied see the results below',
                  'analyzed_text': analyzed}
        djtext = analyzed
    if fullcaps == 'on':
        # code to transform text to uppercase
        analyzed = ""
        for char in djtext:

            analyzed += char.upper()
        params = {'Message': 'Your required functionality is applied see the results below',
                  'analyzed_text': analyzed}
        djtext = analyzed
    if wordcount == 'on':
        analyzed = 0
        for char in djtext:
            analyzed += 1
        params = {'Message': 'Your required functionality is applied see the results below',
                  'analyzed_text': analyzed}
        djtext += str(analyzed)
    if new_line_remover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != "\r":
                analyzed += char
        params = {'Message': 'Your required functionality is applied see the results below',
                  'analyzed_text': analyzed}
        djtext = analyzed
    if space_remover == 'on':
        analyzed = ''
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed += char
        params = {'Message': 'Your required functionality is applied see the results below',
                  'analyzed_text': analyzed}

    if(remove_punc != 'on' and new_line_remover != 'on' and fullcaps != 'on' and space_remover != 'on' and wordcount != 'on'):
        return HttpResponse("Error!........Please select the options to see the functioning")

    return render(request, 'analyze.html', params)

