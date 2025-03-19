import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# incarc fișierul CSV cu low_memory=False pentru a evita warning-ul de date nespecificate
file_path = "C:/Users/ema_a/Desktop/AI/surveyDataSience.csv"
df = pd.read_csv(file_path, low_memory=False)
# elimin prima linie pt ca aceasta conține întrebările și nu date efective
df_cleaned = df.iloc[2:].reset_index(drop=True)


# Respondentii care pot fi considerati "outlieri" din punct de vedere al
# vechimii in programare (puteti folositi un boxplot pentru a identifica aceste valori)


# coloana care conține vechimea în programare
experience_col = "Q6"

# cicționar pentru transformarea intervalelor în valori numerice folosind mijlocul intervalului
experience_mapping = {
    "I have never written code": 0,
    "< 1 years": 0.5,
    "1-3 years": 2,
    "5-10 years": 7.5,
    "10-20 years": 15,
    #  20-70 limita de varsta => mijloc = 45
    "20+ years": 45
}

# aplic mapping-ul
df_cleaned["Years_of_Programming"] = df_cleaned[experience_col].map(experience_mapping)

# elimin valorile NaN (valori goale)
df_experience = df_cleaned.dropna(subset=["Years_of_Programming"])

# creez un boxplot pentru vizualizare
plt.figure(figsize=(8, 5))
sns.boxplot(x=df_experience["Years_of_Programming"], color="skyblue")
plt.title("Distribuția vechimii în programare", fontsize=14)
plt.xlabel("Ani de experiență", fontsize=12)
plt.show()

# identific outlierii folosind regula IQR (Interquartile Range)
Q1 = np.percentile(df_experience["Years_of_Programming"], 25)
Q3 = np.percentile(df_experience["Years_of_Programming"], 75)
IQR = Q3 - Q1  # Intervalul intercuartil

# limite pentru outlieri
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# extrag outlierii
outliers = df_experience[(df_experience["Years_of_Programming"] < lower_bound) |
                         (df_experience["Years_of_Programming"] > upper_bound)]

print(f"Numărul de outlieri: {len(outliers)}")
print("Outlieri identificați:")
print(outliers[[experience_col, "Years_of_Programming"]])
