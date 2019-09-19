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
    
    if len(data) == 0:
        return []
    else:
        pivot = data[0]
        less, equal, greater = Spartition(data, pivot)
        return quick_sort(less) + equal + quick_sort(greater)

def Spartition(data: List[Merchant], pivot: Merchant) \
      -> Tuple[List[Merchant], List[Merchant], List[Merchant]]:
    
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
        index = rand_pivot(data, less, greater)
        if (index - less == k - 1):
            return data[index]
        elif (index - less > k - 1):
            return quick_select(data, less, index - 1, k)
        else:
            return quick_select(data, index + 1, greater, k - index + less - 1) 

def Fpartition(data: List[Merchant], less, greater): 
    x = data[greater].location 
    i = less 
    for j in range(less, greater): 
        if (data[j].location <= x): 
            switch(data, i, j) 
            i += 1
    switch(data, i, greater) 
    return i

def rand_pivot(data: List[Merchant], less, greater): 
    pivot = random.randrange(greater - less + 1)
    switch(data, less + pivot, greater) 
    return Fpartition(data, less, greater)

def switch(data: List[Merchant], a, b):
    temp = data[a] 
    data[a] = data[b] 
    data[b] = temp

def main() -> None:
    """
    The main function.
    :return: None
    """
    merchants = read_merchant("./data/test-1M.txt")

    search_type = input('Insert the search type: ')

    if search_type[0] == 'f':
        median = len(merchants)//2

        t_start = time.perf_counter()
        quick_select(merchants, 0, len(merchants) - 1, median+1)
        elapsedT = time.perf_counter() - t_start

        print(merchants[median])
        print('Search type:', search_type)
        print('Number of merchants:', len(merchants))
        print('Elapsed time:', elapsedT)
        print('Optimal store location:', merchants[median])
        print('Sum of the distances:')

    else:

        t_start = time.perf_counter()

        sorted_merchants = quick_sort(merchants)

        elapsedT = time.perf_counter() - t_start

        median = len(merchants)//2

        print('Search type:', search_type)
        print('Number of merchants:', len(merchants))
        print('Elapsed time:', elapsedT)
        print('Optimal store location:', sorted_merchants[median])
        print('Sum of the distances:')

if __name__ == '__main__':
    main()