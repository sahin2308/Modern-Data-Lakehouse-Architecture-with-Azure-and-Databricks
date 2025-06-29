# 🚀 Modern Data Lakehouse Architecture using Azure & Databricks

An end-to-end Data Engineering solution built using **Azure Data Factory**, **Azure Data Lake Storage Gen2**, **Azure Databricks**, and **Unity Catalog**. This project demonstrates how to design and implement a modern **Lakehouse architecture** using best practices for **data ingestion**, **processing**, **orchestration**, **incremental loading**, and **dimensional modeling**.

---

## 📌 Project Overview

This project simulates a real-world pipeline where:

- Raw files are ingested using **ADF** and stored in **ADLS Gen2**.
- **Databricks Autoloader** incrementally loads data to the **Bronze Layer**.
- Transformation logic is applied in the **Silver Layer** using **PySpark**.
- **Star Schema** (Dimension + Fact tables) is created in the **Gold Layer**.
- **SCD Type 1 & Type 2** logic is implemented using PySpark and **Delta Live Tables**.
- The entire workflow is **orchestrated using Databricks Jobs**.

---

## 🛠️ Tech Stack

| Tool/Service                | Purpose                                      |
|----------------------------|----------------------------------------------|
| Azure Data Factory (ADF)   | Data ingestion from source to ADLS Gen2      |
| ADLS Gen2                  | Raw, Bronze, Silver, and Gold data storage   |
| Azure Databricks           | Data transformation, orchestration, modeling |
| Unity Catalog              | Secure cataloging of Delta tables            |
| Delta Lake                 | Storage format for all structured layers     |
| Delta Live Tables (DLT)    | Streaming & SCD Type 2 implementation        |
| PySpark                    | Data engineering transformations             |
| Databricks Jobs            | Orchestration across pipeline layers         |

---

## 🗂️ Folder Structure

```bash
.
├── notebooks/
│   ├── Bronze_Layer.ipynb     # Incremental load using Autoloader
│   ├── Parameter.ipynb
│   ├── Silver_Customers.ipynb # Cleansing, deduplication, logic
│   ├── Silver_Orders.py
│   ├── Silver_Products.ipynb
│   ├── Silver_Regions.ipynb
│   ├── Gold_Customers.ipynb        # Dimension and Fact tables (SCD1)
│   ├── Gold_Products.ipynb
│   ├── Gold_Orders.ipynb
│   └── scd_dimensional_dlt.py            # DLT pipeline for SCD Type 2
│   └── Databricks ETE Project.dbc

│
├── orchestrated/
│   └── dlt_pipeline_yaml_code        # ADF pipeline export
│   └── Orchestrated Job Python Code

├── data/
│   └── sample-files/                     # Sample Parquet files
│       ├── customer_first.parquet
│       └── customers_second.parquet
│       └── orders_first.parquet
│       └── orders_second.parquet
│       └── products_first.parquet
│       └── products_second.parquet
│       └── regions.parquet
│
├── images/
│   ├── architecture-diagram.png
│   ├── adf-pipeline.png
│   ├── orchestrated-job-screenshot.png
│   └── dlt-pipeline-screenshot.png
│   └── unity-data-catalog-screenshot.png
│
└── README.md
