import numpy as np
import matplotlib.pyplot as plt
import os

# Function to read data from a file and return QPS and 95th percentile values
def read_data(filename):
    data = np.loadtxt(filename, skiprows=1, usecols=(16,12), max_rows=25, dtype=float)
    qps = list(map(lambda x: x/1000, data[:, 0]))
    p95 = list(map(lambda x: x/1000, data[:, 1]))
    return qps, p95

def main():
    # Plotting
    fig = plt.figure(figsize=(10, 6))

    configs = ["T1C1", "T2C1", "T1C2", "T2C2"]
    formats = ["o-", "x-", "s-", "d-"]

    COLS = 25
    RUNS = 3
    # Plot each configuration
    for idx, config in enumerate(configs):
        T = config[1] # num of threads
        C = config[3] # num of core

        qps = [[0]*RUNS for _ in range(COLS)]
        p95 = [[0]*RUNS for _ in range(COLS)]
        for run in range(0, RUNS):
            filename = f'./data/data_part4a/{config}_{run}.txt'
            new_qps, new_p95 = read_data(filename)
            print(T, C, p95)
            for i in range(COLS):
                qps[i][run] = new_qps[i]
                p95[i][run] = new_p95[i]


        qps_mean = np.mean(qps, axis=1)
        p95_mean = np.mean(p95, axis=1)

        qps_std = np.std(qps, axis=1)
        p95_std = np.std(p95, axis=1)

        qps_min = np.min(qps, axis=1)
        qps_max = np.max(qps, axis=1)
        p95_min = np.min(p95, axis=1)
        p95_max = np.max(p95, axis=1)

        # Error bar using min/max
        # plt.errorbar(qps_mean, p95_mean, xerr=[qps_mean - qps_min, qps_max - qps_mean], yerr=[p95_mean - p95_min, p95_max - p95_mean], marker='o', label=f"T={T} C={C}, averaged across {RUNS} runs")

        # Error bar using std
        plt.errorbar(qps_mean, p95_mean, xerr=qps_std, yerr=p95_std, fmt=formats[idx], label=f"T={T} C={C}, averaged across {RUNS} runs")

    # set the x limit from 0
    plt.xlim(0)

    # Add horizontal line for SLO at p95=1.0
    plt.axhline(y=1.0, color='red', linestyle='--', label='SLO at 1.0ms')

    plt.title('95th Percentile Latency vs Achieved QPS for Memcached Configurations', fontsize=16)
    plt.xlabel('Thousands of Achieved Queries per Second (KQPS)', fontsize=14)
    plt.ylabel('95th Percentile Latency (ms)', fontsize=14)
    plt.legend(loc="upper left")
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()