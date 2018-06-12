from BSFOUR import *
import threading

# def retriever_soup(st):
# 	# print (st)
# 	return (st)

# arr =["http://www.facebook.com","http://www.google.com"]
arr =["http://www.google.com"]
arr_of_functions = [retriever_soup,retriever_soup]

def m_thread(arr_of_function):
	threads = []
	for i in range(len(arr_of_function)):
		threads.append(i)
		threads[i] = threading.Thread(target = arr_of_function[0],args=(arr[0],))
		threads[i].start()

	for i in range(len(arr_of_function)):
		threads[i].join()
	return (threads[-1])

save_soup = m_thread(arr_of_functions)

print(save_soup)