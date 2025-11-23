"""
Function Scope Visualization
Shows how function local scope differs from global scope
"""

import streamlit as st
import time

def show_function_scope_visualization():
    """Main function to display the function scope visualization"""
    
    st.markdown('<h2 style="color: #2196F3;">🔄 Function Scope & Memory</h2>', unsafe_allow_html=True)
    st.write("See how functions have their own memory space (local scope) separate from global memory!")
    
    # Initialize session state
    if 'global_vars' not in st.session_state:
        st.session_state.global_vars = {}
    if 'call_history' not in st.session_state:
        st.session_state.call_history = []
    if 'function_active' not in st.session_state:
        st.session_state.function_active = False
    if 'local_vars' not in st.session_state:
        st.session_state.local_vars = {}
    
    # Display function definition
    st.markdown("### 📝 Function Definition")
    st.code("""
def add(a, b):
    c = a + b
    return c
""", language="python")
    
    st.info("💡 This function has its own **local scope** - variables inside the function are separate from global variables!")
    
    # Create two columns for controls and execution
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🎮 Controls")
        
        # Global variable setup
        with st.expander("🌍 Set Global Variables", expanded=True):
            with st.form("global_vars_form"):
                var_a = st.number_input("Variable a", value=10, step=1)
                var_b = st.number_input("Variable b", value=20, step=1)
                set_globals_btn = st.form_submit_button("💾 Set Global Variables")
            
            if set_globals_btn:
                st.session_state.global_vars = {'a': var_a, 'b': var_b}
                st.success("✅ Global variables set!")
                st.rerun()
        
        # Function execution
        with st.expander("▶️ Call Function", expanded=True):
            st.markdown("Execute: `c = add(a, b)`")
            
            if not st.session_state.global_vars:
                st.warning("⚠️ Set global variables first!")
            else:
                if st.button("🚀 Call add(a, b)", use_container_width=True):
                    # Execute the function
                    a_val = st.session_state.global_vars['a']
                    b_val = st.session_state.global_vars['b']
                    
                    # Simulate local scope
                    st.session_state.local_vars = {
                        'a': a_val,  # Parameter a
                        'b': b_val,  # Parameter b
                        'c': a_val + b_val  # Local variable c
                    }
                    
                    # Add to global scope
                    st.session_state.global_vars['c'] = a_val + b_val
                    
                    # Add to history
                    st.session_state.call_history.append({
                        'call_num': len(st.session_state.call_history) + 1,
                        'a': a_val,
                        'b': b_val,
                        'result': a_val + b_val
                    })
                    
                    st.session_state.function_active = True
                    st.success(f"✅ Function returned: {a_val + b_val}")
                    st.rerun()
                
                if st.button("🔄 Reset All", use_container_width=True):
                    st.session_state.global_vars = {}
                    st.session_state.local_vars = {}
                    st.session_state.call_history = []
                    st.session_state.function_active = False
                    st.rerun()
    
    with col2:
        st.markdown("### 🧠 Memory Visualization")
        
        # Global Memory
        st.markdown("#### 🌍 Global Memory (Outside Function)")
        if st.session_state.global_vars:
            for var_name, var_value in st.session_state.global_vars.items():
                # Different colors for different variables
                color = '#4CAF50' if var_name in ['a', 'b'] else '#FF9800'
                
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, {color}22 0%, {color}44 100%);
                    border-left: 5px solid {color};
                    padding: 1rem;
                    border-radius: 8px;
                    margin: 0.5rem 0;
                ">
                    <div style="display: flex; justify-content: space-between;">
                        <span style="font-weight: bold; font-size: 1.2rem;">{var_name}</span>
                        <span style="font-size: 1.2rem; color: {color};">{var_value}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("👈 No global variables yet. Set them in the controls!")
        
        st.markdown("---")
        
        # Function Local Memory
        st.markdown("#### 🔒 Function Local Memory (Inside add function)")
        
        if st.session_state.function_active and st.session_state.local_vars:
            st.markdown("""
            <div style="
                border: 3px dashed #2196F3;
                padding: 1.5rem;
                border-radius: 12px;
                background: #E3F2FD;
            ">
            """, unsafe_allow_html=True)
            
            st.markdown('<p style="color: #1976D2; font-weight: bold; margin-bottom: 1rem;">⚡ Function is executing...</p>', unsafe_allow_html=True)
            
            for var_name, var_value in st.session_state.local_vars.items():
                # Different styling for parameters vs local vars
                if var_name in ['a', 'b']:
                    badge = "📥 Parameter"
                    color = '#2196F3'
                else:
                    badge = "📦 Local Variable"
                    color = '#9C27B0'
                
                st.markdown(f"""
                <div style="
                    background: white;
                    border-left: 5px solid {color};
                    padding: 1rem;
                    border-radius: 8px;
                    margin: 0.5rem 0;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                ">
                    <div style="font-size: 0.8rem; color: #666; margin-bottom: 0.3rem;">{badge}</div>
                    <div style="display: flex; justify-content: space-between;">
                        <span style="font-weight: bold; font-size: 1.2rem;">{var_name}</span>
                        <span style="font-size: 1.2rem; color: {color};">{var_value}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="
                background: #4CAF50;
                color: white;
                padding: 1rem;
                border-radius: 8px;
                margin-top: 1rem;
                text-align: center;
                font-size: 1.2rem;
                font-weight: bold;
            ">
                🎯 Return value: {st.session_state.local_vars['c']}
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.info("📭 Function not active. Call the function to see local memory!")
    
    # Call History
    st.markdown("---")
    st.markdown("### 📊 Function Call History")
    
    if st.session_state.call_history:
        st.markdown(f"**Total calls:** {len(st.session_state.call_history)}")
        
        # Display in a table format
        cols = st.columns([1, 2, 2, 2])
        cols[0].markdown("**Call #**")
        cols[1].markdown("**Input a**")
        cols[2].markdown("**Input b**")
        cols[3].markdown("**Result (c)**")
        
        for call in st.session_state.call_history:
            cols = st.columns([1, 2, 2, 2])
            cols[0].write(f"#{call['call_num']}")
            cols[1].write(call['a'])
            cols[2].write(call['b'])
            cols[3].write(f"✅ {call['result']}")
    else:
        st.info("📝 No function calls yet. Call the function to see history!")
    
    # Educational section
    st.markdown("---")
    with st.expander("📚 Learn More: Function Scope"):
        col_learn1, col_learn2 = st.columns(2)
        
        with col_learn1:
            st.markdown("""
            ### 🌍 Global Scope
            
            **What is it?**
            - Variables defined **outside** any function
            - Accessible from anywhere in your code
            - Lives for the entire program
            
            **In our example:**
            ```python
            a = 10      # Global variable
            b = 20      # Global variable
            c = add(a, b)  # Global variable
            ```
            
            These variables exist in the **main memory** of your program.
            """)
        
        with col_learn2:
            st.markdown("""
            ### 🔒 Local Scope
            
            **What is it?**
            - Variables defined **inside** a function
            - Only accessible within that function
            - Created when function is called
            - Destroyed when function returns
            
            **In our example:**
            ```python
            def add(a, b):
                c = a + b  # Local variable
                return c
            ```
            
            These variables exist in **temporary function memory**.
            """)
        
        st.markdown("""
        ---
        ### 🎯 Key Concepts
        
        1. **Parameters (a, b):**
           - Function receives **copies** of the values
           - Changes inside function don't affect global variables
           - Each function call gets fresh copies
        
        2. **Local Variables (c inside function):**
           - Created when function runs
           - Only exists while function is executing
           - Destroyed after `return`
        
        3. **Return Value:**
           - Function sends value back to caller
           - Gets assigned to global variable `c`
           - This is how data flows from local to global
        
        4. **Multiple Calls:**
           - Each call creates **new** local memory
           - Previous local variables are gone
           - Global variables persist between calls
        
        ### 🧪 Experiment Ideas
        
        Try these to understand scope better:
        
        1. **Same names, different scopes:**
           - Global `c` and local `c` are **different** variables!
           - They just happen to have the same name
        
        2. **Multiple calls:**
           - Call the function multiple times
           - Notice: local memory is created and destroyed each time
           - Global variables keep their values
        
        3. **Change global variables:**
           - Set `a = 5`, `b = 15`
           - Call function again
           - See how function uses new values
        """)

