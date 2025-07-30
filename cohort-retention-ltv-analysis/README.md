# 🧠 Cohort Retention & LTV Analysis Project

This project is part of a Marketing Analyst portfolio, focusing on **Cohort-based Retention & Lifetime Value (LTV)** analysis for a hypothetical product/service with transaction-level user data.

## 📌 Objective

To understand user behavior over time by grouping them into cohorts (by acquisition date) and evaluating:

- Retention Rate (% of users returning over time)
- Lifetime Value (LTV) per user by cohort
- Strategic insights on monetization & engagement

---

## 🗂️ Folder Structure

```

📁 cohort-ltv-analysis/
│
├── 📊 data/
│   └── cohort\_retention\_data.csv
│
├── 📈 notebooks/
│   └── generate\_mock\_data.py
│
├── 📁 outputs/
│   ├── monthly\_retention\_matrix.png
│   ├── weekly\_retention\_matrix.png
│   ├── monthly\_ltv\_matrix.png
│   └── weekly\_ltv\_matrix.png
│
├── 📁 scripts/
│   └── cohort\_retention\_analysis.ipynb
│
├── .gitnore
├── README.md
└── requirements.txt

````

---

## 🧪 Key Features

- ✅ Automatic cohort generation: Daily, Weekly, Monthly
- 📊 Retention Matrix Visualization: Heatmaps of user stickiness over time
- 💰 LTV Matrix Visualization: Cumulative revenue/user by cohort
- 📍 Strategic Insight Cell: Summarized findings and business recommendations

---

## 🧮 Sample Metrics

> Based on sample dataset (generated):

- **Feb 2024 cohort** shows strongest LTV (~280k) and retention
- **May 2024 cohort** displays high scalability potential (LTV 3x growth in 2 months)
- **Week 06 & 19** cohorts reveal early conversion spikes
- Week 2 post-signup is a **drop-off point** → opportunity for reactivation flows

---

## 📌 How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/pbphuoc3927/cohort-ltv-analysis.git
cd cohort-ltv-analysis
````

2. **Set up the environment**

```bash
pip install -r requirements.txt
```

3. **Run the notebook**

```bash
jupyter notebook notebooks/cohort_ltv_retention_analysis.ipynb
```

---

## 🧠 Tools Used

* `pandas` – data manipulation
* `matplotlib`, `seaborn` – visualizations
* `numpy` – cohort transformations
* `Jupyter Notebook` – analysis environment

---

## 🧩 Potential Extension Ideas

* Add CAC data to calculate **Payback Period**
* Segment LTV by user source/channel (if available)
* Analyze behavioral cohort (based on first action, not signup)

---

## 👤 Author

**Pham Ba Phuoc** – Aspiring Marketing Analyst
- **GitHub:** https://github.com/pbphuoc3927/campaign-performance-report
- **LinkedIn:** https://www.linkedin.com/in/pham-ba-phuoc-61a02527a/

---

## 📄 License

MIT License – feel free to reuse and expand with attribution.