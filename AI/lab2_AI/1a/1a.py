import pandas as pd
import numpy as np


# funcție pentru încărcarea și curățarea datelor
def load_and_clean_data(file_path):
    # incarc fișierul CSV cu low_memory=False pentru a evita warning-ul de date nespecificate
    df = pd.read_csv(file_path, low_memory=False)
    # elimin primele 2 linii pt ca acestea conțin întrebările, ci nu inregistrarile efective
    df_cleaned = df.iloc[2:].reset_index(drop=True)
    return df_cleaned


# a) Numărul de respondenți ( de la care s-au colectat informatiile)
def count_respondents(df):
    return df.shape[0]


# b) Numărul și tipul atributelor ((atributelor, proprietatilor) detinute pentru un respondent
#TODO: aici nu e bine
def attributes_info(df):
    # nr total de atribute
    num_attributes = df.shape[1]
    # tipurile unice de date
    attribute_types = df.dtypes.value_counts()
    return num_attributes, attribute_types


# c) Numărul de respondenți cu date complete

# pp ca date complete inseamna sa aiba cel putin un raspuns la intrebarile
# de tip multimple choice (contin "Other" sau "Part" in titlu) si un raspuns la fiecare
# intrebare simpla (cele de tip "Q1", "Q2" etc)

def count_complete_respondents(df):
    # identific întrebările multiple-choice
    multiple_choice_cols = [col for col in df.columns if "Part" in col or "OTHER" in col]

    # identific întrebările simple prin excluderea celor multiple
    single_choice_cols = [col for col in df.columns if col not in multiple_choice_cols]

    #  să aibă cel puțin un răspuns într-o întrebare multiple-choice
    has_multiple_choice = df[multiple_choice_cols].notna().sum(axis=1) > 0

    # să aibă răspunsuri valide la toate întrebările simple
    has_single_choice = df[single_choice_cols].notna().all(axis=1)

    # cati respondenti indeplinesc ambele conditii
    return (has_multiple_choice & has_single_choice).sum()


# d) Durata medie a studiilor
def average_education_years(df):
    # folosesc un dictionar pt nivelul licenta, master si doctorat
    education_years = {
        "Bachelor’s degree": 3,
        "Master’s degree": 5,
        "Doctoral degree": 8
    }

    # coloana care contine nivelul studiilor = Q4
    df["Years_of_Education"] = df["Q4"].map(education_years)
    df_filtered = df.dropna(subset=["Years_of_Education"])

    # filtrez doar respondenții care au studii superioare valide
    mean_all = df_filtered["Years_of_Education"].mean()

    #filtrez respondentii care sunt din Romania (coloana Q3)
    mean_romania = df_filtered[df_filtered["Q3"] == "Romania"]["Years_of_Education"].mean()

    #filtrez femeile din Romania (coloana Q2)
    mean_romania_women = df_filtered[(df_filtered["Q3"] == "Romania") & (df_filtered["Q2"] == "Woman")][
        "Years_of_Education"].mean()

    return mean_all, mean_romania, mean_romania_women


# e) Numărul de femei din România cu date complete
def count_romania_women_complete(df):

    multiple_choice_cols = [col for col in df.columns if "Part" in col or "OTHER" in col]
    single_choice_cols = [col for col in df.columns if col not in multiple_choice_cols]

    romania_women = df[(df["Q3"] == "Romania") & (df["Q2"] == "Woman")]

    #verific cate dintre ele au date complete
    has_multiple_choice = romania_women[multiple_choice_cols].notna().sum(axis=1) > 0
    # has_single_choice = romania_women[single_choice_cols].notna().all(axis=1)
    #macar 80% din intrebarile simple sa aiba raspunsuri, altfel imi afiseaza 0 femei
    has_single_choice = df[single_choice_cols].notna().sum(axis=1) / len(single_choice_cols) > 0.8
    return (has_multiple_choice & has_single_choice).sum()


# f) Numărul de femei din România care programează în Python și C++
def count_romania_women_by_language(df):
    romania_women = df[(df["Q3"] == "Romania") & (df["Q2"] == "Woman")]

    num_python = (romania_women["Q7_Part_1"] == "Python").sum()
    num_cpp = (romania_women["Q7_Part_5"] == "C++").sum()

    return num_python, num_cpp

