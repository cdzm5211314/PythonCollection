class Gun:
    def __init__(self,model):
        # 枪的型号,需要初始化
        self.model = model
        # 枪的子弹数初始化为0
        self.bullet_count = 0

    # 士兵添加子弹
    def add_bullet(self,count):
        self.bullet_count += count

    # 士兵射击
    def shoot(self):
        # 判断枪中是否有子弹
        if self.bullet_count <= 0:
            print("[%s] 没有子弹..."%self.model)
            return
        # 发射子弹 -1
        self.bullet_count -= 1
        # 提示发射信息
        print("[%s] 突突突...,剩余子弹数:[%d]"%(self.model,self.bullet_count))


# 创建枪对象
ak47 = Gun("ak47")

# 给枪添加子弹
ak47.add_bullet(100)

# 射击
ak47.shoot()


