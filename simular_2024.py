
import pandas as pd
import numpy as np
from datetime import timedelta

# Cargar datos existentes (2025)
archivo_csv = "datos_consolidados.csv"
try:
    df_2025 = pd.read_csv(archivo_csv)
    print("Datos cargados correctamente.")
except FileNotFoundError:
    print("No se encontró datos_consolidados.csv")
    exit()

# Filtrar solo 2025 por seguridad
df_real = df_2025[df_2025['año'] == 2025].copy()

# Crear datos simulados para 2024
print("Generando datos simulados para 2024...")
df_2024 = df_real.copy()

# Ajustar fechas: Restar 364 días (para mantener el día de la semana similar) o 1 año exacto
# Usaremos reemplazo directo de año para simplificar correspondencia mensual
df_2024['fecha'] = pd.to_datetime(df_2024['fecha'], errors='coerce')
df_2024['fecha'] = df_2024['fecha'].apply(lambda x: x.replace(year=2024) if pd.notnull(x) else x)
df_2024['año'] = 2024

# Variación aleatoria de montos (Simular que 2024 fue un poco menor, ej: 90% de 2025)
# Multiplicamos ingresos y egresos por un factor aleatorio entre 0.85 y 1.05
np.random.seed(42)
factor_var = np.random.uniform(0.85, 0.95, size=len(df_2024))
df_2024['ingreso'] = df_2024['ingreso'] * factor_var
df_2024['egreso'] = df_2024['egreso'] * factor_var

# Unir ambos dataframes
df_final = pd.concat([df_2024, df_real], ignore_index=True)

# Guardar
df_final.to_csv(archivo_csv, index=False)
print(f"¡Éxito! Ahora datos_consolidados.csv tiene registros de {df_final['año'].unique()}")
print(f"Total registros: {len(df_final)}")
