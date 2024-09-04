# Databricks notebook source
dbutils.fs.mount(
  source="wasbs://delta@upgradtrendenceadis.blob.core.windows.net",
  mount_point="/ent/upgradtrendenceadls/delta",
  extra_configs={"fs.azure.account.key.upgradtrendenceadis.blob.core.windows.net": "GASLB6/5/HRjm5k0vPpBpwrl/FDRbGVA16mp0pu0zi4oRinR1BIHAxwhRXq1E31mZflipu/d/4gIsAST768FXQ"}
)

# COMMAND ----------

#This is for trial
