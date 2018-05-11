from django.contrib import admin
from learning_logs.models import Topic,Entry

# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    list_display = ('text','date_added')    #显示列表
    search_fields = ('text',)       #添加搜索框,必须是元组或列表
    list_filter = ('date_added',)   #添加分类,必须是元组或列表


class EntryAdmin(admin.ModelAdmin):
    list_display = ('text','topic','date_added')
    search_fields = ('text',)
    list_filter = ('date_added',)

admin.site.register(Topic,TopicAdmin)
admin.site.register(Entry,EntryAdmin)
