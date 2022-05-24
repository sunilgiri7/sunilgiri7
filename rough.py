def foo(a_list):
    a_list[2] = 200
    #print(a_list)
    a_list.append(4)
    #a_list[0] = -100

my_list = [1,2,3]
foo(my_list)
print(my_list)