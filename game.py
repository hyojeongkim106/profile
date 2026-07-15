import streamlit as st
import random
import time

st.set_page_config(
    page_title="사다리 게임",
    page_icon="🪜"
)

st.title("🪜 사다리 타기 게임")


# 참가자
players = ["철수", "영희", "민수", "지수"]

# 결과
results = ["꽝", "커피", "치킨", "상품"]


# 사다리 생성
if "ladder" not in st.session_state:
    ladder = []

    for y in range(8):
        row = []

        for x in range(len(players)-1):
            row.append(random.choice([0,1]))

        ladder.append(row)

    st.session_state.ladder = ladder


# 사다리 그리기
st.subheader("🪜 사다리")

for y, row in enumerate(st.session_state.ladder):

    line = ""

    for x in range(len(players)):

        line += "│"

        if x < len(players)-1:
            if row[x]:
                line += "──"
            else:
                line += "  "

    st.write(line)


st.divider()


if st.button("🎮 시작"):

    start = st.selectbox(
        "출발자 선택",
        players
    )

    pos = players.index(start)

    st.write(f"🚶 {start} 출발!")

    box = st.empty()

    # 이동
    for y, row in enumerate(st.session_state.ladder):

        if pos > 0 and row[pos-1]:
            pos -= 1

        elif pos < len(players)-1 and row[pos]:
            pos += 1


        ladder_view = ""

        for i in range(len(players)):
            if i == pos:
                ladder_view += "🟢"
            else:
                ladder_view += "│"

        box.write(ladder_view)

        time.sleep(0.5)


    st.success(
        f"🎉 결과 : {results[pos]}"
    )
