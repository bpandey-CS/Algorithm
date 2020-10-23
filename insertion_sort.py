from datetime import datetime

def insert_sort(array: list):
    """
        :array - list that needs to be sorted in ascending order
    """
    n = len(array)
    for j in range(1, n):
        i = j-1
        # insert array[j] into sorted sequence betwwen [1, .. j-1]
        key = array[j]
        while(i>=0 and array[i]>key):
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = key
        
    return array

input_list = [2,9,6,5,7]
t0 = datetime.utcnow()
output_array = insert_sort(input_list)
print("TIME TAKEN: ",datetime.utcnow()-t0)
print(output_array)