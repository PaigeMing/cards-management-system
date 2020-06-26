import pandas as pd
import csv

# 记录所有的名片字典
card_list = []
name_list = []


def show_menu():

    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V 2.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("4. 修改名片")
    print("5. 删除名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1. 提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    # 判断输入电话号码是否为11位数字
    while True:
        phone_str = input("请输入电话：")
        if len(phone_str) != 11:
            print("输入号码有误，请重新输入！")
        else:
            break
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    # 2. 使用用户输入的信息建立一个列表

    name_list = [name_str, phone_str, qq_str, email_str]

    # 3.
    # 1>加载名片信息——csv文件，保存为名片列表
    # 2>将新建列表添加到名片列表中
    #  如果文件为空，则名片列表=新建列表

    card_list = lode_data()

    if card_list == None:

        card_list = [name_list]
    else:
       card_list.append(name_list)

       # 按字母顺序对名片进行排序
       card_list.sort()
    # 4.将名片信息保存入csv文件
    save = pd.DataFrame(data=card_list)
    save.to_csv('1.csv', header=False, index=False, encoding='gbk')


    print(card_list)


    # 5. 提示用户添加成功
    print("添加 %s 的名片成功！" % name_str)


def show_all():

    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 加载数据
    card_list = lode_data()
    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:

            print("当前没有任何的名片记录，请使用新增功能添加名片")
         # return 可以返回下一个函数执行的结果
         # 下方的代码不会被执行
         # 如果 return 后面没有任何的内容，表示会返回到调用函数的位置
         # 并且不返回任何的结果
            return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print("")

    # 打印分隔线
    print("=" * 50)
    # 遍历文件列表一次输出名片信息

    for row in card_list:

        print('     '.join(row))


def search_card():

    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    card_list = lode_data()
    # 1. 提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名: ")

    # 2. 遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户

    for temp in card_list:
        if temp[0] == find_name:
            print(temp)
            break

    else:

        print("抱歉，没有找到 %s" % find_name)


def deal_card():
    """修改查找到的名片

    """
    print("-" * 50)
    print("修改名片")
    card_list = lode_data()
    # 1. 提示用户输入要修改的姓名
    change_name = input("请输入要修改的姓名: ")

    # 2. 遍历名片列表，查询要修改的姓名，如果没有找到，需要提示用户

    for temp in card_list:
        if temp[0] == change_name:
            print(temp)
            # 针对找到的名片记录执行修改的操作

            while True:

                alter_str = input("请输入你要修改的信息"
                                  "[0]名字 [1] 电话 [2]QQ [3]邮箱 [4]退出")

                if alter_str == "0":
                        temp[0] = input("请输入你要修改的名字：")
                        print("修改成功")
                elif alter_str == "1":
                    while True:

                        temp[1] = input("请输入你要修改的电话：")
                        if len(temp[1]) != 11:
                                print("输入修改手机号有误，请重新输入！")
                        else:
                            print("修改成功")
                            break

                elif alter_str == "2":
                    temp[2] = input("请输入你要修改的QQ：")
                    print("修改成功")

                elif alter_str == "3":
                    temp[3] = input("请输入你要修改的邮箱：")
                    print("修改成功")

                elif alter_str == "4":
                    break
                else:
                    print("输入错误，请重新选择")
            # 按字母顺序对名片进行排序
            card_list.sort()
            # 将修改后的信息存入文档
            save = pd.DataFrame(data=card_list)
            save.to_csv('1.csv', header=False, index=False, encoding='gbk')
            break

    else:

        print("抱歉，查无此人" )


def del_card():
    """
     删除找到的名片
    """
    print("-" * 50)
    print("删除名片")
    card_list = lode_data()
    # 1. 提示用户输入要删除的姓名
    del_name = input("请输入要删除的姓名: ")

    # 2. 遍历名片列表，查询要删除的姓名，如果没有找到，需要提示用户

    for i in card_list:
        if i[0] == del_name:
            card_list.remove(i)
            # 按字母顺序对名片进行排序
            card_list.sort()
            # 将修改后的信息存入文档
            save = pd.DataFrame(data=card_list)
            save.to_csv('1.csv', header=False, index=False, encoding='gbk')
            print("删除名片成功！")
            break

        else:
            print("查无此人！")


# 加载数据函数,用列表接收读取信息
# 如果没有'1.csv'文件，啥都不做，等存档创建
def lode_data():

    try:

        return list(csv.reader(open('1.csv')))

    except:
        pass




"""
说明：
与1.0相比，2.0把存储文件改为csv文件
新增：
1、加载数据功能 可读取csv文件数据并保存为列表
2、判断电话号码输入是否为11位有效数字
3、可对存入名片按字母顺序排序
"""
