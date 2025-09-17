import streamlit as st
import pandas as pd
import re
import joblib
import sklearn

#region load data
df = pd.read_csv("unique_csv/unique_values.csv")

model_str = df[df['Unnamed: 0']=="model"]["Unique Values"].values[0]

modelL = re.sub(r"[\[\]']", "", model_str).split()

va_str = df[df['Unnamed: 0']=="vehicle_age"]["Unique Values"].values[0]

vaL = re.sub(r"[\[\]']", "", va_str).split()

vaL = [int(x) for x in vaL]

km_str = df[df['Unnamed: 0']=="km_driven"]["Unique Values"].values[0]

kmL = re.sub(r"[\[\]']", "", km_str).split()

kmL = [int(x) for x in kmL]

st_str = df[df['Unnamed: 0']=="seller_type"]["Unique Values"].values[0]

stL = re.sub(r"[\[\]']", "", st_str).split()

ft_str = df[df['Unnamed: 0']=="fuel_type"]["Unique Values"].values[0]

ftL = re.sub(r"[\[\]']", "", ft_str).split()

tt_str = df[df['Unnamed: 0']=="transmission_type"]["Unique Values"].values[0]

ttL = re.sub(r"[\[\]']", "", tt_str).split()

ma_str = df[df['Unnamed: 0']=="mileage"]["Unique Values"].values[0]

maL = re.sub(r"[\[\]']", "", ma_str).split()

maL = [float(x) for x in maL]

eng_str = df[df['Unnamed: 0']=="engine"]["Unique Values"].values[0]

engL = re.sub(r"[\[\]']", "", eng_str).split()

engL = [int(x) for x in engL]

mp_str = df[df['Unnamed: 0']=="max_power"]["Unique Values"].values[0]

mpL = re.sub(r"[\[\]']", "", mp_str).split()

mpL = [float(x) for x in mpL]

seat_str = df[df['Unnamed: 0']=="seats"]["Unique Values"].values[0]

seatL = re.sub(r"[\[\]']", "", seat_str).split()

seatL = [int(x) for x in seatL]

default_max_power = mpL[0] if len(mpL) > 0 else 0.0
#endregion

#region load models
@st.cache_resource
def load_models():
    models = {
        "DecisionTree": joblib.load("models/DecisionTree.pkl"),
        "ElasticNet": joblib.load("models/ElasticNet.pkl"),
        "ElasticNetCV": joblib.load("models/ElasticNetCV.pkl"),
        "GaussianNB": joblib.load("models/GaussianNB.pkl"),
        "KNNR": joblib.load("models/KNNR.pkl"),
        "Lasso": joblib.load("models/Lasso.pkl"),
        "LassoCV": joblib.load("models/LassoCV.pkl"),
        "LinearRegression": joblib.load("models/LinearRegression.pkl"),
        "LogisticRegression": joblib.load("models/LogisticRegression.pkl"),
        "Ridge": joblib.load("models/Ridge.pkl"),
        "RidgeCV": joblib.load("models/RidgeCV.pkl")
    }
    return models

# Call once → cached
models = load_models()
#endregion

#region load models
@st.cache_resource
def load_preprocessor():
    return joblib.load("preprocessor/preprocessor.pkl")

# Call once → cached
preprocessor = load_preprocessor()
#endregion

# region load LE
@st.cache_resource
def load_le():
    return joblib.load("models/model_le.pkl")

model_le = load_le()
# endregion


# region predictions
def get_predictions(input):
    input_df = pd.DataFrame([input])
    input_df['model'] = model_le.transform(input_df['model'])
    pin = preprocessor.transform(input_df)
    pred = {name: m.predict(pin)[0] for name, m in models.items()}
    return pred
# endregion

st.title("Prediction Dashboard")

cola, colb = st.columns([2,1])
with cola:
    with st.form("input_form"):
        st.subheader("Enter Input Data")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            model = st.selectbox("Car Model", modelL)  # model_options = list from your CSV
            vehicle_age = st.number_input("Vehicle Age (years)", min_value=0, max_value=20, step=1)
            km_driven = st.number_input("Kilometers Driven", min_value=0)
            seller_type = st.selectbox("Seller Type", stL)
            fuel_type = st.selectbox("Fuel Type", ftL)

        with col2:
            transmission_type = st.radio("Transmission", ttL)
            mileage = st.number_input("Mileage (km/l)")
            engine = st.number_input("Engine Capacity (CC)", min_value=500, max_value= 7000, step=100)
            max_power = st.number_input("Max Power (bhp)", min_value=0.0, max_value=500.0, step=0.5, value=default_max_power)
            seats = st.slider("Number of Seats", min_value=2, max_value=10, step=1)

        # submit button
        submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Form submitted successfully!")
    predictions = get_predictions({"vehicle_age": vehicle_age, "seats": seats, "km_driven": km_driven, "mileage": mileage, "engine": engine, "max_power": max_power, "model": model, "seller_type": seller_type, "fuel_type": fuel_type, "transmission_type": transmission_type
    })
else:
    predictions = pd.DataFrame(columns=["Model", "Prediction"])

with colb:
    st.subheader("Prediction")
    st.dataframe(predictions)