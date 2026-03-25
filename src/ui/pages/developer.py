"""Developer Info Tab UI"""

import streamlit as st


def render_developer_page():
    """Render the Developer Info tab."""
    st.markdown('<div class="dev-shell">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="dev-card">
            <div class="dev-title">Himanshu Kumar</div>
            <div class="dev-role">AI/ML Developer | RAG Systems Builder</div>
            <p class="dev-desc">
                Builder of <strong>RAGNOVA</strong>, focused on practical retrieval-augmented systems, reliable
                document pipelines, and production-ready AI app UX.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="dev-card">
            <div class="dev-grid">
                <div class="dev-pill">
                    <div class="k">Project</div>
                    <div class="v">RAGNOVA</div>
                </div>
                <div class="dev-pill">
                    <div class="k">Domain</div>
                    <div class="v">RAG and LLM Apps</div>
                </div>
                <div class="dev-pill">
                    <div class="k">Primary Stack</div>
                    <div class="v">Python, LangChain, FAISS</div>
                </div>
                <div class="dev-pill">
                    <div class="k">Interface</div>
                    <div class="v">Streamlit</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="dev-card">
            <div class="social-grid">
                <a class="social-link github" href="https://github.com/himanshu231204" target="_blank">
                    <div class="social-icon"><img src="https://cdn.simpleicons.org/github/ffffff" alt="GitHub logo"></div>
                    <div class="social-text">
                        <div class="social-label">GitHub</div>
                        <div class="social-handle">@himanshu231204</div>
                    </div>
                </a>
                <a class="social-link linkedin" href="https://www.linkedin.com/in/himanshu231204" target="_blank">
                    <div class="social-icon"><img src="https://cdn.simpleicons.org/linkedin/ffffff" alt="LinkedIn logo"></div>
                    <div class="social-text">
                        <div class="social-label">LinkedIn</div>
                        <div class="social-handle">/in/himanshu231204</div>
                    </div>
                </a>
                <a class="social-link twitter" href="https://twitter.com/himanshu231204" target="_blank">
                    <div class="social-icon"><img src="https://cdn.simpleicons.org/x/ffffff" alt="Twitter/X logo"></div>
                    <div class="social-text">
                        <div class="social-label">Twitter / X</div>
                        <div class="social-handle">@himanshu231204</div>
                    </div>
                </a>
                <a class="social-link email" href="mailto:himanshu231204@gmail.com">
                    <div class="social-icon"><img src="https://cdn.simpleicons.org/gmail/ffffff" alt="Gmail logo"></div>
                    <div class="social-text">
                        <div class="social-label">Email</div>
                        <div class="social-handle">himanshu231204@gmail.com</div>
                    </div>
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
