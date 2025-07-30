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

# Trajectduur: dropdown + optie om zelf in te vullen
traject_opties = ['2 maanden', '3 maanden', '4 maanden', '5 maanden', '6 maanden', '12 maanden', 'Anders']
traject = st.selectbox("Lengte van traject", traject_opties)

if traject == 'Anders':
    # Als 'Anders' is gekozen, geef de mogelijkheid om zelf in te vullen
    traject = st.text_input("Geef de lengte van het traject in (bv. 8 maanden)")

if st.button("Genereer factuur"):
    totaal = sum([behandelingen[b] for b in geselecteerde_behandelingen])
    vandaag = date.today().strftime("%d-%m-%Y")

    st.subheader("📄 Factuurvoorbeeld:")
    st.markdown(f"""
    **Factuur voor:** {patiënt}  
    **Datum:** {vandaag}  

    **Uitgevoerde behandelingen:**  
    {"".join([f"- {b} – €{behandelingen[b]}  \n" for b in geselecteerde_behandelingen])}

    **Trajectduur:** {traject}  
    **Totaalbedrag:** €{totaal}
    """)

    st.subheader("📧 E-mailtekst:")
    st.text_area("E-mailvoorbeeld", value=f"""Onderwerp: Factuur voor behandeling op {vandaag}

Beste {patiënt},

In de bijlage vindt u de factuur voor uw orthodontiebehandeling.  
Het traject duurt {traject} en bevat de volgende onderdelen:

{"".join([f"- {b} – €{behandelingen[b]}\n" for b in geselecteerde_behandelingen])}

Totaalbedrag: €{totaal},-

Met vriendelijke groet,  
[Naam Orthodontist]
""", height=300)
