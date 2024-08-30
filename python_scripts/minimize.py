from itertools import combinations

# Define the durations of each job in Queue 2 and Queue 
jobs = [
    (duration_q1, duration_q2) for duration_q1, duration_q2 in zip(
        [ 17.172, 41.463, 100.292 , 22.770, 132.726 ,166.220 ,37.658],  # Durations in Queue 2 : radix, black, canneal, dedup, ferret, freqmine, vips 
        [ 25, 40.1, 84.02 , 22.65 , 108.51, 143.67,34.42 ]   # Durations in Queue 3 (different times)
    )
]

# Number of jobs
num_jobs = len(jobs)
#proportion of time spent in eqch queue
time_normal =2122 
time_high = 538 
# Function to calculate the sum of durations in each queue
def calculate_sums(jobs, queue1_indices):
    sum_q1 = ( sum(jobs[i][0] for i in queue1_indices))/time_normal
    sum_q2 = (sum(jobs[i][1] for i in range(num_jobs) if i not in queue1_indices))/time_high
    return sum_q1, sum_q2

# Initialize variables to store the optimal distribution
min_max_sum = float('inf')
best_distribution = None

# Try all possible combinations of assigning jobs to Queue 1
for r in range(num_jobs + 1):
    for queue1_indices in combinations(range(num_jobs), r):
        sum_q1, sum_q2 = calculate_sums(jobs, queue1_indices)
        max_sum = max(sum_q1, sum_q2)
        if max_sum < min_max_sum:
            min_max_sum = max_sum
            best_distribution = (queue1_indices, tuple(i for i in range(num_jobs) if i not in queue1_indices))

# Print the results
print("Optimal distribution to minimize the maximum queue sum:")
print(f"Queue 1 jobs (indices): {best_distribution[0]}")
print(f"Queue 2 jobs (indices): {best_distribution[1]}")
print(f"Sum of times in Queue 1: {(sum(jobs[i][0] for i in best_distribution[0]))/time_normal}")
print(f"Sum of times in Queue 2: {sum(jobs[i][1] for i in best_distribution[1])/time_high}")
print(f"Minimized maximum sum of times: {min_max_sum}")
