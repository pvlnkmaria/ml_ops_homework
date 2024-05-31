import pandas as pd

# Определение признаков
target = 'binary_target'
cat_features = ['регион', 'использование', 'mrg_', 'pack']
col = ['секретный_скор', 'on_net', 'частота_пополнения']


# Функция загрузки данных
def import_data(path_to_file):
    data = pd.read_csv(path_to_file)
    return data

# Основная функция предобработки данных
def run_preproc(input_df):
    # Заполнение пропусков в категориальных признаках
    input_df[cat_features] = input_df[cat_features].fillna('Пропуск')
    
  # Определение признаков     
    col = input_df.columns.to_list()          
    # Возврат итогового DataFrame     
    output_df = input_df[col]    
    
    return output_df
