pr = input('enter the processes').upper().split()
arrival = list(map(int, input('Enter the arrival time').split()))
burst = list(map(int, input('Enter the burst time').split()))
run = [[pr[i], burst[i]] for i in range(len(pr))]
proc = [[pr[i], arrival[i]] for i in range(len(pr))]
current = []
for t in range(100):
    for count in range(len(proc)):
        if len(arrival)==0:
            break
        elif proc[count][1] == t:
            ind = proc.index(proc[count])
            current.append(run[ind])
            arrival.pop(0)
    if len(current)==0:
        continue
    burst = [i for i in burst if i!=0]
    if len(burst)!= 0:
        current.sort(key = lambda x: x[1])
        temp = current[0]
        print(f'Running process {temp[0]}')
        ind = burst.index(temp[1])
        burst[ind] -= 1
        temp[1] -= 1
        if temp[1] == 0:
            current.pop(0)
            pr.pop(0)
    else:
        exit()
