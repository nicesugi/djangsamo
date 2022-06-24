from django.db import models

class Product(models.Model):
    user = models.ForeignKey('user.User', verbose_name="상품작성자", on_delete=models.SET_NULL, null=True)
    thumbnail = models.ImageField("썸네일", upload_to="product/thumbnail", height_field=None, width_field=None)
    description = models.TextField("상품설명")
    created = models.DateTimeField("등록일자", auto_now_add=True)
    modified = models.DateTimeField("수정일자", auto_now=True)
    exposure_end_date = models.DateField("노출 종료 일자")
    is_active = models.BooleanField("활성화여부")
    price = models.IntegerField("가격")
    # title = models.CharField("상품이름", max_length=100)
    # exposure_start_date = models.DateField("노출 시작 일자")
    
    
class Review(models.Model):
    user = models.ForeignKey('user.User', verbose_name="상품작성자", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('Product', verbose_name="상품", on_delete=models.SET_NULL, null=True)
    content = models.TextField("내용")
    created = models.DateTimeField("등록시간", auto_now_add=True)
    rating = models.IntegerField("평점")