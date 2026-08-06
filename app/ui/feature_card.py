import streamlit as st


def show(
    title: str,
    description: str,
    icon: str = "✨",
    color: str = "#8B5CF6",
):

    st.markdown(
        f"""
<div style="
background:{color}15;
border:1px solid {color}40;
border-radius:18px;
padding:18px;
margin-bottom:15px;
">

<h4 style="margin-bottom:8px;">
{icon} {title}
</h4>

<p style="color:#CBD5E1;">
{description}
</p>

</div>
""",
        unsafe_allow_html=True,
    )