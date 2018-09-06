from django.contrib import admin

# Register your models here.

# 관리자 페이지에서 모델을 관리할 수 있게 등록
# 관리자 페이지 커스터마이징 -> 기능
# 디자인 커스터마이징 -> template

from .models import Photo

# 옵션 클래스 만들기
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']
    raw_id_fields = ['author']
    # Todo : 다양한 옵션 필드 추가
    list_filter = ['created','updated','author']
    search_fields = ['text','created']
    ordering = ['-updated','-created']


# 옵션 클래스를 등록하기
admin.site.register(Photo, PhotoAdmin)