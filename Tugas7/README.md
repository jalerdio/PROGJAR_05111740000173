# Tugas 7 Pemrograman Jaringan
## Performance Test Menggunakan Apache Benchmark

Performance Test ini dilakukan pada web server yang sama dengan Tugas 6. Berikut hasil dari Performance Test.

| __No. Test__ | __Concurrency Level__ | __Time Taken fo Test__ | __Complete Request__ | __Failed Request__ | __Total Transferred__ | __Request per Second__ | __Time per Request__ | __Transfer Rate__ |
|--------------|-----------------------|------------------------|----------------------|--------------------|-----------------------|------------------------|----------------------|-------------------|
| 1            | 1                     | 0.135 sec              | 10                   | 0                  | 1350 Bytes            | 74.18 [#/sec]          | 13.480 [ms]          | 9.78 Kb/sec       |     
| 2            | 5                     | 0.108 sec              | 10                   | 0                  | 1350 Bytes            | 92.92 [#/sec]          | 53.808 [ms]          | 12.25 Kb/sec      |
| 3            | 10                    | 0.139 sec              | 10                   | 0                  | 1350 Bytes            | 71.90 [#/sec]          | 139.073 [ms]         | 9.48 Kb/sec       |
| 4            | 1                     | 0.803 sec              | 50                   | 0                  | 6750 Bytes            | 62.27 [#/sec]          | 16.060 [ms]          | 8.21 Kb/sec       |
| 5            | 10                    | 0.290 sec              | 50                   | 0                  | 6750 Bytes            | 172.51 [#/sec]         | 57.967 [ms]          | 22.74 Kb/sec      |
| 6            | 30                    | 0.772 sec              | 50                   | 0                  | 6750 Bytes            | 64.78 [#/sec]          | 463.134 [ms]         | 8.54 Kb/sec       |
| 7            | 50                    | 0.701 sec              | 50                   | 0                  | 6750 Bytes            | 71.35 [#/sec]          | 700.816 [ms]         | 9.41 Kb/sec       |
| 8            | 1                     | 6.217 sec              | 100                  | 0                  | 13500 Bytes           | 16.09 [#/sec]          | 62.168 [ms]          | 2.12 Kb/sec       |
| 9            | 10                    | 4.116 sec              | 100                  | 0                  | 13500 Bytes           | 24.30 [#/sec]          | 411.572 [ms]         | 3.20 Kb/sec       |
| 10           | 50                    | 5.824 sec              | 100                  | 0                  | 13500 Bytes           | 17.17 [#/sec]          | 2912.167 [ms]        | 2.26 Kb/sec       |
| 11           | 100                   | 1.534 sec              | 100                  | 0                  | 13500 Bytes           | 65.19 [#/sec]          | 1534.035 [ms]        | 8.59 Kb/sec       |

Hasil dengan 10 Request

![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas7/Result/10-1.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas7/Result/10-5.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas7/Result/10-10.png)

Hasil dengan 50 Request

![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas7/Result/50-1.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas7/Result/50-10.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas7/Result/50-30.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas7/Result/50-50.png)

Hasil dengan 100 Request

![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas7/Result/100-1.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas7/Result/100-10.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas7/Result/100-50.png)
![alt text](https://github.com/jalerdio/PROGJAR_05111740000173/blob/master/Tugas7/Result/100-100.png)
