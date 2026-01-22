import streamlit as st
import pandas as pd
import random

st.title("Анкета")

if "data" not in st.session_state:
    st.session_state.data = []

if "a" not in st.session_state:
    st.session_state.a = random.randint(1, 10)
    st.session_state.b = random.randint(1, 10)

st.subheader("Попълни анкетата")

name = st.text_input("Име:")
age = st.number_input("Възраст:", min_value=5, max_value=100, step=1)
grade = st.selectbox("Клас:", ["5 клас", "6 клас", "7 клас"])

fav_sport = st.selectbox(
    "Любим спорт:",
    ["Футбол", "Баскетбол", "Волейбол", "Плуване", "Друг"]
)

fav_subject = st.selectbox(
    "Любим предмет:",
    ["Математика", "Български език", "Английски език", "ИТ", "Биология", "История", "Друг"]
)

fav_movie = st.text_input("Напиши любимия си филм:")

st.write(f"🔢 Проверка: {st.session_state.a} + {st.session_state.b} = ?")
answer = st.number_input("Твоят отговор:", step=1)

if st.button("Изпрати"):
    if name.strip() == "":
        st.error("Моля, въведи име.")
    elif fav_movie.strip() == "":
        st.error("Моля, напиши любимия си филм.")
    elif answer != st.session_state.a + st.session_state.b:
        st.error("Грешен отговор на проверката!")
    else:
        st.session_state.data.append({
            "Име": name,
            "Възраст": age,
            "Клас": grade,
            "Любим спорт": fav_sport,
            "Любим предмет": fav_subject,
            "Любим филм": fav_movie
        })

        st.success("Анкетата е изпратена успешно! ✅")

        st.session_state.a = random.randint(1, 10)
        st.session_state.b = random.randint(1, 10)

st.divider()

st.subheader("Резултати от анкетата")

if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df)
else:
    st.info("Все още няма попълнени анкети.")

