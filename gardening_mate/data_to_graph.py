import streamlit as st
import pandas as pd
import altair as alt

st.title("토양 속 수분율 그래프")

csv_file = st.file_uploader("추출된 CSV 파일 업로드", type="csv")

if csv_file:
        df = pd.read_csv(csv_file, names=['date', 'moisture_rate'])

        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['moisture_rate'] = pd.to_numeric(df['moisture_rate'], errors='coerce')

        df = df.dropna(subset=['date', 'moisture_rate'])

        df['time'] = df['date'].dt.strftime('%H:%M:%S')

        st.write("수분율 데이터", df[['date', 'moisture_rate']].head())
        
        chart = alt.Chart(df).mark_line().encode(
                x=alt.X('time:N', title='시간', axis=alt.Axis(labelAngle=-45)),
                y=alt.Y('moisture_rate:Q', title='수분율')
        ).properties(
                title="시간 별 토양 속 수분율",
                width=1000,
                height=400
        )
        
        st.altair_chart(chart, use_container_width=True)