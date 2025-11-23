"""
Self Concept Visualization
Shows how 'self' refers to the specific instance in class methods
"""

import streamlit as st
import time

def show_self_concept_visualization():
    """Main function to display the self concept visualization"""
    
    st.markdown('<h2 style="color: #2196F3;">🎯 Understanding "self" in Classes</h2>', unsafe_allow_html=True)
    st.write("See how `self` is a reference to the specific instance that called the method!")
    
    # Show concept overview first
    with st.expander("💡 Important Concept: Methods are Shared, Data is Not", expanded=False):
        col_concept1, col_concept2 = st.columns(2)
        
        with col_concept1:
            st.markdown("### 📚 Class Level (Shared)")
            st.info("""
            **Methods are defined ONCE in the class:**
            - `deposit()` method exists once
            - `withdraw()` method exists once
            - All instances **share** the same method code
            
            Think: One recipe, many cakes! 🍰
            """)
            st.code("""
class Account:
    # Methods defined once
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
""", language="python")
        
        with col_concept2:
            st.markdown("### 🎨 Instance Level (Unique)")
            st.success("""
            **Each instance has its OWN data:**
            - ac1 has its own balance
            - ac2 has its own balance
            - Changes to one don't affect others
            
            Think: Same recipe, different decorations! 🎂
            """)
            st.code("""
ac1 = Account(101, "Alice")
# ac1.balance = 0

ac2 = Account(102, "Bob")
# ac2.balance = 0

# Same deposit() method
# Different balance data!
""", language="python")
        
        st.warning("""
        **🎯 The Magic of `self`:**
        - When `ac1.deposit(100)` is called, the `deposit()` method receives `self = ac1`
        - When `ac2.deposit(200)` is called, the SAME `deposit()` method receives `self = ac2`
        - The method code is shared, but `self` tells it which instance's data to use!
        """)
    
    # Initialize session state
    if 'accounts' not in st.session_state:
        st.session_state.accounts = {}
    if 'executing_method' not in st.session_state:
        st.session_state.executing_method = None
    if 'execution_steps' not in st.session_state:
        st.session_state.execution_steps = []
    
    # Display class definition with self highlighted
    st.markdown("### 📘 Class Definition with Methods")
    
    col_def1, col_def2 = st.columns([1, 1])
    
    with col_def1:
        st.code("""
class Account:
    def __init__(self, number, name):
        self.accNumber = number
        self.name = name
        self.balance = 0
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            return self.balance
        else:
            return "Insufficient funds"
""", language="python")
    
    with col_def2:
        st.markdown("""
        ### 🤔 What is `self`?
        
        **`self` is like saying "ME" or "THIS OBJECT"**
        
        When you call:
        ```python
        ac1.deposit(100)
        ```
        
        Inside the `deposit` method:
        - `self` = `ac1`
        - `self.balance` = `ac1.balance`
        
        **Think of it like:**
        - 🏠 You have multiple houses (instances)
        - 📍 `self` points to "THIS house" 
        - 🚪 When you open a door, you open THIS house's door
        
        **Key Point:**
        `self` is **automatically** passed by Python!
        """)
    
    st.info("💡 The first parameter in every instance method is `self` - it refers to the instance that called the method!")
    
    # Create accounts section
    st.markdown("---")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### ➕ Create Accounts")
        
        with st.form("create_account_form"):
            acc_num = st.number_input("Account Number", min_value=1, value=101, step=1)
            acc_name = st.text_input("Name", placeholder="e.g., Alice")
            create_btn = st.form_submit_button("🎨 Create Account", use_container_width=True)
        
        if create_btn and acc_name:
            acc_id = f"ac{len(st.session_state.accounts) + 1}"
            st.session_state.accounts[acc_id] = {
                'var_name': acc_id,
                'accNumber': acc_num,
                'name': acc_name,
                'balance': 0
            }
            st.success(f"✅ Created {acc_id}")
            st.rerun()
        
        # Execute methods section
        if st.session_state.accounts:
            st.markdown("### 🎬 Call a Method")
            
            with st.form("call_method_form"):
                selected_acc = st.selectbox(
                    "Select Account (this will be 'self')",
                    options=list(st.session_state.accounts.keys()),
                    format_func=lambda x: f"{x} ({st.session_state.accounts[x]['name']})"
                )
                
                method = st.radio("Method to Call", ["deposit", "withdraw"])
                amount = st.number_input("Amount", min_value=1, value=100, step=10)
                
                execute_btn = st.form_submit_button("▶️ Execute Method", use_container_width=True)
            
            if execute_btn and selected_acc:
                # Prepare execution visualization
                st.session_state.executing_method = {
                    'account': selected_acc,
                    'method': method,
                    'amount': amount,
                    'self_ref': st.session_state.accounts[selected_acc]
                }
                
                # Execute the actual operation
                if method == "deposit":
                    st.session_state.accounts[selected_acc]['balance'] += amount
                    result = st.session_state.accounts[selected_acc]['balance']
                else:  # withdraw
                    if st.session_state.accounts[selected_acc]['balance'] >= amount:
                        st.session_state.accounts[selected_acc]['balance'] -= amount
                        result = st.session_state.accounts[selected_acc]['balance']
                    else:
                        result = "Insufficient funds"
                
                st.session_state.executing_method['result'] = result
                st.success(f"✅ Method executed!")
                st.rerun()
            
            if st.button("🔄 Clear Execution", use_container_width=True):
                st.session_state.executing_method = None
                st.rerun()
            
            if st.button("🗑️ Clear All", use_container_width=True):
                st.session_state.accounts = {}
                st.session_state.executing_method = None
                st.rerun()
    
    with col2:
        st.markdown("### 🧠 Account Instances")
        
        if not st.session_state.accounts:
            st.info("👈 Create accounts first to see how `self` works!")
        else:
            # Show which account is active
            if st.session_state.executing_method:
                active_acc = st.session_state.executing_method['account']
                st.warning(f"⚡ **Active:** `self` currently points to **{active_acc}** (highlighted below)")
            
            # Show all accounts
            for acc_id, acc_data in st.session_state.accounts.items():
                # Highlight the account being executed
                is_executing = (st.session_state.executing_method and 
                               st.session_state.executing_method['account'] == acc_id)
                
                # Use Streamlit container with highlighting
                with st.container():
                    if is_executing:
                        st.markdown(f"### :orange[{acc_data['var_name']}] 👉 **self points here!**")
                    else:
                        st.markdown(f"### :green[{acc_data['var_name']}]")
                    
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.write("**accNumber:**")
                        st.write("**name:**")
                        st.write("**balance:**")
                    with col2:
                        st.write(f"{acc_data['accNumber']}")
                        st.write(f'"{acc_data["name"]}"')
                        if is_executing:
                            st.write(f":orange[**${acc_data['balance']}**]")
                        else:
                            st.write(f"${acc_data['balance']}")
                    
                    st.divider()
    
    # Method execution visualization
    if st.session_state.executing_method:
        st.markdown("---")
        st.markdown("### 🎬 Method Execution Visualization")
        
        exec_data = st.session_state.executing_method
        method_name = exec_data['method']
        amount = exec_data['amount']
        acc_var = exec_data['account']
        acc_name = exec_data['self_ref']['name']
        
        # Show what's happening in big picture
        st.info(f"🎯 **Method Call:** `{acc_var}.{method_name}({amount})`")
        
        # Visual flow diagram
        col_flow1, col_flow2, col_flow3 = st.columns([1, 1, 1])
        with col_flow1:
            st.markdown("**Step 1: Who Called?**")
            st.success(f"✋ **{acc_var}** ({acc_name})")
            st.caption("This is the account calling the method")
        
        with col_flow2:
            st.markdown("**Step 2: self = ?**")
            st.warning(f"👉 **self** = **{acc_var}**")
            st.caption("self becomes a reference to the caller")
        
        with col_flow3:
            st.markdown("**Step 3: What Happens?**")
            st.info(f"🔄 Modify **self**.balance")
            st.caption(f"Changes {acc_var}'s balance only")
        
        st.markdown("---")
        
        # Show step-by-step execution
        col_step1, col_step2 = st.columns([1, 1])
        
        with col_step1:
            st.markdown("#### 📝 Code Being Executed")
            
            if method_name == "deposit":
                code = f"""
def deposit(self, amount):
    # self = {acc_var}
    # amount = {amount}
    
    self.balance = self.balance + amount
    # self.balance = {exec_data['self_ref']['balance'] - amount} + {amount}
    # self.balance = {exec_data['result']}
    
    return self.balance
    # return {exec_data['result']}
"""
            else:
                old_balance = exec_data['self_ref']['balance'] + amount
                code = f"""
def withdraw(self, amount):
    # self = {acc_var}
    # amount = {amount}
    
    if amount <= self.balance:
        # if {amount} <= {old_balance}:
        
        self.balance = self.balance - amount
        # self.balance = {old_balance} - {amount}
        # self.balance = {exec_data['result']}
        
        return self.balance
        # return {exec_data['result']}
"""
            
            st.code(code, language="python")
        
        with col_step2:
            st.markdown("#### 🔍 Step-by-Step Breakdown")
            
            steps = []
            if method_name == "deposit":
                old_balance = exec_data['self_ref']['balance'] - amount
                steps = [
                    ("1️⃣", "Method Called", f"{acc_var}.deposit({amount})", "The account object calls its deposit method"),
                    ("2️⃣", "Python Sets self", f"self = {acc_var}", f"Python automatically passes {acc_var} as self"),
                    ("3️⃣", "Read Current Balance", f"self.balance = {old_balance}", f"Access the balance of {acc_var}"),
                    ("4️⃣", "Calculate New Balance", f"{old_balance} + {amount} = {exec_data['result']}", "Add the deposit amount"),
                    ("5️⃣", "Update Balance", f"self.balance = {exec_data['result']}", f"Store new balance in {acc_var}"),
                    ("6️⃣", "Return Value", f"return {exec_data['result']}", "Send back the new balance")
                ]
            else:
                old_balance = exec_data['self_ref']['balance'] + amount
                if exec_data['result'] != "Insufficient funds":
                    steps = [
                        ("1️⃣", "Method Called", f"{acc_var}.withdraw({amount})", "The account object calls its withdraw method"),
                        ("2️⃣", "Python Sets self", f"self = {acc_var}", f"Python automatically passes {acc_var} as self"),
                        ("3️⃣", "Check Balance", f"{amount} <= {old_balance} ✅", "Verify sufficient funds"),
                        ("4️⃣", "Calculate New Balance", f"{old_balance} - {amount} = {exec_data['result']}", "Subtract the withdrawal"),
                        ("5️⃣", "Update Balance", f"self.balance = {exec_data['result']}", f"Store new balance in {acc_var}"),
                        ("6️⃣", "Return Value", f"return {exec_data['result']}", "Send back the new balance")
                    ]
                else:
                    steps = [
                        ("1️⃣", "Method Called", f"{acc_var}.withdraw({amount})", "The account object calls its withdraw method"),
                        ("2️⃣", "Python Sets self", f"self = {acc_var}", f"Python automatically passes {acc_var} as self"),
                        ("3️⃣", "Check Balance", f"{amount} > {exec_data['self_ref']['balance']} ❌", "Insufficient funds!"),
                    ]
            
            for item in steps:
                if len(item) == 4:
                    emoji, title, code, explanation = item
                    with st.container():
                        st.markdown(f"**{emoji} {title}**")
                        st.code(code, language="python")
                        st.caption(f"💡 {explanation}")
                        st.write("")  # Add spacing
                else:
                    emoji, title, code = item
                    with st.container():
                        st.markdown(f"**{emoji} {title}**")
                        st.code(code, language="python")
                        st.write("")  # Add spacing
        
        # Show the result with clear explanation
        st.markdown("---")
        st.success(f"✅ **Result:** `{acc_var}.balance` is now **${exec_data['result']}**")
        
        # Show method reuse concept
        st.markdown("### 🔄 Method Reuse Concept")
        col_reuse1, col_reuse2, col_reuse3 = st.columns([1, 1, 1])
        
        with col_reuse1:
            st.markdown("**📚 Class Level**")
            st.code(f"""
# Method defined ONCE
def {method_name}(self, amount):
    self.balance += amount
    return self.balance
""", language="python")
            st.caption("This code exists only once in memory")
        
        with col_reuse2:
            st.markdown("**🎯 This Call**")
            st.info(f"""
            **Call:** `{acc_var}.{method_name}({amount})`
            
            **Python does:**
            1. Finds {method_name}() in class
            2. Passes {acc_var} as `self`
            3. Executes with {acc_var}'s data
            
            Result: {acc_var}.balance changed
            """)
        
        with col_reuse3:
            st.markdown("**💭 Other Calls**")
            st.success("""
            Same method can be called by:
            - ac1.deposit(50)
            - ac2.deposit(75)
            - ac3.deposit(100)
            
            Same method code!
            Different self each time!
            """)
        
        # Key takeaway box
        st.markdown("### 🎯 Key Takeaway")
        col_key1, col_key2 = st.columns([1, 2])
        with col_key1:
            st.markdown("**Remember:**")
            st.code(f"self = {acc_var}")
        with col_key2:
            st.markdown(f"""
            - Methods are defined **ONCE** in the class (shared by all)
            - `self` is the **parameter** that receives the calling instance
            - When `{acc_var}` calls the method, Python passes `{acc_var}` as `self`
            - Inside the method, `self` refers to `{acc_var}`
            - Same method code works for ALL instances - `self` makes it specific!
            - Other accounts are **not affected** - only `{acc_var}` changed!
            """)
    
    # Educational section
    st.markdown("---")
    with st.expander("📚 Learn More: Understanding 'self'"):
        col_edu1, col_edu2 = st.columns(2)
        
        with col_edu1:
            st.markdown("""
            ### 🎯 What is `self`?
            
            **`self` is a reference to the instance that called the method.**
            
            **Why do we need `self`?**
            
            Methods are defined ONCE in the class. When multiple instances exist, 
            `self` tells the method which instance's data to work with!
            
            **Analogy 1: Universal Remote Control**
            - One remote (the method) 🎮
            - Many TVs (instances) 📺📺📺
            - Point at TV #1 → controls TV #1 (self = TV1)
            - Point at TV #2 → controls TV #2 (self = TV2)
            - Same remote, different target!
            
            **Analogy 2: Classroom**
            - Teacher says "Raise YOUR hand" (calls a method)
            - "YOUR" = `self` (refers to the specific student)
            - Same instruction, different student responds!
            
            **In Code:**
            ```python
            ac1 = Account(101, "Alice")
            ac2 = Account(102, "Bob")
            
            ac1.deposit(100)  # self = ac1
            ac2.deposit(200)  # self = ac2
            
            # Same deposit() method code!
            # Different self each time!
            ```
            
            **Key Points:**
            1. `self` is the **first parameter** in every instance method
            2. You **don't pass** `self` when calling - Python does it automatically
            3. `self` refers to the **specific instance** that called the method
            4. Inside the method, `self.attribute` accesses that instance's attribute
            
            ### 🔑 Why "self"?
            
            **Without self:**
            ```python
            def deposit(amount):
                balance = balance + amount  # Which balance?
            ```
            
            **With self:**
            ```python
            def deposit(self, amount):
                self.balance = self.balance + amount  # THIS instance's balance!
            ```
            """)
        
        with col_edu2:
            st.markdown("""
            ### 🎬 How It Works
            
            **When you write:**
            ```python
            ac1.deposit(100)
            ```
            
            **Python translates to:**
            ```python
            Account.deposit(ac1, 100)
            ```
            
            **Inside deposit method:**
            ```python
            def deposit(self, amount):
                # self is now ac1
                self.balance = self.balance + amount
                # ac1.balance = ac1.balance + 100
            ```
            
            ### 📊 Multiple Instances Example
            
            ```python
            ac1 = Account(101, "Alice")
            ac2 = Account(102, "Bob")
            
            ac1.balance = 0
            ac2.balance = 0
            
            # Call deposit on ac1
            ac1.deposit(100)
            # Inside method: self = ac1
            # self.balance = 0 + 100 = 100
            
            # Call deposit on ac2
            ac2.deposit(200)
            # Inside method: self = ac2
            # self.balance = 0 + 200 = 200
            
            print(ac1.balance)  # 100
            print(ac2.balance)  # 200
            ```
            
            **Notice:** 
            - Same method (`deposit`)
            - Different instances (`ac1`, `ac2`)
            - `self` points to different instances each time
            - Each modifies its own balance!
            
            ### 🧪 Experiment
            
            Try this:
            1. Create 2-3 accounts
            2. Call deposit on one account
            3. Watch how `self` points to that specific account
            4. Call withdraw on a different account
            5. See how `self` now points to the other account
            6. Notice: each method affects only the instance that called it!
            """)
        
        st.markdown("""
        ---
        ### 💡 Common Mistakes
        
        **❌ Mistake 1: Forgetting self**
        ```python
        class Account:
            def deposit(amount):  # Missing self!
                balance = balance + amount  # Won't work!
        ```
        
        **✅ Correct:**
        ```python
        class Account:
            def deposit(self, amount):  # self is first!
                self.balance = self.balance + amount  # Works!
        ```
        
        **❌ Mistake 2: Passing self when calling**
        ```python
        ac1.deposit(ac1, 100)  # Don't do this!
        ```
        
        **✅ Correct:**
        ```python
        ac1.deposit(100)  # Python adds self automatically!
        ```
        
        ### 🏭 Memory Efficiency & Method Sharing
        
        **Why does Python use `self`?**
        
        Imagine 1000 bank accounts. If Python created a separate copy 
        of `deposit()` and `withdraw()` for each account:
        - 1000 copies of deposit() = wasteful! 😱
        - 1000 copies of withdraw() = wasteful! 😱
        
        **Python's Smart Approach:**
        - ✅ ONE copy of deposit() (in the class)
        - ✅ ONE copy of withdraw() (in the class)
        - ✅ Each account has its own DATA only
        - 🎯 `self` tells the method which account's data to use!
        
        **Result:** Memory efficient + works for all instances! 🚀
        
        ### 🎯 Remember
        
        - **Methods are shared** (created once in the class)
        - **Data is unique** (each instance has its own)
        - **`self`** = "THIS instance" - links method to data
        - **First parameter** in every instance method
        - **Automatically passed** by Python
        - **Allows methods** to access/modify instance attributes
        - **Different each time** - points to whatever instance called it!
        """)

