import streamlit as st
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(
    page_title="Lalith_Nandakumar",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header with profile links
st.title("📊 Data Science Portfolio Showcase")
st.markdown(
    "**Find me on [GitHub](https://github.com/Lal1th) | [LinkedIn](https://www.linkedin.com/in/lalith-n/)**"
)

# Sidebar: Input for GitHub links
st.sidebar.header("Add Your Projects")
links_input = st.sidebar.text_area(
    label="Paste GitHub repo URLs (one per line)",
    value=(
        "https://www.linkedin.com/posts/activity-7303496301101359106-1QHU?utm_source=share&"
        "utm_medium=member_desktop&rcm=ACoAADchgAsB7gIKE5BVo0M96yjGcSnJJ6dmGjM"
        "\nhttps://github.com/yourusername/project2"
    ),
    height=150
)

# Parse links
urls = [url.strip() for url in links_input.splitlines() if url.strip()]

# Collect project entries
projects = []
for url in urls:
    name = url.rstrip('/').split('/')[-1].split('?')[0]
    title = st.sidebar.text_input(f"Title for {name}", value=name, key=f"title_{name}")
    desc = st.sidebar.text_area(f"Description for {name}", value="", key=f"desc_{name}")
    projects.append({"url": url, "title": title, "description": desc})

# Customize first project
if projects:
    projects[0]["title"] = "AWSxKeyera Hackathon"
    projects[0]["url"] = (
        "https://www.linkedin.com/posts/activity-7303496301101359106-1QHU?"
        "utm_source=share&utm_medium=member_desktop&rcm=ACoAADchgAsB7gIKE5BVo0M96yjGcSnJJ6dmGjM"
    )
    projects[0]["image"] = "https://github.com/Lal1th/Portfolio/blob/main/Hac_img.jpg?raw=true"
    projects[0]["description"] = (
        "3rd place at Data Analytics Hackathon building an AWS QuickSight BI dashboard."
    )

# Display projects in grid
if projects:
    st.subheader(f"Showing {len(projects)} projects")
    cols = st.columns(2)
    for idx, proj in enumerate(projects):
        col = cols[idx % 2]
        with col:
            st.markdown(f"### [{proj['title']}]({proj['url']})")
            if idx == 0 and proj.get("description"):
                # Styled text with hover-triggered full-screen confetti
                html(f"""
                    <style>
                        .desc-hover {{
                            cursor: pointer;
                            color: #F97316;
                        }}
                    </style>
                    <p><span class="desc-hover" onmouseover="confetti({{particleCount:200, spread:360, origin:{{y:0.5}}}})">{proj['description']}</span></p>
                    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                    """,
                    height=100,
                )
            else:
                if proj['description']:
                    st.write(proj['description'])
                else:
                    st.write("_No description provided._")
            if proj.get("image"):
                st.image(proj["image"], use_container_width=True)
            st.markdown("---")
else:
    st.info("Paste your GitHub repository URLs in the sidebar to display your projects.")

# Additional dashboard link
st.subheader("Want to check my dynamic dashboard on Gaming Analysis?")
st.markdown("[Explore it here](https://lalithn.streamlit.app/)")
st.write("Just give it a couple of minutes its slow 0_0 sorry!!!")

# Footer
st.markdown("Contact me at lalithpathapati@gmail.com")
