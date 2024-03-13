from django.shortcuts import render,redirect
from .models import Articles
from .forms import articleForm
from .utils import searchProjects
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def articlesPage(request):
    projects, search_query = searchProjects(request)
    context = {'articles':projects,'search_query': search_query}
    return render(request, "articles/articles.html",context)

@login_required(login_url="login")
def singleArticle(request, pk):
    singleArt = Articles.objects.get(id=pk)
    context = {"article":singleArt}

    return render(request, 'articles/single_article.html',context)

@login_required(login_url="login")
def editArticle(request,pk):
    article = Articles.objects.get(id=pk)
   
        
    form = articleForm(instance=article)

    if request.method == 'POST':
        form = articleForm(request.POST,request.FILES,instance=article)
        if form.is_valid:
            form.save()
            return redirect("/")
    
    
    context = {'form':form}
    
    return render(request, "articles/article_form.html",context)