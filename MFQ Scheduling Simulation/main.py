def init_process_list():
    f=open('input.txt','r')
    num_of_ps = int(f.readline())
    process = list()
    for i in range(num_of_ps):
        process.append(list(map(int,f.readline().split())))
    print(process)
    return process

def init_queue():
    Queue = [[],[],[],[]]
    return Queue

def cal_quantum(qn,i):
    if qn < 3:
        return (2 ** (qn+1))
    return i

def operate_process(queue):
    for i,q in enumerate(queue):
        if q:
            return q.pop(0),i
def timeout(on_id,on_queue,burst_ind,quantum,process_list,time,check_end,queue):
    
    # Rule 2 : IO 진입
    if not process_list[on_id-1][burst_ind]:
        if len(process_list[on_id-1]) == burst_ind+1:
            check_end[on_id-1] = 1
                    # last cpu burst
        else: # IO start - reset arrival time
            process_list[on_id-1][1] = time + process_list[on_id-1][burst_ind+1]
            if on_queue == 1 or on_queue == 2:
                on_queue -= 1
            process_list[on_id-1][2] = on_queue
        on_id = 0
    elif not quantum:
        if on_id: # Rule 1 : 퀀텀 소모 /burst time left
            if process_list[on_id-1][burst_ind]:
                if on_queue < 3:
                    on_queue += 1
                queue[on_queue].append(on_id)
        on_id = 0
    else:
        quantum -= 1
        process_list[on_id-1][burst_ind] -= 1
    return on_id,quantum



                



def start(process_list,queue):
    time = 0
    check_end = [0] * len(process_list)
    on_id = 0
    on_queue = 0
    on_cpu_burst = 0
    quantum = 0
    burst_ind = 0
    # 0 id / 1 at / 2 init q / 3 #cycle
    while (1):
        # arrival
        for pc in process_list:
            if pc[1] == time:
                queue[pc[2]].append(pc[0])
        print(queue)
        # Check quantum
        if on_id:
            on_id,quantum=timeout(on_id,on_queue,burst_ind,quantum,process_list,
        time,check_end,queue)
        print('in_id',on_id)
        if not on_id and bool(any(queue)):
            on_id,on_queue = operate_process(queue) 
            burst_ind = 4 # left cpu burst time index
            while not process_list[on_id-1][burst_ind]:
                burst_ind += 2
            on_cpu_burst = process_list[on_id-1][burst_ind]
            quantum = cal_quantum(on_queue,on_cpu_burst)
        print(on_id,on_queue,burst_ind,quantum,process_list,time,check_end)
        if (set(check_end) == {1}):
            print(time)
            print(queue)
            break # check end
        # print(time)
        # print(queue)
        # print(on_id,on_queue,burst_ind)
        time += 1
        # if time == 4:
            # break
        
            
        

def main():
    queue = init_queue()
    process = init_process_list()
    start(process,queue)
    

if __name__ == "__main__":
    main()
    