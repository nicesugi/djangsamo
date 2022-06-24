from rest_framework import serializers
from datetime import datetime
from django.db.models import Avg

from product.models import Product as ProductModel
from product.models import Review as ReviewModel


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.fullname
    
    class Meta:
        model = ReviewModel
        fields = ["user", "content", "created", "rating", ]    


class ProductSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()
    
    def get_review(self, obj):
        reviews = obj.review_set
        return {
            "last_review":ReviewSerializer(reviews.last()).data,
            "average_rating": reviews.aggregate(avg=Avg("rating"))["avg"]
        }
    
    def validate(self, data):
        exposure_end_date = data.get("exposure _end_data", "")
        if exposure_end_date and exposure_end_date < datetime.now().date():
            raise serializers.ValidationError(
                detail= {"error": "유효하지않은 노출종료 날짜입니다"},
            )
        return data
    
    #127.0.0.1:8000/product/1/ post 메소드
    def create(self, validated_data):
        product = ProductModel(**validated_data)
        product.save()
        product.description += f"\n\n{product.created.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다"
        product.save() # 두번 세이브하는 이유는 1차에는 저장되는값이 없어서 저장 product.created 생성되기때문에 저장하고/ replace있는 이유는 자잘한 시간정보가 나오기 때문에 없애주기위함
        return product
    
    #127.0.0.1:8000/product/1/ put 메소드
    def update(self, instance, validated_data):
        for key,value in validated_data.items():
            print(f'{key}키의 밸류는?{value}')
            if key == "description":
                value += f"\n\n{instance.created.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다"
            setattr(instance, key, value)
        instance.save()
        instance.description = f"{instance.modified.replace(microsecond=0, tzinfo=None)} 수정되었습니다. \n\n"\
                                    + instance.description
        instance.save()
        return instance
            
    
    class Meta:
        model = ProductModel
        fields = ["user", "thumbnail", "description", 
                  "created", "modified", "exposure_end_date", "is_active", "price", "review" ]  
        
