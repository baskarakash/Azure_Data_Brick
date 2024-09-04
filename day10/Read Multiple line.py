# Databricks notebook source
df = spark.read.option("multiline", True).json("dbfs:/FileStore/dbfs/ent/upgradtrendenceadls/data.json")


# COMMAND ----------

df.display()

# COMMAND ----------


