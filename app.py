import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

fig = go.Figure()

df = pd.read_csv('./data/mydata.csv')

# global variable
ur1 = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'

st.title('This is my first webapp!!')
col1, col2 = st.columns((4, 1))
with col1:
    with st.expander('SubContent1...'):
        st.subheader('SubContent1...')
        st.video(ur1)

    with st.expander('SubContent2...'):
        st.subheader('Image Content...')
        st.image('./images/catdog.jpg')

    with st.expander('SubContent3...'):
        st.subheader('HTML Content...')
        import streamlit.components.v1 as htmlviewer
        with open('./htmls/index.html', 'r', encoding='utf-8') as f:
            html1 = f.read()
            f.close()
        htmlviewer.html(html1, height=800)

    with st.expander('SubContent4...'):
        st.subheader('Data App Content...')
        st.table(df)
        st.write(df.describe())
        # fig, ax = plt.subplots(figsize=(20,10))
        # df.plot(ax=ax)
        # plt.savefig('./images/mygraph.png')
        # st.image('./images/mygraph.png')

        # 막대 그래프: 학생별 과목 점수
        st.subheader("학생별 과목 점수 (막대 그래프)")
        fig_bar = px.bar(
            df,
            x="name",
            y=["kor", "eng", "math", "info"],
            barmode="group",
            title="학생별 과목별 점수 비교",
            labels={"name": "학생 이름", "value": "점수", "variable": "과목"},
            color_discrete_sequence=px.colors.qualitative.Plotly
        )
        fig_bar.update_layout(
            xaxis_title="학생 이름",
            yaxis_title="점수",
            legend_title="과목",
            template="plotly_white"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

        # 과목 선택 드롭다운
        st.subheader("선택한 과목 점수 (선 그래프)")
        subject = st.selectbox("시각화할 과목을 선택하세요:", options=["kor", "eng", "math", "info"])

        # 선 그래프: 선택한 과목의 점수
        fig_line = px.line(
            df,
            x="name",
            y=subject,
            title=f"학생별 {subject.upper()} 점수",
            labels={"name": "학생 이름", subject: "점수"},
            markers=True,
            color_discrete_sequence=["#1a73e8"]
        )
        fig_line.update_layout(
            xaxis_title="학생 이름",
            yaxis_title="점수",
            template="plotly_white"
        )
        st.plotly_chart(fig_line, use_container_width=True)

        # 추가 정보
        st.markdown("""
        ### 설명
        - **막대 그래프**: 각 학생의 국어, 영어, 수학, 정보 과목 점수를 비교합니다.
        - **선 그래프**: 선택한 과목의 점수를 학생별로 시각화합니다.
        - 데이터는 Pandas DataFrame을 사용하며, Plotly Express로 인터랙티브 그래프를 생성했습니다.
        """)




with col2:
    with st.expander('Tips...'):
        st.info('Tips........')