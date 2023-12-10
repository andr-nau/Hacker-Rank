def print_formatted(number):
    #Set max width of all columns from width of HEX representation of the max number
    spacing = len('{:b}'.format(number))
    
    for num in range(number):
        for base in 'doXb':
            print('{0:{width}{base}}'.format(num+1, width=spacing, base=base), end=' ')
        print()

print_formatted(17)