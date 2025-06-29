# Databricks notebook source
# MAGIC %md
# MAGIC ### **Data Reading**

# COMMAND ----------

df = spark.read.format('parquet').load('abfss://bronze@datalakesaikh.dfs.core.windows.net/orders')
df.display()

# COMMAND ----------

df = df.withColumnRenamed('_rescued_data', 'rescued_data')
df.display()

# COMMAND ----------

df = df.drop('rescued_data')

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# COMMAND ----------

df = df.withColumn('order_date', to_timestamp(col('order_date')))

# COMMAND ----------

df = df.withColumn('year', year(col('order_date')))\
    .withColumn('month', month(col('order_date')))\
    .withColumn('day', dayofmonth(col('order_date')))
df.display()

# COMMAND ----------

df1 = df.withColumn('row_flag', row_number().over(Window.partitionBy('year').orderBy(col('total_amount').desc())))\
        .withColumn('rank_flag', rank().over(Window.partitionBy('year').orderBy(desc('total_amount'))))\
        .withColumn('dense_flag', dense_rank().over(Window.partitionBy('year').orderBy(desc('total_amount'))))
df1.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Classses OOP**

# COMMAND ----------

class windows:
    def row_number(self, df):
        df_row_number = df.withColumn('row_flag', row_number().over(Window.partitionBy('year').orderBy(col('total_amount').desc())))
        return df_row_number

    def rank(self, df):
        df_rank = df.withColumn('rank_flag', rank().over(Window.partitionBy('year').orderBy(desc('total_amount'))))
        return df_rank

    def dense_rank(self, df):
        df_dense_rank = df.withColumn('dense_flag', dense_rank().over(Window.partitionBy('year').orderBy(desc('total_amount'))))
        return df_dense_rank

# COMMAND ----------

df_new = df 

# COMMAND ----------

object = windows()
df_new = object.row_number(df_new)
df_new = object.rank(df_new)
df_new.display()

# COMMAND ----------

# MAGIC %md 
# MAGIC ### **Data Writing**

# COMMAND ----------

df.write.format("delta")\
    .option('mode', 'oberwrite')\
        .option('path', "abfss://silver@datalakesaikh.dfs.core.windows.net/orders")\
            .save()

# COMMAND ----------

# MAGIC %sql 
# MAGIC CREATE TABLE IF NOT EXISTS databricks_cata.silver.orders 
# MAGIC USING DELTA
# MAGIC LOCATION 'abfss://silver@datalakesaikh.dfs.core.windows.net/orders'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM databricks_cata.silver.orders

# COMMAND ----------

