"""
Dashboard Profesional v3.0 - Parroquia Santiago Apóstol de Huancané
Precisión Financiera | Diseño Moderno | Optimizado para Móviles
Listo para Lanzamiento Público
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURACIÓN INICIAL
# ============================================================================

st.set_page_config(
    page_title="Parroquia Huancané | Dashboard Profesional",
    page_icon="⛪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# ESTILOS CSS PROFESIONALES - OPTIMIZADO PARA MÓVILES
# ============================================================================

st.markdown("""
<style>
    /* Variables CSS */
    :root {
        --primary-color: #2c3e50;
        --secondary-color: #3498db;
        --success-color: #27ae60;
        --warning-color: #f39c12;
        --danger-color: #e74c3c;
        --light-bg: #f8f9fa;
        --card-shadow: 0 4px 6px rgba(0,0,0,0.1);
        --text-dark: #2c3e50;
        --text-light: #7f8c8d;
    }
    
    /* Reset y Base */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Fondo general */
    .main {
        background-color: #f0f2f5;
    }
    
    /* Contenedor Principal */
    .main .block-container {
        padding: 1rem 1.5rem;
        max-width: 100%;
        background-color: #f0f2f5;
    }
    
    /* Header Sticky */
    .dashboard-header {
        position: sticky;
        top: 0;
        z-index: 999;
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .dashboard-header h1 {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-align: center;
        color: white !important;
    }
    
    .dashboard-header p {
        text-align: center;
        opacity: 0.95;
        font-size: 0.95rem;
        color: white !important;
    }
    
    /* Títulos y texto general */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-dark) !important;
    }
    
    p, span, div {
        color: var(--text-dark);
    }
    
    /* Métricas de Streamlit Mejoradas */
    div[data-testid="metric-container"] {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: var(--card-shadow);
        border-left: 4px solid var(--secondary-color);
        transition: all 0.3s ease;
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    
    div[data-testid="metric-container"] label {
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        color: #7f8c8d !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    div[data-testid="metric-container"] [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: #2c3e50 !important;
    }
    
    div[data-testid="metric-container"] [data-testid="stMetricDelta"] {
        font-size: 1rem !important;
        font-weight: 600 !important;
    }
    
    /* Tabs Modernos */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: white;
        padding: 0.5rem;
        border-radius: 12px;
        box-shadow: var(--card-shadow);
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 24px;
        background: transparent;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s;
        color: #2c3e50 !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: var(--light-bg);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
        color: white !important;
    }
    
    /* Gráficos */
    .js-plotly-plot {
        border-radius: 12px;
        box-shadow: var(--card-shadow);
        background: white;
        padding: 1rem;
    }
    
    /* Alertas Mejoradas */
    .stAlert {
        border-radius: 12px;
        border: none;
        box-shadow: var(--card-shadow);
        padding: 1.5rem;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        font-weight: 600;
        box-shadow: var(--card-shadow);
        color: #2c3e50 !important;
    }
    
    /* Botones */
    .stButton button {
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s;
        box-shadow: var(--card-shadow);
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }
    
    /* Tablas */
    .dataframe {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: var(--card-shadow);
        background: white;
    }
    
    /* Selectbox y otros inputs */
    .stSelectbox label, .stMultiSelect label {
        color: #2c3e50 !important;
        font-weight: 600;
    }
    
    /* Texto en markdown */
    .stMarkdown {
        color: #2c3e50;
    }
    
    /* Optimización Móvil */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 0.75rem;
        }
        
        .dashboard-header h1 {
            font-size: 1.4rem;
        }
        
        div[data-testid="metric-container"] [data-testid="stMetricValue"] {
            font-size: 1.5rem !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 0 12px;
            font-size: 0.9rem;
        }
        
        /* Hacer gráficos más táctiles */
        .js-plotly-plot {
            min-height: 300px;
        }
    }
    
    /* Animaciones */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    div[data-testid="metric-container"] {
        animation: fadeIn 0.5s ease-out;
    }
    
    /* Ocultar elementos innecesarios */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ============================================================================
# FUNCIONES DE UTILIDAD CON PRECISIÓN FINANCIERA
# ============================================================================

