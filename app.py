
# streamlitをインポートする
import streamlit as st


st.title("画面をデザインしよう")


st.header("いろいろなウィジェット")

st.subheader("ボタン")
clicked = st.button("ボタン")
if clicked==True:
  st.snow()

st.subheader("チェックボックス")
selected = st.checkbox("わかりました")
if selected == True:
  st.text("了解です！")
else:
  st.text("わかりません")

st.subheader("ラジオボタン")
choice = st.radio("どれか選んでください",("みかん","りんご","ぶどう"))
st.text(choice + "が選ばれました")

st.subheader("セレクトボックス")
sel = st.selectbox("好きなお菓子",("チョコレート","せんべい","クッキー"))
st.text(sel + "が選ばれました")

st.subheader("テキストボックス")
name = st.text_input("お名前を入力してください")
st.text(name + "さん、こんにちは。")

st.subheader("数字入力")
num = st.number_input("0〜10までの数字を入力してください。", 0, 10)
st.text(str(num) + "が選ばれました")

st.subheader("日付入力")
date = st.date_input("誕生日を入力してください。")
st.text(str(date) + "ですね")
