import streamlit as st
from datetime import date

# Dummy data
behandelingen = {
    "Behandeling A": 30,
    "Behandeling B": 12,
    "Behandeling C": 8,
    "Behandeling D": 20,
    "Behandeling E": 33,
    "Behandeling F": 36,
}

patienten = [
    "Piet", "Kees", "Jan", "Koen", "Mark",
    "Boas", "Sjors", "Karen", "Ilse", "Matir"
]

# UI
st.title("Ortho Factuur Generator Demo")
st.write("Selecteer een patiënt, behandelingen en trajectduur:")

patiënt = st.selectbox("Patiënt", patienten)
geselecteerde_behandelingen = st.multiselect("Behandelingen", list(behandelingen.keys()))
duur = st.text_input("Lengte van traject (bv. 6 maanden)")

if st.button("Genereer factuur"):
    totaal = sum([behandelingen[b] for b in geselecteerde_behandelingen])
    vandaag = date.today().strftime("%d-%m-%Y")

    st.subheader("📄 Factuurvoorbeeld:")
    st.markdown(f"""
    **Factuur voor:** {patiënt}  
    **Datum:** {vandaag}  

    **Uitgevoerde behandelingen:**  
    {"".join([f"- {b} – €{behandelingen[b]}  \n" for b in geselecteerde_behandelingen])}

    **Trajectduur:** {duur}  
    **Totaalbedrag:** €{totaal}
    """)

    st.subheader("📧 E-mailtekst:")
    st.text_area("E-mailvoorbeeld", value=f"""Onderwerp: Factuur voor behandeling op {vandaag}

Beste {patiënt},

In de bijlage vindt u de factuur voor uw orthodontiebehandeling.  
Het traject duurt {duur} en bevat de volgende onderdelen:

{"".join([f"- {b} – €{behandelingen[b]}\n" for b in geselecteerde_behandelingen])}

Totaalbedrag: €{totaal},-

Met vriendelijke groet,  
[Naam Orthodontist]
""", height=300)

