from django.contrib import admin
from fasite.models import Post, Contact, Comment

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message','created')

@admin.register(Comment)   
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','post','email','website','message','created') 


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')