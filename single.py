class MusicPlay(object):
    #记录第一个被创建对象的引用
    instance = None

    #记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1、判断类属性是否是空对象
        if cls.instance is None:
            # 2、调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3、返回类舒属性保存的对象引用
        return cls.instance

    def __init__(self):
        # 1、判断是否执行过初始化动作
        if self.init_flag:
            return

        # 2、如果没有执行过，再执行初始化动作
        print('初始化播放器')

        # 3、修改类属性的标记
        self.init_flag = True

play1 = MusicPlay()
print(play1)

play2 = MusicPlay()
print(play2)

