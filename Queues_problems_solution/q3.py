from collections import deque

def canCompleteCircuit(gas,cost):
    n = len(gas)
    queue = deque()

    total_gas = 0
    total_cost = 0
    current_gas = 0
    start = 0


    for i in range(n):
        queue.append(i)
        total_gas += gas[i]
        total_cost += cost[i]
        current_gas += gas[i] - cost[i]


        if current_gas < 0:
            while queue:
                queue.popleft()
            start = i + 1
            current_gas = 0
        
    if total_gas < total_cost:
        return -1
    
    return start


gas = [4,5,7,4]
cost = [6,6,3,5]

print(canCompleteCircuit(gas,cost))