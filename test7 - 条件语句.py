#根据一个条件的成立与否,来决定接下来的逻辑走向
#if expression:
#   do_something1
#   do_something2
#next_something

#if expression:
#   do_something1
#else:
#   do_something2

#if expression1:
#   do_something1
#elif expression2:
#   do_something2
#else:
#   do_something2

#让用户输入1表示愿意认真学习,输入2表示躺平
choice = input("输入1表示愿意认真学习,输入2表示躺平: ")
if choice == "1":
    print("能有工作")
elif choice == "2":
    print("没有工作")
else:
    print("重新输入")#对于非法输入的判断


