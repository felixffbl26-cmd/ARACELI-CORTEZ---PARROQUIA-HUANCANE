# Continuación del archivo app_v3.py
# Agregar este código al final del archivo anterior

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
        año_anterior = años_disponibles[-2] if len(años_disponibles) > 1 else None
        
        if año_anterior:
            ing_actual = df_comp[df_comp['Año'] == año_actual]['Ingresos'].values[0]
            ing_anterior = df_comp[df_comp['Año'] == año_anterior]['Ingresos'].values[0]
            variacion = ((ing_actual - ing_anterior) / ing_anterior * 100) if ing_anterior > 0 else 0
            
            if variacion > 0:
                st.success(f"""
                **📈 ANÁLISIS AUTOMÁTICO:**
                
                Los ingresos de {año_actual} son **S/ {ing_actual:,.2f}**, lo que representa un **aumento del {variacion:.1f}%** 
                comparado con {año_anterior} (S/ {ing_anterior:,.2f}).
                
                ✅ **Interpretación:** La gestión financiera muestra una tendencia positiva.
                """)
            elif variacion < 0:
                st.warning(f"""
                **📉 ANÁLISIS AUTOMÁTICO:**
                
                Los ingresos de {año_actual} son **S/ {ing_actual:,.2f}**, lo que representa una **disminución del {abs(variacion):.1f}%** 
                comparado con {año_anterior} (S/ {ing_anterior:,.2f}).
                
                ⚠️ **Recomendación:** Revisar las causas de la disminución y considerar estrategias de mejora.
                """)
            else:
                st.info(f"""
                **📊 ANÁLISIS AUTOMÁTICO:**
                
                Los ingresos se mantuvieron estables entre {año_anterior} y {año_actual}.
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

# Continúa en el siguiente bloque...
