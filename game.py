import streamlit as st
import random

st.set_page_config(
    page_title="랜덤 가챠 뽑기",
    page_icon="🎁"
)

st.title("🎁 랜덤 가챠 뽑기")


# --------------------
# 아이템 데이터
# --------------------
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


# --------------------
# 기록 저장
# --------------------
if "history" not in st.session_state:
    st.session_state.history = []


if "last_item" not in st.session_state:
    st.session_state.last_item = None



# --------------------
# 가챠 함수
# --------------------
def gacha():

    number = random.randint(1, 100)

    total = 0

    for item in items:

        total += item["chance"]

        if number <= total:
            return item



# --------------------
# 뽑기 버튼
# --------------------
if st.button("🎰 가챠 뽑기"):

    result = gacha()

    st.session_state.last_item = result

    st.session_state.history.append(result)



# --------------------
# 결과 창
# --------------------
if st.session_state.last_item:

    item = st.session_state.last_item

    st.success("🎉 아이템 획득!")

    st.subheader(item["name"])

    st.write("📖 설명")
    st.info(item["description"])



# --------------------
# 기록
# --------------------
st.divider()

st.subheader("📜 뽑기 기록")


if len(st.session_state.history) == 0:

    st.write("아직 뽑은 아이템이 없습니다.")

else:

    for i, item in enumerate(
        reversed(st.session_state.history),
        1
    ):

        with st.expander(
            f"{i}번째 뽑기 : {item['name']}"
        ):

            st.write(
                item["description"]
            )



# --------------------
# 초기화
# --------------------
if st.button("🔄 기록 초기화"):

    st.session_state.history = []
    st.session_state.last_item = None

    st.rerun()
