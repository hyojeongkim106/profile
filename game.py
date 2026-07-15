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
    {
        "name": "🌟 전설의 검",
        "chance": 5,
        "description": "최강의 공격력을 가진 전설 등급 무기입니다. 모든 적에게 강력한 피해를 줍니다."
    },
    {
        "name": "💎 영웅의 방패",
        "chance": 15,
        "description": "높은 방어력을 가진 영웅 등급 장비입니다. 피해를 크게 감소시킵니다."
    },
    {
        "name": "🔷 마법 보석",
        "chance": 30,
        "description": "마법 능력을 올려주는 희귀 아이템입니다."
    },
    {
        "name": "🟩 낡은 나무 검",
        "chance": 50,
        "description": "흔하게 얻을 수 있는 일반 아이템입니다. 초보자에게 적합합니다."
    }
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
