"""
Class & Instances Visualization
Shows how classes are blueprints and instances have their own memory
"""

import streamlit as st
import random

def generate_instance_id():
    """Generate a unique instance ID"""
    return f"Instance_{random.randint(1000, 9999)}"

def show_class_instances_visualization():
    """Main function to display the class & instances visualization"""
    
    st.markdown('<h2 style="color: #2196F3;">🏛️ Classes & Instances</h2>', unsafe_allow_html=True)
    st.write("See how classes are blueprints and each instance (object) gets its own memory!")
    
    # Initialize session state
    if 'instances' not in st.session_state:
        st.session_state.instances = {}
    if 'instance_counter' not in st.session_state:
        st.session_state.instance_counter = 1
    
    # Display class definition
    st.markdown("### 📘 Class Definition (Blueprint)")
    
    col_def1, col_def2 = st.columns([1, 1])
    
    with col_def1:
        st.code("""
class Account:
    # Class variables (shared by all)
    bank_name = "MyBank"
    
    def __init__(self, number, name):
        # Instance variables (unique to each)
        self.accNumber = number
        self.name = name
        self.balance = 0
""", language="python")
    
    with col_def2:
        st.markdown("""
        **Class = Blueprint**
        
        Think of a class like a **cookie cutter** 🍪
        - The **class** is the shape/template
        - Each **instance** is a unique cookie
        - All cookies have the same shape
        - But each can have different decorations!
        
        **Class Variables:**
        - `bank_name` - shared by ALL accounts
        
        **Instance Variables:**
        - `accNumber`, `name`, `balance` - unique to EACH account
        """)
    
    st.info("💡 The class is just a definition. It doesn't store actual data until we create instances!")
    
    # Create instances section
    st.markdown("---")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### ➕ Create Instance")
        st.write("Create a new Account object:")
        
        with st.form("create_instance_form"):
            acc_number = st.number_input("Account Number", min_value=1, value=101, step=1)
            acc_name = st.text_input("Account Name", placeholder="e.g., Alice, Bob")
            create_btn = st.form_submit_button("🎨 Create Instance", use_container_width=True)
        
        if create_btn and acc_name:
            instance_id = f"ac{st.session_state.instance_counter}"
            st.session_state.instances[instance_id] = {
                'var_name': instance_id,
                'accNumber': acc_number,
                'name': acc_name,
                'balance': 0,
                'created_order': st.session_state.instance_counter
            }
            st.session_state.instance_counter += 1
            st.success(f"✅ Created instance: {instance_id}")
            st.rerun()
        
        # Modify instance section
        if st.session_state.instances:
            st.markdown("### 💰 Modify Instance")
            
            with st.form("modify_instance_form"):
                selected_instance = st.selectbox(
                    "Select Instance",
                    options=list(st.session_state.instances.keys())
                )
                
                operation = st.radio("Operation", ["Deposit", "Withdraw"])
                amount = st.number_input("Amount", min_value=0, value=100, step=10)
                
                modify_btn = st.form_submit_button("💸 Execute", use_container_width=True)
            
            if modify_btn and selected_instance:
                if operation == "Deposit":
                    st.session_state.instances[selected_instance]['balance'] += amount
                    st.success(f"✅ Deposited ${amount} to {selected_instance}")
                else:
                    if st.session_state.instances[selected_instance]['balance'] >= amount:
                        st.session_state.instances[selected_instance]['balance'] -= amount
                        st.success(f"✅ Withdrew ${amount} from {selected_instance}")
                    else:
                        st.error("❌ Insufficient balance!")
                st.rerun()
        
        # Clear button
        if st.session_state.instances:
            if st.button("🗑️ Clear All Instances", use_container_width=True):
                st.session_state.instances = {}
                st.session_state.instance_counter = 1
                st.rerun()
    
    with col2:
        st.markdown("### 🎨 Instance Memory")
        
        if not st.session_state.instances:
            st.info("👈 Create your first Account instance to see it in memory!")
            
            st.markdown("""
            **What will happen:**
            1. Python allocates new memory space
            2. Copies the blueprint structure
            3. Assigns unique values to instance variables
            4. Each instance is completely independent!
            """)
        else:
            # Show class variable (shared)
            st.markdown("#### 🌍 Class Variable (Shared by All)")
            st.markdown("""
            <div style="
                background: linear-gradient(135deg, #9C27B0 0%, #7B1FA2 100%);
                color: white;
                padding: 1rem;
                border-radius: 8px;
                margin-bottom: 1.5rem;
                text-align: center;
                font-size: 1.2rem;
                font-weight: bold;
            ">
                bank_name = "MyBank"
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### 📦 Instance Memory Spaces")
            st.write(f"**Total instances created:** {len(st.session_state.instances)}")
            
            # Display each instance
            for instance_id, instance_data in st.session_state.instances.items():
                # Create a unique colored box for each instance
                colors = ['green', 'blue', 'orange', 'red', 'violet', 'rainbow']
                color = colors[instance_data['created_order'] % len(colors)]
                
                # Use Streamlit's container with custom styling
                with st.container():
                    st.markdown(f"**::{color}[{instance_data['var_name']} = Account(...)]**")
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.write("**accNumber:**")
                        st.write("**name:**")
                        st.write("**balance:**")
                    with col2:
                        st.write(f"{instance_data['accNumber']}")
                        st.write(f'"{instance_data["name"]}"')
                        st.write(f"${instance_data['balance']}")
                
                    # Add delete button
                    col_del1, col_del2 = st.columns([1, 3])
                    with col_del1:
                        if st.button(f"🗑️ Delete", key=f"del_{instance_id}"):
                            del st.session_state.instances[instance_id]
                            st.rerun()
                    
                    st.divider()
            
            # Show Python code
            st.markdown("---")
            st.markdown("### 🐍 Python Code Equivalent")
            
            code_lines = ["# Class definition", "class Account:", "    bank_name = 'MyBank'", 
                         "    def __init__(self, number, name):", "        self.accNumber = number",
                         "        self.name = name", "        self.balance = 0", ""]
            code_lines.append("# Creating instances")
            
            for instance_id, instance_data in st.session_state.instances.items():
                code_lines.append(f"{instance_data['var_name']} = Account({instance_data['accNumber']}, '{instance_data['name']}')")
            
            if any(inst['balance'] != 0 for inst in st.session_state.instances.values()):
                code_lines.append("\n# Modifying instances")
                for instance_id, instance_data in st.session_state.instances.items():
                    if instance_data['balance'] > 0:
                        code_lines.append(f"# {instance_data['var_name']}.balance = {instance_data['balance']}")
            
            st.code("\n".join(code_lines), language="python")
    
    # Comparison section
    if len(st.session_state.instances) >= 2:
        st.markdown("---")
        st.markdown("### 🔍 Compare Instances")
        
        instance_list = list(st.session_state.instances.keys())
        col_cmp1, col_cmp2, col_cmp3 = st.columns(3)
        
        with col_cmp1:
            st.markdown("**Instance 1**")
            inst1 = st.session_state.instances[instance_list[0]]
            st.write(f"🏷️ {inst1['var_name']}")
            st.write(f"🔢 Account: {inst1['accNumber']}")
            st.write(f"👤 Name: {inst1['name']}")
            st.write(f"💰 Balance: ${inst1['balance']}")
        
        with col_cmp2:
            st.markdown("**vs**")
            st.markdown("""
            <div style="text-align: center; font-size: 3rem; padding: 2rem 0;">
                ≠
            </div>
            """, unsafe_allow_html=True)
        
        with col_cmp3:
            st.markdown("**Instance 2**")
            inst2 = st.session_state.instances[instance_list[1]]
            st.write(f"🏷️ {inst2['var_name']}")
            st.write(f"🔢 Account: {inst2['accNumber']}")
            st.write(f"👤 Name: {inst2['name']}")
            st.write(f"💰 Balance: ${inst2['balance']}")
        
        st.success("✅ Each instance has its own separate memory! Changes to one don't affect the other.")
    
    # Educational section
    st.markdown("---")
    with st.expander("📚 Learn More: Classes & Instances"):
        col_ed1, col_ed2 = st.columns(2)
        
        with col_ed1:
            st.markdown("""
            ### 📘 What is a Class?
            
            A class is a **blueprint** or **template** for creating objects.
            
            **Think of it like:**
            - 🏗️ **Architectural blueprint** for houses
            - 🍪 **Cookie cutter** for making cookies
            - 📋 **Form template** to fill out
            
            **The class defines:**
            - What data each object will store (attributes)
            - What actions each object can perform (methods)
            
            **Example:**
            ```python
            class Account:
                bank_name = "MyBank"  # Class variable
                
                def __init__(self, number, name):
                    self.accNumber = number  # Instance variable
                    self.name = name        # Instance variable
                    self.balance = 0        # Instance variable
            ```
            
            **Class Variables:**
            - Shared by ALL instances
            - `bank_name` is the same for every account
            
            **Instance Variables:**
            - Unique to EACH instance
            - Each account has its own number, name, balance
            """)
        
        with col_ed2:
            st.markdown("""
            ### 🎨 What is an Instance?
            
            An instance is a **specific object** created from a class.
            
            **Creating an instance:**
            ```python
            ac1 = Account(101, "Alice")
            ac2 = Account(102, "Bob")
            ```
            
            **What happens:**
            1. Python allocates new memory space
            2. Copies the structure from the class blueprint
            3. Runs `__init__()` to set initial values
            4. Returns a reference to the new object
            
            **Each instance:**
            - Has its own memory space
            - Has its own copy of instance variables
            - Shares class variables with all other instances
            - Can be modified independently
            
            **Example:**
            ```python
            ac1.balance = 100  # Only affects ac1
            ac2.balance = 200  # Only affects ac2
            
            print(ac1.balance)  # 100
            print(ac2.balance)  # 200
            ```
            """)
        
        st.markdown("""
        ---
        ### 🎯 Key Concepts
        
        1. **Class = Blueprint, Instance = Object**
           - Class is the recipe
           - Instance is the actual cake
        
        2. **Each Instance is Independent**
           - Separate memory space
           - Changes don't affect other instances
           - Can have different values
        
        3. **Instance Variables vs Class Variables**
           - Instance variables: unique to each object (`self.balance`)
           - Class variables: shared by all objects (`bank_name`)
        
        4. **The `__init__` Method**
           - Special method called when creating instance
           - Initializes instance variables
           - `self` refers to the specific instance being created
        
        5. **The `self` Parameter**
           - First parameter in instance methods
           - Refers to the current instance
           - Allows access to instance variables
        
        ### 🧪 Experiment Ideas
        
        1. **Create multiple accounts:**
           - Make 3-4 different accounts
           - Give them different balances
           - See how they're all independent
        
        2. **Modify instances:**
           - Deposit to one account
           - Withdraw from another
           - Notice others aren't affected
        
        3. **Compare instances:**
           - Look at the comparison section
           - See how each instance has unique values
           - All from the same class blueprint!
        """)

