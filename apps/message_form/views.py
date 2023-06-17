from django.shortcuts import render

# Create your views here.
# 配置一个HTML页面显示的步骤
#1.配置url
#2.配置对应的views逻辑
#3.拆分静态放入到static，html放入到template之下
def message_form(requset):
    return  render(requset,'message_form.html')