import pandas as pd
import re

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

print(type(mpL[1]))

print(modelL)
print(vaL)
print(kmL)
print(stL)
print(ftL)
print(ttL)
print(maL)
print(engL)
print(mpL)
print(seatL)

print(max(modelL),min(modelL))
print(max(vaL),min(vaL))
print(max(kmL),min(kmL))
print(max(stL),min(stL))
print(max(ftL),min(ftL))
print(max(ttL),min(ttL))
print(max(maL),min(maL))
print(max(engL),min(engL))
print(max(mpL),min(mpL))
print(max(seatL),min(seatL))