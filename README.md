# Global Price Tracker

A lightweight, automated pipeline that tracks and documents the retail costs of items across different countries. The system runs fully in the cloud via GitHub Actions, pulling the latest macroeconomic index data daily and committing the structured updates back to this repository.

## 📁 Repository Structure

```text
├── .github/workflows/
│   └── run_scraper.yml    # GitHub Actions cron scheduler
├── data/
│   └── global_prices.csv  # Auto-generated dataset (updated daily)
├── get_prices.py          # Python extraction script
├── requirements.txt       # App dependencies
└── README.md              # Documentation
```

## ⚙️ How It Works

1. **Automation:** A GitHub Actions workflow triggers automatically every day at midnight (UTC).
2. **Data Fetching:** The Python environment spins up, runs `get_prices.py`, and extracts normalized local currency and USD prices globally.
3. **Storage:** The script saves the cleaned dataset into `data/global_prices.csv`.
4. **Commit:** The GitHub runner securely commits the updated CSV back to the master branch using a repository write permission payload.

## 🚀 Local Setup & Execution

If you want to test or run this tracker locally on your own machine, follow these steps:

### Prerequisites
Make sure you have Python 3.8+ installed on your system.

### 1. Clone the repository
```bash
git clone https://github.com
cd YOUR_REPO_NAME
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the tracking script
```bash
python get_prices.py
```
After the script finishes executing, you will find the updated prices inside the `data/` directory.

## 🛠️ Deployment Configuration (GitHub Actions)

To ensure the automated cloud runner has permission to push the newly fetched data back to this repository:

1. Navigate to your repository **Settings**.
2. Select **Actions** -> **General** from the left sidebar menu.
3. Scroll down to **Workflow permissions**.
4. Check the box for **Read and write permissions**.
5. Save changes.
