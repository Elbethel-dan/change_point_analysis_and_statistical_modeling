# Brent Oil Price Event Impact Analysis

## Project Overview
This project analyzes how major global political and economic events affect Brent crude oil prices. Conducted in the context of Birhan Energies’ consulting work, the goal is to generate data-driven insights that help investors, policymakers, and energy companies better understand price volatility, structural market shifts, and risk periods in the global oil market.

Brent oil prices are highly sensitive to geopolitical conflicts, macroeconomic shocks, pandemics, and coordinated supply decisions by oil-producing countries. By combining time-series analysis with event-based reasoning, this project aims to identify when significant market changes occur and how they align with real-world events.

---

## Task 1: Laying the Foundation for Analysis

### Objective
Establish a robust analytical foundation by understanding the data, defining the analysis workflow, and compiling relevant global events that may influence Brent oil prices.

### Key Activities
- Defined a clear end-to-end data analysis workflow, from data loading to insight generation.
- Conducted exploratory time-series analysis to examine trends, volatility patterns, and structural behavior in Brent oil prices.
- Tested for stationarity using the Augmented Dickey-Fuller (ADF) test, confirming that price levels are non-stationary while log returns are stationary.
- Analyzed rolling volatility to identify periods of heightened market uncertainty.
- Compiled a structured CSV file of major global events (geopolitical, economic, OPEC-related, and pandemic-related) with approximate start dates and expected price impact direction.
- Documented key assumptions and limitations, emphasizing the distinction between identifying statistical correlations and proving causal relationships.

### Outputs
- A documented analysis workflow and methodological overview.
- A task-compliant event dataset (CSV) containing 10–15 major global events.
- Initial visualizations highlighting trends, volatility clustering, and event-aligned market behavior.

Task 1 provides the analytical and conceptual groundwork for subsequent change point modeling and interactive visualization in later stages of the project.

----

## How to Reproduce This Project

### Requirements
- Python 3.9 or later
- All required Python packages are listed in `requirements.txt`

### Steps
1. **Clone the repository**
   ```bash
        git clone https://github.com/Elbethel-dan/change_point_analysis_and_statistical_modeling.git
    ```

2. **Set up the Python environment**
    ```bash
        python -m venv venv
        source venv/bin/activate   # On Windows: venv\\Scripts\\activate
        pip install -r requirements.txt
    ```