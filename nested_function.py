def pop(list):
    def Get_The_Last_item(my_list):
        return my_list[len(list)-1]
    list.remove(Get_The_Last_item(list))
    return list
a=[1,2,3,4,5,6,7,8,9]
# i=7
for i in a:
    
    print(pop(a))
