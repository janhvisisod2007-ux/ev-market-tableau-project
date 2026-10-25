from flask import Flask, render_template

app = Flask(__name__)

# Tableau Public workbook (from your published link)
BASE = "https://public.tableau.com/views/ElectricvehicleMarketPerformanceandInsights"
DASHBOARD_URL = f"{BASE}/EVMarketDashboard"
STORY_URL = f"{BASE}/Story1"
ANALYSIS_URL = f"{BASE}/AdvancedAnalysis"


@app.route("/")
def home():
    return render_template(
        "index.html",
        dashboard_url=DASHBOARD_URL,
        story_url=STORY_URL,
        analysis_url=ANALYSIS_URL,
    )


if __name__ == "__main__":
    app.run(debug=True)
