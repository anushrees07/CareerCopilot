import streamlit as st


def show():

    st.markdown(
        """
        <style>

        .hero-title{
            font-size:58px;
            font-weight:800;
            line-height:1.05;
            color:white;
            text-shadow:0 0 20px rgba(255,255,255,.25);
        }

        .hero-highlight{
            color:#6EE7FF;
            text-shadow:
                0 0 10px #6EE7FF,
                0 0 25px #6EE7FF,
                0 0 45px #6EE7FF;
        }

        .hero-sub{
            font-size:18px;
            color:#C8D2E3;
            line-height:1.8;
            max-width:720px;
            margin-top:15px;
        }

        .hero-badge{

            display:inline-block;

            padding:8px 18px;

            border-radius:999px;

            color:white;

            font-size:14px;

            background:linear-gradient(
                135deg,
                rgba(80,120,255,.35),
                rgba(0,212,255,.25)
            );

            border:1px solid rgba(110,231,255,.45);

            margin-bottom:25px;

            box-shadow:
                0 0 20px rgba(110,231,255,.20);

        }

        .snapshot-card{

            background:linear-gradient(
                135deg,
                rgba(52,77,156,.95),
                rgba(28,41,89,.95)
            );

            border:1px solid rgba(110,231,255,.50);

            border-radius:24px;

            padding:28px;

            backdrop-filter:blur(18px);

            box-shadow:
                0 0 25px rgba(110,231,255,.25),
                0 0 60px rgba(110,231,255,.12);

            transition:.35s;
        }

        .snapshot-card:hover{

            transform:translateY(-5px);

            border:1px solid #6EE7FF;

            box-shadow:
                0 0 40px rgba(110,231,255,.40),
                0 0 80px rgba(110,231,255,.20);

        }

        .snapshot-title{

            color:white;

            font-size:26px;

            font-weight:700;

            text-shadow:
                0 0 10px #6EE7FF,
                0 0 25px #6EE7FF;

            margin-bottom:20px;
        }

        .snapshot-item{

            color:#EDF7FF;

            font-size:17px;

            padding:12px 0;

            border-bottom:1px solid rgba(255,255,255,.08);

        }

        .snapshot-item:last-child{

            border:none;

        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.8, 1])

    with left:

        st.markdown(
            """
            <div class="hero-badge">
            ✨ AI Powered Career Platform
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hero-title">
            Build Your Dream<br>
            <span class="hero-highlight">
            Career
            </span>
            With AI
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hero-sub">
            Analyze your resume, discover internships,
            identify skill gaps, prepare for interviews,
            generate career roadmaps and accelerate your
            career using your favourite AI provider.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:

        st.markdown(
            """
            <div class="snapshot-card">

            <div class="snapshot-title">
            🚀 Career Snapshot
            </div>

            <div class="snapshot-item">
            📄 Resume Intelligence
            </div>

            <div class="snapshot-item">
            🤖 Multi-AI Providers
            </div>

            <div class="snapshot-item">
            📈 ATS Optimization
            </div>

            <div class="snapshot-item">
            💼 Opportunity Matching
            </div>

            <div class="snapshot-item">
            🗺️ Personalized Roadmap
            </div>

            </div>
            """,
            unsafe_allow_html=True,
        )