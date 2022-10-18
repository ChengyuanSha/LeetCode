def print_all_codes(n, m):

    def print_01_codes(current, num_digits):

        if num_digits == 0:

            print(current)

        else:

            print_01_codes('0' + current, num_digits - 1)

            print_01_codes('1' + current, num_digits - 1)

    upper_bound = 0

    while True:

        for i in range(upper_bound):

            print_01_codes('', n)

        if upper_bound > m:

            break

        upper_bound += 1