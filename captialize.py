#coding:utf-8
'''

把一个英文句子首字母都转换成大写

'''
quote = "How can mirrors be real if our eyes aren't real"

def toJadenCase(string):
    list = quote.split()                             #将string分隔开
    for i in range(len(list)):                       
        list[i] = list[i][0].upper()+list[i][1:]     #首字母大写
    str=' '.join(list)                               #将list转回string，并用空格隔开
    return str                                       #返回str

'''
1.str.split()
变成了一个list

2.list->string：
  string = ''.join(list)
  
'''
