import streamlit as st
import random
import time


st.set_page_config(
    page_title="🐹 두더지 게임",
    page_icon="🐹",
    layout="centered"
)

# ------------------------
# Session State
# ------------------------
if "level" not in st.session_state:
    st.session_state.level = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "mole" not in st.session_state:
    st.session_state.mole = random.randint(0,8)

if "last_move" not in st.session_state:
    st.session_state.last_move = time.time()

# ------------------------
# 레벨별 속도
# ------------------------
MOLE_SPEED = max(0.4, 2.0 - (st.session_state.level-1)*0.4)

# 0.1초마다 새로고침
st_autorefresh(interval=100,key="refresh")

# ------------------------
# 두더지 이동
# ------------------------
if time.time()-st.session_state.last_move >= MOLE_SPEED:
    st.session_state.mole=random.randint(0,8)
    st.session_state.last_move=time.time()

# ------------------------
# 화면
# ------------------------
st.title("🐹 두더지 게임")

c1,c2,c3=st.columns(3)

c1.metric("레벨",st.session_state.level)
c2.metric("점수",st.session_state.score)
c3.metric("속도",f"{MOLE_SPEED:.1f}초")

st.write("---")

# ------------------------
# 게임판
# ------------------------
for r in range(3):

    cols=st.columns(3)

    for c in range(3):

        idx=r*3+c

        if idx==st.session_state.mole:
            text="🐹"
        else:
            text="🟩"

        if cols[c].button(text,key=idx):

            if idx==st.session_state.mole:

                st.session_state.score+=1
                st.session_state.mole=random.randint(0,8)
                st.session_state.last_move=time.time()
                st.rerun()

st.write("---")

# ------------------------
# 다음 레벨
# ------------------------
if st.button("➡️ 다음 레벨"):

    if st.session_state.level<5:

        st.session_state.level+=1

        st.success(f"Level {st.session_state.level}")

    else:

        st.balloons()
        st.success("🏆 모든 레벨 클리어!")

# ------------------------
# 다시 시작
# ------------------------
if st.button("🔄 처음부터"):

    st.session_state.level=1
    st.session_state.score=0
    st.session_state.mole=random.randint(0,8)
    st.session_state.last_move=time.time()

    st.rerun()
