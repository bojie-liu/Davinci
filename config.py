#export PYTHONPATH=$PYTHONPATH:"D:\spark-2.0.0-bin-hadoop2.7\spark-2.0.0-bin-hadoop2.7\python"

import os
import platform

if platform.system() == "Windows":
    pyspark_path = "D:\spark-2.0.0-bin-hadoop2.7\spark-2.0.0-bin-hadoop2.7\python"
else:
    pyspark_path = "/Users/joshualiu/dev/spark-2.0.2-bin-hadoop2.7/python"

os.sys.path.append(pyspark_path)

print(os.sys.path)

mode = "spark"
