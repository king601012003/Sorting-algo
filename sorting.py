import random
from time import time

class sorting:
    def __init__(self):
        self.procedure = {}
        
    def bubble_sort(self, number_list, step=0):
        assert type(number_list) is list
        assert len(number_list) > 1
        
        self.procedure[step] = number_list.copy()
        
        while (True):
            finish = True
            
            for i in range(len(number_list) - 1):
                if (number_list[i] > number_list[i + 1]):
                    finish = False
                    
                    # swap
                    number_list[i], number_list[i + 1] = number_list[i + 1], number_list[i]
            
            step += 1
            self.procedure[step] = number_list.copy()
            
            if finish:
                break
            
        return number_list, self.procedure
                    
        
    def insert_sort(self, number_list, step=0):
        assert type(number_list) is list
        assert len(number_list) > 1
        
        self.procedure[step] = number_list.copy()
        
        for i in range(len(number_list)): 
            for j in range(i):
                if (number_list[i] <= number_list[j]):
                    number_list.insert(j, number_list.pop(i))
                    break
            
            step += 1
            self.procedure[step] = number_list.copy()
            
        return number_list, self.procedure
                
        
    def selection_sort(self, number_list, step=0):
        assert type(number_list) is list
        assert len(number_list) > 1

        self.procedure[step] = number_list.copy()
        
        for i in range(len(number_list)):
            min_value = None
            
            for j in range(i, len(number_list)):
                if (min_value == None):
                    min_value = number_list[j]
                    min_index = j
                    
                else:
                    min_value = min((min_value, 0), (number_list[j], 1))
                    
                    if min_value[1]:
                        min_value = min_value[0]
                        min_index = j
                    
                    else:
                        min_value = min_value[0]
                        
            number_list[i], number_list[min_index] = number_list[min_index], number_list[i]
            
            step += 1
            self.procedure[step] = number_list.copy()
            
        return number_list, self.procedure
                    
    def quick_sort(self, number_list, step=0, left=0, right=None):
        assert type(number_list) is list
        assert len(number_list) > 1

        self.procedure[step] = number_list.copy()
        
        if (right == None):
            right = len(number_list) - 1
        
        # record current starting left and right, which given to next recurrence
        cur_start_left = left
        cur_start_right = right
        

        if (left >= right):
            pass
        else:
            # choose the pivot randomly
            pivot_index = random.randint(left, right)
            pivot = number_list[pivot_index]
            
            # swap pivot to last
            number_list[cur_start_right], number_list[pivot_index] =\
                number_list[pivot_index], number_list[cur_start_right]
            right -= 1
            
            # current pivot index
            pivot_index = cur_start_right
            
            while (True):     
                while ((number_list[left] <= pivot) and (left < right)):
                    left += 1
                
                while ((number_list[right] >= pivot) and (left < right)):
                    right -= 1
                
                if (left < right):
                    #swap
                    number_list[left], number_list[right] = number_list[right], number_list[left]
                else:
                    # check pivot and final index
                    if (number_list[left] > pivot):
                        number_list[left], number_list[cur_start_right] =\
                            number_list[cur_start_right], number_list[left]
                        
                        pivot_index = left
                    break
                
            step += 1
            self.procedure[step] = number_list.copy()
            
            # sub list that is smaller than pivot go to next recurrence
            self.quick_sort(number_list, step, cur_start_left, pivot_index - 1)
            # sub list that is larger than pivot go to next recurrence
            self.quick_sort(number_list, step, pivot_index + 1, cur_start_right)
                
        return number_list, self.procedure 
            
            
    def merge_sort(self, number_list, step=0):
        assert type(number_list) is list
        assert len(number_list) > 1
        
        self.procedure[step] = number_list.copy()
        
        if (type(number_list[0]) is not list):
            for i in range(len(number_list)):
                number_list[i] = [number_list[i]]
        
        # seprate
        step += 1
        self.procedure[step] = number_list.copy()
        
        # merge
        while (len(number_list) != 1):       
            step += 1
            number_list = self.__merge(number_list.copy(), step)
            
        return number_list[0], self.procedure
    
    # private function    
    def __merge(self, number_list, step):        
        new_number_list = []
        
        count = len(number_list)//2
        # check number of set is odd or even 
        more_one_step = bool(len(number_list) % 2)
            
        for i in range(count):
            left = 0
            right = 0
            temp_list = []
            
            while (True):
                if ((left == -1) and (right == -1)):
                    break
                elif (left == -1):
                    temp_list.append(number_list[i*2 + 1][right])
                    right += 1
                        
                    if (right == len(number_list[i*2 + 1])):
                        right = -1
                            
                elif (right == -1):
                    temp_list.append(number_list[i*2][left])
                    left += 1
                        
                    if (left == len(number_list[i*2])):
                        left = -1
                            
                else:
                    if ((number_list[i*2][left] > number_list[i*2 + 1][right])):
                        temp_list.append(number_list[i*2 + 1][right])
                        right += 1
                        
                        if (right == len(number_list[i*2 + 1])):
                            right = -1
                        
                    else:
                        temp_list.append(number_list[i*2][left])
                        left += 1
                        
                        if (left == len(number_list[i*2])):
                            left = -1
            
            new_number_list.append(temp_list)
    
        if more_one_step:
            
            left = 0
            right = 0
            temp_list = []
            
            while (True):
                if ((left == -1) and (right == -1)):
                    break
                elif (left == -1):
                    temp_list.append(number_list[-1][right])
                    right += 1
                        
                    if (right == len(number_list[-1])):
                        right = -1
                            
                elif (right == -1):
                    temp_list.append(new_number_list[-1][left])
                    left += 1
                        
                    if (left == len(new_number_list[-1])):
                        left = -1
                            
                else:
                    if ((new_number_list[-1][left] > number_list[-1][right])):
                        temp_list.append(number_list[-1][right])
                        right += 1
                        
                        if (right == len(number_list[-1])):
                            right = -1
                        
                    else:
                        temp_list.append(new_number_list[-1][left])
                        left += 1
                        
                        if (left == len(new_number_list[-1])):
                            left = -1
                            
            new_number_list.pop(-1)
            new_number_list.append(temp_list)
            
        self.procedure[step] = new_number_list.copy()
        
        return new_number_list
                
                            
