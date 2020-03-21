from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    sentence = request.GET['fulltext']
    word_count = len(sentence.strip().split())

    word_dictionary = {}
    for word in sentence.strip().split():
        if word in word_dictionary:
            # If the word appeared before
            word_dictionary[word] += 1
        else:
            # If the word appeared just now
            word_dictionary[word] = 1

    sortedwords = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'word_count':word_count,'sentence':sentence,'sortedwords':sortedwords})

def about(request):
    return render(request,'about.html')
