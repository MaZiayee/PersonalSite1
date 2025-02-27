from django.contrib import admin
from .models import Post,Category,Tag,Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display = ('id','author','title' ,'counted_views','status','published_date','created_date')
    list_filter = ['status','author']
    search_fields = ['title','content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','email','post','approved','created_date')
    list_filter = ['post','email','approved']
    search_fields = ['post','email','name']


admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)