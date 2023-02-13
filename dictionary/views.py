from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.

def index(request):
    return render(request, 'index.html')
def meaning(request):
    word=request.POST.get('word')
    dictionary=PyDictionary()
    meaning=dictionary.meaning(word)
    synonyms=dictionary.synonym(word)
    antonyms=dictionary.antonym(word)
    context={
        'meaning':meaning['Noun'][0],
        'synonyms':synonyms,
        'antonyms':antonyms
    }
    return render(request, 'word.html',context)