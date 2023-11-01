import streamlit as st

st.set_page_config(
    page_title='공동교육과정',
    page_icon='🦄'
)

menu = st.sidebar.selectbox('MENU',['로그인','자기소개','선택과목 조사','기타'])

if menu == '자기소개':
    st.title('자기소개')
    st.video('https://www.youtube.com/watch?v=phLb8LDDE3k')
elif menu == '선택과목 조사':
    st.title('함지고등학교 선택과목')
    st.subheader('탐구과목')
    선택과목 = st.multiselect(
        '당신이 배울 과목은?(3가지)',
        ['화학2','물리2','지구2','생명2']
    )
    i = len(선택과목)
    if i < 3 :
        st.write(':red[3개를 골라주세요]')
    elif i > 3:
        st.write(':red[3개만 골라주세요]')

    st.subheader('국어')
    st.radio('당신의 배울 과목은?', ['화법과 작문', '언어와 매체'])


    st.subheader('수학')
    st.radio('당신의 배울 과목은?', ['미적분', '확률과 통계'])

    st.subheader('예술')
    st.radio('당신의 배울 과목은?', ['음악', '미술'])

    butt = st.button('제출')
    text = ''
    for value in 선택과목:
        text += value+ " "
    if butt:
        st.write('탐구과목은 '+text+'를 선택하셨습니다.')
    st.image('ghost.jpg')
elif menu == '기타':
    st.title('기타')
elif menu == '로그인':
    st.title('로그인😊')
    id = st.text_input('아이디', placeholder='아이디를 입력하세요.')
    pw = st.text_input('비밀번호', type='password', placeholder='비밀번호를 입력하세요.')
    login = st.button('로그인')
    if login:
        if id == '123' and pw == '1234':
            st.write('로그인 성공')
            st.balloons()
        else:
            st.write(':red[로그인 실패]')

# 짜장면 = st.checkbox('짜장면')
# 탕수육 = st.checkbox('탕수육')
# 짬뽕 = st.checkbox('짬뽕')

# a = ''
# if 짜장면:
#     a = a + '짜장면 '
# if 탕수육:
#     a = a + '탕수육 '
# if 짬뽕:
#     a = a + '짬뽕 '
# st.write(a + '을 선택하셨습니다.')

# 성별 = st.radio('당신의 성별은?', ['남자', '여자'])
# st.write('당신의 성별은 '+성별+'입니다.')

# email = st.selectbox(
#     'E-mail을 선택하세요',
#     ['gmail.com', 'naver.com', 'hanmail.com']
# )

# food = st.multiselect(
#     '당신이 좋아하는 음식은?',
#     ['피자','햄버거','삻은계란','파스타',]
# )

# st.write('이설희의 홈페이지')
# st.subheader('this is subheader')
# st.header('this is header')
# st.title('this is title')
# st.caption('this is caption')
# st.code('x = 10+20')

# btn=st.button('클릭')
# if btn:
#     st.write('버튼 클릭')
# text = '이 버튼을 클릭하면 파일을 다운 받을 수 있습니다.'
# download_btn = st.download_button('다운로드', text)
# link_btn = st.link_button('네이버',"https://www.naver.com")
# link_btn = st.link_button('구글',"https://www.google.com")
# link_btn = st.link_button('함지고',"https://hamji.dge.hs.kr/hamjih/main.do?sysId=hamjih")

# checkbox = st.checkbox('동의')
# if checkbox:
#     st.write('동의하셨습니다.')

