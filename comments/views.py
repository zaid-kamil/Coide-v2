from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import Comment
import operator

from django.db.models import Q


@login_required  # (login_url='/login/') #LOGIN_URL = '/login/'
def comment_delete(request, id):
    # obj = get_object_or_404(Comment, id=id)
    # obj = CommentFormmment.objects.get(id=id)
    try:
        obj = Comment.objects.get(id=id)
    except:
        raise Http404

    if obj.user != request.user:
        # messages.success(request, "You do not have permission to view this.")
        # raise Http404
        reponse = HttpResponse("You do not have permission to do this.")
        reponse.status_code = 403
        return reponse
        # return render(request, "confirm_delete.html", context, status_code=403)

    if request.method == "POST":
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        messages.success(request, "This has been deleted.")
        return HttpResponseRedirect(parent_obj_url)
    context = {
        "object": obj
    }
    return render(request, "confirm_delete.html", context)


def comment_thread(request, id):
    try:
        comment = Comment.objects.filter(id=id)
    except:
        raise Http404
    content_object = comment.content_object  # Post that the comment is on
    content_id = comment.content_object.id

    initial_data = {
        "content_type": comment.content_type,
        "object_id": comment.object_id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated():

        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        article_id = form.cleaned_data.get('article_id')
        content_data = form.cleaned_data.get("content")
        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            article_id=article_id,
            content=content_data,
        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

    context = {
        "comment": comment,
        "form": form,
    }
    return render(request, "comment_thread.html", context)
