import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import random

# Load Excel file
file_path = "tasks.xlsx"
df = pd.read_excel(file_path)

# Check for existing timeline image
if os.path.exists("timeline_latest.png"):
    os.rename("timeline_latest.png", "timeline_old.png")
    print("✔️ Auto-renamed previous timeline to 'timeline_old.png'")

    # print("⚠️ 'timeline_latest.png' already exists.")
    # choice = input("Do you want to rename it to 'timeline_old.png'? (y/n): ").strip().lower()
    # if choice == 'y':
    #     os.rename("timeline_latest.png", "timeline_old.png")
    #     print("✔️ Renamed to 'timeline_old.png'")
    # else:
    #     print("❗Please rename or remove 'timeline_latest.png' before proceeding.")
    #     exit()

# Convert dates
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])
df.sort_values(by='Start Date', inplace=True)
df = df[::-1]  # reverse for top-down Gantt

# Function to generate random colors in hex format
def generate_random_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Get the x-axis limits for the plot
x_min = df['Start Date'].min() - pd.Timedelta(days=7)
x_max = df['End Date'].max() + pd.Timedelta(days=10)

# Get today's date
today = pd.Timestamp(datetime.today().date())

for i, row in enumerate(df.itertuples()):
    start_date = row._3
    end_date = row._4
    duration = (end_date - start_date).days + 1
    color = generate_random_color()  # Generate a random color for each task

    # Determine if the bar is before or after today's date
    if end_date < today:
        # Solid color for tasks ending before today
        fill_color = color
        # edge_color = 'black'
        edge_color = color
    elif start_date > today:
        # Empty color with a colored edge for tasks starting after today
        fill_color = 'none'
        edge_color = color
    else:
        # Tasks that span today will be partially filled
        fill_color = color
        edge_color = 'black'

    # Draw the bar
    ax.barh(i, duration, left=start_date, color=fill_color, edgecolor=edge_color, height=0.6)

    # Duration label (on top of the bar)
    ax.text(start_date + pd.Timedelta(days=duration / 2), i - 0.35, f"{duration}d",
            va='bottom', ha='center', fontsize=9, color='black', weight='bold')

    # 📍 Location label (moved further right dynamically)
    padding = max(2, int(duration * 0.1))
    ax.text(end_date + pd.Timedelta(days=padding), i, str(row.Location),
            va='center', ha='left', fontsize=10, color='blue', style='italic')

    # Draw a horizontal dashed line from the leftmost part of the graph to the start date of each task
    ax.hlines(i, x_min, start_date, color='black', linestyle='--', linewidth=0.8)

# Highlight today's date
ax.axvline(today, color='red', linestyle='--', linewidth=1.4, zorder=0)

# Get y-axis limits for positioning
ymin, ymax = ax.get_ylim()

# Display "Today: YYYY-MM-DD" label above the plot
label_offset = (ymax - ymin) * 0.05  # Adjust 5% of the y-range for the label's position
ax.text(today, - label_offset - 0.5, f"Today: {today.strftime('%Y-%m-%d')}",
        color='red', ha='center', va='bottom', fontsize=11, weight='bold')

# Configure axes
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df["Task Name"], fontsize=10, weight='bold')
ax.invert_yaxis()

# Format x-axis: Automatically adjust the interval based on the date range
date_range = df['End Date'].max() - df['Start Date'].min()

# If the date range is small (less than a month), use DayLocator
if date_range <= pd.Timedelta(days=30):
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
elif date_range <= pd.Timedelta(days=180):  # If the range is up to 6 months
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=1))  # Every week
else:  # If the range exceeds 6 months, use MonthLocator
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))  # Every month

ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
plt.xticks(rotation=45, fontsize=9)
ax.set_xlim(x_min, x_max)

# Aesthetics
plt.title("IC Conferences' Timeline", fontsize=16, weight='bold')
plt.xlabel("Date", fontsize=11)
plt.grid(True, axis='x', linestyle='--', linewidth=0.5, alpha=0.6)
plt.tight_layout()

# Save the figure
plt.savefig("timeline_latest.png")
print("✅ Timeline saved as 'timeline_latest.png'")
plt.close()
