from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from comments.forms import CommentForm
from comments.models import Comment
from poll.forms import DocumentForm
from poll.models import Document, Article


# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html', )


# file upload
@login_required
def list(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES('docfile'))
            newdoc.save()
            return HttpResponseRedirect('/list')
        else:
            form = DocumentForm()
        documents = DocumentForm()
        documents = Document.objects.all()

        return render(request, 'list.html', {'documents': documents, 'form': form})




@login_required
def about_us(request):
    return render(request, "about.html", {})


def user_account(request):
    return render(request, "useraccount.html", {})

@login_required
def articles_list(request):
    list = Article.objects.all()
    page = request.GET.get('page', 1)  # Show 25 contacts per page
    paginator = Paginator(list, 1)

    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list = paginator.page(paginator.num_pages)
    return render(request, "article.html", {"list": list})

@login_required
def article_details(request, id):
    article = get_object_or_404(Article, id=id)
    comments = Comment.objects.filter(article_id=id)
    # logic for saving form

    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment_data = form.cleaned_data.get("content")
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        Article.objects.filter(pk=article.pk).update(comments=article.comments + 1)
        return HttpResponseRedirect(article.get_absolute_url())

    context = {
        "article": article,
        "comments": comments,
        "comment_form": form,
    }
    return render(request, "article_details.html", context)


def article_category(request, category):
    list = Article.objects.filter(category=category)
    context = {
        "article": list,
    }
    return render(request, "article.html", context)


def search_titles(request,):
    if request.method == "GET":
        search_text = request.GET[' search_text']
        if search_text is not None and search_text != u"":
            search_text = request.GET[' search_text']
            list = Article.objects.filter(status__contains=search_text)
        else:
            list = []
        return render(request, 'article.html', {'list': list})
