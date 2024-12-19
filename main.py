import pandas as pd


def get_clean_work_time(work_time_path):
    return (pd.read_csv(work_time_path, sep=';', encoding='utf-8')
            .drop_duplicates()
            .fillna({'Temps annuel de travail (SNCF)': 0,
                     'Temps annuel de travail (France)': 0,
                     'Commentaires': ''})
            .assign(Commentaires=lambda x: x['Commentaires'].str.strip()))



def get_interesting_columns(df, columns):
    missing_columns = [col for col in columns if col not in df.columns]
    if missing_columns:
        print("Columns missing")
        return pd.DataFrame()
    return df[columns]

work_time_file = get_clean_work_time("Data/temps-de-travail-annuel-depuis-1851.csv")

work_time_columns = [
    "Date",
    "Temps annuel de travail (SNCF)",
    "Temps annuel de travail (France)"
]

work_time = get_interesting_columns(work_time_file, work_time_columns)

work_time_filter = work_time[(work_time["Date"] == 2017) | (work_time["Date"] == 2018)]

frequentation_file = pd.read_csv("Data/frequentation-gares.csv", sep=";")
frequentation_columns = [
    "Nom de la gare",
    "Code postal",
    "Total Voyageurs + Non voyageurs 2017",
    "Total Voyageurs + Non voyageurs 2018"
]
frequentation = get_interesting_columns(frequentation_file, frequentation_columns)

# frequentation_filter = frequentation[frequentation["Code postal"].astype(str).str[:1] == '7'].head(3)
frequentation_filter = frequentation[frequentation["Code postal"].astype(str).str[:2] == '75'].head(10)

print(work_time_filter)
print(frequentation_filter)