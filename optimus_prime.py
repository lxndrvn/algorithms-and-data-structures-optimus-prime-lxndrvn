

def count_primes(n):
	sieve = range(2, n + 1)
	prime_numbers = []
	while sieve:
		print("Sieve:")
		print(sieve)
		print("")
		current_number = sieve[0]
		# check current number
		print(current_number)
		print("")
		prime_numbers.append(current_number)
		for i in sieve:
			if i % current_number == 0:
				sieve.remove(i)

	print("Is sieve empty?")
	print(len(sieve) == 0)
	print ("Prime numbers:")
	print(prime_numbers)

	return len(prime_numbers)


print(count_primes(100))





