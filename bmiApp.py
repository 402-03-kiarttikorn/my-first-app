import streamlit as st

st.markdown("# :red[🚨 คำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักเเละส่วนสูง เพื่อเช็กสุขภาพเบื้องต้น")

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", main_value+1.0, value=1.0)
heigt_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):", main_value+1.0, value=1.0)

if st.button("คำนวณค่า BMI 🎯"):
    heigt_m = heigt_cm / 100
    bmi = weight / (heigt_m ** 2)

    st.write("---")
    st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

    if bmi < 18.5:
         st.warning("⚠️ คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
    elif 18.5 <= bmi < 23.0:
         st.success("🎉 คุณมีน้ำหนักอยู่กว่าเกณฑ์ปกติ (สุขภาพดี)")
    elif 23.0 <= bmi < 25.0:
         st.info("💡 คุณมีน้ำหนักน้อยเกินเกณฑ์ (ท้วม)")
    elif bmi >= 25.0:
         st.error("🚨  คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพเเละออกกำลังกาย")

st.divider()
st.write("นายเกียรติกร ศรียาบ เลขที่ 3 ม.4/2")
