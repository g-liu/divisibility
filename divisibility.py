import math
import pprint


class DivisibilityTester:
	divisibility_dict = dict()

	def is_divisible(self, n, by):
		return n % by == 0

	def run_divisibility_check(self):
		for i in range(1, 1000):
			print(i)
			self.divisibility_dict[i] = set([1, i])

			j = int(math.ceil(math.sqrt(i)))
			

			while j >= 2:
				is_already_known_divisor = j in self.divisibility_dict[i]
				if not is_already_known_divisor and self.is_divisible(i, j):
					# check our divisibility_dict to see if we have already calculated the factors for `j`
					try:
						factors_of_j = self.divisibility_dict[j]

						for factor in factors_of_j:
							self.divisibility_dict[i].add(factor)
							self.divisibility_dict[i].add(int(i/factor))

					except KeyError as ke:
						self.divisibility_dict[i].add(j)
						self.divisibility_dict[i].add(int(i/j))

				j -= 1

			self.divisibility_dict[i]

		with open('factors.txt', 'w') as f:
			pp = pprint.PrettyPrinter(indent=4,stream=f)

			pp.pprint(self.divisibility_dict)

		print('done.')

# Run the code
DivisibilityTester().run_divisibility_check()