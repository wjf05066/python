from platform import machine


class book:
    def __init__(self):
        self.books=[]

#添加收入
    def add_shouru(self):
        money=float(input("请输入收入金额："))
        type=input("请输入收入类型：")
        note=input("请输入备注：")
        self.books.append({"金额":money,"类型":type,"备注":note})
        print(
            "添加成功！"
        )


#添加支出

    def add_zhichu(self):
        money=float(input("请输入支出金额："))
        type=input("请输入支出类型：")
        note=input("请输入备注：")
        self.books.append({"金额":money,"类型":type,"备注":note})
        print(
            "添加成功！"
        )


#查看记录
    def  show(self):
        print('全部记录如下')
        print('-------------------')
        if len(self.books)==0:
            print('没有记录')
        else:
            for i in self.books:
                print(i)


#查看统计
    def show_count(self):
        total_shourU=0
        total_zhichu=0
        for i in self.books:
            if i['类型']=='收入':
                total_shourU+=i['金额']
            else:
                total_zhichu+=i['金额']

        yue=total_shourU-total_zhichu
        print("【财务统计】")
        print(f"收入总额为：{total_shourU}")
        print(f"支出总额为：{total_zhichu}")
        print(f"余额为：{yue}")



    def run (self):
        while True:
            print("""
                1.添加收入
                2.添加支出
                3.查看记录
                4.查看统计
                5.退出
            """)
            choice=input("请选择：")
            match choice:
                case '1':
                    self.add_shouru()
                case '2':
                    self.add_zhichu()
                case '3':
                    self.show()
                case '4':
                    self.show_count()
                case '5':
                    break
                case _:
                    print("请输入正确的选项")


if __name__ == "__main__":
    book = book()
    book.run()