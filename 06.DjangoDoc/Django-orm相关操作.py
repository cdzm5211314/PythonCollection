# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-06-12 14:57

### 一般操作: 必知必会13条
# all():                 查询所有结果
# filter(**kwargs):      它包含了与所给筛选条件相匹配的对象
# get(**kwargs):         返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。
# exclude(**kwargs):     它包含了与所给筛选条件不匹配的对象
# values(*field):        返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象，而是一个可迭代的字典序列
# values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
# order_by(*field):      对查询结果排序
# reverse():             对查询结果反向排序，请注意reverse()通常只能在具有已定义顺序的QuerySet上调用(在model类的Meta中指定ordering或调用order_by()方法)。
# distinct():            从返回结果中剔除重复纪录(如果你查询跨越多个表，可能在计算QuerySet时得到重复的结果。此时可以使用distinct()，注意只有在PostgreSQL中支持按字段去重。)
# count():              返回数据库中匹配查询(QuerySet)的对象数量。
# first():              返回第一条记录
# last():               返回最后一条记录
# exists():             如果QuerySet包含数据，就返回True，否则返回False


### 返回QuerySet对象的方法有: all(), filter(), exclude(), order_by(), reverse(), distinct()
### 返回特殊的QuerySet对象的方法有:
# values()      返回一个可迭代的字典序列
# values_list() 返回一个可迭代的元祖序列
### 返回具体对象的方法: get(), first(), last()
### 返回布尔值的方法：exists()
### 返回数字的方法: count()


### 单表查询的双下划綫使用:
# models.Tb1.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值
# models.Tb1.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
# models.Tb1.objects.exclude(id__in=[11, 22, 33])  # not in
# models.Tb1.objects.filter(name__contains="ven")  # 获取name字段包含"ven"的
# models.Tb1.objects.filter(name__icontains="ven") # icontains大小写不敏感
# models.Tb1.objects.filter(id__range=[1, 3])      # id范围是1到3的，等价于SQL的bettwen and
# 类似的还有：startswith，istartswith, endswith, iendswith　
# date字段还可以： models.Class.objects.filter(first_day__year=2017)


### ForeignKey操作:
# 正向查找: 对象查找(跨表)  ---> 对象.关联字段.字段
# book_obj = Book.objects.first()  # 第一本书对象
# print(book_obj.publisher)  # 得到这本书关联的出版社对象
# print(book_obj.publisher.name)  # 得到出版社对象的名称

# 正向查找: 字段查找(跨表) ---> 关联字段__字段
# Book.objects.values_list("publisher__name")

# 反向查找: 对象查找(跨表)  ---> obj.表名_set
# publisher_obj = Publisher.objects.first()  # 找到第一个出版社对象
# books = publisher_obj.book_set.all()  # 找到第一个出版社出版的所有书
# titles = books.values_list("title")  # 找到第一个出版社出版的所有书的书名

# 反向查找: 字段查找(跨表) ---> 表名__字段
# titles = Publisher.objects.values_list("book__title")


### 聚合查询和分组查询:
from django.db.models import Avg, Sum, Max, Min, Count
# 聚合:
# aggregate()是 QuerySet 的一个终止子句，意思是说，它返回一个包含一些键值对的字典
# Book.objects.all().aggregate(Avg("price"))
# Book.objects.aggregate(average_price=Avg('price'))
# 分组:
# Employee.objects.values("dept").annotate(avg=Avg("salary").values(dept, "avg")


### F 查询和 Q 查询
# F() 的实例可以在查询中引用字段，来比较同一个 model 实例中两个不同字段的值
# from django.db.models import F
# Book.objects.filter(commnet_num__gt=F('keep_num'))
# 可以组合& 和|  操作符以及使用括号进行分组来编写任意复杂的Q 对象。同时，Q 对象可以使用~ 操作符取反，这允许组合正常的查询和取反(NOT) 查询
# from django.db.models import Q
# Book.objects.filter(Q(authors__name="小仙女")|Q(authors__name="小魔女"))  # 查询作者名是小仙女或小魔女的


