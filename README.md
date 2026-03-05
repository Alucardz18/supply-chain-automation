# 🚚 Supply Chain Automation Pipeline

An end-to-end data automation project using Python, SQLite, and Power BI.

## 📊 Project Overview
Automated pipeline that ingests raw supply chain data, cleans it, 
stores it in a database, runs SQL analysis, and outputs a summary report.

## 🗂️ Dataset
- **Source:** DataCo Smart Supply Chain Dataset (Kaggle)
- **Size:** 180,519 orders · 50 columns
- **Period:** January 2015 – January 2018

## 🔧 Tech Stack
| Tool | Purpose |
|---|---|
| Python (pandas) | Data cleaning & automation |
| SQLite + SQLAlchemy | Database storage |
| SQL | Business analysis queries |
| Power BI | Interactive dashboard |
| Jupyter Notebook | Exploration & development |

## ⚙️ How It Works
```
Raw CSV → data_cleaning.py → SQLite DB → SQL queries → summary_report.txt
```

## 🚀 How to Run
1. Clone the repo
2. Install dependencies: `pip install pandas sqlalchemy`
3. Run the pipeline: `python scripts/automation_pipeline.py`
4. Check `data/summary_report.txt` for results

## 📈 Key Insights
- **54.8%** of all orders are delivered late
- **First Class** shipping has the worst delay rate at **95.3%**
- **Europe** is the highest revenue market at **$10.9M**
- **Fishing** is the most profitable category at **$756K**
- Order volume dropped sharply after **October 2017**

## 📁 Structure
```
├── data/               ← raw and cleaned datasets
├── notebooks/          ← exploration.ipynb
├── scripts/
│   ├── data_cleaning.py
│   └── automation_pipeline.py
├── sql/
│   └── queries.sql
├── dashboard/
│   └── supply_dashboard.pbix
└── README.md
```