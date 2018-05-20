from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .modelforms import PostModelForm, PostForm, CommentForm
from .models import Post, Comment


# 글 리스트.
def post_list(request):
    # name = 'Django'
    # return HttpResponse('''
    # <h1>Hello {myname}</h1>
    # '''.format(myname=name))

    # 일자로 조회하고 정렬한다.
    # posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    # 모두 조회
    posts = Post.objects.all()

    # 일자로 조회
    # posts = Post.objects.filter(published_date__year='2018', published_date__month='05', published_date__day='08')

    # html에 값을 전달......db쿼리 결과 전달.
    return render(request, 'blog/post_list.html', {'posts': posts})


# 글 한건 상세 조회
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


<<<<<<< HEAD
# 신규 등록 ModelForm사용
def post_new(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostModelForm()

    #print(form)
    return render(request, 'blog/post_edit.html', {'form':form})

#신규등록 Form 사용
def post_new_form(request):
    if request.method =='POST':
        form = PostForm(request.POST)
        #print(form)
        if form.is_valid():
            print(form.cleaned_data)
            #방법1 Post객체생성 save()호출
            # post = Post(author=request.user,
            #             title = form.cleaned_data['title'],
            #             text = form.cleaned_data['text'],
            #             published_date=timezone.now())
            # post.save()

            #방법2 Post.objects.create() 호출
            post = Post.objects.create(
                author=request.user,
                title = form.cleaned_data['title'],
                text = form.cleaned_data['text'],
                published_date=timezone.now()
            )

            return redirect('post_detail', pk=post.pk)
        else:   #검증에 실패
            print(form.errors)

    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form':form} )


#수정 ModelForm사용
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print('test')
    if request.method =="POST":
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostModelForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form} )


#삭제
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

# comment관련 처리 추가
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

# 댓글
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk= comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
=======
#신규등록 
def post_new(request):
    
    return ""
>>>>>>> blog/views.py 수정
