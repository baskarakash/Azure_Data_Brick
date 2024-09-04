-- Databricks notebook source
-- MAGIC %run /Workspace/Users/akash_1724384726998@npupgradassessment.onmicrosoft.com/day10/includes

-- COMMAND ----------

create table if not exists silver.products_silver as (select ProductID as product_id, ProductName as product_name ,Category as category, ListPrice as list_price from ab_upgrad_630069716375523.bronze.products_bronze)

-- COMMAND ----------

create table if not exists gold.category_count as select category, count(*) as count from ab_upgrad_630069716375523.silver.products_silver group by category order by count desc

-- COMMAND ----------

select * from gold.category_count

-- COMMAND ----------


