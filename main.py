from fizzbuzz_3 import print_first_100
from binary_6 import binary
from merge_7 import merge_sorted_arrays
from bst_to_list_8 import BinarySearchTree
from knapsack_10 import KnapSack
print('------------------------------------------------- FizzBuzz ----------------------------------------------------')
print_first_100()
print('------------------------------------------------ Binary form --------------------------------------------------')
n = int(input('Enter the decimal number: '))
binary(n)
print('--------------------------------------------- Merge sorted lists ----------------------------------------------')
test_list = [-100, -50, 0, 10, 3000, 5000, 7000]
test_list2 = [10000, 200, 100, 0, -1, -100, -200, -600, -800, -1000, -1111]
print('1st list is {0}\n2nd list is {1}'.format(test_list, test_list2))
print('Resulting list is {}'.format(merge_sorted_arrays(test_list, test_list2)))
print('------------------------------------------- Make sorted list from BST -----------------------------------------')
bst = BinarySearchTree(lst=[1, 10, 222, 123, 0, 6])
print(bst.make_sorted_list(bst.root))
print('-------------------------------- Knapsack (dynamic programming implementation) --------------------------------')
values = [16, 19, 23, 28]
sizes = [2, 3, 4, 5]
capacity = 7
max_weight, indexes = KnapSack(sizes, values).solve(capacity)

elements_sizes = []
sum_str = ''
for index in indexes:
    elements_sizes.append(sizes[index])
    sum_str += str(values[index])
    if index is not len(indexes) + 1:
        sum_str += ' + '

print('You can take elements with sizes {0}\n'
      'Which equals to {1} = {2}'.format(elements_sizes, sum_str, max_weight))