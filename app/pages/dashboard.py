import streamlit as st

from app.components import navbar
from app.components import hero
from app.components import cards
from app.components import stats
from app.components import footer


def show():

    st.write("STEP 1")
    navbar.show()

    st.write("STEP 2")
    hero.show()

    st.write("STEP 3")
    cards.show()

    st.write("STEP 4")
    stats.show()

    st.write("STEP 5")
    footer.show()