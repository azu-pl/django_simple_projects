from django.shortcuts import render

# Create your views here.


def welcome(request):
    return render(request, 'mymath/welcome.html')


def add(request, a, b):
    result = a + b
    ctx = {'first_num': a, 'second_num': b, 'result': result}

    return render(request, 'mymath/add.html', ctx)


def subtraction(request, a, b):
    result = a - b
    ctx = {'first_num': a, 'second_num': b, 'result': result}

    return render(request, 'mymath/sub.html', ctx)


def division(request, a, b):
    result = a / b
    ctx = {'first_num': a, 'second_num': b, 'result': result}

    return render(request, 'mymath/div.html', ctx)


def multiply(request, a, b):
    result = a * b
    ctx = {'first_num': a, 'second_num': b, 'result': result}

    return render(request, 'mymath/multi.html', ctx)
