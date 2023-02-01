"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	
	### TODO
  if left > right:
    #print(mylist)
    return -1
    #mid=len(mylist)//2
  
  mid = (left + right) // 2
  mid_element = mylist[mid]
  if mylist[mid] == key:
    return mid
  elif mylist[mid] > key:
    return _binary_search(mylist, key, left, mid - 1)
    #return binary_search(mylist[0:mid-1], key)
  else:
    return _binary_search(mylist, key, mid +1, right)
    #return binary_search(mylist[mid+1:len(mylist)], key)

    ###

	###

def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	### TODO: add two more tests here.

	###


def time_search(search_fn, mylist, key):
	
	### TODO
  
  start=time.time()
  search_fn(mylist, key)
  end = time.time()
  return (end-start)*1000
	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	
	### TODO
  time_results = []
  ### TODO
  for n in sizes:
    key = -1
    my_list = list(range(int(n)))

  
    linear_search_time = time_search(linear_search, my_list, key)
    binary_search_time = time_search(binary_search, my_list, key)

 
    #time_results.append(len(sizes))
    #time_results.append(linear_search_time)
    #time_results.append(binary_search_time)
    time_results.append((int(n), linear_search_time, binary_search_time))
  
  return time_results
	###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1




