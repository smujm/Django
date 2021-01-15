from django.db import models

# Create your models here.
"""
1.定义模型类
2.模型迁移
    2.1 先生成迁移文件(不会在数据库中生成表，只会创建一个 数据库和模型的对应关系)
    python manage.py makemigrations
    2.2 再迁移(会在数据库中生成表)
    python manage.py migrate
3.操作数据库

① 在哪里定义模型
② 模型继承自谁
③ ORM对应的关系：
    表-->类
    字段-->属性
    
"""


class BookInfo(models.Model):
    """
    1.主键，当前会自动生成,不需要再写了
    2.属性， 复制过来就可以
    3.选项：Charfield 必须设置 max_length
                varchar(M)
                null    是否为空
                default
                unique  唯一

    """
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)
    
    
    class Meta:
        # 改变表名
        db_table = 'bookinfo'
        # 修改后台admin的显示信息的配置
        # verbose_name = '后台显示'
        
        
    # 重写模型str方法
    def __str__(self):
        return self.name
    

class PeopleInfo(models.Model):
    # 有序字典
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=1000, null=True, verbose_name='描述')
    # on_delete 级联操作
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='书籍')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    
    
    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'
    
    # 重写模型str方法
    def __str__(self):
        return self.name