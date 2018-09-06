from django.db import models
from django.urls import reverse
# Create your models here.
"""
앱을 만들 때 작업 과정
1. startapp 앱을 생성
2. settings.py 앱 등록
3. 모델 작성
4. migrate
5-1. view.py 작성
5-2. 템플릿 작성
6. route url 작성
"""

"""
Model!
모델은 데이터베이스에 무엇을 어떻게 저장할 것인지 묘사하는 개념
형태 : Class
"""

from django.contrib.auth.models import User
from tagging.fields import TagField

class Photo(models.Model):
    # 프로그래머가 작성하는 모델 내부에는 데이터베이스와 상호작용하는 코드가 없다
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    tag = TagField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])







