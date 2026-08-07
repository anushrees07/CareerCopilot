import streamlit as st

from app.storage.profile_manager import load_profile

from app.services.opportunity_engine import load_opportunities
from app.services.recommendation_engine import calculate_match

from app.components.opportunity_cards import show as opportunity_cards


def show():

    st.title("💼 Opportunity Intelligence")

    st.caption(
        "Discover opportunities matched specifically to your profile."
    )

    profile = load_profile()

    if not profile["skills"]:

        st.warning(
            "Please upload and analyze your resume first."
        )

        return

    opportunities = load_opportunities()

    ranked = []

    for opp in opportunities:

        score = calculate_match(
            opp,
            profile["skills"],
        )

        ranked.append(
            (score, opp)
        )

    ranked.sort(
        reverse=True,
        key=lambda x: x[0],
    )

    for score, opp in ranked:

        opportunity_cards(
            opp,
            score,
        )