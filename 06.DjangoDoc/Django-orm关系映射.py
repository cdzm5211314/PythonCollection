# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-06-12 14:50

from django.db import models

### 模型类中的字段
class OneModelFields(models.Model):
    # 自增长字段，int型
    Auto = models.AutoField()
    BigAuto = models.BigAutoField()

    # 二进制数据
    Binary = models.BinaryField()

    # 布尔型
    Boolean = models.BooleanField()          # 不为空
    NullBoolean = models.NullBooleanField()  # 允许为空

    # 整型
    PositiveSmallInteger = models.PositiveSmallIntegerField()   # 5个字节正整数
    SmallInteger = models.SmallIntegerField()                   # 6个字节整数
    PositiveInteger = models.PositiveIntegerField()             # 10个字节正整数
    Integer = models.IntegerField()                             # 11个字节整数
    BigInteger = models.BigIntegerField()                       # 20个字节整数

    # 字符串类型
    Char = models.CharField()       # 对应数据库 varchar
    Test = models.TextField()       # 对应数据库 longtext

    # 时间日期类型
    Date = models.DateField()           # 年月日
    DateTime = models.DateTimeField()   # 年月日时分秒
    Duration = models.DurationField()   # 表示一段时间，int型，底层python timedelta实现

    # 浮点型
    Float = models.FloatField()
    Decimal = models.DecimalField()

    # 其他字段
    Email = models.EmailField()
    Image = models.ImageField()
    File = models.FileField()
    FilePath = models.FilePathField()
    URL = models.URLField()
    GenericIPAddress = models.GenericIPAddressField()


### 关系型字段
""" 
    一对一： OneToOne
    多对一： ForeignKey
    多对多： ManyToMany
"""
class A(models.Model):
    onetoon = models.OneToOneField(OneModelFields)

class B(models.Model):
    foreign = models.ForeignKey(A)

class C(models.Model):
    manytomany = models.ManyToManyField(B)

### 关系型字段参数
class A(models.Model):
    """ related_name: 反向查询，父表查子表
    子表A，父表OneModelFields
    通过OneModelFields查询A的数据
    """
    onetoon = models.OneToOneFields(OneModelFields, related_name="one")

class B(models.Model):
    """on_delete 的六种操作
        1. models.CASCADE: 将定义有外键的模型对象同时删除 ，django模板的默认操作
        2. model.PROTECT: 阻止上面的删除操作，但是弹出ProtectedError异常
        3. models.SET_NULL: 将外键字段设为null，只有当字段设置了null=True时，方可使用该值
        4. models.SET_DEFAULT: 将外键字段设为默认值，只有当字段设置了default参数时，方可使用
        5. models.DO_NOTHING: 什么也不做
        6. models.SET: 设置为一个传递给SET()的值或者一个回调函数的返回值，注意大小写
    """
    foreign = models.ForeignKey(A, on_delete=models.CASCADE)    # 删除级联
    foreign = models.ForeignKey(A, on_delete=models.PROTECT)
    foreign = models.ForeignKey(A, on_delete=models.SET_NULL, null=True, blank=True)   # 删除置空
    foreign = models.ForeignKey(A, on_delete=models.SET_DEFAULT, default=0)
    foreign = models.ForeignKey(A, on_delete=models.DO_NOTHING)
    foreign = models.ForeignKey(A, on_delete=models.SET)

### 字段共有的参数
# db_column: 在数据库中的字段名称，默认和变量同名
# verbose_name: 后台显示名称
# primary_key=True：主键
# null=True: 允许字段为空，默认False
# blank=True: 提交表单可以为空，默认False，此参数为True，null参数必须为True
# db_index=True: 设置索引，默认False
# help_text: 表单帮助信息
# editable: 该字段是否可编辑，默认为True
# unique: 字段唯一，默认False
# default: 默认值
class OneModelFields(models.Model):  # 表名：appname_onemodelfield
    PositiveSmallInteger = models.PositiveSmallIntegerField(db_column="age", verbose_name="年龄")
    SmallInteger = models.SmallIntegerField(primary_key=True)
    Integer = models.IntegerField(null=True, blank=True)
    BigInteger = models.BigIntegerField(unique=True, db_index=True, default=0)
    Char = models.CharField(help_text="表单帮助信息")
    Test = models.TextField(editable=False)


### 个别字段具有的参数
# 字符串型
# max_length: 必须指定数值的参数，utf8编码的最大长度
# 时间日期类型
# unique_for_date: 日期必须唯一
# unique_for_month: 月份必须唯一
# unique_for_year: 年份必须唯一
# auto_now_add: 增加记录时的时间
# auto_now: 更新当前记录的时间
# 浮点型
# max_digits: DecimalField字段必须指定，一共多少位
# decimal_places: DecimalField字段必须指定，小数点位数

class OneModelFields(models.Model):

    # 字符串类型
    Char = models.CharField(max_length=100)       # 对应数据库 varchar
    Test = models.TextField()       # 对应数据库 longtext

    # 时间日期类型
    Date = models.DateField(unique_for_date=True, auto_now=True)           # 年月日
    DateTime = models.DateTimeField(unique_for_year=True, unique_for_month=True, auto_now_add=True)   # 年月日时分秒
    Duration = models.DurationField()   # 表示一段时间，int型，底层python timedelta实现

    # 浮点型
    Float = models.FloatField()
    Decimal = models.DecimalField(max_length=4, decimal_places=2)   # 例如 12.11

### 元数据Meta
class AddressInfos(models.Model):

    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="地址")
    pid = models.ForeignKey('self', null=True, blank=True, verbose_name="自关联字段")
    note = models.CharField(max_length=200, null=True, blank=True, verbose_name="说明")

    def __str__(self):
        return self.address

    class Meta:
        db_table = "addressinfo"    # 表的名称
        ordering = 'pid'                    # 排序字段
        verbose_name = "省市县地址信息"
        verbose_name_plural = verbose_name  # 复数
        # abstract = True   # 基类用于继承，默认为False
        unique_together = ("address", "note")  # 联合唯一健，还可以用二维元组 ((), ())
        app_label = 'app_name'  # 模型类属于哪一个应用
        # db_tablespace       # 定义数据库表空间的名称