# f partea 2) intervalul de varsta cu cele mai multe femei care programeaza in Python? Dar in C++?
def most_common_age_by_language(df):
    # filtrez femeile din România cu date complete
    romania_women_complete = df[(df["Q3"] == "Romania") & (df["Q2"] == "Woman")]

    # selectez femeile care programează în Python
    python_programmers = romania_women_complete[romania_women_complete["Q7_Part_1"] == "Python"]

    # selectez femeile care programează în C++
    cpp_programmers = romania_women_complete[romania_women_complete["Q7_Part_5"] == "C++"]

    # calculez intervalele de varsta (dacă există)
    # folosesc mode() care returneaza cea mai frecventa valoare (modul) dintr-o coloana
    most_common_age_python = python_programmers["Q1"].mode()
    most_common_age_C = cpp_programmers["Q1"].mode()

    return (
        most_common_age_python[0] if not most_common_age_python.empty else None,
        most_common_age_C[0] if not most_common_age_C.empty else None
    )


# g) Transformarea vechimii în programare în ani și calculul momentelor statistice
def programming_experience_stats(df):
    #dictionar pt vechime folosind mijlocul intervalului
    experience_mapping = {
        "I have never written code": 0,
        "< 1 years": 0.5,
        "1-3 years": 2,
        "5-10 years": 7.5,
        "10-20 years": 15,
        "20+ years": 25
    }

    # coloana care contine vechimea = Q6
    df["Years_of_Experience"] = df["Q6"].map(experience_mapping)
    experience_values = df["Years_of_Experience"].dropna()

    min_years = experience_values.min()
    max_years = experience_values.max()
    #media
    mean_years = experience_values.mean()
    #deviatia standard
    std_dev_years = experience_values.std()
    #mediana
    median_years = experience_values.median()

    interpretare = "dreaptă (majoritatea cu experiență mică)" if mean_years > median_years else \
        "stânga (mai mulți cu experiență mare)" if mean_years < median_years else "simetrică"

    return min_years, max_years, mean_years, std_dev_years, median_years, interpretare


if __name__ == "__main__":
    file_path = "C:/Users/ema_a/Desktop/AI/surveyDataSience.csv"
    df = load_and_clean_data(file_path)

    print(f"Numărul de respondenți: {count_respondents(df)} \n")

    num_attributes, attribute_types = attributes_info(df)
    print(f"Numărul de atribute: {num_attributes} \n")
    print(f"Tipurile de date ale atributelor:\n{attribute_types} \n")

    print(f"Numărul de respondenți cu date complete: {count_complete_respondents(df)} \n")

    mean_all, mean_romania, mean_romania_women = average_education_years(df)
    print(f"Durata medie a studiilor (toți respondenții): {mean_all:.2f} ani ")
    print(f"Durata medie a studiilor (România): {mean_romania:.2f} ani")
    print(f"Durata medie a studiilor (femei din România): {mean_romania_women:.2f} ani \n")

    print(f"Numărul de femei din România cu date complete: {count_romania_women_complete(df)} \n")

    num_python, num_cpp = count_romania_women_by_language(df)
    print(f"Numărul de femei din România care programează în Python: {num_python}")
    print(f"Numărul de femei din România care programează în C++: {num_cpp} \n")

    most_common_python, most_common_cpp = most_common_age_by_language(df)

    if most_common_python:
        print(f"Intervalul de vârstă cel mai frecvent pentru femeile care programează în Python: {most_common_python}")
    else:
        print("Nu există date pentru femeile care programează în Python.")

    if most_common_cpp:
        print(f"Intervalul de vârstă cel mai frecvent pentru femeile care programează în C++: {most_common_cpp}")
    else:
        print("Nu există date pentru femeile care programează în C++.")

    print()

    if num_python > num_cpp:
        print("Mai multe femei din România programează în Python decât în C++.")
    elif num_cpp < num_python:
        print("Mai multe femei din România programează în C++ decât în Python.")
    else:
        print("Numărul de femei din România care programează în Python și C++ este egal.")

    print()

    min_exp, max_exp, mean_exp, std_exp, median_exp, interpretare = programming_experience_stats(df)
    print(f"Minimul experienței în programare: {min_exp} ani")
    print(f"Maximul experienței în programare: {max_exp} ani")
    print(f"Media experienței în programare: {mean_exp:.2f} ani")
    print(f"Deviația standard: {std_exp:.2f} ani")
    print(f"Mediana experienței în programare: {median_exp} ani")
    print(f"Distribuția experienței este {interpretare}.")

