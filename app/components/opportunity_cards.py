import streamlit as st


def show(opportunity, score):

    with st.container(border=True):

        c1, c2 = st.columns([4, 1])

        with c1:

            st.subheader(opportunity.title)

            st.caption(
                f"{opportunity.company} • {opportunity.location}"
            )

        with c2:

            st.metric(
                "Match",
                f"{score}%"
            )

        st.progress(score / 100)

        st.write("### Required Skills")

        cols = st.columns(4)

        for i, skill in enumerate(opportunity.skills):

            with cols[i % 4]:

                st.success(skill)

        st.link_button(
            "Apply Now 🚀",
            opportunity.apply_link,
            use_container_width=True,
        )

        st.divider()