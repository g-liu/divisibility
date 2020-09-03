import math
import pprint


def is_divisible(n, by):
	return n % by == 0

def main():
	divisibility_dict = dict()

	for i in range(1,1000):
		print(i)
		divisibility_dict[i] = []
		upper_bound = int(math.ceil(math.sqrt(i)))
		for j in range(1, upper_bound):
			if is_divisible(i, j):
				divisibility_dict[i].append(j)
				# and add its pair
				divisibility_dict[i].append(int(i/j))

		divisibility_dict[i].sort()

	with open('factors.txt', 'w') as f:
		pp = pprint.PrettyPrinter(indent=4,stream=f)

		pp.pprint(divisibility_dict)

	print('done.')

main()