from django.contrib import admin
from .models import Article,Comment # Bu şekilde modeldeki article dahil ettik

admin.site.register(Comment) # Bu şekilde commentti kaydettik.

# Register your models here.
# admin.site.register(Article) # Bu şekilde article ı admin panelişnde gösterdik.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin): # Burada admin içindeki modeladminden türettik
    list_display = ["title","author","created_date"] # Bu şekilde articlen yazar ve başlığını gömsterdik.
    list_display_links = ["title","created_date"] # Bu şekilde linke çevirdik.
    search_fields = ["title"] # Bu şekilde sadece title bilgisine göre arama motoru oluşturulur.
    list_filter = ["created_date"] # Bu şekilde gün ve ay bilgisine görre makale oluşturulma tarihlerini gösteren kısım oluşturur.
    
    class Meta: # Meta olmak zorunda 
        model = Article # Bu şekilde articleadmin ile article birleştirdik
