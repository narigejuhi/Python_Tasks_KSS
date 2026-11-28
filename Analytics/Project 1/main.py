##
##Analytics - Q1: Railway Gauges
##Covers Scenarios 1-5: cleaning -> analysis -> visualization -> PDF report
##Run:  python main.py
##Needs: pandas numpy matplotlib reportlab
##
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")          # save graphs without opening a window
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(BASE, "railway_gauges.csv")
GRAPHS = os.path.join(BASE, "graphs")
os.makedirs(GRAPHS, exist_ok=True)
plt.style.use("ggplot")
results = {}                   # stores findings for the PDF report

# ------------------------------------------------------------------
# SCENARIO 1: Basic Data Loading & Cleaning
# ------------------------------------------------------------------
'''
You are given a CSV file containing railway gauge data. 
Tasks: 
1. Load the dataset into a Pandas DataFrame. 
2. Display the first 5 rows and column names. 
3. Check for missing values and replace them with 0. 
4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.
'''

print("=" * 60, "\nSCENARIO 1: Data Loading & Cleaning\n" + "=" * 60)
df = pd.read_csv(CSV)
print("First 5 rows:\n", df.head())
print("\nColumn names:", list(df.columns))

print("\nMissing values before cleaning:\n", df.isnull().sum())
results["missing_before"] = int(df.isnull().sum().sum())
df = df.fillna(0)

gauge_cols = ["Broad Gauge", "Metre Gauge", "Narrow Gauge", "Total"]
for col in gauge_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
print("\nData types after conversion:\n", df.dtypes)

# Year is like "1964-65" -> keep label, and make a numeric start year
df["Start_Year"] = df["Year"].str[:4].astype(int)
results["rows"] = len(df)
results["first_year"], results["last_year"] = df["Year"].iloc[0], df["Year"].iloc[-1]

# ------------------------------------------------------------------
# SCENARIO 2: Simple Visualization
# ------------------------------------------------------------------
'''
You want a quick understanding of total railway track growth. 
Tasks: 
1. Extract Year and Total columns. 
2. Plot a line graph showing Total tracks over years. 
3. Add: 
○ Title 
○ X and Y labels 
4. Identify whether the trend is increasing or decreasing.
'''



print("\n" + "=" * 60, "\nSCENARIO 2: Total Track Growth\n" + "=" * 60)
plt.figure(figsize=(12, 6))
plt.plot(df["Year"], df["Total"], marker="o", color="tab:blue")
plt.title("Growth of Total Railway Network Over Time")
plt.xlabel("Year")
plt.ylabel("Total Track Length")
plt.xticks(df["Year"][::3], rotation=45)   # every 3rd label so they don't overlap
plt.tight_layout()
plt.savefig(os.path.join(GRAPHS, "scenario2_total_line.png"), dpi=150)
plt.close()

first_total, last_total = df["Total"].iloc[0], df["Total"].iloc[-1]
trend = "INCREASING" if last_total > first_total else "DECREASING"
results.update(first_total=int(first_total), last_total=int(last_total), trend=trend,
               min_total=int(df["Total"].min()),
               min_total_year=df.loc[df["Total"].idxmin(), "Year"],
               max_total=int(df["Total"].max()),
               max_total_year=df.loc[df["Total"].idxmax(), "Year"])
print(f"Total went from {first_total} ({results['first_year']}) to {last_total} "
      f"({results['last_year']}) -> overall trend is {trend}")
print(f"Lowest: {results['min_total']} in {results['min_total_year']}, "
      f"Highest: {results['max_total']} in {results['max_total_year']}")

# ------------------------------------------------------------------
# SCENARIO 3: Filtering + Bar Chart
# ------------------------------------------------------------------
'''
You are asked to analyze modern railway expansion. 
Tasks: 
1. Filter the dataset for years after 2000. 
2. Select Broad Gauge, Metre Gauge, and Narrow Gauge. 
3. Plot a grouped bar chart comparing all three gauges. 
4. Add legend and proper labels. 
5. Identify which gauge dominates in recent years.
'''

print("\n" + "=" * 60, "\nSCENARIO 3: Years After 2000 - Grouped Bar\n" + "=" * 60)
recent = df[df["Start_Year"] > 2000].reset_index(drop=True)
print(recent[["Year", "Broad Gauge", "Metre Gauge", "Narrow Gauge"]])

x = np.arange(len(recent))
w = 0.27
plt.figure(figsize=(12, 6))
plt.bar(x - w, recent["Broad Gauge"], w, label="Broad Gauge", color="tab:blue")
plt.bar(x,     recent["Metre Gauge"], w, label="Metre Gauge", color="tab:orange")
plt.bar(x + w, recent["Narrow Gauge"], w, label="Narrow Gauge", color="tab:green")
plt.title("Gauge Comparison After 2000")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.xticks(x, recent["Year"], rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(GRAPHS, "scenario3_grouped_bar.png"), dpi=150)
plt.close()

