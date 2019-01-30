## Tutorial materials for hadoop and mapreduce distributed system

### Toy project
A project that helps people get a general sense of what mapreduce does
### Currency project
A simple hands on project about mapreduce + hadoop

### Hadoop Install:
https://dtflaneur.wordpress.com/2015/10/02/installing-hadoop-on-mac-osx-el-capitan/
http://hanslen.me/2018/01/19/How-to-install-Hadoop-on-macOS-High-Sierra/

### Hadoop Command for Single Node Local Mode:
hdfs dfs -mkdir -p /user/gabriel/daily
hdfs dfs -put /Users/gabriel/desktop/hadoop_mapreduce/currency_project/* daily
hdfs dfs -ls daily
bin/hadoop jar /usr/local/Cellar/hadoop/3.1.1/libexec/share/hadoop/tools/lib/hadoop-*streaming*.jar -file daily/mapper.py -mapper daily/mapper.py -file daily/reducer.py  -reducer daily/reducer.py  -input daily/daily.csv -output daily/output
