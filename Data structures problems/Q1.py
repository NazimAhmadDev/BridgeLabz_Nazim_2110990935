l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

odd_index_l1 = l1[1::2]
even_index_l2 = l2[::2]

final_list = odd_index_l1 + even_index_l2
print("Element at odd-index positions from list one", odd_index_l1)
print("Element at even-index positions from list two", even_index_l2)
print("Printing Final third list", final_list)
