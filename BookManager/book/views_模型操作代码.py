from django.db.models import F, Q, Sum
from django.shortcuts import render

from book.models import BookInfo, PeopleInfo

# Create your views here.

"""
视图
1.就是python函数
2.函数的第一个参数就是  请求  和请求相关的
3.我们必须要返回一个响应  响应是HTTPResponse的实例对象/子类实例对象
"""


def index(request):
    # 实现业务逻辑
    # 1.先把所以书籍查询出来
    # sql实现 select * from bookinfo
    # ORM
    books = BookInfo.objects.all()
    # books = [BookInfo.objects.all()]
    context = {
        'books': books
    }
    # render
    # 参数1：当前的请求
    # 参数2：模板文件
    # 参数3：context传递参数
    return render(request, 'index.html', context=context)
    
    # return HttpResponse('index')


################################新增数据#################################

# 方式1
book = BookInfo(
    name='python',
)
#  需要手动调用save方法
book.save()

# 方式2 直接入库
# object 模型的管理类
# 我们对模型的 增删改查 都找它

BookInfo.objects.create(
    name='java',
    pub_date='2010-2-1'
)

###############################修改(更新)数据####################################

from book.models import BookInfo

# 方式1
# 1.先查询数据
# select * from BookInfo where id=1
book = BookInfo.objects.get(id=1)  # 返回一个对象
# 2.直接修改实例的属性
book.readcount = 20
# 3. 调用save方法保存修改
book.save()

# 方式2 直接更新
# filter 过滤
BookInfo.objects.filter(id=1).update(
    readcount=100,
    commentcount=200,
)

###################################删除数据####################################
# 方式1
# 1.先查询出数据
book = BookInfo.objects.get(id=2)
book.delete()

# 方式2
BookInfo.objects.filter(id=3).delete()

###################################基本查询##########################################

# get 得到某一个数据
# all 获取所有的
# count 个数
try:
    book = BookInfo.objects.get(id=100)  # 查询不存在的数据
# except Exception:
#     pass
except BookInfo.DoesNotExist:
    pass

# 返回所有结果，列表
BookInfo.objects.all()
# count
BookInfo.objects.all().count()
BookInfo.objects.count()

#################################filter, get, exclude#####################################
"""
select name form bookinfo where 条件语句
相当于where查询
filter      # 筛选/过滤 返回n个结果（n = 0/1/n）   列表
get         #           返回1个结果
exclude     # 排除掉符合条件剩下的结果  想当于 not
语法形式：
    以filter(字段名__运算法=值)     # 双下划线
"""

# 查询
# exact
BookInfo.objects.get(id_exact=1)
BookInfo.objects.get(id=1)  # 和上面一样

BookInfo.objects.get(id=1)
BookInfo.objects.get(id_exact=1)

# 查询书名包含'游'的图书
# contains 包含
BookInfo.objects.filter(name__contains='游')

# endwith 结尾
BookInfo.objects.filter(name__endswith='记')

# 查询书名为空
BookInfo.objects.filter(name__isnull=True)

# 查询多个
BookInfo.objects.filter(id__in=[1, 2, 5])
# 查询按条件
# gt 大于, gte 大于等于      equal
# lt, lte   less than
BookInfo.objects.filter(id__gt=3)

# exclude
BookInfo.objects.exclude(id=3)

BookInfo.objects.filter(pub_date__year='2010')

#################################F对象########################################

# 两个属性怎么比较
"""
F对象的语法形式
filter(字段名__运算符=F('字段名'))
"""
# 查询阅读量大于评论量的图书
BookInfo.objects.filter(readcount__gt=F('commentcount'))
# 查询阅读量大于评论量2倍的图书
BookInfo.objects.filter(readcount__gt=F('commentcount') * 2)

##################################Q对象#######################################

# 查询id>2且阅读量大于20的图书

# 方式1
# filter().filter()
BookInfo.objects.filter(id__gt=2).filter(readcount__gt=20)
# 方式2
# filter(条件, 条件)
BookInfo.objects.filter(id__gt=2, readcount__gt=20)

# 那要是 id>2 或者 阅读量>20呢
"""
Q(字段名__运算符=值)
或 Q() | Q()
并且 Q() & Q()
not ~Q()
"""
BookInfo.objects.filter(Q(id__gt=2) | Q(readcount__gt=20))


####################################聚合函数###########################################

"""
Sum, Max, Avg, Count
聚合函数需要使用aggregate
语法形式是：aggregate(Xxx('字段'))
"""
BookInfo.objects.aggregate(Sum('readcount'))


###################################排序######################################
# 默认升序
BookInfo.objects.all().order_by('readcount')
# 降序
BookInfo.objects.all().order_by('-readcount')

####################################关联查询##########################################
"""
语法形式：
    1.已知 主表数据，关联查询从表数据
    主表模型.关联模型类名小写_set
    book=BookInfo.objects.get(id=1)
    book.peopleinfo_set.all()
    2.已知从表数据，关联查询主表数据
    从表模型(实例对象).外键
    person=PeoPleInfo.objects.get(id=1)
    person.book.name
"""

####################################关联查询的筛选##########################################
"""
语法形式：
    需要  主表数据，已知 从表信息
    filter(关联模型名小写__字段__运算符=值)
    需要  从表数据，已知 主表信息
    filter(外键__字段__运算符=值)
"""
BookInfo.objects.filter(peopleinfo__name='xxx')
PeopleInfo.objects.filter(book__readcount__gt=20)

#############################分页查询#######################################
from django.core.paginator import Paginator

books = BookInfo.objects.all()
p = Paginator(book, 2)
book_page = p.page(1)
book_page.object_list