dominant = recent[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]].mean().idxmax()
results["recent_dominant"] = dominant
results["recent_avg"] = recent[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]].mean().round(0).astype(int).to_dict()
print(f"\nDominant gauge after 2000: {dominant}")

# ------------------------------------------------------------------
# SCENARIO 4: Feature Engineering + pie chart
# ------------------------------------------------------------------
'''
You want to analyze the contribution of each gauge type. 
Tasks: 
1. Calculate total sum of each gauge across all years. 
2. Create a new structure (Series/DataFrame) for totals. 
3. Plot a pie chart showing percentage contribution. 
4. Add percentage labels (autopct). 
5. Interpret which gauge contributes the most.
'''


print("\n" + "=" * 60, "\nSCENARIO 4: Gauge Contribution - Pie\n" + "=" * 60)
gauge_totals = df[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]].sum()   # Pandas Series
print(gauge_totals)

plt.figure(figsize=(7, 7))
plt.pie(gauge_totals, labels=gauge_totals.index, autopct="%.1f%%",
        explode=(0.08, 0, 0), startangle=90,
        colors=["tab:blue", "tab:orange", "tab:green"])
plt.title("Percentage Contribution of Each Gauge (All Years)")
plt.savefig(os.path.join(GRAPHS, "scenario4_pie.png"), dpi=150)
plt.close()

share = (gauge_totals / gauge_totals.sum() * 100).round(1)
results["pie_share"] = share.to_dict()
results["pie_top"] = share.idxmax()
print(f"\nShare (%):\n{share}\nLargest contributor: {share.idxmax()}")

# ------------------------------------------------------------------
# SCENARIO 5: Advanced Analysis + Multiple Graphs
# ------------------------------------------------------------------
'''
You are asked to perform a complete analysis of railway trends. 
Tasks: 
1. Create new columns: 
○ % Broad Gauge 
○ % Metre Gauge 
○ % Narrow Gauge 
2. Use NumPy (np.diff) to calculate yearly growth of Total tracks. 
3. Plot: 
○ Line graph for all gauges
○ Stacked bar chart showing composition 
4. Highlight: 
○ Years with highest growth 
○ Decline in any gauge 
5. Provide a final conclusion: 
Is the railway system shifting towards a single dominant gauge?” 
'''

