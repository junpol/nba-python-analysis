# 🏀 NBA Stats Correlation Analysis
**Exploring relationships between NBA player stats—built from scratch without Pandas/NumPy to master core Python, data cleaning, and algorithm design!**  
## What Does This Project Do?
1. This project analyzes how different NBA metrics correlate using **raw CSV data**  and a **manually implemented Pearson correlation coefficient**
2. Loads & cleans 2024 NBA season stats from a CSV (handling missing/outlier values).
3. **Calculates correlations**  between:
- 3P% and PPG | Age and MPG | FTA and FT%
- **Validates results** with manual test cases against statistical theory.

**Example!:**

"Players with higher free throw attempts (FTA) tend to have slightly lower FT%, possibly due to pressure or fatigue."

## 🛠️ Why I Built This
1. **Skill Depth**: Avoided Pandas/NumPy to strengthen:
2. **Data wrangling** (parsing raw CSVs, type handling)
3. **Algorithm design** (Pearson coefficient from math formulas)
4. **Testing rigor** (edge cases for correlation logic)
5. **Showcase**: Clean, modular Python with real-world data!

# 🚀 How to Run
bash
git clone https://github.com/junpol/nba-python-analysis.git  
cd nba-python-analysis  
python3 nba_analysis.py  
(CSV file included in /data)
