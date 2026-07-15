if "level" not in st.session_state:
    st.session_state.level = 1

if "speed" not in st.session_state:
    st.session_state.speed = 2.0
    col1, col2 = st.columns(2)

col1.metric("레벨", st.session_state.level)
col2.metric("두더지 등장 시간", f"{st.session_state.speed:.1f}초")
if st.button("🚀 속도 UP"):

    if st.session_state.level < 5:
        st.session_state.level += 1
        st.session_state.speed -= 0.4

        st.success(
            f"Level {st.session_state.level} "
            f"(등장 시간 {st.session_state.speed:.1f}초)"
        )

    else:
        st.info("이미 최고 레벨입니다.")
   if st.button("속도 UP"):
    if st.session_state.level < 5:
        st.session_state.level += 1

    st.rerun()
