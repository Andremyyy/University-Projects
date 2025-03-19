import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer

# citesc fișierului text
file_path = "C:/Users/ema_a/Desktop/AI/texts.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# impart textul în propoziții folosind delimitatorii ".", "!", "?", ";"
sentences = re.split(r'[.!?;]+', text)
# elimin propozițiile goale
sentences = [s.strip() for s in sentences if s.strip()]

# creez o listă cu frecvența cuvintelor în fiecare propoziție
word_counts = []
for sentence in sentences:
    # transform în lowercase și extrag cuvintele
    words = re.findall(r'\b\w+\b', sentence.lower())
    word_count = len(words)
    word_counts.append(word_count)

# convertesc în numpy array pentru normalizare
word_counts_array = np.array(word_counts).reshape(-1, 1)

# aplic metodele de normalizare
#Min-Max
scaler_minmax = MinMaxScaler()
#normalizare cu media = 0, deviatia standard = 1
scaler_standard = StandardScaler()
#normalizare cu norma euclidiana = norma L2 (suma patratelor elementelor unui vector este 1 )
# nu e aplicabila pe acest set de date, ar fi trebit macar 2 feature-uri ca sa aiba sens aceasta normalizare
scaler_l2 = Normalizer(norm="l2")

word_counts_minmax = scaler_minmax.fit_transform(word_counts_array)
word_counts_standard = scaler_standard.fit_transform(word_counts_array)
word_counts_l2 = scaler_l2.fit_transform(word_counts_array)


# --------- GRAFIC -------------
plt.figure(figsize=(14, 6))

# distribuția originală
plt.subplot(2, 2, 1)
#kde estimează distribuția probabilistică a numărului de cuvinte per propoziție
sns.histplot(word_counts, bins=10, color="blue", kde=True)
plt.title("Distribuția originală a numărului de cuvinte")
plt.xlabel("Număr de cuvinte per propoziție")


# scalare Min-Max
plt.subplot(2, 2, 2)
sns.histplot(word_counts_minmax.flatten(), bins=10, color="red", kde=True)
plt.title("Normalizare Min-Max")
plt.xlabel("Normalizat Min-Max (0-1)")

# Stardardizare
plt.subplot(2, 2, 3)
sns.histplot(word_counts_standard.flatten(), bins=10, color="green", kde=True)
plt.title("Standardizare")
plt.xlabel("Standardizare")

# Normalizare L2   -  nu e aplicabila pe acest set de date, ar fi trebit macar 2 feature-uri ca sa aiba sens aceasta normalizare
plt.subplot(2, 2, 4)
sns.histplot(word_counts_l2.flatten(), bins=10, color="purple", kde=True)
plt.title("L2 Normalization")
plt.xlabel("Normalizat L2")

plt.tight_layout()
plt.show()

# afisez rezultatele normalizate
print("Număr de cuvinte în propoziții:", word_counts)
print("Normalizare Min-Max:", word_counts_minmax.flatten())
print("Standardizare:", word_counts_standard.flatten())
print("Normalizare euclidiana(L2):", word_counts_l2.flatten())

