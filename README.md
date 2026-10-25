# Electric Vehicle Market Performance & Insights

A Tableau data analytics project that analyses an electric vehicle (EV) market dataset (200,000 rows, 37 columns) and presents the results as an interactive dashboard, a data story, and a Flask web app that embeds both.

## Live Tableau Public links

- [EV Market Dashboard](https://public.tableau.com/app/profile/janhvi.sisodiya/viz/ElectricvehicleMarketPerformanceandInsights/EVMarketDashboard)
- [Advanced Analysis](https://public.tableau.com/app/profile/janhvi.sisodiya/viz/ElectricvehicleMarketPerformanceandInsights/AdvancedAnalysis)
- [Data Story](https://public.tableau.com/app/profile/janhvi.sisodiya/viz/ElectricvehicleMarketPerformanceandInsights/Story1)

## Dataset

Electric Vehicle (EV) Market Classification Dataset on Kaggle (author: Harish Reddy). The CSV file is not included in this repository because of its size. Download `ev_market_train.csv` from Kaggle to reproduce the Tableau workbook.

## What is inside

- 16 worksheets: bar charts, pie, donut, line, heatmap, map and KPI cards
- 3 calculated fields: Revenue USD, Price per km of Range, Rating Level
- Filters: Market Region, Category, Manufacturing Country, Top 10 Manufacturers
- 2 dashboards and a 6-slide data story with recommendations
- Flask app that embeds the dashboards and story in three tabs

## Repository structure

```
.
├── README.md
├── docs/
│   └── EV_Market_Performance_Insights_-_Project_Documentation_updated.pdf
└── ev_flask_app/
    ├── app.py
    ├── requirements.txt
    └── templates/
        └── index.html
```

## Run the Flask app locally

```
cd ev_flask_app
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser. The page has three tabs: Dashboard, Advanced Analysis and Story.

## Documentation

Step-by-step development procedure, calculated fields, insights, recommendations and performance testing are in the PDF inside the `docs` folder.

## Tools

Tableau Public, Python 3, Flask, HTML/CSS/JavaScript.
