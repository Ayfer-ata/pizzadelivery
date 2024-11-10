import streamlit as st
import sqlite3


conn = sqlite3.connect("pizzadb.sqlite3")
c = conn.cursor()


c.execute("CREATE TABLE IF NOT EXISTS siparisler(isim TEXT, adres TEXT, pizza TEXT, boy TEXT, icecek TEXT, fiyat REAL)")
conn.commit()


c.execute("SELECT isim FROM pizzalar")
isimler = c.fetchall()


isimlerlist = [i[0] for i in isimler]


st.header("Sipariş")

with st.form("pizzaekle", clear_on_submit=True):

    isim = st.text_input("İsim Soyisim")
    adres = st.text_area("Adres")
    pizza = st.selectbox("Pizza Seç", isimlerlist)
    boy = st.selectbox("Boy", ["Small", "Medium", "Large"])
    icecek = st.selectbox("İçecek", ["Ayran", "Su", "Cola", "Fanta"])
    siparisver = st.form_submit_button("Sipariş Ver")

    if siparisver:

        if boy == "Small":
            c.execute("SELECT smfiyat FROM pizzalar WHERE isim=?", (pizza,))
            fiyat = c.fetchall()
        elif boy == "Medium":
            c.execute("SELECT mdfiyat FROM pizzalar WHERE isim=?", (pizza,))
            fiyat = c.fetchall()
        elif boy == "Large":
            c.execute("SELECT lgfiyat FROM pizzalar WHERE isim=?", (pizza,))
            fiyat = c.fetchall()


        icecekfiyat = {
            "Ayran": 15,
            "Su": 10,
            "Cola": 20,
            "Fanta": 20
        }


        icecekfiyat_secilen = icecekfiyat.get(icecek, 0)


        fiyat_pizza = fiyat[0][0] if fiyat else 0


        toplamfiyat = fiyat_pizza + icecekfiyat_secilen


        c.execute("INSERT INTO siparisler (isim, adres, pizza, boy, icecek, fiyat) VALUES (?, ?, ?, ?, ?, ?)",
                  (isim, adres, pizza, boy, icecek, toplamfiyat))
        conn.commit()


        st.success(f"Sipariş Başarılı Bir Şekilde Oluşturuldu. Toplam Ücret: {toplamfiyat} TL")

