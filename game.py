import streamlit as st
import random

st.set_page_config(
    page_title="랜덤 가챠 뽑기",
    page_icon="🎁"
)

st.title("🎁 랜덤 가챠 뽑기")

# 뽑기 결과 저장
if "history" not in st.session_state:
    st.session_state.history = []


# 가챠 목록
items = [
    ("🌟 전설 아이템", 5),
    ("💎 영웅 아이템", 15),
    ("🔷 희귀 아이템", 30),
    ("🟩 일반 아이템", 50)
]


def gacha():

    rand = random.randint(1, 100)

    total = 0

    for item, chance in items:
        total += chance

        if rand <= total:
            return item



st.write("버튼을 눌러 랜덤 아이템을 뽑아보세요!")

if st.button("🎰 가챠 뽑기"):

    result = gacha()

    st.session_state.history.append(result)

    st.success(f"획득 결과 : {result}")



st.divider()

if st.button("📖 아이템 설명 보기"):

    st.subheader("📖 아이템 설명")

    for item in items:

        with st.expander(item["name"]):

            st.write(item["description"])

            st.write(
                f"획득 확률 : {item['chance']}%"
            )



st.divider()

st.subheader("📜 뽑기 기록")

if len(st.session_state.history) == 0:
    st.write("아직 뽑은 기록이 없습니다.")

else:
    for i, item in enumerate(
        reversed(st.session_state.history),
        1
    ):
        st.write(
            f"{i}번째 뽑기 : {item}"
        )


# 초기화
if st.button("🔄 기록 초기화"):

    st.session_state.history = []

    st.rerun()
