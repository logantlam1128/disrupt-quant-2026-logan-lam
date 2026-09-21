# Disrupt Quant — 2026 Quantitative  Challenge

Markets rarely tell you which variables matter, which relationships will persist, or whether a pattern represents genuine structure rather than noise. Approach this unfamiliar multi-asset market as a quantitative researcher: develop a systematic strategy supported by evidence, disciplined validation, and sound risk management.

**Released:** Thursday, September 17, 2026  
**Deadline:** Sunday, September 20, 2026 at 11:59 PM Eastern Time

The challenge is designed for approximately **4–6 hours of focused work**. You are not expected to spend the entire three-day window working on it. The window lets you work around academic and personal commitments.

## Start here

Use Python 3.12 or 3.13; the evaluation environment uses Python 3.13. No GPU or container software is required on your laptop.

```bash
# Clone the challenge repository using the URL in your invitation,
# or unzip the supplied candidate archive and enter its directory.
cd Disrupt_Quant_2026_Challenge
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python starter/backtester.py
```

The command evaluates the equal-weight example on development data and writes metrics, daily returns and six diagnostic plots to `results/development/`.

1. Read [CHALLENGE.md](CHALLENGE.md), [RULES.md](RULES.md), and the [data dictionary](data/data_dictionary.md).
2. Research development data and edit **the root `strategy.py`**.
3. Freeze your approach before inspecting validation performance. Run validation explicitly:

```bash
python starter/backtester.py --split validation
python starter/backtester.py --split validation --cost-multiplier 1.5
python validate_submission.py --starter-check
```

4. Write a research note of at most two pages as `research_note.pdf` and update this README with reproduction instructions and AI disclosure.
5. Run `python validate_submission.py`. Submit your private repository URL and full 40-character commit SHA through the form linked in your invitation. Grant access to the reviewer account specified in that invitation.

Sophisticated machine-learning models are not inherently preferred. A simple strategy supported by strong reasoning, robust validation, and thoughtful risk management may score better than a complex model.

Your final ranking will not be determined solely by P&L or Sharpe ratio. We care about how you think, test hypotheses, manage risk, and support conclusions with evidence.

## Your submission README

Replace or extend this section:

- Candidate name: Logan Lam
  
- Strategy name and 2–3 sentence summary: Inverse Volatility Defensive Allocation. A long-only, fully-invested strategy that allocates more capital to calmer assets and less to volatile ones, based on realized_vol_20d, rather than attempting to predict return direction.
  
- Reproduction command and environment:
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 starter/backtester.py --strategy strategy.py --split development
python3 starter/backtester.py --strategy strategy.py --split validation

- Development and validation metrics, with dates:
  - Development (Jan 1, 2021 – Jun 28, 2024, 910 sessions): total return 14.3%, annualized return 3.8%, Sharpe 0.38, Sortino 0.61, max drawdown -10.8%, average daily turnover 2.3%, cumulative transaction costs 1.0% of NAV.
  - Validation (Jul 1 – Dec 31, 2024, 132 sessions): total return -1.9%, annualized return -3.6%, Sharpe -0.27, Sortino -0.39, max drawdown -4.3%, average daily turnover 3.7%, cumulative transaction costs 0.24% of NAV.
    
- Important assumptions and known limitations: Volatility-based weighting manages risk magnitude, not direction. It cannot distinguish a stable, slowly-declining asset from a stable, flat/rising one. Validation period showed a loss, with only 132 sessions. This is not conclusive evidence against the approach, but is disclosed honestly. After viewing the initial validation result, a stronger (non-dampened) volatility tilt was also tested and found to perform similarly. The dampened version was retained for its lower turnover and cost. Additionally, No formal equal-weight baseline comparison was run. 
  
- AI tools used: Claude
  
- How they were used: Used throughout as a research sounding board and coding tutor, explaining quant/finance concepts and terminology, reviewing my hypothesis-testing approach and helping interpret results, helping debug environment/file-path issues. All hypotheses tested, interpretation of results, and the final strategy design decisions (long-only, fully invested, inverse-volatility tilt, choice between tilt strengths) were made by me. Claude wrote/debugged code implementing logic I specified rather than originating the strategy itself.

Only documentation, the example, and market observations are provided. Any explanatory research examples in `starter/` demonstrate the API; they are not trading recommendations.
