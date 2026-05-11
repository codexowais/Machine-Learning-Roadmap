# # Day 003 - String Methods and Text Cleaning
#
# Learn: `.lower()`, `.strip()`, `.split()`, `.join()`, `.replace()`, f-strings, and basic text normalization.
#
# Practice: clean a messy list of names and emails.
#
# Output: print cleaned names and emails in a consistent format.
#
# Review: why is text cleaning important before ML?
#

# Code here
names = [
    "  OWAIS SUHAIL ",
    "rIShAn khan",
    " SAMEER  ALI "
]

emails = [
    " OWAIS@GMAIL.COM ",
    "RiShAn123@Yahoo.Com ",
    " SAMEER@OUTLOOK.COM"
]

for name in names:

    cleaned_name = name.strip().lower()

    print(cleaned_name)

print()

for email in emails:

    cleaned_email = email.strip().lower()

    print(cleaned_email)