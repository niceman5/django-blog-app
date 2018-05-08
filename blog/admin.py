from django.contrib import admin

# Register your models here.
from blog.models import Post

class PostAdmin( admin.ModelAdmin):
    #title컬럼
    list_display = ['id','title', 'count_text']
    #link연결
    list_display_links = ['id','title']

    def count_text(self, post):
        return '{}글자'.format(len(post.text))

    count_text.short_description = "내용 글자수"


#생성한 application을 등록
admin.site.register(Post, PostAdmin)