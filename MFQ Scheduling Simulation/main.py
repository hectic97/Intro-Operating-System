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
    for q in queue:
        if q:
            return q.pop(0)

def start(process_list,queue):
    time = 0
    check_end = [0] * len(process_list)
    on_id = 0
    # 0 id / 1 at / 2 init q / 3 #cycle
    while (1):
        if (set(check_end) == {1}):
            break # check end
        # arrival
        for pc in process_list:
            if pc[1] == time:
                queue[pc[2]].append(pc[0])
        print(queue)
        break
        # Check quantum
        if not quantum:
            new_p_id = operate_process(queue) 
            quantum = cal_quantum(qn,i)
        else:
            quantum -= 1
        i = 4
        while not process_list[on_id-1][i]:
            i += 2
        for qn,q in enumearte(queue):
            if on_id in q:
                break
        

        
        






def main():
    queue = init_queue()
    process = init_process_list()
    start(process,queue)
    

if __name__ == "__main__":
    main()
    