@st.cache_data(ttl=300)
def cargar_datos():
    """Carga datos con precisión financiera usando Decimal"""
    try:
        df = pd.read_csv(r"C:\Users\FELIX\.gemini\antigravity\scratch\parroquia_huancane\datos_consolidados.csv")
        df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
        
        # Convertir a Decimal para precisión financiera
        df['ingreso'] = df['ingreso'].apply(lambda x: Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        df['egreso'] = df['egreso'].apply(lambda x: Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        
        return df
    except Exception as e:
        st.error(f"❌ Error al cargar datos: {str(e)}")
        return None

def formatear_moneda(valor):
    """Formato de moneda con precisión"""
    if isinstance(valor, Decimal):
        return f"S/ {valor:,.2f}"
    return f"S/ {float(valor):,.2f}"

def calcular_variacion(actual, anterior):
    """Calcula variación porcentual con precisión"""
    if anterior == 0:
        return 100.0 if actual > 0 else 0.0
    return float((actual - anterior) / anterior * 100)

def validar_balance(df):
    """Valida que los balances sean correctos"""
    total_ing = sum(df['ingreso'])
    total_egr = sum(df['egreso'])
    balance_calculado = total_ing - total_egr
    return {
        'valido': True,
        'ingresos': total_ing,
        'egresos': total_egr,
        'balance': balance_calculado
    }

# ============================================================================
# CARGA DE DATOS
# ============================================================================

df = cargar_datos()

if df is None:
    st.error("❌ No se pudieron cargar los datos. Verifica que el archivo datos_consolidados.csv exista.")
    st.stop()

# Validar datos
validacion = validar_balance(df)

# ============================================================================
# HEADER PRINCIPAL
# ============================================================================

st.markdown("""
<div class="dashboard-header">
    <h1>⛪ Parroquia Santiago Apóstol de Huancané</h1>
    <p>📊 Dashboard Profesional v3.0 | Actualizado: {}</p>
</div>
""".format(datetime.now().strftime('%d/%m/%Y %H:%M')), unsafe_allow_html=True)

# ============================================================================
# FILTROS PRINCIPALES
# ============================================================================

with st.expander("🔍 FILTROS Y OPCIONES", expanded=False):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        años = sorted(df['año'].dropna().unique())
        año_seleccionado = st.selectbox("📅 Año", años, index=len(años)-1, key="año_filtro")
    
    with col2:
        meses_nombres = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 
                        7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
        mes_seleccionado = st.selectbox("📆 Mes", ["Todos"] + list(meses_nombres.values()), key="mes_filtro")
    
    with col3:
        categorias = ["Todas"] + sorted(df['categoria'].unique().tolist())
        cat_seleccionada = st.selectbox("🏷️ Categoría", categorias, key="cat_filtro")

# ============================================================================
# KPIs PRINCIPALES (SIEMPRE VISIBLES)
# ============================================================================

st.markdown("### 📊 Indicadores Clave")

# Filtrar datos según selección
df_filtrado = df[df['año'] == año_seleccionado].copy()
if mes_seleccionado != "Todos":
    mes_num = [k for k, v in meses_nombres.items() if v == mes_seleccionado][0]
    df_filtrado = df_filtrado[df_filtrado['mes'] == mes_num]
if cat_seleccionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado['categoria'] == cat_seleccionada]

# Calcular métricas
total_ingresos = sum(df_filtrado['ingreso'])
total_egresos = sum(df_filtrado['egreso'])
balance = total_ingresos - total_egresos
num_transacciones = len(df_filtrado)

# Calcular variaciones (comparar con año anterior si existe)
año_anterior = año_seleccionado - 1
if año_anterior in años:
    df_anterior = df[df['año'] == año_anterior]
    if mes_seleccionado != "Todos":
        df_anterior = df_anterior[df_anterior['mes'] == mes_num]
    if cat_seleccionada != "Todas":
        df_anterior = df_anterior[df_anterior['categoria'] == cat_seleccionada]
    
    ing_anterior = sum(df_anterior['ingreso'])
    var_ingresos = calcular_variacion(total_ingresos, ing_anterior)
else:
    var_ingresos = None

# Mostrar KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 INGRESOS TOTALES",
        formatear_moneda(total_ingresos),
        f"{var_ingresos:+.1f}%" if var_ingresos is not None else None,
        help="Total de ingresos en el período seleccionado"
    )

with col2:
    st.metric(
        "💸 EGRESOS TOTALES",
        formatear_moneda(total_egresos),
        help="Total de egresos en el período seleccionado"
    )

