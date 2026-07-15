import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="두더지 게임",
    page_icon="🐹",
    layout="centered"
)

# 상태 저장
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------------
# 홈 화면
# -------------------------
def home():

    st.title("🐹 두더지 게임")
    st.write("재미있는 두더지 잡기 게임입니다!")

    st.divider()

    col1, col2 = st.columns(2)

    # 시작 버튼
    with col1:
        if st.button("🎮 시작하기", use_container_width=True):
            st.session_state.page = "game"
            st.rerun()

    # 설명 버튼
    with col2:
        if st.button("📖 게임 설명", use_container_width=True):
            st.session_state.page = "info"
            st.rerun()


# -------------------------
# 설명 화면
# -------------------------
def info():

    st.title("📖 게임 설명")

    st.write("""
    ## 🐹 두더지 게임 방법

    1. 게임 시작 버튼을 눌러 게임을 시작합니다.
    2. 나타나는 두더지를 클릭해서 점수를 얻습니다.
    3. 빠르게 두더지를 잡아 높은 점수를 기록하세요!

    앞으로 추가될 기능:
    - 레벨 시스템
    - 점수 시스템
    - 난이도 증가
    - 최고 점수 저장
    """)

    if st.button("🏠 홈으로 돌아가기"):
        st.session_state.page = "home"
        st.rerun()


# -------------------------
# 게임 화면
# -------------------------
def game():

    st.title("🎮 두더지 게임")

    st.write("여기는 게임 화면입니다.")

    # 추후 두더지 게임 코드 추가 위치

    if st.button("🏠 홈으로 돌아가기"):
        st.session_state.page = "home"
        st.rerun()


# -------------------------
# 페이지 이동
# -------------------------
if st.session_state.page == "home":
    home()

elif st.session_state.page == "info":
    info()

elif st.session_state.page == "game":
    game()