if __name__ == "__main__":
    '''
    action => 0: single example test, 1: avg speed test for single algo, 2: avg speed test for all algo
    algo   => selection_sort, bubble_sort, insert_sort, quick_sort, merge_sort (slow => fast)
    '''
    action = 2
    algo = "merge_sort"
    
    sorting = sorting()
    
    if (action == 0):    
        number_list = random.sample(range(0, 100), 10)
            
        before = int(time() * 1000)
        
        '''
        let the class function name become variable  
        getattr(sorting, "merge_sort") == sorting.merge_sort
        '''
        result, procedure = getattr(sorting, algo)(number_list.copy())
        
        after = int(time() * 1000)
        
        if result != sorted(number_list):
            print("{} is wrong".format(algo))
        else:
            print("correct")
            print("{} cost: {} ms".format(algo, after - before))
    
    elif (action == 1):
        from tqdm import tqdm
        
        test_time = 100
        test_min = 0
        test_max = 10000
        test_number = 1000
        
        avg_time = 0
        acc = True
        
        for i in tqdm(range(test_time)):
        
            number_list = random.sample(range(test_min, test_max), test_number)
            
            before = int(time() * 1000)
            
            result, procedure = getattr(sorting, algo)(number_list.copy())
            
            after = int(time() * 1000)
            
            if result != sorted(number_list):
                print("wrong")
                acc = False
                break            
            
            avg_time += (after - before)/test_time
        
        if acc:
            print("each case combine {} numbers that are range from {} to {} "\
                  .format(test_number, test_min, test_max))
            print("{} avg time in {} cases: {:.3f} ms".format(algo, test_time, avg_time))
        else:
            print("{} is wrong".format(algo))
            
    elif (action == 2):
        from tqdm import tqdm
        
        test_time = 100
        test_min = 0
        test_max = 10000
        test_number = 1000
        
        algo_set = ["selection_sort", "bubble_sort", "insert_sort", "quick_sort", "merge_sort"]
        result_set = []
        
        for algo in algo_set:
            avg_time = 0
            
            print("start evaluating ", algo)
            
            for i in tqdm(range(test_time)):
            
                number_list = random.sample(range(test_min, test_max), test_number)
                
                before = int(time() * 1000)
                
                result, procedure = getattr(sorting, algo)(number_list.copy())
                
                after = int(time() * 1000)
                
                if result != sorted(number_list):
                    print("wrong")
                    break            
                
                avg_time += (after - before)/test_time
                
            result_set.append([algo, avg_time])
            
        print("the avg time for all algo by testing {} cases".format(test_time))
        print("each case combine {} numbers that are range from {} to {} "\
                  .format(test_number, test_min, test_max))
        
        for i in range(len(algo_set)):
            print("{} avg time: {:.3f} ms".format(result_set[i][0], result_set[i][1]))
            
    else:
        print("WTF????????")
    

    
    