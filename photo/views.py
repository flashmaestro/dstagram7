from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
from .models import Photo
#from django.views.generic.list import ListView

# Decorator : 함수형 뷰 (데코레이터 명시)
# Mixin : 클래스형 뷰 (상속)
# 접근 권한 제어나 특별한 기능을 수행하고 싶을 때

@login_required
def photo_list(request):
    # objects : 기본 매니저
    photos = Photo.objects.all()
    # get, filter
    # 렌더링
    return render(request,'photo/list.html', {'photos':photos})

class UploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'


from django.views.generic import TemplateView
from tagging.views import TaggedObjectList

class TagListView(TemplateView):
    template_name = 'photo/tag_list.html'

class TagPhotoList(TaggedObjectList):
    model = Photo
    template_name = 'photo/tag_photo_list.html'









