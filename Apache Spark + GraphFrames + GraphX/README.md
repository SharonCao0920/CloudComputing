# **PySpark: DataFrames / SparkSQL  + GraphFrames / GraphX**
## **Step 1: Create Cluster on GCP**


*   Refer to previous HW to create
*   Open a terminal through SSH
![My_image](image/start.png)

## **Step 2: Data Prepare**

*   Upload the csv data files from local to cluster

![My_image](image/upload.png)

*   Check Upload

```
$ ls
```
![My_image](image/check.png)


*   Create HDFS file system and copy the data files to HDFS

```
$ hdfs dfs -mkdir hdfs:///mydata
$ hdfs dfs -put ./*.csv hdfs:///mydata/
$ hdfs dfs -ls hdfs:///mydata
```
![My_image](image/hdfs.png)

*   Create the graphdemo.py file and change the path for data files

![My_image](image/path.png)


## **Step 3: Run the code in pyspark shell line by line**

```
$ pyspark
```

*   GraphFrame module not found, solve the problem by adding packages

```
$ pyspark --packages graphframes:graphframes:0.8.2-spark2.4-s_2.11
```

![My_image](image/firsttry.png)

*   New error

![My_image](image/error.png)

*   Check pyspark version and find correspondence jar [package](https://spark-
packages.org/package/graphframes/graphframes)

![My_image](image/pyspark_v.png)

*   Try again

```
$ pyspark --packages graphframes:graphframes:0.8.2-spark3.1-s_2.12
```
![My_image](image/shell_c.png)

*   Success in pyspark-shell, run remaining code

![My_image](image/shell_1.png)
![My_image](image/shell_2.png)
![My_image](image/shell_3.png)
![My_image](image/shell_4.png)
![My_image](image/shell_5.png)
![My_image](image/shell_6.png)
![My_image](image/shell_7.png)
![My_image](image/shell_8.png)
![My_image](image/shell_9.png)
![My_image](image/shell_10.png)
![My_image](image/shell_11.png)
![My_image](image/shell_12.png)
![My_image](image/shell_13.png)


## **Step 4: Run the code with spark-submit**

*   With experience of fixed errors earlier
*   Run code

```
$ spark-submit --packages graphframes:graphframes:0.8.2-spark3.1-s_2.12
graphdemo.py
```
![My_image](image/submit_c.png)

*   No spark found, add initial code for spark session

![My_image](image/session.png)

*   Run again
*   Typo found

![My_image](image/typo.png)

*   Fixed and run, successfully execute

![My_image](image/submit_1.png)
![My_image](image/submit_2.png)
![My_image](image/submit_3.png)
![My_image](image/submit_4.png)
![My_image](image/submit_5.png)
![My_image](image/submit_6.png)
![My_image](image/submit_7.png)



