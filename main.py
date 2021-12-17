import math
import random


def fermats_little_theorem_check(a, n):
	"""
	Returns True if the remainder is 1 according to Fermat's
	Little Theorem, if not returns False.
	"""
	flt = (a ** (n-1)) % n # if != 1, n in not a prime

	return flt == 1


def is_prime(n):
	"""
	Runs fermats_little_theorem_check function k times to check if it 
	always holds. If yes, n is likely a prime, if no, n is definitely 
	not a prime.
	"""
	if n == 1:
		return False
	elif n in [2, 3]:
		return True

	k = math.ceil(n * 0.20)

	for i in range(k):
		a = random.randint(2, n-1)

		if not fermats_little_theorem_check(a, n):
			return False

	return True


if __name__ == "__main__":

	test_set = [2, 3, 4, 5, 7, 8, 11, 21, 29]

	for t in test_set:
		if is_prime(t):
			print(f"{t} is most likely a prime.")
		else:
			print(f"{t} is not a prime.")
