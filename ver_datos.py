import pandas as pd

df = pd.read_csv('datos_consolidados.csv')

print('='*80)
print('ANÁLISIS DETALLADO DEL ARCHIVO CONSOLIDADO')
print('='*80)

print(f'\n📊 INFORMACIÓN GENERAL:')
print(f'  Total registros: {len(df)}')
print(f'  Columnas: {list(df.columns)}')

print(f'\n📅 AÑOS DISPONIBLES:')
for año in sorted(df['año'].unique()):
    count = len(df[df['año'] == año])
    print(f'  {año}: {count} registros')

print(f'\n🏷️ CATEGORÍAS:')
for cat in sorted(df['categoria'].unique()):
    count = len(df[df['categoria'] == cat])
    total = df[df['categoria'] == cat]['ingreso'].sum()
    print(f'  {cat}: {count} registros, S/ {total:,.2f}')

print(f'\n💰 TOTALES FINANCIEROS:')
print(f'  Total Ingresos: S/ {df["ingreso"].sum():,.2f}')
print(f'  Total Egresos:  S/ {df["egreso"].sum():,.2f}')
print(f'  Balance:        S/ {(df["ingreso"].sum() - df["egreso"].sum()):,.2f}')

print(f'\n📈 ESTADÍSTICAS POR AÑO:')
for año in sorted(df['año'].unique()):
    df_año = df[df['año'] == año]
    ing = df_año['ingreso'].sum()
    egr = df_año['egreso'].sum()
    bal = ing - egr
    print(f'\n  {año}:')
    print(f'    Ingresos: S/ {ing:,.2f}')
    print(f'    Egresos:  S/ {egr:,.2f}')
    print(f'    Balance:  S/ {bal:,.2f}')

print('\n' + '='*80)
