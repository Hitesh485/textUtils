from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newLine = request.POST.get('newLine', 'off')
    spaceRemove = request.POST.get('spaceRemove', 'off')
    extraSpaceRemove = request.POST.get('extraSpaceRemove', 'off')
    charCount = request.POST.get('charCount', 'off')

    analyzed = djtext

    if (removepunc == 'on'):
        method = "Remove Punctuation"
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        tempStr = ""
        for char in djtext:
            if (char not in punctuation):
                tempStr = tempStr + char
            analyzed = tempStr

    if (fullcaps == 'on'):
        method = "UPPERCASE"
        analyzed = analyzed.upper()

    if (newLine == 'on'):
        method = "New Line Removed"
        tempStr = ""
        for char in analyzed:
            if (char != '\n' and char != '\r'):
                tempStr = tempStr + char
            analyzed = tempStr

    if (spaceRemove == 'on'):
        method = "Removed Spaces"
        tempStr = ""
        for char in analyzed:
            if (char not in ' '):
                tempStr = tempStr + char
            analyzed = tempStr

    if (extraSpaceRemove == 'on'):
        method = "Removed Extra Space"
        tempStr = ""
        index = 0
        n = len(analyzed)
        for char in analyzed:
            if (index < n):
                if (not(analyzed[index] == ' ' and analyzed[index+1] == ' ')):
                    tempStr = tempStr + char
                index = index + 1
        analyzed = tempStr
    
    if (charCount == 'on'):
        method = "Charachter Count"
        count = 0
        count = len(analyzed)
        analyzed = "Generated String: |" + analyzed + "|" + " The charachter in given string is : " + str(count)
            
    if (removepunc == 'on' or fullcaps == 'on' or newLine == 'on' or spaceRemove == 'on' or extraSpaceRemove == 'on' or charCount == 'on'):
        params = {'purpose': method, 'analyzed_text': analyzed}
        # Analyze text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error!")