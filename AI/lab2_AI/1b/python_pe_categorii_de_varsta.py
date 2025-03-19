import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# incarc fișierul CSV cu low_memory=False pentru a evita warning-ul de date nespecificate
file_path = "C:/Users/ema_a/Desktop/AI/surveyDataSience.csv"
df = pd.read_csv(file_path, low_memory=False)
# elimin prima linie pt ca aceasta conține întrebările și nu date efective
df_cleaned = df.iloc[2:].reset_index(drop=True)


#  Vizualizarea distribuției programatorilor Python pe categorii de vârstă

# coloanele care contin datele relevante pt aceasta cerinta
age_col = "Q1"
python_col = "Q7_Part_1"

# filtrez doar respondenții care programează în Python
df_python = df_cleaned[df_cleaned[python_col] == "Python"]

# contorizez numărul de respondenți în fiecare categorie de vârstă
age_distribution = df_python[age_col].value_counts().sort_index()

# creez graficul de distribuție
plt.figure(figsize=(10, 6))
sns.barplot(x=age_distribution.index, y=age_distribution.values, palette="pastel")

# setez titlul și etichetele axelor
plt.title("Distribuția respondenților care programează în Python pe categorii de vârstă", fontsize=14)
plt.xlabel("Categorie de vârstă", fontsize=12)
plt.ylabel("Număr de respondenți", fontsize=12)
plt.xticks(rotation=45)  # rotesc etichetele de pe axa X pentru vizibilitate

# afisez graficul
plt.show()
