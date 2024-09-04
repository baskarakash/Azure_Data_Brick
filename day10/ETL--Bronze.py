# Databricks notebook source
# MAGIC %run /Workspace/Users/akash_1724384726998@npupgradassessment.onmicrosoft.com/day10/includes
# MAGIC

# COMMAND ----------

dbutils.widgets.text("environment","dev")
v=dbutils.widgets.get("environment")

# COMMAND ----------

df = spark.read.csv("dbfs:/FileStore/dbfs/ent/upgradtrendenceadls/products.csv", header=True, inferSchema=True)
df1 = add_ingestion_col(df)
df2=df1.withColumn("environment",lit(v))
df2.write.mode("overwrite").option("mergeSchema", "true").saveAsTable("bronze.products_bronze")


# COMMAND ----------


