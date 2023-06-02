from django.http import HttpResponse


def main(request):
    return HttpResponse('<h1> HOME page </h1>')


def index(request):
    return HttpResponse('Hello, world. You re at the polls index.')


def product(request, product_id):
    return HttpResponse(f'<h1>PRODUCT</h1> <p>{product_id}</p>')
