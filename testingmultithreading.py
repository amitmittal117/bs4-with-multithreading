import threading

def c_square(num):
	for i in num:
		print ("Square: "+str(i*i))

def c_cube(num):
	for i in num:
		print ("Cube: "+str(i*i*i))

arr =[2,3,4,5]
arr_of_functions = [c_square,c_cube,c_square,c_cube]

def m_thread(arr_of_function):
	threads = []
	for i in range(len(arr_of_function)):
		threads.append(i)
		threads[i] = threading.Thread(target = arr_of_function[0],args=(arr,))
		threads[i].start()

	for i in range(len(arr_of_function)):
		threads[i].join()

m_thread(arr_of_functions)