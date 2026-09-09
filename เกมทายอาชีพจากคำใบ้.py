import time
import streamlit as st

st.title("⏱️ เกมทายอาชีพจากคำใบ้จับเวลา")

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""

if "ans6_val" not in st.session_state:
    st.session_state.ans6_val = ""

if "ans7_val" not in st.session_state:
    st.session_state.ans7_val = ""

def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""  # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 4
    st.session_state.ans5_val = ""  # เคลียร์ค่าช่องข้อ 5
    st.session_state.ans6_val = ""  # เคลียร์ค่าช่องข้อ 6
    st.session_state.ans7_val = ""  # เคลียร์ค่าช่องข้อ 7
    st.session_state.start = time.time()  
    st.session_state.is_ended = False  


# ----------------------------------------------------

# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower() 
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower() 
    u_ans6 = ans6.strip().lower()
    u_ans7 = ans7.strip().lower()


    if u_ans1 == "ตำรวจ":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")


    if u_ans2 == "หมอ":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

   
    if u_ans3 == "ครู":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

   
    if u_ans4 == "พยาบาล":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    if u_ans5 == "นักบินอวกาศ":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

   
    if u_ans6 == "นักดับเพลิง":
        st.success("✅ ข้อ 6: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 6: ยังไม่ถูกต้อง (คุณตอบ '{u_ans6}')")

   
    if u_ans7 == "จิตรกร":
        st.success("✅ ข้อ 7: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 7: ยังไม่ถูกต้อง (คุณตอบ '{u_ans7}')")

   

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

   if score == 0:
    st.error("💀 You lose! แพ้เกม")
   elif 1 <= score <= 3:
    st.warning("📉 You lose! พยายามอีกนิดนะ")
   elif 4 <= score <= 6:
    st.info("👍 เก่งมาก! อีกนิดเดียว")
   elif score == 7:
    st.success("🎉 You win! ระดับนักปราชญ์")
   else:
    st.error("❌ คะแนนไม่อยู่ในระบบ (กรุณาตรวจสอบข้อผิดพลาด)")



# ----------------------------------------------------

# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(60 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

ans1 = st.text_input(
    "ข้อ 1: อะไรเอ่ยชอบทำหน้าเข้ม สุดท้ายวิ่งเล่นไล่จับทรงเอ",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: อะไรเอ่ยชอบบอกให้เราลดน้ำหนักแถมบอกอ้วนขึ้นนะครับเบาหวานคิดถึง",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: อะไรเอ่ยชอบสั่งงานแถมให้การบ้านอย่างกับทอร์นาโด",
    value=st.session_state.ans3_val,
)
    
ans4 = st.text_input(
 "ข้อ 4: อะไรเอ่ยชอบของมีคมบอกตรงๆ เจ็บเหมือนมดกัดนิดเดียวค่ะ",
    value=st.session_state.ans4_val,
)

ans5 = st.text_input(
    "ข้อ 5:  อะไรเอ่ยชอบใส่หมวกกันนอกลอยขึ้นฟ้า",
    value=st.session_state.ans5_val,
)
ans6 = st.text_input(
    "ข้อ 6: อะไรเอ่ยชอบดับไฟที่ร้อนแรงยิ่งกว่าอยู่ในปาร์ตี้ร้อนอย่างกับไฟเยอร์",
    value=st.session_state.ans6_val,
)
    
ans7 = st.text_input(
 "ข้อ 7: อะไรเอ่ยจินตนาการสำคัญกว่าความคิดเลยติดอยู่กับเทปแปะกล้วย ",
    value=st.session_state.ans7_val,
)

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
st.session_state.ans6_val = ans6
st.session_state.ans7_val = ans7



if "start" in st.session_state and not st.session_state.get("is_ended", False):
    
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()


if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2 , ans3 , ans4 , ans5 , ans6 , ans7)

st.divider()
st.write("กลุ่ม 6 เลขที่ 1 3 21 26 ม.4/2")
