"""
Python Concepts Visualizer
An interactive tool to help kids understand Python programming concepts
"""

import streamlit as st
import streamlit.components.v1 as components

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
    /* Reduce top padding aggressively - override the 96px and 160px */
    div[data-testid="stAppViewContainer"] > .main {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    
    .main .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 1rem !important;
        padding-left: 20px !important;
        padding-right: 20px !important;
        max-width: 100%;
    }
    
    div.block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 1rem !important;
        padding-left: 20px !important;
        padding-right: 20px !important;
    }
    
    /* Hide Streamlit's default header */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Remove toolbar */
    .stApp header {
        display: none !important;
    }
    
    /* Adjust main content area */
    section[data-testid="stSidebar"] {
        top: 0 !important;
    }
    
    .main {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    
    .main-header {
        font-size: 2.5rem;
        color: #4CAF50;
        text-align: center;
        padding: 0.25rem 1rem 0rem 1rem;
        margin-bottom: 0.25rem;
        margin-top: 0;
        line-height: 1.2;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2196F3;
        margin-bottom: 1rem;
    }
    
    /* Container for tabs with buttons */
    .stTabs {
        position: relative;
    }
    
    /* Make tabs scrollable horizontally */
    .stTabs [data-baseweb="tab-list"] {
        overflow-x: auto;
        overflow-y: hidden;
        white-space: nowrap;
        display: flex;
        flex-wrap: nowrap;
        gap: 12px;
        padding: 15px 0;
        margin: 0 40px;
        scroll-behavior: smooth;
        background: transparent;
        border-bottom: none;
    }
    
    /* Hide scrollbar but keep functionality */
    .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
        display: none;
    }
    
    /* Style individual tab buttons - modern card style */
    .stTabs [data-baseweb="tab-list"] button {
        flex-shrink: 0;
        min-width: fit-content;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
        text-transform: none !important;
    }
    
    /* Hover effect for tabs */
    .stTabs [data-baseweb="tab-list"] button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
    }
    
    /* Active/selected tab */
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%) !important;
        box-shadow: 0 6px 20px rgba(76, 175, 80, 0.6) !important;
        transform: translateY(-3px) !important;
    }
    
    /* Remove the bottom border line */
    .stTabs [data-baseweb="tab-border"] {
        display: none;
    }
    
    .stTabs [data-baseweb="tab-highlight"] {
        display: none;
    }
    
    /* Add border around content section */
    .stTabs [data-baseweb="tab-panel"] {
        border: 2px solid #e0e0e0;
        border-radius: 12px;
        padding: 20px;
        margin-top: 10px;
        background: #ffffff;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    /* Footer styling */
    footer {
        margin-top: 3rem;
        border-top: 2px solid #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🐍 Python Concepts Visualizer</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 0.95rem; color: #666; margin-top: 0; margin-bottom: 0.25rem; padding: 0; line-height: 1.2;">Learn Python by seeing it in action!</p>', unsafe_allow_html=True)

# Add scroll buttons using HTML component
components.html("""
    <script>
    // Function to scroll tabs
    function scrollTabs(direction) {
        const tabList = window.parent.document.querySelector('.stTabs [data-baseweb="tab-list"]');
        if (tabList) {
            const scrollAmount = 300;
            if (direction === 'left') {
                tabList.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
            } else {
                tabList.scrollBy({ left: scrollAmount, behavior: 'smooth' });
            }
        }
    }
    
    // Wait for tabs to load
    function setupButtons() {
        const parentDoc = window.parent.document;
        const tabList = parentDoc.querySelector('.stTabs [data-baseweb="tab-list"]');
        
        if (!tabList) {
            setTimeout(setupButtons, 100);
            return;
        }
        
        // Remove old buttons if they exist
        const oldLeft = parentDoc.getElementById('tab-scroll-left');
        const oldRight = parentDoc.getElementById('tab-scroll-right');
        if (oldLeft) oldLeft.remove();
        if (oldRight) oldRight.remove();
        
        // Get tab position
        const tabRect = tabList.getBoundingClientRect();
        const tabTop = tabList.offsetTop;
        
        // Create container for buttons
        const container = tabList.parentElement;
        
        // Create left button
        const leftBtn = parentDoc.createElement('button');
        leftBtn.id = 'tab-scroll-left';
        leftBtn.innerHTML = '◀';
        leftBtn.onclick = () => scrollTabs('left');
        leftBtn.style.cssText = `
            position: absolute;
            left: 0px;
            top: 50%;
            transform: translateY(-50%);
            z-index: 1001;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 50%;
            width: 32px;
            height: 32px;
            font-size: 16px;
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        `;
        leftBtn.onmouseover = () => {
            leftBtn.style.background = '#45a049';
            leftBtn.style.transform = 'translateY(-50%) scale(1.1)';
        };
        leftBtn.onmouseout = () => {
            leftBtn.style.background = '#4CAF50';
            leftBtn.style.transform = 'translateY(-50%) scale(1)';
        };
        
        // Create right button
        const rightBtn = parentDoc.createElement('button');
        rightBtn.id = 'tab-scroll-right';
        rightBtn.innerHTML = '▶';
        rightBtn.onclick = () => scrollTabs('right');
        rightBtn.style.cssText = `
            position: absolute;
            right: 0px;
            top: 50%;
            transform: translateY(-50%);
            z-index: 1001;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 50%;
            width: 32px;
            height: 32px;
            font-size: 16px;
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        `;
        rightBtn.onmouseover = () => {
            rightBtn.style.background = '#45a049';
            rightBtn.style.transform = 'translateY(-50%) scale(1.1)';
        };
        rightBtn.onmouseout = () => {
            rightBtn.style.background = '#4CAF50';
            rightBtn.style.transform = 'translateY(-50%) scale(1)';
        };
        
        // Make container position relative
        container.style.position = 'relative';
        
        // Add buttons to container
        container.appendChild(leftBtn);
        container.appendChild(rightBtn);
    }
    
    // Start setup
    setupButtons();
    </script>
""", height=0)

# Create tabs for different visualizations
tabs = st.tabs(["🐍 Introduction", "📦 Variables & Memory", "💬 Print & Input", "🔢 Data Types", "➕ Operators", "🔀 Conditionals", "🔧 Functions", "🔄 Function Scope", "🏛️ Classes & Instances", "🎯 Understanding 'self'", "📝 Strings", "📚 Lists", "🎁 Tuples & Sets", "📖 Dictionaries", "🔁 Loops", "🛡️ Try-Except"])

# Tab 1: Introduction to Python
with tabs[0]:
    from visualizations.python_intro import show
    show()

# Tab 2: Variables & Memory
with tabs[1]:
    from visualizations.variables_memory import show_variables_visualization
    show_variables_visualization()

# Tab 3: Print & Input
with tabs[2]:
    from visualizations.print_input import show
    show()

# Tab 4: Data Types
with tabs[3]:
    from visualizations.data_types import show
    show()

# Tab 5: Operators
with tabs[4]:
    from visualizations.operators import show
    show()

# Tab 6: Conditionals
with tabs[5]:
    from visualizations.conditionals import show
    show()

# Tab 7: Functions
with tabs[6]:
    from visualizations.functions import show
    show()

# Tab 8: Function Scope
with tabs[7]:
    from visualizations.function_scope import show_function_scope_visualization
    show_function_scope_visualization()

# Tab 9: Classes & Instances
with tabs[8]:
    from visualizations.class_instances import show_class_instances_visualization
    show_class_instances_visualization()

# Tab 10: Understanding 'self'
with tabs[9]:
    from visualizations.self_concept import show_self_concept_visualization
    show_self_concept_visualization()

# Tab 11: Strings
with tabs[10]:
    from visualizations.strings import show
    show()

# Tab 12: Lists
with tabs[11]:
    from visualizations.lists import show
    show()

# Tab 13: Tuples & Sets
with tabs[12]:
    from visualizations.tuples_sets import show
    show()

# Tab 14: Dictionaries
with tabs[13]:
    from visualizations.dictionaries import show
    show()

# Tab 15: Loops
with tabs[14]:
    from visualizations.loops import show
    show()

# Tab 16: Try-Except
with tabs[15]:
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
    st.info("🐍 Start with the Introduction to learn about Python!")
    st.success("💡 Learn Variables to understand how Python stores data in memory!")
    st.warning("💬 Learn print() and input() to communicate with your program!")
    st.info("🔢 Learn about Data Types - int, str, float, bool, and more!")
    st.success("➕ Try operators to perform operations on your data!")
    st.warning("🔀 Make decisions with if-elif-else statements!")
    st.info("🔧 Create reusable functions with parameters and return values!")
    st.success("🔄 Explore Function Scope to see local vs global memory!")
    st.warning("🏛️ Learn about Classes and create multiple instances!")
    st.info("🎯 Understand how 'self' works in class methods!")
    st.success("📝 Master string manipulation - slicing, methods, and formatting!")
    st.warning("📚 Build and modify lists interactively!")
    st.info("🎁 Learn about tuples (immutable) and sets (unique items)!")
    st.success("📖 Master dictionaries with key-value pairs!")
    st.warning("🔁 Watch loops execute step-by-step!")
    st.info("🛡️ Learn exception handling to make your programs robust!")

# Copyright footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 20px 0; color: #666; font-size: 0.9rem;">
        <p style="margin: 5px 0;">© 2025 <strong>Madhan Babu</strong>. All rights reserved.</p>
        <p style="margin: 5px 0; font-size: 0.85rem;">Python Concepts Visualizer - An educational tool for learning Python programming</p>
    </div>
""", unsafe_allow_html=True)

