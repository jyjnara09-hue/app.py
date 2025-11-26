import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="숫자 맞추기 게임", page_icon="🎯")

st.title("🎯 숫자 맞추기 게임")
st.write("1부터 최대값 사이의 숫자를 맞춰보세요!")

# 난이도 선택
level = st.selectbox("난이도 선택", ("보통 (1~100)", "쉬움 (1~20)", "어려움 (1~500)"))
if level == "쉬움 (1~20)":
    MIN, MAX = 1, 20
elif level == "어려움 (1~500)":
    MIN, MAX = 1, 500
else:
    MIN, MAX = 1, 100

# 세션 상태 초기화
if "answer" not in st.session_state or "max_val" not in st.session_state:
    st.session_state.answer = random.randint(MIN, MAX)
    st.session_state.count = 0
    st.session_state.max_val = MAX

# 난이도 변경 시 정답 재설정
if st.session_state.get("max_val", None) != MAX:
    st.session_state.answer = random.randint(MIN, MAX)
    st.session_state.count = 0
    st.session_state.max_val = MAX

st.write(f"범위: **{MIN} ~ {MAX}**")

# 사용자 입력
guess = st.number_input("숫자를 입력하세요", min_value=MIN, max_value=MAX, step=1, value=MIN)

# 버튼들
col1, col2, col3 = st.columns([1, 1, 1])

# 제출 버튼
with col1:
    if st.button("제출"):
        st.session_state.count += 1
        if guess > st.session_state.answer:
            st.warning("🔽 다운!")
        elif guess < st.session_state.answer:
            st.warning("🔼 업!")
        else:
            st.success(f"🎉 정답입니다! ({st.session_state.answer})")
            st.write(f"총 시도 횟수: **{st.session_state.count}번**")

# 힌트 버튼
with col2:
    if st.button("힌트"):
        diff = st.session_state.answer - guess
        if diff == 0:
            st.info("이미 정답을 맞췄어요!")
        else:
            if abs(diff) <= max(1, (MAX - MIN) // 10):
                st.info("정답에 아주 가까워요!")
            elif diff > 0:
                st.info("정답은 입력한 숫자보다 큽니다.")
            else:
                st.info("정답은 입력한 숫자보다 작습니다.")

# 재시작 버튼
with col3:
    if st.button("게임 재시작"):
        st.session_state.answer = random.randint(MIN, MAX)
        st.session_state.count = 0
        st.experimental_rerun()
