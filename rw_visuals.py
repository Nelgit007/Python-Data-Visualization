import matplotlib.pyplot as plt 

from random_walk import RandomWalk


#Keep generating new walk as long as the program is running
while True:

	#Make a random walk
	rw = RandomWalk(5000)
	rw.fill_walk()

	#Plat graph for walk
	plt.style.use('classic')
	#fig, ax = plt.subplots()
	fig, ax = plt.subplots(figsize=(10, 6), dpi=128 )
	point_num = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values, c=point_num, cmap=plt.cm.Greens,
				edgecolors='none', s =2)

	#Creating emphasis on the start and end points of random walk.
	ax.scatter(0, 0, c='blue', edgecolors='none', s=100)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100 )

	#Remove axis from plot
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	#Show plot
	plt.show()

	keep_running = input('Make another walk chart (y/n): ')
	if keep_running == 'n':
		break
