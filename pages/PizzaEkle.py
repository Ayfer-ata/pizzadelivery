import streamlit as st
import sqlite3

conn=sqlite3.connect("pizzadb.sqlite3")
c=conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS pizzalar(isim TEXT, smfiyat REAL, mdfiyat REAL, lgfiyat REAL, icindekiler TEXT, resim TEXT)")
conn.commit()



st.header("Pizza Ekle")

with st.form("piizaekle",clear_on_submit=True):
   isim=st.text_input("Pizza İsmi")
   smfiyat = st.number_input("Small Fiyat")
   mdfiyat = st.number_input("Medium Fiyat")
   lgfiyat = st.number_input("Large Fiyat")
   icindekiler = st.multiselect("İçindekiler", ["Mantar", "Sucuk", "Mozeralla", "Fesleğen", "Yeşil Zeytin",
                                                "Tavuk","Siyah Zeytin","Yeşil Biber","Mısır","Kavurma"])


   resim=st.file_uploader("Pizza Resmi Ekleyiniz")

   ekle=st.form_submit_button("Pizza Ekle")

   if ekle:
      icindekiler=str(icindekiler)
      icindekiler = icindekiler.replace("[", "")
      icindekiler = icindekiler.replace("[", "")
      icindekiler = icindekiler.replace("[", "")

      resimurl="img/"+resim.name

      open(resimurl, "wb").write(resim.read())

      c.execute("INSERT INTO pizzalar Values(?,?,?,?,?,?)", (isim,smfiyat,mdfiyat,lgfiyat,icindekiler,resimurl))
      conn.commit()

      st.success("Pizza Başarıyla Eklendi")





