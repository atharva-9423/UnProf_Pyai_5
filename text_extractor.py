
import re

# ── Regex Patterns ──────────────────────────────────────────────

EMAIL_PATTERN = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

PHONE_PATTERN = r'(\+?\d{1,3}[\s\-]?)?(\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{4}|\d{10})'

DATE_PATTERN = (
    r'\b(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4})'   # DD/MM/YYYY or DD-MM-YYYY
    r'|(\d{4}[\/\-]\d{2}[\/\-]\d{2})'           # YYYY-MM-DD (ISO format)
    r'|(\d{1,2}\s+(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?'
    r'|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?'
    r'|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4})'  # 12 January 2024
    r'|((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?'
    r'|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?'
    r'|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},?\s+\d{4})'  # January 12, 2024
    r'\b'
)

# ── Extractor Functions ──────────────────────────────────────────

def extract_emails(text):
    """Extract all email addresses from text."""
    return re.findall(EMAIL_PATTERN, text)


def extract_phones(text):
    """Extract and validate phone numbers with various formats."""
    matches = re.findall(PHONE_PATTERN, text)
    phones = []
    for match in matches:
        full = ''.join(match).strip()
        if len(re.sub(r'\D', '', full)) >= 10:
            phones.append(full)
    return phones


def extract_dates(text):
    """Extract dates in multiple formats (DD/MM/YYYY, YYYY-MM-DD, Month DD YYYY)."""
    matches = re.findall(DATE_PATTERN, text, re.IGNORECASE)
    dates = []
    for match in matches:
        date = next((m for m in match if m), None)
        if date:
            dates.append(date.strip())
    return dates


def clean_phone(phone):
    """
    Format phone numbers to a readable format.
    - 10 digits → (XXX) XXX-XXXX
    - 12+ digits → +XX XXXXX-XXXXX
    """
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 10:
        return re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', digits)
    elif len(digits) == 12:
        return re.sub(r'(\d{2})(\d{5})(\d{5})', r'+\1 \2-\3', digits)
    return phone


def contains_sensitive_info(text):
    """Check if text contains emails or phone numbers."""
    if re.search(EMAIL_PATTERN, text) or re.search(PHONE_PATTERN, text):
        return True
    return False


# ── Display Results ──────────────────────────────────────────────

def display_results(text):
    """Display extracted emails, phones, and dates in formatted output."""
    print("\n" + "=" * 45)
    print("        🔍 EXTRACTION RESULTS")
    print("=" * 45)

    if not contains_sensitive_info(text):
        print("  ⚠️  No recognizable data found in the text.")
        print("=" * 45)
        return

    emails = extract_emails(text)
    print(f"\n  📧 Emails Found ({len(emails)}):")
    print("  " + "-" * 40)
    if emails:
        for email in emails:
            print(f"    • {email}")
    else:
        print("    None found.")

    phones = extract_phones(text)
    print(f"\n  📱 Phone Numbers Found ({len(phones)}):")
    print("  " + "-" * 40)
    if phones:
        for phone in phones:
            cleaned = clean_phone(phone)
            print(f"    • Raw     : {phone}")
            print(f"      Cleaned : {cleaned}")
    else:
        print("    None found.")

    dates = extract_dates(text)
    print(f"\n  📅 Dates Found ({len(dates)}):")
    print("  " + "-" * 40)
    if dates:
        for date in dates:
            print(f"    • {date}")
    else:
        print("    None found.")

    print("\n" + "=" * 45)


# ── Sample Text ──────────────────────────────────────────────────

SAMPLE_TEXT = """
Hello, my name is Atharva. You can reach me at atharva@gmail.com
or call me on +91 9876543210. My colleague Sara can be contacted
at sara.patil@company.org or (022) 123-4567.

Our project deadline is 25/06/2025 and the kickoff meeting was on
2024-01-15. The final review is scheduled for August 10, 2025.

Feel free to also email support@unprof.io for any queries.
"""

# ── Main Menu ────────────────────────────────────────────────────

def main():
    """Main menu loop for the text extractor."""
    print("🔍 Text Information Extractor")
    print("Extracts emails, phone numbers & dates from any text.\n")

    while True:
        print("===== MENU =====")
        print("1. Enter text manually")
        print("2. Use sample text")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            print("\nPaste your text below. Type 'END' on a new line when done:")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                lines.append(line)
            text = "\n".join(lines)
            if text.strip():
                display_results(text)
            else:
                print("⚠️  No text provided.\n")

        elif choice == "2":
            print("\n📄 Sample Text:")
            print("-" * 45)
            print(SAMPLE_TEXT)
            display_results(SAMPLE_TEXT)

        elif choice == "3":
            print("✅ Goodbye!")
            break

        else:
            print("❌ Invalid choice! Enter 1-3.\n")


if __name__ == "__main__":
    main()
      
