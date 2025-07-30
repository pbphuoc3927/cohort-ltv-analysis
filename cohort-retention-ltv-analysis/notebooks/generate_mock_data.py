import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Config
NUM_USERS = 1000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 6, 30)
OUTPUT_PATH = r"C:\Users\phuoc\cohort-retention-ltv-analysis\data\cohort_retention_data.csv"

# Ensure output folder exists
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# Generate user signups
user_ids = [f"user_{i}" for i in range(1, NUM_USERS + 1)]
signup_dates = [START_DATE + timedelta(days=random.randint(0, (END_DATE - START_DATE).days)) for _ in range(NUM_USERS)]

signup_df = pd.DataFrame({
    "user_id": user_ids,
    "signup_date": signup_dates
})

# Generate activity logs
activity_records = []
for user_id, signup in zip(user_ids, signup_dates):
    num_sessions = random.randint(1, 10)
    for _ in range(num_sessions):
        activity_offset = random.randint(0, 60)  # user returns within 60 days
        activity_date = signup + timedelta(days=activity_offset)
        if activity_date > END_DATE:
            continue
        revenue = round(random.uniform(0, 100), 2)
        activity_records.append({
            "user_id": user_id,
            "signup_date": signup.date(),
            "activity_date": activity_date.date(),
            "revenue": revenue
        })

df = pd.DataFrame(activity_records)

# Save to CSV
df.to_csv(OUTPUT_PATH, index=False)
print(f"✅ Mock data saved to {OUTPUT_PATH}")