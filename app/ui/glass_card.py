import streamlit as st


def show(
    title="",
    value="",
    subtitle="",
    icon="✨",
):

    with st.container(border=True):

        c1, c2 = st.columns([6, 1])

        with c1:

            st.markdown(
                f"### {icon} {title}"
            )

        with c2:

            st.markdown("⭐")

        if value:

            st.markdown(
                f"""
<h1 style="
font-size:38px;
margin-top:0;
margin-bottom:0;
">
{value}
</h1>
""",
                unsafe_allow_html=True,
            )

        if subtitle:

            st.caption(subtitle)