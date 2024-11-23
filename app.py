import streamlit as st
import math

# Path gambar
image_path = "img/geometry.jpg"

# Fungsi untuk perhitungan setiap bangun ruang
def calculate_volume(shape, **kwargs):
    if shape == "Tabung (Cylinder)":
        r = kwargs.get("radius", 0)
        h = kwargs.get("height", 0)
        return math.pi * r**2 * h
    elif shape == "Prisma Segi Enam (Hexagonal Prism)":
        a = kwargs.get("side", 0)
        h = kwargs.get("height", 0)
        return (3 * math.sqrt(3) / 2) * a**2 * h
    elif shape == "Bola (Sphere)":
        r = kwargs.get("radius", 0)
        return (4 / 3) * math.pi * r**3
    elif shape == "Kubus (Cube)":
        s = kwargs.get("side", 0)
        return s**3
    elif shape == "Balok (Cuboid)":
        l = kwargs.get("length", 0)
        w = kwargs.get("width", 0)
        h = kwargs.get("height", 0)
        return l * w * h
    elif shape == "Limas Persegi (Square-based Pyramid)":
        b = kwargs.get("base", 0)
        h = kwargs.get("height", 0)
        return (1 / 3) * b**2 * h
    elif shape == "Kerucut (Cone)":
        r = kwargs.get("radius", 0)
        h = kwargs.get("height", 0)
        return (1 / 3) * math.pi * r**2 * h
    else:
        return None

# Layout aplikasi
st.markdown("<h1 style='text-align: center;'>Kalkulator Bangun Ruang 3D</h1>", unsafe_allow_html=True)
st.image(image_path, caption="Bangun Ruang", use_column_width=True)

# Dropdown untuk memilih bangun ruang
shape = st.selectbox(
    "Pilih Bangun Ruang:",
    [
        "Tabung (Cylinder)",
        "Prisma Segi Enam (Hexagonal Prism)",
        "Bola (Sphere)",
        "Kubus (Cube)",
        "Balok (Cuboid)",
        "Limas Persegi (Square-based Pyramid)",
        "Kerucut (Cone)"
    ]
)

# Form untuk input nilai
st.header(f"Hitung Volume {shape}")

if shape == "Tabung (Cylinder)":
    radius = st.number_input("Jari-jari (r):", min_value=0.0, step=0.1)
    height = st.number_input("Tinggi (h):", min_value=0.0, step=0.1)
    if st.button("Hitung"):
        volume = calculate_volume(shape, radius=radius, height=height)
        st.success(f"Volume {shape} adalah {volume:.2f}")
elif shape == "Prisma Segi Enam (Hexagonal Prism)":
    side = st.number_input("Panjang sisi (a):", min_value=0.0, step=0.1)
    height = st.number_input("Tinggi (h):", min_value=0.0, step=0.1)
    if st.button("Hitung"):
        volume = calculate_volume(shape, side=side, height=height)
        st.success(f"Volume {shape} adalah {volume:.2f}")
elif shape == "Bola (Sphere)":
    radius = st.number_input("Jari-jari (r):", min_value=0.0, step=0.1)
    if st.button("Hitung"):
        volume = calculate_volume(shape, radius=radius)
        st.success(f"Volume {shape} adalah {volume:.2f}")
elif shape == "Kubus (Cube)":
    side = st.number_input("Panjang sisi (s):", min_value=0.0, step=0.1)
    if st.button("Hitung"):
        volume = calculate_volume(shape, side=side)
        st.success(f"Volume {shape} adalah {volume:.2f}")
elif shape == "Balok (Cuboid)":
    length = st.number_input("Panjang (l):", min_value=0.0, step=0.1)
    width = st.number_input("Lebar (w):", min_value=0.0, step=0.1)
    height = st.number_input("Tinggi (h):", min_value=0.0, step=0.1)
    if st.button("Hitung"):
        volume = calculate_volume(shape, length=length, width=width, height=height)
        st.success(f"Volume {shape} adalah {volume:.2f}")
elif shape == "Limas Persegi (Square-based Pyramid)":
    base = st.number_input("Panjang sisi alas (b):", min_value=0.0, step=0.1)
    height = st.number_input("Tinggi (h):", min_value=0.0, step=0.1)
    if st.button("Hitung"):
        volume = calculate_volume(shape, base=base, height=height)
        st.success(f"Volume {shape} adalah {volume:.2f}")
elif shape == "Kerucut (Cone)":
    radius = st.number_input("Jari-jari (r):", min_value=0.0, step=0.1)
    height = st.number_input("Tinggi (h):", min_value=0.0, step=0.1)
    if st.button("Hitung"):
        volume = calculate_volume(shape, radius=radius, height=height)
        st.success(f"Volume {shape} adalah {volume:.2f}")
