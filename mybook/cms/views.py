from django.shortcuts import render
from django.http import HttpResponse


def book_list(request):
    return HttpResponse('List of Book info')


def book_edit(request, book_id=None):
    return HttpResponse('Edit Book info')


def book_del(request, book_id):
    return HttpResponse('Delete Book')