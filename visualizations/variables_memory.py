"""
Variables & Memory Visualization
Shows how variables are stored in memory with visual representation
"""

import streamlit as st
import random

def generate_memory_address():
    """Generate a fake memory address for visualization"""
    return f"0x{random.randint(0x1000, 0xFFFF):04X}"

def show_variables_visualization():
    """Main function to display the variables & memory visualization"""
    
    st.markdown('<h2 style="color: #2196F3;">📦 Variables & Memory</h2>', unsafe_allow_html=True)
    st.write("See how variables work like labeled boxes that store values in computer memory!")
    
    # Initialize session state for variables
    if 'variables' not in st.session_state:
        st.session_state.variables = {}
        st.session_state.memory_addresses = {}
    
    # Create two columns: input form and visualization
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### ➕ Add/Edit Variable")
        
        with st.form(key="variable_form", clear_on_submit=True):
            var_name = st.text_input(
                "Variable Name",
                placeholder="e.g., age, name, balance",
                help="Enter a variable name (letters, numbers, underscore)"
            )
            
            var_value = st.text_input(
                "Value",
                placeholder="e.g., 10, 'Tom', True",
                help="Enter the value to store"
            )
            
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                submit_btn = st.form_submit_button("💾 Save", use_container_width=True)
            with col_btn2:
                clear_btn = st.form_submit_button("🗑️ Clear All", use_container_width=True)
        
        # Handle form submission
        if submit_btn and var_name:
            # Determine the type and store the variable
            value_to_store = var_value
            var_type = "str"
            
            # Try to parse the value
            if var_value.lower() in ['true', 'false']:
                value_to_store = var_value.lower() == 'true'
                var_type = "bool"
            elif var_value.isdigit() or (var_value.startswith('-') and var_value[1:].isdigit()):
                value_to_store = int(var_value)
                var_type = "int"
            elif var_value.replace('.', '', 1).isdigit():
                value_to_store = float(var_value)
                var_type = "float"
            elif var_value.startswith("'") or var_value.startswith('"'):
                value_to_store = var_value.strip("'\"")
                var_type = "str"
            
            # Assign or update variable
            if var_name not in st.session_state.memory_addresses:
                # New variable - assign new memory address
                st.session_state.memory_addresses[var_name] = generate_memory_address()
            
            st.session_state.variables[var_name] = {
                'value': value_to_store,
                'type': var_type,
                'display_value': var_value
            }
            st.success(f"✅ Variable '{var_name}' saved!")
            st.rerun()
        
        if clear_btn:
            st.session_state.variables = {}
            st.session_state.memory_addresses = {}
            st.success("🗑️ All variables cleared!")
            st.rerun()
        
        # Show variable count
        if st.session_state.variables:
            st.info(f"📊 Total variables: {len(st.session_state.variables)}")
    
    with col2:
        st.markdown("### 🧠 Memory View")
        
        if not st.session_state.variables:
            st.info("👈 Add your first variable to see it appear in memory!")
            st.markdown("""
            **How it works:**
            - Each variable is like a **labeled box** in memory
            - The **name** is the label on the box
            - The **value** is what's inside the box
            - The **memory address** is the box's location
            """)
        else:
            # Display variables as memory boxes
            st.write("#### Computer Memory")
            
            for var_name, var_data in st.session_state.variables.items():
                memory_addr = st.session_state.memory_addresses[var_name]
                value = var_data['value']
                var_type = var_data['type']
                display_value = var_data['display_value']
                
                # Choose color based on type
                type_colors = {
                    'int': '#4CAF50',
                    'float': '#2196F3',
                    'str': '#FF9800',
                    'bool': '#9C27B0'
                }
                color = type_colors.get(var_type, '#757575')
                
                # Create a beautiful card for each variable
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, {color}22 0%, {color}44 100%);
                    border-left: 5px solid {color};
                    padding: 1.5rem;
                    border-radius: 10px;
                    margin: 1rem 0;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                ">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div style="flex: 1;">
                            <div style="font-size: 0.9rem; color: #666; margin-bottom: 0.5rem;">
                                📍 Memory: <code>{memory_addr}</code>
                            </div>
                            <div style="font-size: 1.5rem; font-weight: bold; color: {color}; margin-bottom: 0.5rem;">
                                {var_name}
                            </div>
                            <div style="font-size: 1.8rem; font-weight: bold; color: #333;">
                                = {display_value}
                            </div>
                        </div>
                        <div style="text-align: right;">
                            <div style="
                                background: {color};
                                color: white;
                                padding: 0.5rem 1rem;
                                border-radius: 20px;
                                font-size: 0.9rem;
                                font-weight: bold;
                            ">
                                {var_type}
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Add delete button
                col_del1, col_del2, col_del3 = st.columns([1, 1, 3])
                with col_del1:
                    if st.button(f"🗑️ Delete", key=f"del_{var_name}"):
                        del st.session_state.variables[var_name]
                        del st.session_state.memory_addresses[var_name]
                        st.rerun()
            
            # Show Python code equivalent
            st.markdown("---")
            st.markdown("### 🐍 Python Code Equivalent")
            code_lines = []
            for var_name, var_data in st.session_state.variables.items():
                display_value = var_data['display_value']
                if var_data['type'] == 'str' and not (display_value.startswith("'") or display_value.startswith('"')):
                    code_lines.append(f"{var_name} = '{display_value}'")
                else:
                    code_lines.append(f"{var_name} = {display_value}")
            
            code = "\n".join(code_lines)
            st.code(code, language="python")
    
    # Educational section at the bottom
    st.markdown("---")
    with st.expander("📚 Learn More: How Variables Work"):
        st.markdown("""
        ### Understanding Variables and Memory
        
        **What is a variable?**
        - A variable is like a **labeled storage box** in the computer's memory
        - You give it a **name** (like `age`, `balance`, `name`)
        - You put a **value** inside it (like `15`, `100`, `'Tom'`)
        
        **What is memory?**
        - Your computer has memory (RAM) where it stores information
        - Each storage location has an **address** (like a house address)
        - Addresses are in hexadecimal format (like `0x1A4F`)
        
        **What happens when you create a variable?**
        1. Python finds empty space in memory
        2. It stores your value there
        3. It creates a **label** (variable name) pointing to that location
        4. Now you can use the name instead of remembering the address!
        
        **Example:**
        ```python
        age = 15  # Python stores 15 in memory and labels it 'age'
        print(age)  # Python finds the memory location and reads: 15
        ```
        
        **Try this:**
        - Create a variable called `balance` with value `100`
        - Create another called `deposit` with value `50`
        - See how each gets its own memory location!
        - Change `balance` to `150` - see how the address stays the same but value changes!
        """)

