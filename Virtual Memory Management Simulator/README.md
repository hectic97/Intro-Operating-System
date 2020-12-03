# Virtual Memory Management Simulation

## 개발환경
OS: Ubuntu 20.04.1 LTS<br>
Python: 3.8.2

## 실행방법
![image](https://user-images.githubusercontent.com/61140071/100998446-e0598480-359e-11eb-9a1e-4845eecabb1a.png)
>python main.py --info input.txt --log log.txt --algorithm MIN<br>
알고리즘 목록: MIN, FIFO, LFU, LRU, Clock, WS

## input
page 수, memory frame 개수, window size, page reference string 길이<br>
page reference string<br>
<br>
<br>
Example input.txt<br>
5 4 3 10<br>
2 0 3 1 4 1 0 1 2 3 <br>
<br><br>
