from django import forms
from .models import Article

class ArticleForm(forms.ModelForm): # Burada formları ModelForm bir modele göre oluşturduk..
    class Meta:
        model = Article
        fields = ["title","content","article_image"]