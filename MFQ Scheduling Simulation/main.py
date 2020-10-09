def init_process_list():
    f=open('input.txt','r')
    num_of_ps = int(f.readline())
    process = list()
    for i in range(num_of_ps):
        process.append(list(map(int,f.readline().split())))
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
def timeout(on_id,on_queue,burst_ind,quantum,process_list,time,check_end,queue,AT,TT,WT):
    
    # Rule 2 : IO 진입
    if not process_list[on_id-1][burst_ind]:
        if len(process_list[on_id-1]) == burst_ind+1:
            check_end[on_id-1] = 1
            TT[on_id-1] = time - AT[on_id-1] - 1

            # last cpu burst
        else: # IO start - reset arrival time
            process_list[on_id-1][1] = time -1 + process_list[on_id-1][burst_ind+1]
            if on_queue:
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

def cal_wt(queue,WT):
    for q in queue:
        for pid in q:
            WT[pid-1] += 1



def start(process_list,queue):
    time = 0
    check_end = [0] * len(process_list)
    on_id = 0
    on_queue = 0
    on_cpu_burst = 0
    quantum = 0
    burst_ind = 0
    AT = [pc[1] for pc in process_list]
    TT = [0] * len(process_list)
    WT = [0] * len(process_list)
    history=[]
    # 0 id / 1 at / 2 init q / 3 #cycle
    while (1):
        # arrival
        
        for pc in process_list:
            if pc[1] == time:
                queue[pc[2]].append(pc[0])
        time += 1

        # Check quantum
        if on_id:
            on_id,quantum=timeout(on_id,on_queue,burst_ind,quantum,process_list,
        time,check_end,queue,AT,TT,WT)
        
        if not on_id and bool(any(queue)):
            on_id,on_queue = operate_process(queue) 
            burst_ind = 4 # left cpu burst time index
            while not process_list[on_id-1][burst_ind]:
                burst_ind += 2
            on_cpu_burst = process_list[on_id-1][burst_ind]
            quantum = cal_quantum(on_queue,on_cpu_burst)
            quantum -= 1
            process_list[on_id - 1][burst_ind] -= 1
        cal_wt(queue,WT)
        history.append([time,on_id])
        if (set(check_end) == {1}):
            pt_report(time,TT,WT,history)
            break # check end


def pt_report(time,TT,WT,history):
    f = open('report.txt','w')
    past = 1
    print('='*25+'Gantt Chart'+'='*25+'\n')
    f.write('='*25+'Gantt Chart'+'='*25+'\n\n')
    for t,pd in history:
        try:
            recent_pid
        except:
            recent_pid = pd
        if pd != recent_pid:
            if not recent_pid:
                f.write('Time {:<2} ~ {:<2} :  No process\n'.format(past-1,t-1))
                print('Time {:<2} ~ {:<2} :  No process'.format(past-1,t-1))
            else:
                f.write('Time {:<2} ~ {:<2} :  Process {}\n'.format(past-1,t-1,recent_pid))
                print('Time {:<2} ~ {:<2} :  Process {}'.format(past-1,t-1,recent_pid))
            past = t
            recent_pid = pd
    print('\n'+'='*50+'\n')
    f.write('\n'+'='*50+'\n')
    print('Process  Turnaround Time  Waiting Time')
    f.write('Process  Turnaround Time  Waiting Time\n')
    for i,result in enumerate(zip(TT,WT)):
        print('{:>5}  {:>10}  {:>13}'.format(i+1,result[0],result[1]))
        f.write('{:>5}  {:>10}  {:>13}\n'.format(i+1,result[0],result[1]))
    print('\nAverage TT: {:.4f}\nAverage WT: {:.4f}'.format(sum(TT)/len(TT),sum(WT)/len(WT)))
    f.write('\nAverage TT: {:.4f}\nAverage WT: {:.4f}'.format(sum(TT)/len(TT),sum(WT)/len(WT)))
    f.close()
        
def main():
    queue = init_queue()
    process = init_process_list()
    start(process,queue)
    

if __name__ == "__main__":
    main()
    