"""
CSAPX Lab 3: Merchants of Venice

Given a list of merchants at integer locations on a road, find the optimal
location to place a new merchant, such that the sum of the distances the
new merchant must travel to all other merchants is minimized.

$ python3 merchants.py [slow|fast] input-file

Author: Sean Strout @ RIT CS
Author: Danilo Sosa
"""

import collections      # namedtuple
from typing import Tuple
import sys              # arg
import time             # clock
import random           # random

from typing import List # List

Merchant = collections.namedtuple( 'Merchant',
                                 ('name', 'location') )

def read_merchant( filename: str ) -> List[ Merchant ]:

#Function that serves to read the .txt file and add
#each merchant with its corresponding name and location
    merchants = list( )
    with open( filename ) as f:
        for line in f:
            fields = line.split( ' ' )
            merchants.append( Merchant(
                name=fields[ 0 ],
                location=int(fields[ 1 ])
            ) )
    return merchants

def quick_sort(data: List[Merchant]) -> List[Merchant]:
#Recursive function that keeps calling itself with the subarrays 
#as arguments with the pivot being the first index from left to right
    if len(data) == 0:
        return []
    else:
        pivot = data[0]
        less, equal, greater = Spartition(data, pivot)
        return quick_sort(less) + equal + quick_sort(greater)

def Spartition(data: List[Merchant], pivot: Merchant) \
      -> Tuple[List[Merchant], List[Merchant], List[Merchant]]:
#The partition function for the quick sort, it inserts the values
#in their corresponding subarrays depending if they are less, greater
#or equal to the pivot
    less, equal, greater = [], [], []
    for element in data:
        if element.location < pivot.location:
            less.append(element)
        elif element.location > pivot.location:
            greater.append(element)
        else:
            equal.append(element)
    return less, equal, greater

def quick_select(data: List[Merchant], less, greater, k):
#Recursive function that calls itslef wiht different ranges
#from the original list instead of subarrays, these ranges are determined
#with the value of the random pivot compared to the k value

        index = rand_pivot(data, less, greater)
        if (index - less == k - 1):
            return data[index]
        elif (index - less > k - 1):
            return quick_select(data, less, index - 1, k)
        else:
            return quick_select(data, index + 1, greater, k - index + less - 1) 

def Fpartition(data: List[Merchant], less, greater):
#Partition for the quick select method it sorts the array by
#comparing the values inside tha list and switching values to
#fix the ranges (less, greater)
    x = data[greater].location 
    i = less 
    for j in range(less, greater): 
        if (data[j].location <= x): 
            switch(data, i, j) 
            i += 1
    switch(data, i, greater) 
    return i

def rand_pivot(data: List[Merchant], less, greater):
#Function to select the random pivot within the range of the List
    pivot = random.randrange(greater - less + 1)
    switch(data, less + pivot, greater) 
    return Fpartition(data, less, greater)

def switch(data: List[Merchant], a, b):
#Function that serves to switch values within the List
    temp = data[a] 
    data[a] = data[b] 
    data[b] = temp

def main() -> None:
    
    merchants = read_merchant(sys.argv[2])

    if sys.argv[1] == 'slow':
        t_start = time.perf_counter()

        sorted_merchants = quick_sort(merchants)

        elapsedT = time.perf_counter() - t_start

        median = len(merchants)//2

        print('Search type: slow')
        print('Number of merchants:', len(merchants))
        print('Elapsed time:', elapsedT)
        print('Optimal store location:', sorted_merchants[median])

    else:
        median = len(merchants)//2

        t_start = time.perf_counter()
        quick_select(merchants, 0, len(merchants) - 1, median+1)
        elapsedT = time.perf_counter() - t_start
    
        print('Search type: fast')
        print('Number of merchants:', len(merchants))
        print('Elapsed time:', elapsedT)
        print('Optimal store location:', merchants[median])

if __name__ == '__main__':
    main()