import random


def miller_rabin_test(n, t=10):
	if n == 1:
		return False
	elif n in [2, 3]:
		return True
	elif not n % 2:
		return False

	k, m = 0, n-1
	while not m % 2:
		k += 1
		m //= 2

	for _ in range(t):
		a = random.randint(2, n-2)

		b = pow(a, m) % n
		if b in [1, n-1]:
			continue

		test_passed = False
		for _ in range(k-1):
			b = (b**2) % n
			if b == n-1:
				test_passed = True
				break
		
		if not test_passed:
			return False

	return True


if __name__ == "__main__":

	test_set = [2, 3, 4, 5, 7, 8, 11, 21, 29]

	for n in test_set:
		if miller_rabin_test(n):
			print(f"{n} is a prime.")
		else:
			print(f"{n} is not a prime.")
