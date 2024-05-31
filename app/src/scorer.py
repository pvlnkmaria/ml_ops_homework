import pandas as pd
from catboost import CatBoostClassifier

# Функция для предсказания
def make_pred(input_data, path_to_file):
    print('Importing pretrained model...')
    
    # Импорт модели
    model = CatBoostClassifier()
    model.load_model('./models/my_catboost_model.cbm')

    # Создание submission dataframe
    submission = pd.DataFrame({
        'client_id': pd.read_csv(path_to_file)['client_id'],
        'preds': model.predict_proba(input_data)[:, 1]
        })
    
    # Возврат вероятности для положительного класса
    return submission
