#第一课

#列表
#movies = ['肖申克的救赎', '霸王别姬', '大话西游', '无间道']

# movies.append('1994')
# movies.insert(1, 1994)

#for语句
# for i in movies:
#     print(i)

#print(movies)


# movies = [
#     "肖申克的救赎", 1994, "弗兰克·德拉邦特", 142,
#     [
#         "蒂姆·罗宾斯",
#         ["摩根·弗利曼", "鲍勃·塞德勒", "法兰西·布朗"]]]
# print(movies[4][1][0])

#if语句
# num = [1, 2, 3]
#
#
# if isinstance(num, list):
#     len1 = len(num)
#     if isinstance(len1, int):
#         print(len1)
#     print(num)


# movies = [
#     "肖申克的救赎", 1994, "弗兰克·德拉邦特", 142,
#     [
#         "蒂姆·罗宾斯",
#         ["摩根·弗利曼", "鲍勃·塞德勒", "法兰西·布朗"]]]

#迭代
# for each_item in movies:
#     if isinstance(each_item, list):
#         for nested_item in each_item:
#             if isinstance(nested_item, list):
#                 for deeper_item in nested_item:
#                     print(deeper_item)
#             else:
#                 print(nested_item)
#     else:
#         print(each_item)



#递归函数
# def print_lol(the_list):
#     for each_item in the_list:
#         if isinstance(each_item, list):
#             print("---", each_item)
#             print_lol(each_item)
#         else:
#             print(each_item)
# print_lol(movies)


#作业
#定义一个函数，参数为列表（数据项为int型），返回这个列表相中的最大值和最小值


#list_test = [22, 123, 343, 1231, 11, 1231, 44, 13]

# def max_min(the_list):
#     for i in the_list:
#         if the_list.index(i) == 0:
#             max_value = i
#             min_value = i
#         the_list.pop(0)
#         for j in the_list:
#             if j > max_value:
#                 max_value = j
#             if j < min_value:
#                 min_value = j
#     print(max_value, min_value)

#max_min(list_test)



def max_min(the_list):
    max_value = the_list[0]
    min_value = the_list[0]
    for j in the_list[1:]:
        if j > max_value:
            max_value = j
        if j < min_value:
            min_value = j
    print(max_value, min_value)


if __name__ == '__main__':
    num = [1, 2, 8, 5, 90, 0]
    max_min(num)




