# PiTE Project

PiTE Project is an academic cryptocurrency analysis workspace focused on signals related to potential **pump-and-dump** behavior.  
The repository combines tweet collection, sentiment analysis, price visualization, and an experimental machine learning model.

## Project Scope

The project is organized into independent modules:

- **Tweet collection** from X/Twitter (via Tweety)
- **Tweet analytics** (tweet volume and engagement over time)
- **Price data download and visualization** (Yahoo Finance + Streamlit)
- **Sentiment vs. price correlation analysis** (NLTK VADER + Streamlit)
- **Machine learning experiments** for risk classification (`0/1/2`)

## Repository Structure

```text
PiTE_Project/
├── Download_tweets/
│   ├── Twitter_scrapper/            # Tweet scraping service + CSV export
│   └── tweets_analysis/             # Streamlit tweet analytics charts
├── Download_and_show_data/
│   ├── main.py                      # Streamlit app for BTC/DOGE/ETH prices
│   ├── yfinance_test/               # Scripts to fetch 1y price history
│   └── streamlit_test/              # Streamlit app from static CSV files
├── Sentiment_correlation_analysis/
│   ├── sentiment_analysis.py        # Sentiment scoring + correlation + UI
│   └── files/                       # Input/output CSV files
└── Machine_learning/
    ├── csv_tweets/                  # Example tweet datasets
    └── ML_model_and_data/           # Model, merged datasets, notebooks
```

## Prerequisites

- Python 3.9+ recommended
- `pip`
- Internet access (for Yahoo Finance and Twitter scraping)

## Installation

Install dependencies per module (there is no single global `requirements.txt`):

```bash
# Price visualization module
pip install -r /home/runner/work/PiTE_Project/PiTE_Project/Download_and_show_data/requirements.txt

# Sentiment/correlation module
pip install -r /home/runner/work/PiTE_Project/PiTE_Project/Sentiment_correlation_analysis/requirements.txt

# Twitter scraping module
pip install -r /home/runner/work/PiTE_Project/PiTE_Project/Download_tweets/Twitter_scrapper/requirements.txt
```

For machine learning notebooks:

```bash
pip install -r /home/runner/work/PiTE_Project/PiTE_Project/Machine_learning/ML_model_and_data/requirement/requirement.txt
```

## How to Run

### 1) Cryptocurrency price dashboard

```bash
cd /home/runner/work/PiTE_Project/PiTE_Project/Download_and_show_data
streamlit run main.py
```

### 2) Sentiment and correlation analysis

```bash
cd /home/runner/work/PiTE_Project/PiTE_Project/Sentiment_correlation_analysis
streamlit run sentiment_analysis.py
```

### 3) Tweet analytics dashboard

```bash
cd /home/runner/work/PiTE_Project/PiTE_Project/Download_tweets/tweets_analysis
streamlit run tweets_analyzer.py
```

### 4) Twitter scraping service

Core scraper logic is in:

`/home/runner/work/PiTE_Project/PiTE_Project/Download_tweets/Twitter_scrapper/twitter_service/twitter_handler.py`

See module details in:

`/home/runner/work/PiTE_Project/PiTE_Project/Download_tweets/Twitter_scrapper/README.md`

## Machine Learning Notes

The ML workflow is notebook-based (`train_model.ipynb`, `use_model.ipynb`) and includes:

- pretrained model file: `model_epoch_307.hdf5`
- merged datasets with required columns:
  - `Close`
  - `compound`
  - `likes`
  - `retweets`

Model output classes are interpreted as:

- `0` – no pump-and-dump risk
- `1` – potential risk
- `2` – high risk

## Important Notes

- This repository is research/academic in nature and contains experimental code and datasets.
- Some scripts are standalone prototypes rather than production-ready services.
- Data files in CSV format are included to help reproduce local experiments quickly.
