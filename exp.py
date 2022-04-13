import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def find_quartiles(values):
    values.sort()
    n = len(values)
    q1 = values[0]
    q5 = values[-1]
    q3 = (values[(n - 1) // 2] + values[n // 2]) / 2

    i1 = (n + 3) // 4 - 1
    frac1 = (n + 3) / 4 - i1 - 1
    q2 = frac1 * (values[i1 + 1] - values[i1]) + values[i1]

    i2 = (3 * n + 1) // 4 - 1
    frac2 = (3 * n + 1) / 4 - i2 - 1
    q4 = frac2 * (values[i2 + 1] - values[i2]) + values[i2]

    return [q1, q2, q3, q4, q5]


def v_mean(values):
    n = len(values)
    return sum(values) / n if values else 0


def standard_deviation(values):
    n = len(values)
    mean = sum(values) / n if values else 0
    std_dev = 0
    for v in values:
        std_dev += (v - mean) ** 2
    std_dev = math.sqrt(std_dev / (n - 1)) if n > 1 else 0
    return std_dev


def elements_around_mean(values, std_coeff=1):
    mean = v_mean(values)
    std_dev = standard_deviation(values)
    sorted(values)
    count = 0
    for v in values:
        if mean - std_coeff * std_dev <= v <= mean + std_coeff * std_dev:
            count += 1
    return count


if __name__ == '__main__':
    np.random.seed(33)

    data_1 = np.random.logistic(1, 0.5, 200)
    data_2 = np.random.standard_exponential(200)
    data_3 = np.random.uniform(1, 4, 200)

    data = [data_1, data_2, data_3]
    labels = ['logistic', 'exponential', 'uniform']

    # your code here
    plt.boxplot(data, vert=False, labels=labels, meanline=True, showmeans=True)

    plt.ylabel('Values')
    plt.xlabel('Data sets')
    plt.title('Sample random distributions', fontsize=14)

    plt.show()