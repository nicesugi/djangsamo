from rest_framework import serializers
from user.models import User as UserModel
from user.models import Hobby as HobbyModel
from user.models import UserProfile as UserProfileModel
from blog.serializers import ArticleSerializer


class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        user = self.context["request"].user
        return [up.user.fullname for up in obj.userprofile_set.exclude(user=user)]

    class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]


class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True, read_only=True)
    get_hobbys = serializers.ListField(required=False)
    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age", "hobby", "get_hobbys"]
        
        
        
class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer() 
    articles = ArticleSerializer(many=True, source="article_set", read_only=True)
    # # 사용자의 게시글 user's article
    # login_user_fullname = serializers.SerializerMethodField()
    # def get_login_user_fullname(self, obj):
    #     return self.context["request"].user.fullname
    
    
    # validate : 기존 validation + custom validation
    def validate(self, data):
        print(data) # 회원가입 is_valid로 이동하여 검증
        print(self.context)
        print(self.context.get("request", {}).method)
        # try:
        #     http_method = self.context.get("request", {}).method
        # except:
        #     http_method == ""
        valid_email_list = ["naver.com", "gmail.com", "yahoo.com"] # > 이런 선언은 임포트 아래쪽에 하는것이 좋음
        if data.get("email", "").split("@")[-1] not in valid_email_list:
            raise serializers.ValidationError(
                detail={"error": "유효한 이메일이 아닙니다."}
            )
        # if not data.get("email", "").endwith("@naver.com"):
        #     raise serializers.ValidationError(
        #         detail={"error": "네이버 이메일만 가입할 수 있습니다"}
        #     )
        # if not data.get("fullname", "").startwith("이"):
        #     raise serializers.ValidationError(
        #         detail={"error": "이씨 성만 가입할 수 있습니다"}
        #     )
        return data
    
    # 기존함수를 덮어씀
    def create(self, validate_data):
        user_profile = validate_data.pop("userprofile")
        get_hobbys = user_profile.pop("user_hobbys", [])
        password = validate_data.pop("password")
        print(user_profile)
        print(get_hobbys)   
           
        user = UserModel(**validate_data)
        user.set_password(password)
        user.save()
        
        
        user_profile = UserProfileModel.objects.create(
            user=user
            **user_profile
            )
        user_profile.hobby.add(*get_hobbys)
        return user
    
    def update(self, instance, validated_data):
        # instance에는 입력된 object가 담깁니다
        print(f'instance : {instance}')
        print(f'validated_data : {validated_data}')
        user_profile = validated_data.pop("userprofile")
        get_hobbys = user_profile.pop("get_hobbys", [])
        
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue
            setattr(instance, key, value)
        instance.save()
            
        user_profile_object = instance.userprofile
        for key, value in user_profile.items():
            setattr(user_profile_object, key, value)

            user_profile_object.save()
            user_profile_object.hobby.set(get_hobbys)
        return instance
    
    class Meta:
        model = UserModel
        fields = [
            "username", "fullname", "email", "password",
            "join_date", 
            "userprofile", "articles"
        ]
        
        # 각 필드에 해당하는 다양한 옵션 지정
        extra_kwargs = {
            # write_only : 해당 필드를 쓰기 전용으로 만들어 준다.
            # 쓰기 전용으로 설정 된 필드는 직렬화 된 데이터에서 보여지지 않는다.
            'password': {'write_only': True}, # default : False
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