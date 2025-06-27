
from datetime import datetime, timedelta
import pandas as pd

def produtos_vencidos(df: pd.DataFrame) -> pd.DataFrame:
    hoje = datetime.today()
    return df[df['data_validade'] < hoje]

def produtos_a_vencer(df: pd.DataFrame, dias: int) -> pd.DataFrame:
    hoje = datetime.today()
    limite = hoje + timedelta(days=dias)
    return df[(df['data_validade'] >= hoje) & (df['data_validade'] <= limite)]
