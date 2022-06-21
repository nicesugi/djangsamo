from django.db import models

class Product(models.Model):
    user = models.ForeignKey(to='user.User', on_delete=models.CASCADE, verbose_name="상품작성자")
    name = models.CharField("상품이름", max_length=100)
    thumbnail = models.FileField("썸네일", upload_to="product/")
    description = models.TextField("상품설명")
    created = models.DateTimeField("등록일자", auto_now_add=True)
    
    exposure_start_date = models.DateField("노출 시작 일자")
    exposure_end_date = models.DateField("노출 종료 일자")
    