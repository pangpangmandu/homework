from django.shortcuts import render
import operator
def home(request):
    return render(request,'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET.get('fulltext')
    word_list = full_text.split()
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    sorted_wd = sorted(word_dictionary.items(), key=operator.itemgetter(1))

    return render(request, 'wordcount/count.html', {'fulltext':full_text, 'total': len(word_list), 'dictionary':word_dictionary.items(), 'stwd':sorted_wd})
# Create your views here.
