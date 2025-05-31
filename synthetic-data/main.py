import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Define number of samples
n_samples = 1000

# Generate synthetic features
age = np.random.randint(18, 60, size=n_samples)
education_level = np.random.choice(['No formal', 'Primary', 'High School', 'Graduate'], size=n_samples)
employment_type = np.random.choice(['Unemployed', 'Casual', 'Self-employed', 'Salaried'], size=n_samples)
region = np.random.choice(['Rural', 'Semi-urban', 'Urban'], size=n_samples)
night_light = np.random.normal(loc=50, scale=15, size=n_samples)  # simulate satellite data
gov_subsidy = np.random.choice([0, 1], size=n_samples)
electricity_access = np.random.choice([0, 1], size=n_samples)

# Create a simple rule-based label for repayment capability
def generate_repayment_status(age, employment_type, subsidy):
    if employment_type == 'Salaried':
        return 'Good'
    elif employment_type == 'Self-employed' and subsidy == 1:
        return 'Medium'
    else:
        return 'Poor'

repayment_status = [
    generate_repayment_status(age[i], employment_type[i], gov_subsidy[i])
    for i in range(n_samples)
]

# Create a DataFrame
df = pd.DataFrame({
    'age': age,
    'education_level': education_level,
    'employment_type': employment_type,
    'region': region,
    'night_light': night_light,
    'gov_subsidy': gov_subsidy,
    'electricity_access': electricity_access,
    'repayment_status': repayment_status
})

# Show first few rows
print(df.head())

# Save dataset to CSV
df.to_csv("synthetic_income_data.csv", index=False)
print("✅ Dataset saved as 'synthetic_income_data.csv'")

