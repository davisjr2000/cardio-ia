"""
Baixa o UCI Heart Disease Dataset (id=45), renomeia colunas para português
e salva em data/pacientes_cardiacos.csv.

Uso:
    python scripts/baixar_dataset.py
"""

import os
import pandas as pd
from ucimlrepo import fetch_ucirepo

COLUNA_MAP = {
    "age":      "idade",
    "sex":      "sexo",
    "cp":       "tipo_dor_peito",
    "trestbps": "pressao_arterial_repouso",
    "chol":     "colesterol_serico",
    "fbs":      "glicemia_jejum_alta",
    "restecg":  "eletrocardiograma_repouso",
    "thalach":  "freq_cardiaca_maxima",
    "exang":    "angina_por_exercicio",
    "oldpeak":  "depressao_st",
    "slope":    "inclinacao_st",
    "ca":       "vasos_coloridos",
    "thal":     "talassemia",
    "num":      "diagnostico",
}

FAIXAS = [0, 30, 40, 50, 60, 70, 120]
LABELS = ["<30", "30-39", "40-49", "50-59", "60-69", "70+"]


def main():
    print("Baixando UCI Heart Disease Dataset (id=45)...")
    hd = fetch_ucirepo(id=45)

    df = pd.concat([hd.data.features, hd.data.targets], axis=1)
    df = df.rename(columns=COLUNA_MAP)

    os.makedirs("data", exist_ok=True)
    out = os.path.join("data", "pacientes_cardiacos.csv")
    df.to_csv(out, index=False)
    print(f"Salvo em {out}")

    print("\n=== Dimensões ===")
    print(f"Linhas: {df.shape[0]}  |  Colunas: {df.shape[1]}")

    print("\n=== Describe (numéricas) ===")
    print(df.describe().to_string())

    print("\n=== Nulos por coluna ===")
    nulos = df.isnull().sum()
    print(nulos[nulos > 0].to_string() if nulos.any() else "Nenhum nulo encontrado.")

    print("\n=== Distribuição por sexo ===")
    sexo_map = {1: "Masculino", 0: "Feminino"}
    print(df["sexo"].map(sexo_map).value_counts().to_string())

    print("\n=== Distribuição por faixa etária ===")
    df["faixa_etaria"] = pd.cut(df["idade"], bins=FAIXAS, labels=LABELS, right=False)
    print(df["faixa_etaria"].value_counts().sort_index().to_string())


if __name__ == "__main__":
    main()
