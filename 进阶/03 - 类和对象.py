# 类为设计图纸,对象为基于图纸的具体实体
# 设计一个闹钟类
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

# 构建2个闹钟对象并让其工作
clock1 = Clock()
clock1.id = 'id1'
clock1.price = 100
print(clock1.id, clock1.price)
clock1.ring()

clock2 = Clock()
clock2.id = 'id2'
clock2.price = 100
print(clock2.id, clock2.price)
clock2.ring()
