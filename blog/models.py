from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=50, default='')
    desc = models.TextField("설명")
    
    def __str__(self):
        return self.name
    
    
class Article(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="사용자")
    title = models.CharField("글제목", max_length=100)
    category = models.ManyToManyField("Category", verbose_name="카테고리")
    content = models.TextField("글내용")
    
    def __str__(self):
        return f'{self.author}: {self.title}'
    
    