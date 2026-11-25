"""Create four sample charts in one figure (bonus: plt.subplots(2, 2))."""

from pathlib import Path
import matplotlib.pyplot as plt

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 18, 15, 23, 27, 31]
expenses = [8, 11, 10, 14, 16, 19]
study_hours = [2, 3, 2.5, 4, 4.5, 5]
scores = [55, 62, 60, 72, 78, 85]
categories = ["Python", "Git", "Data", "Charts"]
time_spent = [40, 25, 20, 15]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("AI Training Week 1 — Chart Dashboard", fontsize=16)

axes[0, 0].plot(months, sales, marker="o", label="Sales")
axes[0, 0].plot(months, expenses, marker="s", label="Expenses")
axes[0, 0].set_title("Sales and Expenses")
axes[0, 0].set_ylabel("Units")
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].bar(months, study_hours)
axes[0, 1].set_title("Study Hours")
axes[0, 1].set_ylabel("Hours")

axes[1, 0].scatter(study_hours, scores)
axes[1, 0].set_title("Study Hours vs Test Score")
axes[1, 0].set_xlabel("Study hours")
axes[1, 0].set_ylabel("Test score")
axes[1, 0].grid(True, alpha=0.3)

axes[1, 1].pie(time_spent, labels=categories, autopct="%1.1f%%", startangle=90)
axes[1, 1].set_title("Training Time Distribution")

fig.tight_layout()
output_file = OUTPUT_DIR / "four_charts.png"
fig.savefig(output_file, dpi=150, bbox_inches="tight")
print(f"Chart saved to: {output_file}")
plt.show()
