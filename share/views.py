
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Share
from .forms import ShareABookForm

#Views.

"""
Form for users to share a book
"""
def share_a_book(request):
    shared_list = Share.objects.all().filter(
        approved = True)
    if request.method == "POST":
        share_a_book_form = ShareABookForm(request.POST, request.FILES)
        if share_a_book_form.is_valid():
            shared_book = share_a_book_form.save(commit = False)
            shared_book.name = request.user.username
            shared_book.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for sharing!!")

    """
    Renders the Share page
    """

    share_a_book_form = ShareABookForm
    return render(
        request,
        "share/share.html",
        {"share_a_book_form": share_a_book_form,
        'shared':shared_list}
 )

"""
    Edit a shared post
    """
def share_edit(request, share_id):
 
    if request.method == "POST":
        share_to_edit = get_object_or_404(Share, pk=share_id)
        share_a_book_form = ShareABookForm(request.POST, request.FILES)
        if share_a_book_form.is_valid():
            share_to_edit.author = request.POST.get('author')
            share_to_edit.title = request.POST.get('title')
            share_to_edit.save()
            messages.add_message(request, messages.SUCCESS, "Updated !!")
        else:
            messages.add_message(request, messages.ERROR,
            'Error updating recipe!')
        return redirect('share')

def share_delete(request, share_id):
    """
    Delete a shared post
    """
    share = get_object_or_404(Share, pk = share_id)
    if share.name == request.user.username:
        share.delete()
        messages.add_message(request, messages.SUCCESS, 'Cookbook deleted!')
    else:
        messages.add_message(request, messages.ERROR,
            'You can only delete your own shared cookbooks!')
    return redirect('share')
