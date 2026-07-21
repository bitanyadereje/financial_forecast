#  Forecasting Financial Inclusion in Ethiopia

> **A data-driven forecasting system tracking Ethiopia's digital financial transformation using time series methods.**


##  Overview

This project was developed for **Selam Analytics**, a financial technology consulting firm, as part of the **10 Academy - KAIM 9** challenge. The goal is to forecast Ethiopia's financial inclusion progress on two core dimensions defined by the World Bank's Global Findex Database:

1. **Access** → Account Ownership Rate  
2. **Usage** → Digital Payment Adoption Rate  

The system forecasts these indicators for **2025–2027** to help a consortium of stakeholders (development finance institutions, mobile money operators, and the National Bank of Ethiopia) make data-driven policy and investment decisions.

---

##  Business Context

Ethiopia is undergoing a rapid digital financial transformation:

- **Telebirr** (launched May 2021) has grown to **54+ million users**.
- **M-Pesa** (entered August 2023) has **10+ million users**.
- **P2P digital transfers** have surpassed ATM cash withdrawals for the first time (Oct 2024).

Despite this, the 2024 Global Findex survey shows only **49%** of Ethiopian adults have a financial account—just **3 percentage points higher** than in 2021.

**The consortium needs to understand:**
- What drives financial inclusion in Ethiopia?
- How do events (product launches, policies, infrastructure) affect inclusion?
- How will inclusion evolve in 2025, 2026, and 2027?

---

## Project Structure

```
ethiopia-fi-forecast/
├── .github/workflows/
│   └── unittests.yml          # CI/CD pipeline
├── data/
│   ├── raw/                   # Starter datasets (unchanged)
│   │   ├── ethiopia_fi_unified_data.csv
│   │   └── reference_codes.csv
│   └── processed/             # Enriched & analysis-ready data
│       ├── ethiopia_fi_enriched.csv
│       └── event_impact_matrix.csv
├── notebooks/
│   ├── 01_explore.ipynb       # Task 1 & 2: EDA + 5 Insights
│   ├── 02_impact_modeling.ipynb # Task 3: Event Impact Matrix
│   └── 03_forecasting.ipynb   # Task 4: 2025-2027 Forecasts
├── dashboard/
│   └── app.py                 # Task 5: Streamlit Dashboard
├── reports/
│   └── figures/
│       └── forecast_2025_2027.png
├── src/                       # (Optional) Utility modules
├── tests/                     # Unit tests
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── INTERIM_REPORT.md          # Interim submission report
├── data_enrichment_log.md     # Task 1 enrichment documentation
└── .gitignore
```

---

##  Data Sources & Schema

### Unified Schema
The dataset uses a unified schema where `record_type` indicates row meaning:

| `record_type` | Description |
| :--- | :--- |
| `observation` | Actual measured values (Findex surveys, operator reports, infrastructure data) |
| `event` | Policies, product launches, market entries, milestones |
| `impact_link` | Modeled relationships connecting events to indicators via `parent_id` |
| `target` | Official policy goals (e.g., NFIS-II 60% target) |

### Key Enrichments Added
| Addition | Type | Rationale |
| :--- | :--- | :--- |
| ATM Density (2024) | Observation | Leading indicator for Access |
| Mobile Subscription Penetration (2024) | Observation | Enabler for Usage |
| Telebirr → Mobile Money (+4.75pp) | Impact Link | Actual observed impact |
| Telebirr → Account Ownership (+3.0pp) | Impact Link | Observed partial impact |
| M-Pesa → Digital Usage (+2.0pp) | Impact Link | Comparable evidence |

---

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/bitanyadereje/financial_forecast.git
cd financial_forecast
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Dashboard (Streamlit)
```bash
streamlit run dashboard/app.py
```

---

##  Key Findings (EDA)

| # | Insight | Supporting Evidence |
| :--- | :--- | :--- |
| 1 | **Stagnation Post-2021:** Account ownership grew only +3pp (46%→49%) between 2021–2024, compared to +11–13pp previously. | Growth rate calculations |
| 2 | **Persistent Gender Gap:** Women (36%) lag men (56%) by 20 percentage points. | Findex gender-disaggregated data |
| 3 | **Mobile Money Doubled:** Mobile Money accounts grew from 4.7% (2021) to 9.45% (2024). | Operator & Findex data |
| 4 | **Telebirr Paradox:** 54M+ registrations did not accelerate national account ownership—users already had bank accounts. | Event overlay analysis |
| 5 | **Infrastructure Correlation:** 4G coverage (37.5%→70.8%) aligns with digital payment growth. | Correlation heatmap |

---

##  Event-Impact Matrix

| Event | Account Ownership | Mobile Money | Digital Usage |
| :--- | :--- | :--- | :--- |
| **Telebirr Launch** | +3.0 pp | +4.75 pp | 0.0 |
| **M-Pesa Launch** | 0.0 | 0.0 | +2.0 pp |

*Interpretation: Telebirr drove mobile money adoption, while M-Pesa is expected to drive digital payment usage.*

--

##  Forecasts 2025–2027

| Scenario | 2027 Access | 2027 Usage |
| :--- | :--- | :--- |
| **Pessimistic** | 62.1% | 40.9% |
| **Base** | 63.2% | 41.5% |
| **Optimistic** | 64.2% | 42.1% |

**Bottom Line:** Ethiopia is projected to **exceed** the NFIS-II 60% target by 2027, even under the Pessimistic scenario.

---

##  Dashboard Features

- **Overview:** Key metrics (Account Ownership, Mobile Money, Gender Gap)
- **Trends:** Interactive time series charts with multi-indicator selection
- **Forecasts:** Scenario selector (Base/Optimistic/Pessimistic) with 60% target overlay
- **Inclusion Projections:** Progress toward the NFIS-II 60% target

--

