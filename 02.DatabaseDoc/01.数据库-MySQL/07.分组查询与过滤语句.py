# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### SQL语句的执行顺序: from ---> where ---> group by ---> having ---> select ---> order by

### group by : 将表中数据分成若干组   ---> group by 跟在where语句后面,order by 不能写在group by 的前面
# 统计每个部门的平均工资
    # select deptno, avg(sal) from emp group by deptno
# 注: 存在group by 分组,select 子句不能写group by 后面没有跟过的字段,除非这些字段用在了聚合函数中

### having: 过滤语句,只能出现在group by 分组的后面
# 统计每个部门的人数,平均工资,最高工资,但是部门的平均工资不能少于2000
    # select deptno,count(1), avg(sal), max(sal) from emp group by deptno having avg(sal) > 2000;



