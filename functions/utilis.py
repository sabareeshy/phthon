def is_prime(number):
    result = True
    for index in range(2, number):
        if number % index == 0:
            result = False
            break
    return result