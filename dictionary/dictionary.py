dictionary = {}
def operate_dict():
    print("Dict運作選單：")
    print("1.加入")
    print("2.刪除")
    print("3.顯示")
    print("4.結束")
    option = int(input("請輸入選項："))
    if(option == 1):
        key = int(input(f"輸入鍵(整數)："))
        value = input("輸入值：")
        add_dict(key,value)
    if(option == 2):
        key = int(input(f"輸入鍵："))
        del_dict(key)
    if(option == 3):
        display_dict()
    if(option == 4):
        exit_operation()

def add_dict(key,value):
    dictionary.update({key:value})
    print("產生一Dict元素...",{key:dictionary[key]})
    print("------我是帥氣分隔線------")
    operate_dict()

def del_dict(key):
    removedValue = dictionary.get(key,'none')
    if(removedValue == 'none'):
        print("無效的鍵")
    else:
        del dictionary[key]
        print({key:removedValue},"已被刪除")

    print("------我是帥氣分隔線------")
    operate_dict()
    
def display_dict():
    print("Dict所有的鍵值：")
    for key in dictionary.keys():
        print(key, dictionary[key])
    print("------我是帥氣分隔線------")
    operate_dict()
    
def exit_operation():
    print("------掰掰 祝你比賽得冠軍------")
    
operate_dict()