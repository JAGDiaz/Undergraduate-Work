"""
Joseph Diaz
Project Code for Knapsack problem with Branch and Bound.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['savefig.format'] = 'jpg'


class Node(object):
    """
    This class acts as each node of the tree that the branch and bound
    uses as part of it's execution
    """
    def __init__(self, level, benefit, weight, taken):
        self.level = level
        self.benefit = benefit
        self.weight = weight
        self.taken = taken
        self.available = self.taken[:self.level] + [1] * (len(data_sorted) - level)
        self.ub = self.upperbound()

    def upperbound(self):
        """
        This function computes an upper bound for the given node.
        """
        upperbound = 0
        weight_accumulate = 0
        for avail, (_, wei, val) in zip(self.available, data_sorted):
            if wei * avail <= max_weight - weight_accumulate:
                weight_accumulate += wei * avail
                upperbound += val * avail
            else:
                upperbound += val * (max_weight - weight_accumulate) / wei * avail
                break
        return upperbound

    def develop(self):
        """
        This function uses the current weight to determine which branch would be most
        fruitful to explore.
        """
        level = self.level + 1
        _, weight, value = data_sorted[self.level]
        left_weight = self.weight + weight
        if left_weight <= max_weight:
            left_benefit = self.benefit + value
            left_taken = self.taken[:self.level] + [1] + self.taken[level:]
            left_child = Node(level, left_benefit, left_weight, left_taken)
        else:
            left_child = None
        right_child = Node(level, self.benefit, self.weight, self.taken)
        return ([] if left_child is None else [left_child]) + [right_child]


np.random.seed(18*37)
c = 500
iters = [None]*c
x = np.arange(c) + 1
for i in x:
    n = 5*i
    item = np.arange(n) + 1
    weights = np.random.uniform(1, 5, size=(n,))
    values = np.random.uniform(10, 20, size=(n,))

    data_sorted = sorted(zip(item, weights, values),
                         key=lambda i: i[2]/i[1], reverse=True)

    max_weight = n*np.random.uniform(.5, .75)

    Root = Node(0, 0, 0, [0] * len(data_sorted))
    waiting_States = []
    current_state = Root
    j = 0
    while current_state.level < len(data_sorted):
        waiting_States.extend(current_state.develop())
        waiting_States.sort(key=lambda x: x.ub)
        current_state = waiting_States.pop()
        j += 1
    best_item = [item for tok, (item, _, _)
                 in zip(current_state.taken, data_sorted) if tok == 1]

    iters[i-1] = j

x *= 5

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(x, np.log10(iters), 'r-', label="Branch and Bound Iterations")
ax.plot(x, np.log10(2)*x, 'k-', label="Brute Force Iterations")

ax.set_xlabel("Number of items", size=20)
ax.set_ylabel("$log_{10}$(Iterations)", size=15)
ax.set_title("Brute Force vs. Branch and Bound", size=30)
ax.legend(loc='upper left', fontsize=15)
ax.grid()

fig.savefig("ForceVsBound")

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(x, np.log10(iters), 'r-')

ax.set_xlabel("Number of items", size=20)
ax.set_ylabel("$log_{10}$(Iterations)", size=15)
ax.set_title("Knapsack problem: Branch and Bound", size=30)
ax.grid()

fig.savefig("BnBalone")
