import numpy as np
arr = np.array((2, 2, 2, 2))
volume=(arr[0]*arr[1]*arr[2])/arr[3]
if volume==0:
    print("Volume gas ideal adalah:0")
else:
    print("Volume gas ideal adalah:",volume)  

"""
keterangan:
arr[0]= n
arr[1]= R
arr[2]= T
"""    
    
