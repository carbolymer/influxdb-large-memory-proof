# InfluxDB High Memory Utilization Proof
Proof of high memory utilization during batch imports in influxDB.
**Runing this can freeze your computer**
## Contents
The docker image run-import is based on debian jessie with python 3.5.2 and contains following python packages:
* numpy==1.11.1
* numexpr==2.6.0
* bottleneck==1.1.0
* tables==3.2.3.1
* pandas==0.18.1
* influxdb==3.0.0

## How to run
```
docker-compose up
```
This command will pull `carbolymer/python3:pandas-018.1` and `influxdb:0.13-alpine` images from dockerhub. After that the import.py script will be executed. This script reads price entries from db.hdf and inserts the into InfluxDB. You can notice that during execution of this script memory utilization grows extremely fast.