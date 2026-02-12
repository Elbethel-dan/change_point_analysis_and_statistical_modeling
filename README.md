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
## Task 2: Bayesian Change Point Detection

### Objective
Identify statistically significant structural breaks in Brent oil price returns using probabilistic programming, moving beyond subjective event selection to allow the data to reveal its own regime shifts.

### Key Activities
- Prepared daily log return series from raw Brent price data (1987–2022).

- Implemented a Bayesian change point model using PyMC with a discrete uniform prior over all possible switch points.

- Modeled two distinct mean regimes (μ₁, μ₂) with a switch function selecting the appropriate parameter based on temporal index.

- Ran MCMC sampling with 4 chains, 2,000 draws each, and 1,000 warmup iterations.

- Verified convergence using r_hat statistics and examined posterior distributions.

- Mapped the posterior change point index back to calendar date for business interpretation.

- Quantified the magnitude and direction of the estimated structural shift.

### Outputs

- Posterior distribution of the change point (tau) with 94% high density interval.

- Estimated mean daily returns before and after the detected break.

- Convergence diagnostics and trace plots.

- change_point_results.json containing all model parameters for API consumption.

- Visualization of the price series with the Bayesian change point overlaid.

**Key Finding:** The model detected a change point around Day 4,395 (approximately 2004) , though the wide credible interval confirms that Brent oil returns lack a single, dominant structural break. This reinforces that the market is better characterized by multiple, event-driven dislocations rather than one monolithic regime shift.


----
## Task 3: Full-Stack Interactive Dashboard

### Objective
Transform the statistical analysis into an accessible, interactive decision-support tool by building a full-stack web application with Flask backend and React frontend.

### Key Activities
**Backend (Flask):**

- Developed REST API with CORS support for cross-origin requests.

- Created /api/prices endpoint serving Brent historical data with dynamic date range filtering.

- Created /api/events endpoint serving the curated geopolitical event catalog.

- Created /api/changepoint endpoint serving pre-computed Bayesian model results from JSON.

- Created /api/volatility endpoint computing 30-day rolling log-return volatility.

- Implemented efficient data loading using pandas with datetime parsing.

**Frontend (React):**

- Built component-based architecture with dedicated UI modules.

- Implemented api.js service layer using Axios for all backend communication.

- Created PriceChart.jsx using Recharts to visualize price trends, event markers, and change point reference lines.

- Developed Filters.jsx for interactive date range selection.

- Built MetricsPanel.jsx displaying Bayesian statistics including mean before/after and estimated percentage shift.

- Connected all components in App.js with React hooks (useState, useEffect) for state management.

### Outputs

- Fully functional Flask API on port 5000.

- Responsive React dashboard on port 3000.

- Interactive price chart with change point annotation.

- Event-ready architecture for future event marker integration.

- Clean separation of concerns between data, logic, and presentation layers.

**Business Value:** The dashboard enables investors, policymakers, and analysts to explore structural breaks in Brent oil prices dynamically, filter by date ranges, and immediately visualize how Bayesian change point detection aligns with historical geopolitical events.


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

3. Run the Flask API server
    ```bash
        cd backend
        python app.py

    ```

4. Navigate to the frontend directory
    ```bash
        cd ../frontend
        npm install
        npm start
    ```