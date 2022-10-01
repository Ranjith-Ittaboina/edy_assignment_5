sample_lst = [1, 2, 3, 4, 5, 6, 7]
print(sample_lst)
sample_lst_tripler = list(map((lambda sample_lst : sample_lst * 3),sample_lst))
print(sample_lst_tripler)