import streamlit as st
import random
import math

g = 9.81  # 중력 가속도 (m/s^2)

st.set_page_config(page_title="진자 길이 맞추기 게임", page_icon="⚙️")
st.title("⚙️ 진자 길이 맞추기 게임")
st.write("주어진 주기(T)에 해당하는 진자의 길이(L)를 맞춰보세요! (단위: m)")

# 랜덤 주기 생성 (1~5초)
T = round(random.uniform(1.0, 5.0), 2)
st.write(f"주기: **{T} 초**")

# 세션 상태 초기화
if "answer" not in st.session_state:
    st.session_state.answer = round((T/(2*math.pi))**2 * g, 2)
    st.session_state.count = 0

# 사용자 입력
guess = st.number_input("추측한 진자 길이(L)를 입력하세요 (m)", min_value=0.1, max_value=10.0, step=0.01, value=1.0)

# 제출 버튼
if st.button("제출"):
    st.session_state.count += 1
    if abs(guess - st.session_state.answer) < 0.05:
        st.success(f"🎉 정답입니다! 진자 길이 L = {st.session_state.answer} m")
        st.write(f"총 시도 횟수: **{st.session_state.count}번**")
    elif guess < st.session_state.answer:
        st.warning("🔼 길이가 더 깁니다!")
    else:
        st.warning("🔽 길이가 더 짧습니다!")

# 재시작 버튼
if st.button("게임 재시작"):
    T = round(random.uniform(1.0, 5.0), 2)
    st.session_state.answer = round((T/(2*math.pi))**2 * g, 2)
    st.session_state.count = 0
    st.experimental_rerun()
