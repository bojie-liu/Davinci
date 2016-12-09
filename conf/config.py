#export PYTHONPATH=$PYTHONPATH:"D:\spark-2.0.0-bin-hadoop2.7\spark-2.0.0-bin-hadoop2.7\python"


import os

pyspark_path = "D:\spark-2.0.0-bin-hadoop2.7\spark-2.0.0-bin-hadoop2.7\python"
os.sys.path.append(pyspark_path)

use_spark = False

print __package__
print __name__