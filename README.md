.
├── notebooks/
│   ├── source_to_bronze_loader.ipynb     # Uses Autoloader, parameterized
│   ├── bronze_to_silver_transforms.ipynb # Cleansing, deduplication, null handling
│   ├── silver_to_gold_facts.ipynb        # Fact table creation
│   └── scd_dimensional_dlt.py            # DLT pipeline for SCD Type 2
│
├── pipelines/
│   └── data_factory_pipeline.json        # ADF pipeline export
│
├── data/
│   └── sample-files/                     # Sample Parquet files
│
├── images/
│   ├── architecture-diagram.png
│   ├── adf-pipeline.png
│   ├── orchestrated-job-screenshot.png
│   └── dlt-pipeline-screenshot.png
│
└── README.md
