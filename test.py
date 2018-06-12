from BSFOUR import *
import threading

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


save_soup = m_thread(arr_of_functions)

print(save_soup)