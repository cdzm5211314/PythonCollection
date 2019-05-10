class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 家具,占地面积%.2f"%(self.name,self.area)

class House:
    def __init__(self,house_type,area):
        # 房子户型
        self.house_type = house_type
        # 房子总面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []
    def __str__(self):
        # Python 能够自动将一对括号内部的代码连接在一起
        return ("户型: %s\n房子总面积: %.2f [剩余: %.2f]\n家具: %s"
                %(self.house_type,self.area,self.free_area,self.item_list))

    def add_item(self,item):
        # 判断家具面积是否超过房子剩余面积
        if self.free_area > item.area:
            self.item_list.append(item.name)
            self.free_area = self.free_area - item.area
            # print("已添加 %s"%item)
            print(self)
        else:
            print("[%s] 家具面积太大,不能放进房间..."%item.name)
# 创建家具
bed = HouseItem("席梦思",4)
chest = HouseItem("衣柜",2)
table = HouseItem("餐桌",55)
print(bed)
print(chest)
print(table)

# 创建房子
my_home = House("两室一厅",60)
print(my_home)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

# print(my_home)





