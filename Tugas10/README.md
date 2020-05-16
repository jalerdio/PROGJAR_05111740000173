# Tugas 10 Pemrograman Jaringan
## Perbandingan Performance Test pada Server Asynchronous menggunakan Load Balancer Menggunakan Apache Benchmark

1. async_server.py pada port 9002, 9003, 9004, 9005 dijalankan dengan menggunakan script runserver.sh

2. Load Balancer (lb.py) dijalankan pada port 44444

3. Uji coba Performnace Test pada port 44444 dijalankan dengan :
* Jumlah request 1000
* Concurrency level 1, 10, 100, 500, 1000

Berikut hasil dari Performance Test Menggunakan Load Balancer (pada async server) dengan perbandingan tanpa Load Balancer
| __No. Test__ | __Server Model__ | __Concurrency Level__ | __Time Taken fo Test__ | __Complete Request__ | __Failed Request__ | __Total Transferred__ | __Request per Second__ | __Time per Request__ | __Transfer Rate__ |
|--------------|------------------|-----------------------|------------------------|----------------------|--------------------|-----------------------|------------------------|----------------------|-------------------|
| 1            |Asynchronous      | 1                     | 155.120 sec            | 1000                 | 0                  | 122000 Bytes          | 6.45 [#/sec]           | 155.120 [ms]         | 0.78 Kb/sec       |     
| 2            |Asynchronous      | 10                    | 475.142 sec            | 1000                 | 0                  | 122000 Bytes          | 2.10 [#/sec]           | 4751.421 [ms]        | 0.25 Kb/sec       |
| 3            |Asynchronous      | 100                   | 159.386 sec            | 1000                 | 0                  | 122000 Bytes          | 6.27 [#/sec]           | 15938.577 [ms]       | 0.76 Kb/sec       |
| 4            |Asynchronous      | 500                   | 64.881 sec             | 1000                 | 0                  | 122000 Bytes          | 15.41 [#/sec]          | 32440.722 [ms]       | 1.88 Kb/sec       |
| 5            |Asynchronous      | 1000                  | 192.361 sec            | 1000                 | 0                  | 122000 Bytes          | 5.20 [#/sec]           | 192361.271 [ms]      | 0.63 Kb/sec       |
| 6            |Thread            | 1                     | 801.508 sec            | 1000                 | 0                  | 135000 Bytes          | 1.25 [#/sec]           | 801.508 [ms]         | 0.16 Kb/sec       |     
| 7            |Thread            | 10                    | 466.848 sec            | 1000                 | 0                  | 135000 Bytes          | 2.14 [#/sec]           | 4668.477 [ms]        | 0.28 Kb/sec       |
| 8            |Thread            | 100                   | 499.012 sec            | 1000                 | 0                  | 135000 Bytes          | 2.00 [#/sec]           | 49901.221 [ms]       | 0.26 Kb/sec       |
| 9            |Thread            | 500                   | 8.936 sec              | 1000                 | 246                | 33345 Bytes           | 111.91 [#/sec]         | 4467.817 [ms]        | 3.64 Kb/sec       |
| 10           |Thread            | 1000                  | 21.234 sec             | 1000                 | 131                | 17685 Bytes           | 47.09 [#/sec]          | 21234.037 [ms]       | 0.81 Kb/sec       |
| 11           |Asynchronous+LB   | 1                     | 4.336 sec              | 1000                 | 0                  | 122000 Bytes          | 230.63 [#/sec]         | 4.336 [ms]           | 27.48 Kb/sec      |     
| 12           |Asynchronous+LB   | 10                    | 1.710 sec              | 1000                 | 0                  | 122000 Bytes          | 584.84 [#/sec]         | 17.099 [ms]          | 69.68 Kb/sec      |
| 13           |Asynchronous+LB   | 100                   | 1.898 sec              | 1000                 | 0                  | 122000 Bytes          | 526.84 [#/sec]         | 189.809 [ms]         | 62.77 Kb/sec      |
| 14           |Asynchronous+LB   | 500                   | 0.168 sec              | 1000                 | 66                 | 8296 Bytes            | 5964.70 [#/sec]        | 83.826 [ms]          | 48.32 Kb/sec      |
| 15           |Asynchronous+LB   | 1000                  | 0.212 sec              | 1000                 | 203                | 24766 Bytes           | 4719.34 [#/sec]        | 211.894 [ms]         | 114.14 Kb/sec     |


Hasil Performance Test Asynchronous Server menggunakan Load Balancer

![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas10/Results/1000-1.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas10/Results/1000-10.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas10/Results/1000-100.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas10/Results/1000-500.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas10/Results/1000-1000.png)
