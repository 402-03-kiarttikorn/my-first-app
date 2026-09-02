import streamlit as st
import math

st.set_page_config(
    page_title="คำนวณพื้นที่เรขาคณิต",
    page_icon="📐"
)

st.title("📐 โปรแกรมคำนวณพื้นที่เรขาคณิต")
st.write("เลือกชนิดของรูปเรขาคณิต แล้วกรอกข้อมูลเพื่อคำนวณพื้นที่")

shape = st.selectbox(
    "เลือกรูปเรขาคณิต",
    [
        "วงกลม",
        "สี่เหลี่ยมจัตุรัส",
        "สี่เหลี่ยมผืนผ้า",
        "สามเหลี่ยม"
    ]
)

if shape == "วงกลม":
    radius = st.number_input(
        "รัศมี",
        min_value=0.0,
        value=1.0
    )

    if st.button("คำนวณพื้นที่"):
        area = math.pi * radius ** 2
        st.success(f"พื้นที่วงกลม = {area:.2f} ตารางหน่วย")

elif shape == "สี่เหลี่ยมจัตุรัส":
    side = st.number_input(
        "ความยาวด้าน",
        min_value=0.0,
        value=1.0
    )

    if st.button("คำนวณพื้นที่"):
        area = side ** 2
        st.success(f"พื้นที่สี่เหลี่ยมจัตุรัส = {area:.2f} ตารางหน่วย")

elif shape == "สี่เหลี่ยมผืนผ้า":
    width = st.number_input(
        "ความกว้าง",
        min_value=0.0,
        value=1.0
    )

    length = st.number_input(
        "ความยาว",
        min_value=0.0,
        value=1.0
    )

    if st.button("คำนวณพื้นที่"):
        area = width * length
        st.success(f"พื้นที่สี่เหลี่ยมผืนผ้า = {area:.2f} ตารางหน่วย")

elif shape == "สามเหลี่ยม":
    base = st.number_input(
        "ความยาวฐาน",
        min_value=0.0,
        value=1.0
    )

    height = st.number_input(
        "ความสูง",
        min_value=0.0,
        value=1.0
    )

    if st.button("คำนวณพื้นที่"):
        area = 0.5 * base * height
        st.success(f"พื้นที่สามเหลี่ยม = {area:.2f} ตารางหน่วย")

st.divider()
st.caption("โปรแกรมคำนวณพื้นที่เรขาคณิต")

