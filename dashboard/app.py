import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="SafetySignal-X",
    page_icon="💊",
    layout="wide"
)

st.title("💊 SafetySignal-X")
st.subheader("Drug Safety Signal Detection System")

file = r"C:\MCA_Projects\SafetySignal-X\outputs\ml_ranked_signals.csv"

df = pd.read_csv(file)

st.sidebar.header("Filters")

drug_info_file = r"C:\MCA_Projects\SafetySignal-X\data\processed\drug_information_20.csv"

drug_info = pd.read_csv(drug_info_file)


remove_drugs = {
    "ZEPBOUND",
    "CETIRIZINE HYDROCHLORIDE",
    "DEXAMETHASONE",
    "ELIGARD",
    "INFLECTRA",
    "MOUNJARO",
    "OMALIZUMAB",
    "VEDOLIZUMAB"
}

signal_drugs = (
    df["drugname"]
    .dropna()
    .astype(str)
    .str.upper()
    .str.strip()
)

signal_drugs = [
    drug for drug in signal_drugs.unique()
    if drug not in remove_drugs
]

drugs = ["All"] + sorted(signal_drugs)

selected_drug = st.sidebar.selectbox(
    "Select Drug",
    drugs
)

if selected_drug == "All":

    filtered = df.copy()

else:

    signal_df = df.copy()

    signal_df["drug_match"] = (
        signal_df["drugname"]
        .astype(str)
        .str.upper()
        .str.strip()
    )

    selected_name = (
        str(selected_drug)
        .upper()
        .strip()
    )

    name_map = {
        "ACTEMRE": "ACTEMRA"
    }

    selected_name = name_map.get(
        selected_name,
        selected_name
    )

    filtered = signal_df[
        signal_df["drug_match"] == selected_name
    ].copy()


# -----------------------------------------
# SIGNAL PRIORITY
# -----------------------------------------

filtered["ROR"] = pd.to_numeric(
    filtered["ROR"],
    errors="coerce"
)

filtered["ML_signal_score"] = pd.to_numeric(
    filtered["ML_signal_score"],
    errors="coerce"
)


def signal_priority(row):

    if row["ROR"] >= 5 and row["ML_signal_score"] >= 0.75:
        return "High"

    elif row["ROR"] >= 2 and row["ML_signal_score"] >= 0.50:
        return "Medium"

    else:
        return "Low"


filtered["Signal Priority"] = filtered.apply(
    signal_priority,
    axis=1
)


# -----------------------------------------
# SUMMARY METRICS
# -----------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Signals", len(filtered))

col2.metric(
    "Unique Drugs",
    filtered["drugname"].nunique()
)

col3.metric(
    "Unique Reactions",
    filtered["reaction"].nunique()
)

col4.metric(
    "Highest ROR",
    round(filtered["ROR"].max(), 2)
)


st.divider()

st.subheader("Top Safety Signals")


# -----------------------------------------
# SIGNAL TABLE
# -----------------------------------------

columns = [
    "drugname",
    "reaction",
    "ROR",
    "ROR_95CI_lower",
    "ROR_95CI_upper",
    "report_frequency",
    "ML_signal_score",
    "Signal Priority"
]


st.dataframe(
    filtered[columns].head(20),
    width="stretch"
)

st.subheader("Signal Visualization")

chart_data = filtered.head(10).copy()

chart_data["Drug - Reaction"] = (
    chart_data["drugname"].astype(str)
    + " - "
    + chart_data["reaction"].astype(str)
)

st.bar_chart(
    chart_data.set_index("Drug - Reaction")["ML_signal_score"]
)

st.info(
    "A detected signal does not prove that a drug caused an adverse reaction."
)

# -----------------------------------------
# DRUG INFORMATION
# -----------------------------------------

st.divider()
st.subheader("💊 Drug Information")

drug_info_file = r"C:\MCA_Projects\SafetySignal-X\data\processed\drug_information_20.csv"

drug_info = pd.read_csv(drug_info_file)

if selected_drug != "All":

    name_map = {
        "ACTEMRE": "ACTEMRA",
        "ACETAMINOPHEN": "ACETAMINOPHEN",
        "DUPIXENT": "DUPIXENT",
        "FOLIC ACID": "FOLIC ACID",
        "HUMIRA": "HUMIRA",
        "ADALIMUMAB": "HUMIRA",
        "METHOTREXATE": "METHOTREXATE",
        "ORENCIA": "ORENCIA",
        "PREDNISONE": "PREDNISONE",
        "RITUXIMAB": "RITUXIMAB",
        "SULFASALAZINE": "SULFASALAZINE",
        "INFLECTRA": "INFLECTRA",
        "MOUNJARO": "MOUNJARO",
        "ZEPBOUND": "ZEPBOUND",
        "VEDOLIZUMAB": "VEDOLIZUMAB",
        "ASPIRIN": "ASPIRIN",
        "ELIGARD": "ELIGARD",
        "ALBUTEROL SULFATE": "ALBUTEROL SULFATE",
        "OMALIZUMAB": "OMALIZUMAB",
        "CETIRIZINE HYDROCHLORIDE": "CETIRIZINE HYDROCHLORIDE",
        "DEXAMETHASONE": "DEXAMETHASONE"
    }

    selected_name = str(selected_drug).upper().strip()

    selected_name = name_map.get(
        selected_name,
        selected_name
    )

    info = drug_info[
        drug_info["drug"]
        .astype(str)
        .str.strip()
        .str.upper()
        == str(selected_drug).strip().upper()
    ]

    if not info.empty:

        drug = info.iloc[0]

        st.markdown(f"### 💊 {selected_drug}")
        st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Adalimumab_structure.png/512px-Adalimumab_structure.png",
    width=250
)
        st.write("**Generic Name:**", drug["generic_name"])

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("#### ✅ Common Uses")
            st.write(drug["common_uses"])

            st.markdown("#### 💉 Dosage")
            st.write(drug["dosage"])

            st.markdown("#### 👥 Who Can Use It")
            st.write(drug["who_can_use"])

        with col2:

            st.markdown("#### ⚠️ Important Risks / Adverse Effects")
            st.write(drug["important_risks_or_adverse_effects"])

            st.markdown("#### ⏱️ Half-Life / Body Presence")
            st.write(drug["half_life_or_body_presence"])

            st.markdown("#### 🚨 Important Precautions")
            st.write(drug["important_precautions"])

        st.markdown("#### 📚 Reliable Source")

        st.markdown(
            f"[View official drug information]({drug['source_url']})"
        )

    else:

        st.info(
            "Detailed information for this drug has not been added to the database yet."
        )

else:

    st.info(
        "Select a drug from the left-side filter to view detailed drug information."
    )