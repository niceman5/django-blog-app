from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post

# 글 리스트.
def post_list(request):
    # name = 'Django'
    # return HttpResponse('''
    # <h1>Hello {myname}</h1>
    # '''.format(myname=name))

    #일자로 조회하고 정렬한다.
    #posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    #모두 조회
    posts = Post.objects.all()

    #일자로 조회
    #posts = Post.objects.filter(published_date__year='2018', published_date__month='05', published_date__day='08')


    #html에 값을 전달......db쿼리 결과 전달.
    return render(request, 'blog/post_list.html', {'posts':posts} )

#글 한건 상세 조회
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    return ""