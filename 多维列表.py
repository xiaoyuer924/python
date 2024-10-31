#!C:\Users\15998\AppData\Local\Programs\Python\Python312\python.exe

#  Copyright 2008-2015 Nokia Networks
#  Copyright 2016-     Robot Framework Foundation
#  
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  
#      http://www.apache.org/licenses/LICENSE-2.0
#  
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import sys

from robotide import main

# Must be protected against reimporting
# As multiprocessing has an odd requirement
# and we use multiprocessing
# http://docs.python.org/library/multiprocessing.html#windows
if __name__ == '__main__':
    line_list = input().split(';')
    temp_list = []
    for i in line_list:
        temp_list.append(i.split(','))
    # 请不要更改此行以上的代码
    # print("11111111111111")
    # print(line_list)
    # print("222222222222")
    # print(temp_list)
    # 在这里编写代码
    def sum_of_matrix(temp_list):
        sum=0
        for j in range(len(line_list)):
            for n in range(len(temp_list)):
                sum += int(temp_list[j][n])
        return sum
    # 请不要更改此行以下的代码
    print(sum_of_matrix(temp_list))    # 请不要更改此行以上的代码

