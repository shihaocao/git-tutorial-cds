some_list = [1,2,3]

def func(some_list):
    some_list.append(4,7,8,9)
    
    def func2():
        print(some_list)
        
    func2()
    print(some_list)
    
func(some_list)