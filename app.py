import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Load model and columns
model = joblib.load("salary_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# Load dataset for graph
df = pd.read_csv("job_salaries.csv")

# ---------------- TITLE ----------------

st.title("💼 ML-Based Salary Estimation System")

st.info(
    "This system provides approximate salary estimates based on available dataset features. "
    "Actual salaries may vary depending on skills, education, company reputation, location, "
    "market demand, and experience."
)

st.write("Fill the details below to estimate salary.")

# ---------------- INPUTS ----------------

experience_level = st.selectbox(
    "Experience Level",
    [
        "Entry Level",
        "Mid Level",
        "Senior Level",
        "Executive Level"
    ]
)

employment_type = st.selectbox(
    "Employment Type",
    [
        "Full Time",
        "Part Time",
        "Contract",
        "Freelance"
    ]
)

remote_ratio = st.slider(
    "Remote Work Percentage",
    0,
    100,
    50
)

st.caption(
    "0 = Fully Onsite | 50 = Hybrid | 100 = Fully Remote"
)

company_size = st.selectbox(
    "Company Size",
    [
        "Small",
        "Medium",
        "Large"
    ]
)

job_title = st.selectbox(
    "Job Category",
    [
        "Data Scientist",
        "Data Engineer",
        "ML/AI",
        "Data Analyst",
        "Management",
        "Other"
    ]
)

# ---------------- MAPPINGS ----------------

experience_map = {
    "Entry Level": "EN",
    "Mid Level": "MI",
    "Senior Level": "SE",
    "Executive Level": "EX"
}

employment_map = {
    "Full Time": "FT",
    "Part Time": "PT",
    "Contract": "CT",
    "Freelance": "FL"
}

company_size_map = {
    "Small": "S",
    "Medium": "M",
    "Large": "L"
}

# ---------------- PREDICTION ----------------

if st.button("Estimate Salary"):

    # Create empty dataframe with all columns
    input_data = pd.DataFrame(
        np.zeros((1, len(model_columns))),
        columns=model_columns
    )

    # Numerical feature
    input_data["remote_ratio"] = remote_ratio

    # Encode experience level
    exp_value = experience_map[experience_level]
    exp_col = f"experience_level_{exp_value}"

    if exp_col in input_data.columns:
        input_data[exp_col] = 1

    # Encode employment type
    emp_value = employment_map[employment_type]
    emp_col = f"employment_type_{emp_value}"

    if emp_col in input_data.columns:
        input_data[emp_col] = 1

    # Encode company size
    size_value = company_size_map[company_size]
    size_col = f"company_size_{size_value}"

    if size_col in input_data.columns:
        input_data[size_col] = 1

    # Encode job title
    job_col = f"job_title_{job_title}"

    if job_col in input_data.columns:
        input_data[job_col] = 1

    # Predict log salary
    prediction_log = model.predict(input_data)[0]

    # Convert back to real salary
    prediction = np.exp(prediction_log)

    # Display prediction
    st.success(
        f"Estimated Salary: ${prediction:,.2f}"
    )

# ---------------- GRAPH ----------------

st.subheader("📊 Salary Distribution in Dataset")

fig, ax = plt.subplots()

ax.hist(df["salary_in_usd"], bins=30)

ax.set_xlabel("Salary in USD")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Salaries")

st.pyplot(fig)