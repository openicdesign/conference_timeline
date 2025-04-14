
---

# 📊 Project- Conference Timeline Visualizer

This Python script generates a Gantt-style timeline visualization from an Excel file containing project tasks. The resulting chart, saved as `timeline_latest.png`, highlights task durations, start and end dates, and their relative position to today's date.

---

## 📁 Input File

The script expects an Excel file named **`tasks.xlsx`** in the same directory, with the following columns:

| Column Name  | Description                          |
|--------------|--------------------------------------|
| Task Name    | Name or title of the task            |
| Start Date   | When the task starts (YYYY-MM-DD)    |
| End Date     | When the task ends (YYYY-MM-DD)      |
| Location     | Optional label for each task (e.g., team, phase) |

---

## 📈 Features

- Visualizes each task on a horizontal bar (Gantt-style)
- Automatically handles:
  - Tasks in the past (solid-colored bars)
  - Ongoing tasks (colored bars with black outlines)
  - Future tasks (empty bars with colored outlines)
- Shows task durations directly on bars
- Annotates locations next to each task
- Highlights today's date with a red dashed line
- Automatically adjusts the time scale based on project duration

---

## 📦 Requirements

Install the required Python libraries using pip:

```bash
pip install pandas matplotlib openpyxl
```

---

## ▶️ Usage

1. Make sure your Excel file is named `tasks.xlsx` and structured correctly.
2. Run the script:

```bash
python plot_timeline.py
```

If a `timeline_latest.png` already exists, the script will prompt you to rename it to `timeline_old.png`.

---

## 🖼️ Output

- A PNG file named **`timeline_latest.png`** is saved in the same folder.

  ![timeline_latest](https://raw.githubusercontent.com/openicdesign/conference_timeline/main/timeline_latest.png?ts=2)

- Example visualization elements:
  - 📅 Duration labels above each bar
  - 📍 Location labels to the right
  - ⏳ Past, present, and future task color distinction
  - 🔴 Today marker with date label

---

## ✏️ Customization

Feel free to customize:
- Bar colors (currently randomized)
- Date formatting
- Location label styling
- Output filename or figure size

---

## ✅ Example Output

After running the script, you'll see this message:

```
✅ Timeline saved as 'timeline_latest.png'
```

---

## 📌 Notes

- Ensure your Excel dates are properly formatted as `Date` cells.
- The script reverses the task order (most recent at the top) for a more intuitive top-down view.
- You can rename the script file from `plot_timeline.py` to whatever you'd like.

---

Let me know if you'd like a sample `tasks.xlsx` template too!