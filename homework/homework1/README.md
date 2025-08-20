# ETF Premium/Discount and Market Liquidity Analysis  
**Stage:** Problem Framing & Scoping (Stage 01)  

---

## Problem Statement  
Exchange-Traded Funds (ETFs) often trade at prices that deviate from their Net Asset Value (NAV), creating a premium or discount. This phenomenon becomes more pronounced during periods of low liquidity or high market volatility, potentially leading to arbitrage opportunities but also systemic risks.  

This project aims to investigate the **relationship between ETF premiums/discounts and market liquidity**, identify the main drivers of deviations, and, where possible, predict conditions under which premiums or discounts may widen. This analysis is highly relevant for portfolio managers and market makers when making trading and risk management decisions in stressed market environments.  

---

## Stakeholder & User  
**Primary Stakeholders:**  
- Portfolio managers  
- Market makers  

**Users:**  
- Quantitative researchers  
- Data analysts  

**User Needs:**  
- Quantitative analysis of the historical relationship between ETF premiums/discounts and liquidity indicators  
- Early-warning signals for widening premiums/discounts  
- Decision-support artifacts such as reports or visualizations  

---

## Useful Answer & Decision  
- **Type:** Descriptive + Predictive (with potential for Causal analysis)  
- **Outputs Include:**  
  - Historical correlation between premiums/discounts and liquidity metrics  
  - Predictive models for widening premiums under certain market conditions  
- **Deliverables:**  
  - Metrics: premium/discount ratio, bid-ask spread, trading volume  
  - Artifacts: charts, dashboards, written reports  

---

## Assumptions & Constraints  
- ETF NAV and trading data are publicly available (e.g., Yahoo Finance, ETF.com, SEC filings)  
- Liquidity metrics (e.g., trading volume, bid-ask spread) reasonably reflect market conditions  
- Extreme market interventions (e.g., trading halts, policy shocks) are excluded from the scope  
- Computations will be limited to a personal workstation  

---

## Known Unknowns / Risks  
- Missing data or delayed NAV updates  
- Regulatory or structural changes in ETF market-making rules  
- Premiums/discounts may be influenced by multiple drivers (e.g., flows, costs of arbitrage), not just liquidity  
- Models may fail during extreme market stress  

---

## Lifecycle Mapping  

| Goal | Stage | Deliverable |  
|------|-------|-------------|  
| Understand the relationship between ETF premiums/discounts and liquidity | Problem Framing & Scoping (Stage 01) | Scoping paragraph, stakeholder memo |  
| Collect ETF price, NAV, and trading data | Data Acquisition & Processing | Cleaned datasets in `/data/` |  
| Analyze the relationship between premiums/discounts and liquidity | Modeling | Analysis scripts in `/src/`, notebooks in `/notebooks/` |  
| Deliver visualizations and insights | Reporting | Charts and reports in `/docs/` |  

---

## Repo Plan  
**Folder Structure:**  
- `/data/` → ETF NAV and trading data (raw and processed)  
- `/src/` → Scripts and functions (premium/discount calculation, regression, etc.)  
- `/notebooks/` → Exploratory analysis, correlation studies, predictive modeling  
- `/docs/` → Stakeholder memo, slides, reports  

**Update Cadence:** Initial framing commit, followed by updates at the completion of each stage  
