# 📊 Social Media Trend Analysis 

This project analyzes sentiment across multiple social media platforms (Reddit, Instagram, and Facebook) and visualizes the insights using Power BI.

---

## 📚 About the Project

The goal of this project is to understand public sentiment by analyzing real-world social media data.  
- **Reddit** was specifically chosen because it represents authentic, community-driven discussions, providing rich and unbiased sentiment data.  
- **Instagram** and **Facebook** were included to broaden the perspective by covering more visual and social interaction-driven platforms.

### ❌ Why Twitter Was Not Used:
Twitter data was **initially considered**, but later **excluded** because:
- Twitter’s API access and data policies are now **very restricted** and **paid** (not free for public projects).
- It was **difficult to obtain relevant and sufficient data** under the project constraints.
- Also, Twitter posts are very short (limited character count), which **may not provide deeper sentiment** compared to Reddit posts.

---

## 💾 Dataset

- **Source:** Extracted posts from Reddit, Instagram, and Facebook.
- **File Used:** `Processed_Social_Media_Final.csv`
- **Fields Available:**
  - Platform
  - Post Text
  - Sentiment (Positive / Negative / Neutral)
  - Date/Time



---

## 🛠️ Tech Stack

- **Power BI** - For Data Visualization
- **CSV Files** - As the primary data source
- *(Optional: Python for data preprocessing)*

---

## 📈 Dashboard Features

- ✅ Total number of posts across all platforms
- ✅ Sentiment distribution (Positive, Negative, Neutral)
- ✅ Sentiment trend over time (line charts)
- ✅ Platform-wise sentiment comparison (bar charts, pie charts)
- ✅ Slicers/Filters to explore specific platforms or sentiments

---

## 🚀 How to Use

1. Clone or download this repository.
2. Open **Power BI Desktop**.
3. Load the file `Processed_Social_Media_Final.csv`.
4. Create or import the visuals as described in the layout.
5. Interact with slicers and explore the dashboard!

---

## 📂 Project Structure

| Folder/File                     | Description |
|----------------------------------|-------------|
| `/data/Processed_Social_Media_Final.csv` | Final cleaned dataset used in the dashboard |
| `/dashboard/`                   | Screenshots, PBIX file (Power BI file) |
| `/readme_assets/`                | Any supporting images or diagrams used in the README |
| `README.md`                     | Project description |

---

## 🎯 Conclusion

This project highlights how data from multiple social media platforms can be combined, processed, and visualized to extract real-world insights.  
The dashboard allows quick exploration of public opinions, trends, and sentiment distribution across platforms, helping businesses and researchers make data-driven decisions.

---

> **Special Note:**  
> Reddit was preferred for its depth and authenticity of discussions.  
> Twitter was skipped due to API restrictions and data limitations.

---
