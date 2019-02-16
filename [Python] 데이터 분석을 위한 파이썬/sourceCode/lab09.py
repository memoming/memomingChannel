

import numpy as np

# python 기본 List 연산
# list_A = [1,2,3]
# list_B = [1,1,1]
# list_C = list_A + list_B
# print(list_C)

# numpy list 연산
# np_list_A = np.array( list_A )
# np_list_B = np.array( list_B )
# np_list_C = np_list_A + np_list_B
# print(np_list_C)

# shape 확인하기
arr = np.array( range(1,9) ) # np.array( [1,2,3,4,5,6,7,8] )
# print(arr.shape)
# print(arr)
arr2 = np.reshape(arr, [2,2,2] )
print(arr2.shape)
print(arr2)

