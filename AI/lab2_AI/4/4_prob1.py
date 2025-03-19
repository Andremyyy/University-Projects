import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# incarc date
file_path = "C:/Users/ema_a/Desktop/AI/surveyDataSience.csv"
df = pd.read_csv(file_path, low_memory=False)

df_cleaned = df.iloc[2:].reset_index(drop=True).copy()

# mapez valorile pentru educație și experiență (folosind informatiile de la ex 1)
education_years = {"Bachelor’s degree": 3,
                   "Master’s degree": 5,
                   "Doctoral degree": 8
                   }
experience_mapping = {
    "I have never written code": 0,
    "< 1 years": 0.5,
    "1-3 years": 2,
    "3-5 years": 4,
    "5-10 years": 7.5,
    "10-20 years": 15,
    "20+ years": 25
}

df_cleaned["Years_of_Education"] = df_cleaned["Q4"].map(education_years)
df_cleaned["Years_of_Experience"] = df_cleaned["Q6"].map(experience_mapping)

# elimin datele goale
valid_data = df_cleaned.dropna(subset=["Years_of_Education", "Years_of_Experience"]).copy()

# normalizare
scaler_minmax = MinMaxScaler()
#standardizare
scaler_standard = StandardScaler()

valid_data["Years_of_Education_Norm"] = scaler_minmax.fit_transform(valid_data[["Years_of_Education"]])
valid_data["Years_of_Education_Std"] = scaler_standard.fit_transform(valid_data[["Years_of_Education"]])

valid_data["Years_of_Experience_Norm"] = scaler_minmax.fit_transform(valid_data[["Years_of_Experience"]])
valid_data["Years_of_Experience_Std"] = scaler_standard.fit_transform(valid_data[["Years_of_Experience"]])

# Verificăm dacă coloanele există
# print(valid_data.columns)

# -------- VIZUALIZARE -------------

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# ----------- DURATA STUDIILOR ----------------
# grafic 1: Distribuția originală a duratei studilor
sns.histplot(valid_data["Years_of_Education"], bins=5, color="blue", ax=axes[0, 0])
axes[0, 0].set_title("Distribuția originală a duratei studiilor")

# grafic 2: normalizare Min-Max
sns.histplot(valid_data["Years_of_Education_Norm"], bins=5, color="red", ax=axes[0, 1])
axes[0, 1].set_title("Normalizare Min-Max (0-1)")

# grafic 3: standardizare
sns.histplot(valid_data["Years_of_Education_Std"], bins=5, color="green", ax=axes[0, 2])
axes[0, 2].set_title("Standardizare (media 0, dev 1)")


# ----------- EXPERIENȚA ÎN PROGRAMARE ---------------
# grafic 4: distribuția originală pt experienta in programare
sns.histplot(valid_data["Years_of_Experience"], bins=7, color="blue", ax=axes[1, 0])
axes[1, 0].set_title("Distribuția originală a experienței în programare")

# grafic 5: normalizare Min-Max
sns.histplot(valid_data["Years_of_Experience_Norm"], bins=7, color="red", ax=axes[1, 1])
axes[1, 1].set_title("Normalizare Min-Max (0-1)")

# Grafic 6: standardizare
sns.histplot(valid_data["Years_of_Experience_Std"], bins=7, color="green", ax=axes[1, 2])
axes[1, 2].set_title("Standardizare (media 0, dev 1)")

plt.tight_layout()
plt.show()
