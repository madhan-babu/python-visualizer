"""
Python Concepts Visualizer
An interactive tool to help kids understand Python programming concepts
"""

import streamlit as st

# Configure page
st.set_page_config(
    page_title="Python Concepts Visualizer",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better visuals
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #4CAF50;
        text-align: center;
        padding: 1rem;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2196F3;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🐍 Python Concepts Visualizer</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Learn Python by seeing it in action!</p>', unsafe_allow_html=True)

# Create tabs for different visualizations
tabs = st.tabs(["📦 Variables & Memory", "🔢 Data Types", "➕ Operators", "🔀 Conditionals", "🔧 Functions", "🔄 Function Scope", "🏛️ Classes & Instances", "🎯 Understanding 'self'", "📝 Strings", "📚 Lists", "🎁 Tuples & Sets", "📖 Dictionaries", "🔁 Loops", "🛡️ Try-Except"])

# Tab 1: Variables & Memory
with tabs[0]:
    from visualizations.variables_memory import show_variables_visualization
    show_variables_visualization()

# Tab 2: Data Types
with tabs[1]:
    from visualizations.data_types import show
    show()

# Tab 3: Operators
with tabs[2]:
    from visualizations.operators import show
    show()

# Tab 4: Conditionals
with tabs[3]:
    from visualizations.conditionals import show
    show()

# Tab 5: Functions
with tabs[4]:
    from visualizations.functions import show
    show()

# Tab 6: Function Scope
with tabs[5]:
    from visualizations.function_scope import show_function_scope_visualization
    show_function_scope_visualization()

# Tab 7: Classes & Instances
with tabs[6]:
    from visualizations.class_instances import show_class_instances_visualization
    show_class_instances_visualization()

# Tab 8: Understanding 'self'
with tabs[7]:
    from visualizations.self_concept import show_self_concept_visualization
    show_self_concept_visualization()

# Tab 9: Strings
with tabs[8]:
    from visualizations.strings import show
    show()

# Tab 10: Lists
with tabs[9]:
    from visualizations.lists import show
    show()

# Tab 11: Tuples & Sets
with tabs[10]:
    from visualizations.tuples_sets import show
    show()

# Tab 12: Dictionaries
with tabs[11]:
    from visualizations.dictionaries import show
    show()

# Tab 13: Loops
with tabs[12]:
    from visualizations.loops import show
    show()

# Tab 14: Try-Except
with tabs[13]:
    from visualizations.exceptions import show
    show()

# Sidebar
with st.sidebar:
    st.markdown("### About")
    st.write("This tool helps kids learn Python concepts through interactive visualizations.")
    
    st.markdown("### How to Use")
    st.write("1. Choose a tab above")
    st.write("2. Interact with the visualization")
    st.write("3. See concepts come to life!")
    
    st.markdown("### Tips")
    st.success("💡 Start with Variables to understand how Python stores data in memory!")
    st.info("🔢 Learn about Data Types - int, str, float, bool, and more!")
    st.warning("➕ Try operators to perform operations on your data!")
    st.success("🔀 Make decisions with if-elif-else statements!")
    st.info("🔧 Create reusable functions with parameters and return values!")
    st.warning("🔄 Explore Function Scope to see local vs global memory!")
    st.success("🏛️ Learn about Classes and create multiple instances!")
    st.info("🎯 Understand how 'self' works in class methods!")
    st.warning("📝 Master string manipulation - slicing, methods, and formatting!")
    st.success("📚 Build and modify lists interactively!")
    st.info("🎁 Learn about tuples (immutable) and sets (unique items)!")
    st.warning("📖 Master dictionaries with key-value pairs!")
    st.success("🔁 Watch loops execute step-by-step!")
    st.info("🛡️ Learn exception handling to make your programs robust!")

