
import re
from collections import Counter

# -----------------------------------
# TASK - Email extraction with regex
# -----------------------------------

text = '''
asha.sharma@codetrade.io wrote to ravi_k99@gmail.com
meera.p+work@company.co.in, phone 022-2555-1234
dev@sub.domain.example.org and +91 98765 43210
not.an.email@ nor @nothing.com -- watch these
'''

# -----------------------------------
# 1. Extract every email address
# -----------------------------------

email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

emails = re.findall(email_pattern, text)

print("Email addresses:")
for email in emails:
    print(email)

print("Total emails:", len(emails))


# -----------------------------------
# 2. Extract phone numbers
# -----------------------------------

phone_pattern = r'(?:\+91[- ]?)?[6-9]\d{4}[- ]?\d{5}|\b0\d{2,4}[- ]?\d{3,4}[- ]?\d{4}\b'

phones = re.findall(phone_pattern, text)

print("\nPhone numbers:")
for phone in phones:
    print(phone)


# -----------------------------------
# 3. Split email into username and domain
# -----------------------------------

email_parts_pattern = r'([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Za-z]{2,})'

email_parts = re.findall(email_parts_pattern, text)

print("\nUsername and domain:")
for username, domain in email_parts:
    print("Username:", username)
    print("Domain:", domain)


# -----------------------------------
# 4. Count emails by domain
# -----------------------------------

domains = [domain for username, domain in email_parts]

domain_counts = Counter(domains)

print("\nEmail count by domain:")
for domain, count in domain_counts.items():
    print(domain, ":", count)
