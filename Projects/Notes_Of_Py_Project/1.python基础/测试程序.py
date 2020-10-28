# -*- coding: utf-8 -*- 
name=input('请输入您的名字：')
s1=int(input('请输入去年的成绩：'))   #转化为数值型
s2=int(input('请输入今年的成绩：'))
if s1>s2:
   r=(s1-s2)/s1*100
   print("%s同学，你的成绩下降了%s %%" %('name',r))
if s1<s2:
   r=(s2-s1)/s1*100
   print("%s同学，你的成绩下降了%s %%" %(name,r))