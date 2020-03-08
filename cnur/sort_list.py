# coding = utf-8

def sort_list(the_list):
    """
    取出列表内的最大值和最小值

    列表 比较最大值
    [4,2,7,1,9]
    [2,4,7,1,9]
    [2,4,7,1,9]
    [2,4,1,7,9]
    [2,4,1,7,9]
    """

    for i in range(0, len(the_list)):
        for j in range(i+1, len(the_list)):
           #print(the_list)
            if the_list[i] > the_list[j]:
                #print(the_list)
                the_list[i], the_list[j] = the_list[j], the_list[i]
    return the_list


if __name__ == '__main__':
    news = sort_list([2, 4, 7, 1, 9])
    print(news)