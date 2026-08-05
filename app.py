import streamlit as st
import json
import os

st.set_page_config(page_title="Cargo Bordeaux", layout="wide")

st.title("🚲 Promos Cargo – Bordeaux")

if os.path.exists("data.json"):
    with open("data.json", "r", encoding="utf-8") as f:
        content = json.load(f)
    
    st.caption(f"Mis à jour le : {content.get('last_updated', 'N/A')}")
    items = content.get("items", [])
    
    for item in items:
        if item.get("img"):
            st.image(item["img"], use_container_width=True)
        st.subheader(f"{item['marque']} {item['modele']}")
        st.write(f"📍 {item['magasin']} ({item['type']})")
        st.markdown(f"**{item['prix_promo']} €** ~({item['prix_original']} €)~ **-{item['remise_pct']}%**")
        st.markdown(f"[🔗 Voir en boutique]({item['url']})")
        st.divider()
else:
    st.info("Initialisation des données en cours...")
