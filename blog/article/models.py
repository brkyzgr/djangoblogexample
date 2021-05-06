from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="Yazar") # Bunla user tablosuna işaret ediyor. on_delete= models.CASCADE ise user silindimi ona iat olan article ların silinmesini sağlar
    title = models.CharField(max_length=50,verbose_name="Başlık") # Bu model içindeki charfield ı kullanır.
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add = True,verbose_name="Oluşturulma Tarihi") # Burası tarih alanı için . auto_now_add = True --> bu o anki tarihi created date de atar.
    article_image = models.FileField(blank=True,null=True,verbose_name="Makaleye Fotoğraf Ekleyin") # null = true yazmamızın sebebi bu alan hem boş hem null olabilir.
    def __str__(self): # Bunun sayesinde title bilgisi gözükecek
        return self.title
    class Meta:
        ordering = ['-created_date'] # Bu şekilde en son eklenen makale ilk başta gösterir.
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comment") # related_name --> article ların commentlerini almamızı sağlar
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']