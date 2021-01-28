import random


def moving_window_average(x, n_neighbors=1):
    width = n_neighbors*2 + 1
    x = [x[0]] * n_neighbors + x + [x[-1]] * n_neighbors

    list_of_means = []
    for ind, val in enumerate(x):
        left_ind = ind - n_neighbors
        right_ind = ind + n_neighbors

        if left_ind < 0 or right_ind > len(x)-1:
            continue

        mean = 0
        for item in x[left_ind:right_ind + 1]:
            mean += item
        mean /= width
        list_of_means.append(mean)
    return list_of_means


# Exercise 3a -----------------------------------------
lst = [0, 10, 5, 3, 1, 5]
print(moving_window_average(lst, 1))


# Exercise 3b -----------------------------------------
random.seed(1)
lst = [random.random() for i in range(1000)]

Y = [lst]
for n in range(1, 10):
    Y.append(moving_window_average(lst, n))

print(Y[5][9])


# Exercise 3c -----------------------------------------
ranges = []
for i in Y:
    ranges.append(max(i)-min(i))

print(ranges)
