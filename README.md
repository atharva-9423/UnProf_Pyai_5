# UnProf_Pyai_5

<div align="center">

# 🔍 Text Information Extractor

**A regex-powered CLI tool that extracts emails, phone numbers, and dates from raw text.**

`Python 3` · `re module` · `Phase 1 — Day 5`

</div>

---

## 📖 Overview

This tool scans any block of text and pulls out structured information — email addresses, phone numbers, and dates — using regular expressions. It also formats raw phone numbers into a clean, readable layout.

Built as part of the **Python Intermediate** track, focused on `re`, pattern matching, groups, and text substitution.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📧 Email Extraction | Finds all valid email addresses in any text |
| 📱 Phone Extraction | Detects multiple formats — `+91 98765 43210`, `(022) 123-4567`, `9876543210` |
| 📅 Date Extraction | Matches `DD/MM/YYYY`, `YYYY-MM-DD`, and `Month DD, YYYY` |
| 🔧 Phone Formatting | Cleans raw numbers into a consistent, readable format |
| 🖥️ Interactive CLI | Paste your own text or run the built-in sample |

---

## ⚙️ Installation & Usage

No external dependencies — uses Python's built-in `re` module only.

```bash
python text_extractor.py
```

You'll see a simple menu:

```
===== MENU =====
1. Enter text manually
2. Use sample text
3. Exit
```

---

## 🧪 Example

**Input:**
```
Contact me at atharva@gmail.com or call +91 9876543210.
Meeting scheduled for August 10, 2025.
```

**Output:**
```
📧 Emails Found (1):
    • atharva@gmail.com

📱 Phone Numbers Found (1):
    • Raw     : +91 9876543210
      Cleaned : +91 98765-43210

📅 Dates Found (1):
    • August 10, 2025
```

---

## 🧩 Regex Patterns

| Pattern | Purpose | Matches |
|---|---|---|
| `EMAIL_PATTERN` | Email detection | `name@domain.com` |
| `PHONE_PATTERN` | Phone detection | Country codes, brackets, dashes, spaces |
| `DATE_PATTERN` | Date detection | Numeric, ISO, and written-month formats |

**Core regex concepts used:**
- `findall()` → collects every match in the text
- `search()` → checks if at least one match exists
- `sub()` → reformats raw phone digits into a clean pattern
- **Groups `()`** → isolate parts of a match (e.g., country code vs. number)
- **Alternation `|`** → match one of several date formats
- **Non-capturing groups `(?:...)`** → group month-name options without storing them separately

---

## 📁 Project Structure

```
.
├── text_extractor.py   # Main script
├── README.md           # This file
└── LINKEDIN-POST       # linkedin post url
```

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Module:** `re` (built-in, no installation needed)

---

<div align="center">

Built during **Phase 1 – Python Intermediate**, Day 5: *Regex & Text Processing*

</div>
