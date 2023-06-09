#used to carryout Http requests
from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    return render(request,'index.html',{})

def analyze(request):
    text=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    nocaps=request.POST.get('nocaps','off')
    removedigi=request.POST.get('removedigi','off')
    find=request.POST.get('find','')
    replace=request.POST.get('replace','')
    analyzed=""
    if text !='default':
        analyzed=text
    charcount=0
    if removepunc=='on':
        #punctuations: !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ 
        analyzed=re.sub(r'[^\w\s]', '', analyzed)
    
    if fullcaps=='on' and nocaps=='off':
        analyzed=analyzed.upper()
    
    if nocaps=='on' and fullcaps=='off':
        analyzed=analyzed.lower()

    if removedigi=='on':
        #digits: 0-9
        analyzed=re.sub(r'\d', '', analyzed)
    
    analyzed=analyzed.replace(find,replace)
    for i in analyzed:
        if i != ' ':
            charcount+=1
    params={'analyzed_text':analyzed,'charcount':str(charcount)}
    return render(request,'analyze.html',params) 
    
    