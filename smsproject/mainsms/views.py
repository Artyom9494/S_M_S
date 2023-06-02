from django.http import HttpResponse, HttpResponseNotFound


def main(request):
    return HttpResponse('<h1> HOME page </h1>')


def index(request):
    return HttpResponse('Hello, world. You re at the polls index.')


def product(request, product_id):
    return HttpResponse(f'<h1>PRODUCT</h1> <p>{product_id}</p>')


# обработка неверных урл адресов
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>page_not_found 404</h1>')
