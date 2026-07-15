import streamlit as st
import random

st.set_page_config(
    page_title="사다리 게임",
    page_icon="🪜"
)

st.title("🪜 사다리 게임")

# 참가자 입력
names = st.text_input(
    "참가자 이름을 입력하세요 (쉼표로 구분)",
    "철수,영희,민수,지수"
)

# 결과 입력
results = st.text_input(
    "결과를 입력하세요 (쉼표로 구분)",
    "꽝,커피,간식,선물"
)


if st.button("🎮 사다리 시작"):

    people = [x.strip() for x in names.split(",")]
    prizes = [x.strip() for x in results.split(",")]

    if len(people) != len(prizes):
        st.error("참가자 수와 결과 개수가 같아야 합니다.")

    else:
        st.divider()
        st.subheader("🪜 결과")

        random.shuffle(prizes)

        for person, prize in zip(people, prizes):
            st.write(f"👤 {person}  ➡️  🎁 {prize}")

        st.success("사다리 게임 종료!")
