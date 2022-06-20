from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=50, default='')
    desc = models.TextField("설명")
    
    def __str__(self):
        return self.name
    
    
class Article(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="사용자",null=True, blank=True)
    title = models.CharField("글제목", max_length=100, default='')
    category = models.ManyToManyField('Category', verbose_name="카테고리", default='')
    content = models.TextField("글내용", default='')
    exposure_start_date = models.DateField("노출 시작 일자")
    exposure_end_date = models.DateField("노출 시작 일자")
    
    def __str__(self):
        return f'{self.author}: {self.title}'
    
    
class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="댓글")
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="사용자")
    content = models.TextField("댓글내용")
    
    # def __str__(self):
    #     return self.article