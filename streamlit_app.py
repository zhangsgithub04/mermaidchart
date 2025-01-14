import streamlit as st
from mermaid2 import Mermaid

# Define a Mermaid chart code
mermaid_code = """
    graph LR
        Customer[Customer] --> Order[Order]
        Order[Order] --> Salesperson[Salesperson]
"""

# Render Mermaid chart
mermaid = Mermaid()
mermaid.graph = mermaid_code
diagram = mermaid.render()

# Display Mermaid chart in Streamlit
st.title("Mermaid Chart")
st.image(diagram)
