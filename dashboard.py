import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

COLORS = {
    'yellow': '#FFD84D',
    'red':    '#f87171',
    'green':  '#4ade80',
    'bg':     '#1a1a1a',
    'border': '#2a2a2a',
    'text':   '#ffffff',
    'muted':  '#555555',
}

PLOT_LAYOUT = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='#888888',
    font_size=11,
    margin=dict(l=10, r=10, t=10, b=10),
    showlegend=False,
)

def show():
    st.markdown("""
    <div style='margin-bottom:1.5rem;'>
        <h1 style='font-size:1.6rem;font-weight:800;color:#1a1a1a;margin:0;'>
            HR Attrition Dashboard
        </h1>
        <p style='font-size:11px;color:#555;margin-top:4px;'>
            IBM HR Analytics · 1,470 employees · Logistic Regression Model
        </p>
    </div>
    """, unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    metrics = [
        ("Total Employees", "1,470", "IBM HR dataset", "#fff"),
        ("Attrition Rate", "16.1%", "237 employees left", "#f87171"),
        ("Avg Salary (Stayed)", "₹6,833", "vs ₹4,787 who left", "#4ade80"),
        ("Model Recall", "59%", "Leavers identified", "#FFD84D"),
    ]
    for col, (label, val, sub, color) in zip([m1, m2, m3, m4], metrics):
        with col:
            st.markdown(f"""
            <div style='background:#fff;border:1px solid #e0d9ce;
                border-radius:12px;padding:1rem 1.2rem;'>
                <div style='font-size:10px;color:#555;text-transform:uppercase;
                    letter-spacing:1px;margin-bottom:6px;'>{label}</div>
                <div style='font-size:24px;font-weight:800;color:{color};'>{val}</div>
                <div style='font-size:10px;color:#666;margin-top:3px;'>{sub}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""<div style='background:#fff;border:1px solid #e0d9ce;
            border-radius:12px;padding:1.2rem 1.4rem;'>
            <div style='font-size:11px;font-weight:700;text-transform:uppercase;
                letter-spacing:1px;color:#1a1a1a;'>Attrition by Department</div>
            <div style='font-size:10px;color:#555;margin-bottom:0.5rem;'>
                % of employees who left per department</div>
        """, unsafe_allow_html=True)

        dept_data = pd.DataFrame({
            'Department': ['Human Resources', 'Research & Development', 'Sales'],
            'Attrition Rate': [19.0, 13.8, 20.6]
        })
        fig = px.bar(dept_data, x='Department', y='Attrition Rate',
                     color='Attrition Rate',
                     color_continuous_scale=[[0, '#2a2a2a'], [1, '#FFD84D']])
        fig.update_traces(marker_cornerradius=4)
        fig.update_layout(**PLOT_LAYOUT,
                          yaxis_title='Attrition %',
                          coloraxis_showscale=False,
                          height=250)
        fig.update_yaxes(gridcolor='#222', range=[0, 25])
        fig.update_xaxes(gridcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("""<div style='background:#fff;border:1px solid #e0d9ce;
            border-radius:12px;padding:1.2rem 1.4rem;'>
            <div style='font-size:11px;font-weight:700;text-transform:uppercase;
                letter-spacing:1px;color:##1a1a1a;'>Monthly Income vs Attrition</div>
            <div style='font-size:10px;color:#555;margin-bottom:0.5rem;'>
                Average income: stayed vs left</div>
        """, unsafe_allow_html=True)

        income_data = pd.DataFrame({
            'Status': ['Stayed', 'Left'],
            'Avg Income': [6833, 4787],
            'Color': ['#4ade80', '#f87171']
        })
        fig2 = go.Figure(go.Bar(
            x=income_data['Status'],
            y=income_data['Avg Income'],
            marker_color=income_data['Color'],
            marker_cornerradius=4,
            width=0.4
        ))
        fig2.update_layout(**PLOT_LAYOUT, height=250,
                           yaxis_title='Monthly Income (₹)')
        fig2.update_yaxes(gridcolor='#222', range=[0, 8500])
        fig2.update_xaxes(gridcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    c3, c4 = st.columns(2)

    with c3:
        st.markdown("""<div style='background:#fff;border:1px solid #e0d9ce;
            border-radius:12px;padding:1.2rem 1.4rem;'>
            <div style='font-size:11px;font-weight:700;text-transform:uppercase;
                letter-spacing:1px;color:##1a1a1a;'>Attrition by Job Role</div>
            <div style='font-size:10px;color:#555;margin-bottom:0.5rem;'>
                Top roles by exit rate</div>
        """, unsafe_allow_html=True)

        role_data = pd.DataFrame({
            'Role': ['Sales Rep', 'Lab Technician', 'HR', 'Sales Exec',
                     'Research Sci', 'Mfg Director', 'Healthcare Rep',
                     'Manager', 'Research Dir'],
            'Rate': [39.8, 23.9, 23.1, 17.5, 16.1, 6.9, 6.9, 4.9, 2.5]
        }).sort_values('Rate')

        fig3 = px.bar(role_data, x='Rate', y='Role', orientation='h',
                      color='Rate',
                      color_continuous_scale=[[0, '#2a2a2a'], [1, '#FFD84D']])
        fig3.update_traces(marker_cornerradius=4)
        fig3.update_layout(**PLOT_LAYOUT, height=300,
                           xaxis_title='Attrition %',
                           coloraxis_showscale=False)
        fig3.update_xaxes(gridcolor='#222')
        fig3.update_yaxes(gridcolor='rgba(0,0,0,0)', tickfont_size=10)
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c4:
        st.markdown("""<div style='background:#fff;border:1px solid #e0d9ce;
            border-radius:12px;padding:1.2rem 1.4rem;'>
            <div style='font-size:11px;font-weight:700;text-transform:uppercase;
                letter-spacing:1px;color:##1a1a1a;'>Top 10 Risk Factors</div>
            <div style='font-size:10px;color:#555;margin-bottom:0.8rem;'>
                Feature importance from model coefficients</div>
        """, unsafe_allow_html=True)

        features = [
            ('YearsAtCompany', 0.97),
            ('OverTime_Yes', 0.93),
            ('Lab Technician', 0.90),
            ('Marital_Single', 0.78),
            ('YearsInRole', 0.72),
            ('Travel_Frequently', 0.71),
            ('Dept_Sales', 0.62),
            ('Sales Rep Role', 0.61),
            ('YearsWithMgr', 0.56),
            ('HR Role', 0.54),
        ]
        for name, val in features:
            pct = int(val * 100)
            color = '#f87171' if name in ['OverTime_Yes', 'Travel_Frequently'] else '#FFD84D'
            st.markdown(f"""
            <div style='display:flex;align-items:center;gap:8px;margin-bottom:7px;'>
                <span style='font-size:10px;color:#888;width:130px;
                    text-align:right;flex-shrink:0;'>{name}</span>
                <div style='flex:1;background:#222;border-radius:4px;height:5px;'>
                    <div style='width:{pct}%;height:5px;border-radius:4px;
                        background:{color};'></div>
                </div>
                <span style='font-size:10px;color:#555;width:30px;'>{val}</span>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background:#fff;border:1px solid #e0d9ce;border-radius:12px;
        padding:1.2rem 1.4rem;'>
        <div style='font-size:11px;font-weight:700;text-transform:uppercase;
            letter-spacing:1px;color:##1a1a1a;margin-bottom:1rem;'>
            Model Comparison Results</div>
    """, unsafe_allow_html=True)

    results_df = pd.DataFrame({
        'Model': ['Logistic Regression ✅', 'Random Forest', 'Gradient Boosting'],
        'Accuracy': ['72%', '87%', '87%'],
        'Recall (Leavers)': ['59%', '8%', '18%'],
        'AUC-ROC': ['0.766', '0.734', '0.779'],
        'Best For HR?': ['Yes — catches most leavers', 'No — misses 92%', 'No — misses 82%']
    })
    st.dataframe(
        results_df,
        use_container_width=True,
        hide_index=True
    )
    st.markdown("</div>", unsafe_allow_html=True)
