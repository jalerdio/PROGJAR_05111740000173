# Tugas 9 Pemrograman Jaringan
## Perbandingan Performance Test pada Server Asynchronous dan Thread Menggunakan Apache Benchmark

1. Terdapat dua model server, server Asynchronous dijalankan pada port 45000 dan server Thread pada port 46000.

2. Uji coba dijalankan dengan :
* Jumlah request 1000
* Concurrency level 1, 10, 100, 500, 1000

Berikut hasil dari Performance Test pada kedua model server
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


Hasil Pada Server Asynchronous

![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas9/Results/async_1000-1.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas9/Results/async_1000-10.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas9/Results/async_1000-100.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas9/Results/async_1000-500.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas9/Results/async_1000-1000.png)


Hasil Pada Server Thread

![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas9/Results/thread_1000-1.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas9/Results/thread_1000-10.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas9/Results/thread_1000-100.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas9/Results/thread_1000-500.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas9/Results/thread_1000-1000.png)