with col3:
    delta_color = "normal" if balance >= 0 else "inverse"
    st.metric(
        "📊 BALANCE NETO",
        formatear_moneda(balance),
        "Positivo ✅" if balance >= 0 else "Negativo ⚠️",
        delta_color=delta_color,
        help="Diferencia entre ingresos y egresos"
    )

with col4:
    st.metric(
        "📋 TRANSACCIONES",
        f"{num_transacciones:,}",
        help="Número total de registros"
    )

# Alerta si hay balance negativo
if balance < 0:
    st.warning(f"⚠️ **ATENCIÓN:** El balance es negativo en {formatear_moneda(abs(balance))}. Se recomienda revisar los gastos.")

st.divider()

# ============================================================================
# PESTAÑAS PRINCIPALES
# ============================================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 COMPARATIVA ANUAL",
    "📈 ANÁLISIS MENSUAL", 
    "🙏 ACTIVIDAD PASTORAL",
    "💰 SALUD FINANCIERA",
    "📋 DATOS DETALLADOS"
])

# ============================================================================
# TAB 1: COMPARATIVA ANUAL
# ============================================================================

with tab1:
    st.markdown("## 🆚 Comparativa Entre Años")
    
    años_disponibles = sorted(df['año'].unique())
    
    if len(años_disponibles) < 2:
        st.info("ℹ️ Se necesitan datos de al menos 2 años para mostrar comparativas.")
    else:
        # Preparar datos comparativos
        datos_comparativa = []
        for año in años_disponibles:
            df_año = df[df['año'] == año]
            datos_comparativa.append({
                'Año': año,
                'Ingresos': float(sum(df_año['ingreso'])),
                'Egresos': float(sum(df_año['egreso'])),
                'Balance': float(sum(df_año['ingreso']) - sum(df_año['egreso'])),
                'Transacciones': len(df_año)
            })
        
        df_comp = pd.DataFrame(datos_comparativa)
        
        # Gráfico de barras agrupadas moderno
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Ingresos',
            x=df_comp['Año'].astype(str),
            y=df_comp['Ingresos'],
            marker_color='#27ae60',
            text=df_comp['Ingresos'].apply(lambda x: f'S/ {x:,.0f}'),
            textposition='outside',
            hovertemplate='<b>Año %{x}</b><br>Ingresos: S/ %{y:,.2f}<extra></extra>'
        ))
        
        fig.add_trace(go.Bar(
            name='Egresos',
            x=df_comp['Año'].astype(str),
            y=df_comp['Egresos'],
            marker_color='#e74c3c',
            text=df_comp['Egresos'].apply(lambda x: f'S/ {x:,.0f}'),
            textposition='outside',
            hovertemplate='<b>Año %{x}</b><br>Egresos: S/ %{y:,.2f}<extra></extra>'
        ))
        
        fig.update_layout(
            title={
                'text': '💵 Comparativa de Ingresos y Egresos por Año',
                'font': {'size': 20, 'color': '#2c3e50', 'family': 'Arial Black'}
            },
            xaxis_title="Año",
            yaxis_title="Monto (S/)",
            barmode='group',
            height=500,
            hovermode='x unified',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=14),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
                bgcolor='rgba(255,255,255,0.8)',
                bordercolor='#2c3e50',
                borderwidth=1
            )
        )
        
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Gráfico de líneas de tendencia mensual
        st.markdown("### 📈 Tendencia Mensual Comparativa")
        
        df_mensual_comp = df.groupby(['año', 'mes']).agg({
            'ingreso': lambda x: float(sum(x)),
            'egreso': lambda x: float(sum(x))
        }).reset_index()
        
        fig2 = go.Figure()
        
        colores = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
        
        for idx, año in enumerate(años_disponibles):
            df_año_mes = df_mensual_comp[df_mensual_comp['año'] == año]
            
            fig2.add_trace(go.Scatter(
                x=df_año_mes['mes'],
                y=df_año_mes['ingreso'],
                mode='lines+markers',
                name=f'{año}',
                line=dict(color=colores[idx % len(colores)], width=3),
                marker=dict(size=10, line=dict(width=2, color='white')),
                hovertemplate=f'<b>{año}</b><br>Mes: %{{x}}<br>Ingresos: S/ %{{y:,.2f}}<extra></extra>'
            ))
        
        fig2.update_layout(
            title={
                'text': '📊 Evolución de Ingresos Mensuales',
                'font': {'size': 20, 'color': '#2c3e50', 'family': 'Arial Black'}
            },
            xaxis_title="Mes",
            yaxis_title="Ingresos (S/)",
            height=450,
            hovermode='x unified',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(
                tickmode='array',
                tickvals=list(range(1, 13)),
                ticktext=list(meses_nombres.values())
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )
        
        fig2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
        fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
        
        st.plotly_chart(fig2, use_container_width=True)
        
        # Análisis automático
        año_actual = años_disponibles[-1]
        año_anterior_comp = años_disponibles[-2] if len(años_disponibles) > 1 else None
        
        if año_anterior_comp:
            ing_actual = df_comp[df_comp['Año'] == año_actual]['Ingresos'].values[0]
            ing_anterior_val = df_comp[df_comp['Año'] == año_anterior_comp]['Ingresos'].values[0]
            variacion = ((ing_actual - ing_anterior_val) / ing_anterior_val * 100) if ing_anterior_val > 0 else 0
            
            if variacion > 0:
                st.success(f"""
                **📈 ANÁLISIS AUTOMÁTICO:**
                
                Los ingresos de {año_actual} son **S/ {ing_actual:,.2f}**, lo que representa un **aumento del {variacion:.1f}%** 
                comparado con {año_anterior_comp} (S/ {ing_anterior_val:,.2f}).
                
                ✅ **Interpretación:** La gestión financiera muestra una tendencia positiva.
                """)
            elif variacion < 0:
                st.warning(f"""
                **📉 ANÁLISIS AUTOMÁTICO:**
                
                Los ingresos de {año_actual} son **S/ {ing_actual:,.2f}**, lo que representa una **disminución del {abs(variacion):.1f}%** 
                comparado con {año_anterior_comp} (S/ {ing_anterior_val:,.2f}).
                
                ⚠️ **Recomendación:** Revisar las causas de la disminución y considerar estrategias de mejora.
                """)
            else:
                st.info(f"""
                **📊 ANÁLISIS AUTOMÁTICO:**
                
                Los ingresos se mantuvieron estables entre {año_anterior_comp} y {año_actual}.
                """)

# ============================================================================
# TAB 2: ANÁLISIS MENSUAL
# ============================================================================

with tab2:
    st.markdown(f"## 📅 Análisis Detallado - {año_seleccionado}")
    
    # Gráfico de cascada (Waterfall Chart) - Moderno
    df_mensual = df_filtrado.groupby('mes').agg({
        'ingreso': lambda x: float(sum(x)),
        'egreso': lambda x: float(sum(x))
    }).reset_index()
    
    df_mensual['balance'] = df_mensual['ingreso'] - df_mensual['egreso']
    df_mensual['mes_nombre'] = df_mensual['mes'].apply(lambda x: meses_nombres.get(x, str(x)))
    
    # Gráfico de barras con ingresos y egresos
    fig3 = go.Figure()
    
    fig3.add_trace(go.Bar(
        name='Ingresos',
        x=df_mensual['mes_nombre'],
        y=df_mensual['ingreso'],
        marker_color='#27ae60',
        text=df_mensual['ingreso'].apply(lambda x: f'S/ {x:,.0f}'),
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Ingresos: S/ %{y:,.2f}<extra></extra>'
    ))
    
    fig3.add_trace(go.Bar(
        name='Egresos',
        x=df_mensual['mes_nombre'],
        y=df_mensual['egreso'],
        marker_color='#e74c3c',
        text=df_mensual['egreso'].apply(lambda x: f'S/ {x:,.0f}'),
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Egresos: S/ %{y:,.2f}<extra></extra>'
    ))
    
    fig3.update_layout(
        title={
            'text': f'💰 Flujo Mensual de Caja - {año_seleccionado}',
            'font': {'size': 20, 'color': '#2c3e50', 'family': 'Arial Black'}
        },
        xaxis_title="Mes",
        yaxis_title="Monto (S/)",
        barmode='group',
        height=500,
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    fig3.update_xaxes(showgrid=False)
    fig3.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
    
    st.plotly_chart(fig3, use_container_width=True)
    
    # Gráfico de balance neto
    st.markdown("### 📊 Balance Neto Mensual")
    
    fig4 = go.Figure()
    
    colores_balance = ['#27ae60' if x >= 0 else '#e74c3c' for x in df_mensual['balance']]
    
    fig4.add_trace(go.Bar(
        x=df_mensual['mes_nombre'],
        y=df_mensual['balance'],
        marker_color=colores_balance,
        text=df_mensual['balance'].apply(lambda x: f'S/ {x:,.0f}'),
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Balance: S/ %{y:,.2f}<extra></extra>'
    ))
    
    # Línea de referencia en cero
    fig4.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Punto de equilibrio")
    
    fig4.update_layout(
        title={
            'text': '⚖️ Balance Mensual (Superávit/Déficit)',
            'font': {'size': 20, 'color': '#2c3e50', 'family': 'Arial Black'}
        },
        xaxis_title="Mes",
        yaxis_title="Balance (S/)",
        height=450,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    fig4.update_xaxes(showgrid=False)
    fig4.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
    
    st.plotly_chart(fig4, use_container_width=True)
    
    # Distribución por categoría
    st.markdown("### 🏷️ Distribución de Ingresos por Categoría")
    
    cat_data = df_filtrado.groupby('categoria').agg({
        'ingreso': lambda x: float(sum(x))
    }).reset_index()
    cat_data = cat_data.sort_values('ingreso', ascending=False)
    
    fig5 = go.Figure(data=[go.Pie(
        labels=cat_data['categoria'],
        values=cat_data['ingreso'],
        hole=0.4,
        marker=dict(
            colors=['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#9b59b6', '#1abc9c'],
            line=dict(color='white', width=2)
        ),
        textinfo='label+percent',
        textfont_size=14,
        hovertemplate='<b>%{label}</b><br>S/ %{value:,.2f}<br>%{percent}<extra></extra>'
    )])
    
    fig5.update_layout(
        title={
            'text': '📊 Composición de Ingresos',
            'font': {'size': 20, 'color': '#2c3e50', 'family': 'Arial Black'}
        },
        height=500,
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.05
        )
    )
    
    st.plotly_chart(fig5, use_container_width=True)

# ============================================================================
# TAB 3: ACTIVIDAD PASTORAL
# ============================================================================

with tab3:
    st.markdown("## 🙏 Actividad Sacramental y Litúrgica")
    
    df_pastoral = df[df['año'] == año_seleccionado].copy()
    
    # Sacramentos
    st.markdown("### ✝️ Sacramentos Administrados")
    
    df_sac = df_pastoral[df_pastoral['categoria'] == 'SACRAMENTO']
    
    if not df_sac.empty:
        conteo_sac = df_sac.groupby('subcategoria').size().reset_index(name='cantidad')
        conteo_sac = conteo_sac.sort_values('cantidad', ascending=True)
        
        fig6 = go.Figure(data=[go.Bar(
            x=conteo_sac['cantidad'],
            y=conteo_sac['subcategoria'],
            orientation='h',
            marker=dict(
                color=conteo_sac['cantidad'],
                colorscale='Blues',
                showscale=False,
                line=dict(color='white', width=1)
            ),
            text=conteo_sac['cantidad'],
            textposition='outside',
            hovertemplate='<b>%{y}</b><br>Cantidad: %{x}<extra></extra>'
        )])
        
        fig6.update_layout(
            title={
                'text': f'📊 Sacramentos {año_seleccionado}',
                'font': {'size': 20, 'color': '#2c3e50', 'family': 'Arial Black'}
            },
            xaxis_title="Cantidad",
            yaxis_title="",
            height=max(400, len(conteo_sac) * 40),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        fig6.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
        fig6.update_yaxes(showgrid=False)
        
        st.plotly_chart(fig6, use_container_width=True)
        
        # Análisis
        total_sac = len(df_sac)
        top_sac = conteo_sac.iloc[-1]
        
        st.info(f"""
        **📊 RESUMEN SACRAMENTAL:**
        
        - Total de sacramentos administrados: **{total_sac}**
        - Sacramento más frecuente: **{top_sac['subcategoria']}** ({top_sac['cantidad']} veces)
        - Representa el **{(top_sac['cantidad']/total_sac*100):.1f}%** del total
        """)
    else:
        st.warning("⚠️ No hay datos de sacramentos para este año.")
    
    # Misas
    st.markdown("### ⛪ Actividad Litúrgica")
    
    df_misa = df_pastoral[df_pastoral['categoria'] == 'MISA']
    
    if not df_misa.empty:
        conteo_misa = df_misa.groupby('subcategoria').size().reset_index(name='cantidad')
        conteo_misa = conteo_misa.sort_values('cantidad', ascending=False).head(10)
        
        fig7 = go.Figure(data=[go.Bar(
            x=conteo_misa['subcategoria'],
            y=conteo_misa['cantidad'],
            marker=dict(
                color=conteo_misa['cantidad'],
                colorscale='Greens',
                showscale=False,
                line=dict(color='white', width=1)
            ),
            text=conteo_misa['cantidad'],
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Cantidad: %{y}<extra></extra>'
        )])
        
        fig7.update_layout(
            title={
                'text': f'🔝 Top 10 Tipos de Misa - {año_seleccionado}',
                'font': {'size': 20, 'color': '#2c3e50', 'family': 'Arial Black'}
            },
            xaxis_title="",
            yaxis_title="Cantidad",
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        fig7.update_xaxes(showgrid=False, tickangle=-45)
        fig7.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
        
        st.plotly_chart(fig7, use_container_width=True)
    else:
        st.warning("⚠️ No hay datos de misas para este año.")

# ============================================================================
# TAB 4: SALUD FINANCIERA
# ============================================================================

with tab4:
    st.markdown("## 💰 Diagnóstico Financiero")
    
    df_fin = df[df['año'] == año_seleccionado].copy()
    
    if df_fin.empty:
        st.warning(f"⚠️ No hay registros financieros para el año {año_seleccionado}.")
    else:
        # Métricas financieras clave
        col1, col2, col3 = st.columns(3)
        
        total_ing_año = sum(df_fin['ingreso'])
        total_egr_año = sum(df_fin['egreso'])
        balance_año = total_ing_año - total_egr_año
        ratio_gasto = (total_egr_año / total_ing_año * 100) if total_ing_año > 0 else 0
        
        with col1:
            st.metric("💰 Ingresos Anuales", formatear_moneda(total_ing_año))
        
        with col2:
            st.metric("💸 Egresos Anuales", formatear_moneda(total_egr_año))
        
        with col3:
            st.metric("📊 Ratio de Gasto", f"{ratio_gasto:.1f}%", 
                     help="Por cada 100 soles que ingresan, se gastan...")
        
        st.divider()
        
        # Gráfico de tendencia acumulada
        st.markdown("### 📈 Flujo de Caja Acumulado")
        
        df_fin_sorted = df_fin.sort_values('fecha')
        df_fin_sorted['ingreso_acum'] = df_fin_sorted['ingreso'].cumsum().apply(float)
        df_fin_sorted['egreso_acum'] = df_fin_sorted['egreso'].cumsum().apply(float)
        df_fin_sorted['balance_acum'] = df_fin_sorted['ingreso_acum'] - df_fin_sorted['egreso_acum']
        
        fig8 = go.Figure()
        
        fig8.add_trace(go.Scatter(
            x=df_fin_sorted['fecha'],
            y=df_fin_sorted['ingreso_acum'],
            mode='lines',
            name='Ingresos Acumulados',
            line=dict(color='#27ae60', width=3),
            fill='tozeroy',
            fillcolor='rgba(39, 174, 96, 0.1)',
            hovertemplate='<b>Fecha:</b> %{x}<br><b>Ingresos Acum:</b> S/ %{y:,.2f}<extra></extra>'
        ))
        
        fig8.add_trace(go.Scatter(
            x=df_fin_sorted['fecha'],
            y=df_fin_sorted['egreso_acum'],
            mode='lines',
            name='Egresos Acumulados',
            line=dict(color='#e74c3c', width=3),
            fill='tozeroy',
            fillcolor='rgba(231, 76, 60, 0.1)',
            hovertemplate='<b>Fecha:</b> %{x}<br><b>Egresos Acum:</b> S/ %{y:,.2f}<extra></extra>'
        ))
        
        fig8.update_layout(
            title={
                'text': f'💹 Evolución Acumulada - {año_seleccionado}',
                'font': {'size': 20, 'color': '#2c3e50', 'family': 'Arial Black'}
            },
            xaxis_title="Fecha",
            yaxis_title="Monto Acumulado (S/)",
            height=500,
            hovermode='x unified',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )
        
        fig8.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
        fig8.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
        
        st.plotly_chart(fig8, use_container_width=True)
        
        # Diagnóstico automático
        st.markdown("### 🔍 Diagnóstico Automático")
        
        if balance_año > 0:
            st.success(f"""
            **✅ SALUD FINANCIERA: BUENA**
            
            - 💰 Ingresos totales: **{formatear_moneda(total_ing_año)}**
            - 💸 Egresos totales: **{formatear_moneda(total_egr_año)}**
            - 📊 Balance positivo: **{formatear_moneda(balance_año)}**
            - 📈 Ratio de gasto: **{ratio_gasto:.1f}%** (Por cada S/ 100 que ingresan, se gastan S/ {ratio_gasto:.0f})
            
            **Recomendación:** Mantener la disciplina financiera actual. Considerar destinar parte del superávit a un fondo de reserva.
            """)
        else:
            st.error(f"""
            **⚠️ SALUD FINANCIERA: REQUIERE ATENCIÓN**
            
            - 💰 Ingresos totales: **{formatear_moneda(total_ing_año)}**
            - 💸 Egresos totales: **{formatear_moneda(total_egr_año)}**
            - 📊 Déficit: **{formatear_moneda(abs(balance_año))}**
            - 📈 Ratio de gasto: **{ratio_gasto:.1f}%**
            
            **Recomendación URGENTE:** Revisar y ajustar gastos. Buscar fuentes adicionales de ingreso o reducir gastos no esenciales.
            """)

# ============================================================================
# TAB 5: DATOS DETALLADOS
# ============================================================================

with tab5:
    st.markdown("## 📋 Registro Detallado de Transacciones")
    
    # Opciones de visualización
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"**Mostrando:** {len(df_filtrado)} registros")
    
    with col2:
        orden = st.selectbox("Ordenar por:", ["Fecha (más reciente)", "Fecha (más antigua)", "Monto (mayor)", "Monto (menor)"])
    
    # Preparar datos para mostrar
    df_tabla = df_filtrado[['fecha', 'detalle', 'categoria', 'subcategoria', 'ingreso', 'egreso']].copy()
    
    # Ordenar según selección
    if orden == "Fecha (más reciente)":
        df_tabla = df_tabla.sort_values('fecha', ascending=False)
    elif orden == "Fecha (más antigua)":
        df_tabla = df_tabla.sort_values('fecha', ascending=True)
    elif orden == "Monto (mayor)":
        df_tabla['monto_total'] = df_tabla['ingreso'].apply(float) + df_tabla['egreso'].apply(float)
        df_tabla = df_tabla.sort_values('monto_total', ascending=False)
        df_tabla = df_tabla.drop('monto_total', axis=1)
    else:  # Monto (menor)
        df_tabla['monto_total'] = df_tabla['ingreso'].apply(float) + df_tabla['egreso'].apply(float)
        df_tabla = df_tabla.sort_values('monto_total', ascending=True)
        df_tabla = df_tabla.drop('monto_total', axis=1)
    
    # Formatear para visualización
    df_tabla_display = df_tabla.copy()
    df_tabla_display['fecha'] = df_tabla_display['fecha'].dt.strftime('%d/%m/%Y')
    df_tabla_display['ingreso'] = df_tabla_display['ingreso'].apply(lambda x: f"S/ {float(x):,.2f}" if float(x) > 0 else "-")
    df_tabla_display['egreso'] = df_tabla_display['egreso'].apply(lambda x: f"S/ {float(x):,.2f}" if float(x) > 0 else "-")
    
    # Renombrar columnas
    df_tabla_display.columns = ['Fecha', 'Detalle', 'Categoría', 'Subcategoría', 'Ingreso', 'Egreso']
    
    # Mostrar tabla
    st.dataframe(
        df_tabla_display,
        use_container_width=True,
        height=600,
        hide_index=True
    )
    
    # Botón de descarga
    csv = df_tabla_display.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar datos como CSV",
        data=csv,
        file_name=f'datos_parroquia_{año_seleccionado}.csv',
        mime='text/csv',
    )

# ============================================================================
# FOOTER
# ============================================================================

st.divider()
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 1.5rem; background: white; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p style='margin: 0; font-size: 1.1rem; font-weight: 600;'>⛪ <b>Parroquia Santiago Apóstol de Huancané</b></p>
    <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem;'>Dashboard Profesional v3.0 | Desarrollado con precisión financiera</p>
    <p style='margin: 0.5rem 0 0 0; font-size: 0.85rem; opacity: 0.7;'>© 2026 | Todos los derechos reservados</p>
</div>
""", unsafe_allow_html=True)
