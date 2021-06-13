'''Bob is preparing to pass IQ test. The most frequent task in this test is to find 
out which one of the given numbers differs from the others. Bob observed that one 
number usually differs from the others in evenness. Help Bob — to check his answers, 
he needs a program that among the given numbers finds one that is different in 
evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes
 of the elements start from 1 (not 0)

Examples:
    # Third number is odd, while the rest of the numbers are even
    iq_test("2 4 7 8 10") = > 3

    # Second number is even, while the rest of the numbers are odd
    iq_test("1 2 1 1") = > 2'''


def iq_test(numbers):
    even = []
    odd = []
    numbers = list(map(int, numbers.split(' ')))
    for a in numbers:
        if a % 2 == 0:
            even.append(a)
        else:
            odd.append(a)
    if len(odd) == 1:
        return (numbers.index(odd[0]))+1
    return (numbers.index(even[0]))+1