print("\n" + "=" * 60, "\nSCENARIO 5: Advanced Analysis\n" + "=" * 60)
# 1) percentage columns
df["% Broad Gauge"] = df["Broad Gauge"] / df["Total"] * 100
df["% Metre Gauge"] = df["Metre Gauge"] / df["Total"] * 100
df["% Narrow Gauge"] = df["Narrow Gauge"] / df["Total"] * 100
print(df[["Year", "% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]].round(2).head())

# 2) yearly growth using np.diff
growth = np.diff(df["Total"].to_numpy())
growth_years = df["Year"].iloc[1:].to_numpy()     # growth[i] = change into growth_years[i]
top = np.argsort(growth)[::-1][:3]
results["top_growth"] = [(growth_years[i], int(growth[i])) for i in top]
bottom = np.argsort(growth)[:3]
results["top_decline"] = [(growth_years[i], int(growth[i])) for i in bottom]
print("\nYears with highest growth in Total:")
for yr, g in results["top_growth"]:
    print(f"  {yr}: +{g}")
print("Years with biggest drop in Total:")
for yr, g in results["top_decline"]:
    print(f"  {yr}: {g}")

# 3a) line graph of percentage composition
plt.figure(figsize=(12, 6))
plt.plot(df["Start_Year"], df["% Broad Gauge"], marker="o", color="tab:blue", label="% Broad Gauge")
plt.plot(df["Start_Year"], df["% Metre Gauge"], marker="o", color="tab:orange", label="% Metre Gauge")
plt.plot(df["Start_Year"], df["% Narrow Gauge"], marker="o", color="tab:green", label="% Narrow Gauge")
plt.title("Percentage Composition of Each Gauge Over Time")
plt.xlabel("Year")
plt.ylabel("Percentage of Total (%)")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(GRAPHS, "scenario5_percent_line.png"), dpi=150)
plt.close()

# 3b) stacked bar of raw composition
plt.figure(figsize=(12, 6))
plt.bar(df["Start_Year"], df["Narrow Gauge"], label="Narrow Gauge", color="tab:green")
plt.bar(df["Start_Year"], df["Metre Gauge"], bottom=df["Narrow Gauge"],
        label="Metre Gauge", color="tab:orange")
plt.bar(df["Start_Year"], df["Broad Gauge"],
        bottom=df["Narrow Gauge"] + df["Metre Gauge"], label="Broad Gauge", color="tab:blue")
plt.title("Composition of Railway Network by Gauge (Stacked)")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend(loc="lower left")
plt.tight_layout()
plt.savefig(os.path.join(GRAPHS, "scenario5_stacked_bar.png"), dpi=150)
plt.close()

# Extra: yearly growth bar chart, highlighting the best years in green, drops in red
colors = ["tab:green" if g > 0 else "tab:red" for g in growth]
plt.figure(figsize=(12, 6))
plt.bar(growth_years, growth, color=colors)
plt.axhline(0, color="black", linewidth=0.8)
plt.title("Yearly Change in Total Track Length (np.diff)")
plt.xlabel("Year")
plt.ylabel("Change vs Previous Year")
plt.xticks(growth_years[::3], rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(GRAPHS, "scenario5_yearly_growth.png"), dpi=150)
plt.close()

# 4) decline in any gauge: compare each gauge's first vs last value, and by decade
decline = {}
for g in ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]:
    decline[g] = (int(df[g].iloc[0]), int(df[g].iloc[-1]))
results["gauge_change"] = decline
df["Decade"] = (df["Start_Year"] // 10) * 10
decade_metre = df.groupby("Decade")["Metre Gauge"].agg(["first", "last"])
decade_metre["change"] = decade_metre["last"] - decade_metre["first"]
results["metre_worst_decade"] = int(decade_metre["change"].idxmin())
results["metre_worst_change"] = int(decade_metre["change"].min())
print("\nGauge first vs last:", decline)
print(f"Steepest Metre Gauge fall: the {results['metre_worst_decade']}s ({results['metre_worst_change']})")

results["pct_first"] = df[["% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]].iloc[0].round(1).to_dict()
results["pct_last"] = df[["% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]].iloc[-1].round(1).to_dict()
print("\n% share first year:", results["pct_first"])
print("% share last year :", results["pct_last"])
print("\nCONCLUSION: Yes - the network is shifting toward Broad Gauge as the single dominant gauge.")

df.to_csv(os.path.join(BASE, "railway_gauges_cleaned.csv"), index=False)

# ------------------------------------------------------------------
# PDF REPORT
# ------------------------------------------------------------------
def build_report():
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors as C
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Image,
                                    Table, TableStyle, PageBreak, KeepTogether)

    ss = getSampleStyleSheet()
    H1 = ParagraphStyle("H1", parent=ss["Title"], textColor=C.HexColor("#1a56c4"), fontSize=22)
    H2 = ParagraphStyle("H2", parent=ss["Heading2"], textColor=C.HexColor("#c0392b"), spaceBefore=10)
    BODY = ParagraphStyle("B", parent=ss["BodyText"], fontSize=10.5, leading=15)
    CAP = ParagraphStyle("C", parent=BODY, fontName="Helvetica-Oblique", textColor=C.grey)

    def img(name, width=16.5 * cm):
        from PIL import Image as PI
        path = os.path.join(GRAPHS, name)
        w, h = PI.open(path).size
        return Image(path, width=width, height=width * h / w)

    def table(data, widths=None):
        t = Table(data, colWidths=widths, hAlign="LEFT")
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), C.HexColor("#1a56c4")),
            ("TEXTCOLOR", (0, 0), (-1, 0), C.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, C.grey),
            ("FONTSIZE", (0, 0), (-1, -1), 9.5),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [C.white, C.HexColor("#f1f5fb")]),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
        return t

    r = results
    s = []
    s += [Spacer(1, 0.5 * cm), Paragraph("Data Analytics Project: Railway Gauge Trends", H1),
          Paragraph("Dataset: railway_gauges.csv &nbsp;|&nbsp; Tools: Pandas, NumPy, Matplotlib", ss["Normal"]),
          Spacer(1, 0.5 * cm),
          Paragraph("<b>Project goal:</b> analyse how the Broad, Metre and Narrow gauge networks "
                    f"changed between {r['first_year']} and {r['last_year']} "
                    f"({r['rows']} yearly records).", BODY)]

    s += [Paragraph("Scenario 1: Data Loading &amp; Cleaning", H2),
          Paragraph(f"The CSV was loaded into a Pandas DataFrame with columns Year, Broad Gauge, Metre Gauge, "
                    f"Narrow Gauge and Total. Missing values found: <b>{r['missing_before']}</b> (any would have been "
                    "replaced with 0). All gauge columns were converted to numeric types.", BODY),
          Spacer(1, 6)]
    head = [list(df.columns[:5])] + df.iloc[:5, :5].values.tolist()
    s += [table(head, [3 * cm] * 5), Paragraph("First 5 rows of the dataset", CAP)]

    s += [Paragraph("Scenario 2: Total Track Growth", H2), img("scenario2_total_line.png", 14 * cm),
          Paragraph(f"Total track length rose from {r['first_total']} ({r['first_year']}) to {r['last_total']} "
                    f"({r['last_year']}), so the overall trend is <b>{r['trend'].lower()}</b>. It dipped to a low of "
                    f"{r['min_total']} in {r['min_total_year']} and peaked at {r['max_total']} in "
                    f"{r['max_total_year']}.", BODY)]

    s += [PageBreak(), Paragraph("Scenario 3: Gauges After 2000", H2), img("scenario3_grouped_bar.png"),
          Paragraph(f"<b>{r['recent_dominant']}</b> clearly dominates after 2000 (average "
                    f"{r['recent_avg']['Broad Gauge']} vs Metre {r['recent_avg']['Metre Gauge']} and Narrow "
                    f"{r['recent_avg']['Narrow Gauge']}). Metre and Narrow gauge keep shrinking, which points to "
                    "standardisation on Broad Gauge.", BODY)]

    s += [Paragraph("Scenario 4: Overall Gauge Contribution", H2), img("scenario4_pie.png", 9 * cm),
          Paragraph("Across all years: " + ", ".join(f"{k} {v}%" for k, v in r["pie_share"].items()) +
                    f". <b>{r['pie_top']}</b> contributes the most.", BODY)]

    s += [PageBreak(), Paragraph("Scenario 5: Advanced Analysis", H2),
          img("scenario5_percent_line.png", 15 * cm),
          Paragraph("Share of the network (%) in the first vs last year:", BODY)]
    comp = [["Gauge", f"{r['first_year']}", f"{r['last_year']}"]]
    for k in ["% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]:
        comp.append([k, f"{r['pct_first'][k]}%", f"{r['pct_last'][k]}%"])
    s += [table(comp, [5 * cm, 3 * cm, 3 * cm]), Spacer(1, 8),
          img("scenario5_stacked_bar.png", 15 * cm), PageBreak(),
          img("scenario5_yearly_growth.png", 15 * cm)]

    g = [["Highest growth (year)", "Change"]] + [[y, f"+{v}"] for y, v in r["top_growth"]]
    d = [["Biggest drop (year)", "Change"]] + [[y, str(v)] for y, v in r["top_decline"]]
    s += [Spacer(1, 8), table(g, [5 * cm, 3 * cm]), Spacer(1, 8), table(d, [5 * cm, 3 * cm]),
          Spacer(1, 8),
          Paragraph("Using <font name='Courier'>np.diff</font> on the Total column gives the yearly change. "
                    f"Metre Gauge shows the steepest decline, falling from {r['gauge_change']['Metre Gauge'][0]} to "
                    f"{r['gauge_change']['Metre Gauge'][1]}; its sharpest decade was the {r['metre_worst_decade']}s "
                    f"({r['metre_worst_change']}). Narrow Gauge also declined "
                    f"({r['gauge_change']['Narrow Gauge'][0]} to {r['gauge_change']['Narrow Gauge'][1]}), while "
                    f"Broad Gauge grew from {r['gauge_change']['Broad Gauge'][0]} to "
                    f"{r['gauge_change']['Broad Gauge'][1]}.", BODY)]

    s += [Paragraph("Final Conclusion", H2),
          Paragraph("<b>Is the railway system shifting towards a single dominant gauge? Yes.</b> Broad Gauge's share "
                    f"rose from {r['pct_first']['% Broad Gauge']}% to {r['pct_last']['% Broad Gauge']}% while Metre and "
                    "Narrow gauges fell steadily. The total network size stayed fairly stable, so this is mainly "
                    "<i>gauge conversion</i> (Metre/Narrow lines converted to Broad) rather than purely new track. "
                    "The system is consolidating around Broad Gauge.", BODY),
          Paragraph("What I learned", H2),
          Paragraph("Cleaning data and fixing types with Pandas, computing changes with NumPy (np.diff), and "
                    "presenting trends with line, bar, pie and stacked charts in Matplotlib.", BODY)]

    SimpleDocTemplate(os.path.join(BASE, "Railway_Gauge_Report.pdf"), pagesize=A4,
                      leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2 * cm,
                      bottomMargin=2 * cm, title="Railway Gauge Trends").build(s)


try:
    build_report()
    print("\nPDF report created: Railway_Gauge_Report.pdf")
except ImportError:
    print("\nInstall reportlab to build the PDF:  pip install reportlab pillow")

print("All graphs saved in the 'graphs' folder.")
