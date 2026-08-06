import streamlit as st


def opportunity_card(title, company, location, stipend, match, url):

    with st.container(border=True):

        c1, c2 = st.columns([4, 1])

        with c1:

            st.subheader(title)

            st.caption(company)

            st.write(f"📍 {location}")

            st.write(f"💰 {stipend}")

        with c2:

            st.metric("Match", f"{match}%")

        st.link_button(
            "Apply 🚀",
            url,
            use_container_width=True,
        )


def show():

    st.markdown(
        """
<div class="ai-badge">
💼 AI Opportunity Finder
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="section-title">
Find Opportunities Smarter
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="section-sub">
Search internships, jobs and hackathons with AI-powered matching.
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3 = st.columns(3)

    keyword = c1.text_input(
        "Role",
        "Python Developer",
    )

    location = c2.text_input(
        "Location",
        "Bengaluru",
    )

    opportunity_type = c3.selectbox(
        "Type",
        [
            "Internship",
            "Job",
            "Hackathon",
        ],
    )

    st.write("")

    if st.button(
        "🔍 Search Opportunities",
        use_container_width=True,
    ):

        st.success("3 opportunities found")

        st.write("")

        opportunity_card(
            "Python Developer Intern",
            "Google",
            "Bengaluru",
            "₹50,000/month",
            96,
            "https://careers.google.com",
        )

        opportunity_card(
            "AI Intern",
            "Microsoft",
            "Hyderabad",
            "₹60,000/month",
            92,
            "https://careers.microsoft.com",
        )

        opportunity_card(
            "ML Engineer Intern",
            "NVIDIA",
            "Remote",
            "₹80,000/month",
            95,
            "https://www.nvidia.com/en-us/about-nvidia/careers/",
        )