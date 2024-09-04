# Databricks notebook source
# MAGIC %sql
# MAGIC create table climate

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO climate
# MAGIC FROM 'dbfs:/FileStore/dbfs/ent/upgradtrendenceadls/data.json'
# MAGIC FILEFORMAT = JSON
# MAGIC FORMAT_OPTIONS ('multiLine' = 'true')
# MAGIC COPY_OPTIONS ('mergeSchema' = 'true')
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM climate;
# MAGIC

# COMMAND ----------


