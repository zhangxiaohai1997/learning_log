from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Topic,Entry
from .forms import TopicForm,EntryForm

# Create your views here.

def index(request):
    return render(request,'learning_logs/index.html')

def topics(request):
    topics=Topic.objects.order_by('-date_added')
    context={'topics':topics}
    return  render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):   #函数中的方法映射到模板中
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')   #通过外键连接
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

def new_topic(request):
    if request.method !='POST':
        form=TopicForm()
    else:
        form=TopicForm(request.POST)
        if form.is_valid():   #如果数据有效,存储到数据库中
            form.save()
            return  HttpResponseRedirect(reverse('learning_logs:topics'))   #将网页定向到topics

    context={'form':form}
    return render(request,'learning_logs/new_topic.html',context)

def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)

    if request.method!='POST':
        form=EntryForm()
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)     #创建新的条目对象
            new_entry.topic=topic     #关联相应主题
            new_entry.save()    #存储到数据库中
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))

    context={'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

def edit_entry(request,entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic

    if request.method!='POST':
        form=EntryForm(instance=entry)    #创建一个EntryForm实例
    else:
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))

    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)


