from django.shortcuts import render
from django.http import HttpResponse


def book_list(request):
    return HttpResponse('List of Book info')


def book_edit(request, book_id=None):
    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'cms/book_edit.html', dict(form=form, book_id=book_id))


def book_del(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('cms:book_list')