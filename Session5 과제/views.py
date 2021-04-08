from django.shortcuts import render

# Create your views here.


def hello(request):
    return render(request, "hello.html")


def count(request):
    return render(request, "count.html")


def result(request):
    text = request.POST['text']
    total_len = len(text)
    no_space_text_len = len(text.replace(' ', ''))
    count_words = len(text.split(' '))
    return render(request, 'result.html', {
        "text": text,
        "total_len": total_len,
        "no_space_text_len": no_space_text_len,
        "count_words": count_words
    })
