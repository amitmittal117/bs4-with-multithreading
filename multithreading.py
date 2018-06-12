import time
import threading
def c_square(num):
	for i in num:
		time.sleep(0.2)
		print ("Square: "+str(i*i))

def c_cube(num):
	for i in num:
		time.sleep(0.2)
		print ("Cube: "+str(i*i*i))

arr =[2,3,4,5]

t = time.time()
x =0
threads = [x,x]
threads[0] = threading.Thread(target = c_square,args=(arr,))

threads[1] = threading.Thread(target = c_cube,args=(arr,))

threads[0].start()

threads[1].start()

threads[0].join()
threads[1].join()

print("time taken: "+ str(time.time()-t))

# def m_thread(number_of_threads):
# 	n_o_t = number_of_threads
# 	threads =[]
# 	temp = 0
# 	for i in range(number_of_threads):
# 		threads.append(temp)

# 	for i in threads:




# m_thread(5)