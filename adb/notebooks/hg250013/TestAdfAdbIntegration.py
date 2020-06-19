# Databricks notebook source
# MAGIC %python
# MAGIC storageAccountName = "tdaastrgdls"
# MAGIC path = "abfss://hg250013@tdaastrgdls.dfs.core.windows.net/"
# MAGIC 
# MAGIC #dbutils.fs.ls(path)

# COMMAND ----------

dbutils.fs.ls(path)

# COMMAND ----------

df = spark.read.parquet("abfss://hg250013@tdaastrgdls.dfs.core.windows.net/output1")
display(df)

# COMMAND ----------

df.write.mode("overwrite").format('json').save("abfss://hg250013@tdaastrgdls.dfs.core.windows.net/output5")