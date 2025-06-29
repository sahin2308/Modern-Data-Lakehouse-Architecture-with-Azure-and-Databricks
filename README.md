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
│   ├── source_to_bronze_loader.ipynb     # Incremental load using Autoloader
│   ├── bronze_to_silver_transforms.ipynb # Cleansing, deduplication, logic
│   ├── silver_to_gold_facts.ipynb        # Dimension and Fact tables (SCD1)
│   └── scd_dimensional_dlt.py            # DLT pipeline for SCD Type 2
│
├── pipelines/
│   └── data_factory_pipeline.json        # ADF pipeline export
│
├── data/
│   └── sample-files/                     # Sample Parquet files
│       ├── sample_file_1.parquet
│       └── sample_file_2.parquet
│
├── images/
│   ├── architecture-diagram.png
│   ├── adf-pipeline.png
│   ├── orchestrated-job-screenshot.png
│   └── dlt-pipeline-screenshot.png
│
└── README.md
