from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer, ReadOnlyField
#from cities_light.models import City

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password':{'write_only':True,'required':True}}
        
    def create(self, validated_data):
      user = User.objects.create_user(**validated_data)
      print(user)
      Token.objects.create(user=user)
      return user

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name',queryset=Category.objects.all())
    user_name = serializers.ReadOnlyField(source='user.username', read_only=True)
   # city_name = serializers.ReadOnlyField(source='city.name', read_only=True)
    condition = serializers.SlugRelatedField(slug_field='condition',queryset=Condition.objects.all())
    major = serializers.SlugRelatedField(slug_field='major',queryset=Major.objects.all(), allow_null=True)
    subject = serializers.SlugRelatedField(slug_field='subject',queryset=Subject.objects.all(),allow_null=True)
    city = serializers.SlugRelatedField(slug_field='name',queryset=City.objects.all())
    school = serializers.SlugRelatedField(slug_field='school',queryset=School.objects.all(),allow_null=True)
    date_created = serializers.DateTimeField(format="%d-%m-%Y", required=False, read_only=True)
    # product_id = serializers.CharField(source='product.url', read_only=True)
    # #category = serializers.CharField(source='category.name', read_only=True)
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # user_id = serializers.CharField(source='user.id', read_only=True)
    # subject = serializers.CharField(source='subject.subject', read_only=True)
    # condition = serializers.CharField(source='condition.condition', read_only=True)
    # major = serializers.CharField(source='major.major', read_only=True)
    # state = serializers.CharField(source='state.state', read_only=True)
    # school = serializers.CharField(source='school.school', read_only=True)
    # location = serializers.CharField(source='location.location', read_only=True)
    
    class Meta:
        model = Product
        #fields = '__all__'
        fields = ['id', 'title','category', 'major', 'condition', 'subject', 'school', 'price', 'description', 'image', 'user', 'user_name', 'date_created', 'city']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__'
