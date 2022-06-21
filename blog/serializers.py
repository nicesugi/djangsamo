from rest_framework import serializers
from blog.models import Comment as CommentModel
from blog.models import Article as ArticleModel



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = CommentModel
        fields = ["user", "content"]
        
        
class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, source="comment_set", read_only=True)
    
    
    def get_category(self, obj):
        return [category.name for category in obj.category.all()]

    class Meta:
        model = ArticleModel
        fields = ["author", "category", "title", "content", "comments", 
                  "exposure_start_date", "exposure_end_date"
                  ]
        
        # 각 필드에 해당하는 다양한 옵션 지정
        extra_kwargs = {
            # write_only : 해당 필드를 쓰기 전용으로 만들어 준다.
            # 쓰기 전용으로 설정 된 필드는 직렬화 된 데이터에서 보여지지 않는다.
            'user': {'write_only': True}, # default : False
            'email': {
                # error_messages : 에러 메세지를 자유롭게 설정 할 수 있다.
                'error_messages': {
                    # required : 값이 입력되지 않았을 때 보여지는 메세지
                    'required': '이메일을 입력해주세요.',
                    # invalid : 값의 포맷이 맞지 않을 때 보여지는 메세지
                    'invalid': '알맞은 형식의 이메일을 입력해주세요.'
                    },
                    # required : validator에서 해당 값의 필요 여부를 판단한다.
                    'required': False # default : True
                    },
            }