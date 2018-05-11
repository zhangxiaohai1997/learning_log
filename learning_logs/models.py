from django.db import models

# Create your models here.
class Topic(models.Model):
    "用户学习的主题"
    text=models.CharField(max_length=200,verbose_name='主题')
    date_added=models.DateTimeField(auto_now_add=True,verbose_name='时间')

    def __str__(self):
        """返回字符串表示"""
        return self.text
    class Meta:
        verbose_name='主题'
        verbose_name_plural=verbose_name

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE,verbose_name='主题')
    text=models.TextField(verbose_name='内容')
    date_added=models.DateTimeField(auto_now_add=True,verbose_name='时间')

    class Meta:
         verbose_name='条目'
         verbose_name_plural='条目'

    def __str__(self):
        return self.text[:30]+"..."

