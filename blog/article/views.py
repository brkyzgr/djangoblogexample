from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword) # title__contains : Bu sorgu keywordün geçtiği article ları döndürecek.
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all() # Bu şekilde bütün makaleleri veri tabanından aldık ve bir objeye atadık(bir sözlük içinde olacak templatelardan erişebilmek için).
    return render(request,"articles.html",{"articles":articles})


def index(request): # Http requestte atılınca django bilgileri taşıyan bu değişkeni gönderir. Ve her fonksiyonda bulunması gerekir ve ilk parametre olarak bulunması gerekir.
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author= request.user) # Burada sitede girmiş olan kullanıcıların makalelerini gösterir.
    context = {
        "articles" : articles
    }

    return render(request,"dashboard.html",context)

@login_required(login_url = "user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user

        article.save()

        messages.success(request,"Makale başarıyla oluşturuldu...")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    # article = Article.objects.filter(id = id).first()  Burada makalenin verisini aldık.
    article = get_object_or_404(Article,id = id)
    
    comments = article.comment.all()

    return render(request,"detail.html",{"article":article,"comments":comments})

@login_required(login_url = "user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article) # intance içine objeyi gönderirsek bu objedeji tüm bilgiler article fromun içine yazılır.
    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user

        article.save()

        messages.success(request,"Makale başarıyla güncellendi...")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form})

@login_required(login_url = "user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete() # Böyle veri silinir
    messages.success(request,"Makale Başarıyla Silindi")

    return redirect("article:dashboard")

def addComment(request,id):
    # İlk önce id ye göre postu alcaz.
    article = get_object_or_404(Article,id = id)
    # Bu methodun post mu get mi olduğunu kontrol edecez.
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        # Article da alttaki gibi ekleyecez.

        newComment = Comment(comment_author = comment_author,comment_content=comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))