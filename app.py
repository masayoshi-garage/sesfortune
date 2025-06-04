import streamlit as st
import datetime
import time
import urllib.parse

siteUrl = "https://sesfortune-u6ogjxviqbehow8t9ywv6b.streamlit.app/";

def pick_line_with_hash(file_path: str,userName: str):
    dt_now = datetime.datetime.now()
    try:
        with open(file_path, 'r',encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return "未来が見通せない"
    
    if not lines:
        return "未来が空虚になっている"

    key = hash(userName + str(dt_now.day))
    index = key % len(lines)
    return lines[index]

st.header("SES fortune",divider='red')

if handleName := st.text_input("あなたの名前を入力してください"):
    if st.button("占う"):
        # 考えているフリ
        sleepTime = hash(datetime.datetime.now())
        sleepTime = sleepTime / (abs(sleepTime) +1)
        with st.spinner("Wait for it...", show_time=True):
            time.sleep(abs(sleepTime))
        st.divider()
        st.header("💼 あなたの次の案件",divider="red")
        nextjob = pick_line_with_hash('nextjob',handleName)
        st.write(nextjob)
        st.header("👨‍💼 指揮命令者の特徴",divider="red")
        # lead ではないのか
        reader = pick_line_with_hash('reader',handleName)
        st.write(reader)
        st.header("🪙 想定される単価感",divider="red")
        price = pick_line_with_hash('price',handleName)
        st.write(price)
        st.header("🧠 案件を抜ける時の引き留めコメント",divider="red")
        comment = pick_line_with_hash('comment',handleName)
        st.write(comment)

        #tweet用テキスト
        tweet_text = f"""#SES占い 
{handleName} さんが次にやる案件は?
💼案件: {nextjob}
👨‍💼指揮命令者: {reader}
"""
        tweet_footer = f"""👇全文はこちら
{siteUrl}
"""
        # tweet_textの内容を140文字に制限
        tweet_text = tweet_text[:138+len(tweet_footer)] + "…" + tweet_footer
        # URLエンコード
        tweet_url = "https://twitter.com/intent/tweet?text=" + urllib.parse.quote(tweet_text)

        st.markdown(f"[📝 結果をXに投稿する]({tweet_url})", unsafe_allow_html=True)