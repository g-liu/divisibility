import math
import pprint


class DivisibilityTester:
	divisibility_dict = dict()

	def is_divisible(self, n, by):
		return n % by == 0

	def run_divisibility_check(self):
		for i in range(1, 480000):
			if i % 1000 == 0:
				print(i)
			self.divisibility_dict[i] = set([1, i])

			j = int(math.ceil(i / 2))

			while j >= 2:
				if self.is_divisible(i, j):
					# check our divisibility_dict to see if we have already calculated the factors for `j`
					factors_of_j = self.divisibility_dict[j]

					self.divisibility_dict[i] |= factors_of_j

					for factor in factors_of_j:
						self.divisibility_dict[i].add(int(i/factor))

					j = int(math.ceil(j / 2))
				else: 
					j -= 1

		with open('factors.txt', 'w') as f:
			pp = pprint.PrettyPrinter(indent=4,stream=f)

			pp.pprint(self.divisibility_dict)

		print('done.')

# Run the code
DivisibilityTester().run_divisibility_check()