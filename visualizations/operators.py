import streamlit as st

def show():
    st.markdown('<h2 style="color: #2196F3;">➕ Python Operators Playground</h2>', unsafe_allow_html=True)
    st.write("Learn how to perform operations on values in Python!")
    
    # Overview
    with st.expander("📚 What are Operators?", expanded=False):
        st.markdown("""
        **Operators** are special symbols that perform operations on values.
        
        Think of operators like **action buttons** on a calculator:
        - ➕ Add two numbers
        - ➖ Subtract one from another
        - ✖️ Multiply them together
        - ➗ Divide them
        
        Python has different types of operators for different jobs!
        """)
    
    # Create tabs for different operator types
    op_tabs = st.tabs(["🔢 Arithmetic", "⚖️ Comparison", "🔀 Logical", "🎯 Assignment"])
    
    # ============================================
    # TAB 1: ARITHMETIC OPERATORS
    # ============================================
    with op_tabs[0]:
        st.markdown("### 🔢 Arithmetic Operators")
        st.write("Perform math operations on numbers!")
        
        # Show all arithmetic operators
        col_table1, col_table2 = st.columns(2)
        
        with col_table1:
            st.markdown("""
            | Operator | Name | Example | Result |
            |----------|------|---------|--------|
            | `+` | Addition | `5 + 3` | `8` |
            | `-` | Subtraction | `5 - 3` | `2` |
            | `*` | Multiplication | `5 * 3` | `15` |
            | `/` | Division | `10 / 3` | `3.333...` |
            """)
        
        with col_table2:
            st.markdown("""
            | Operator | Name | Example | Result |
            |----------|------|---------|--------|
            | `//` | Floor Division | `10 // 3` | `3` |
            | `%` | Modulus (Remainder) | `10 % 3` | `1` |
            | `**` | Exponent (Power) | `2 ** 3` | `8` |
            |  |  |  |  |
            """)
        
        st.markdown("---")
        st.markdown("#### 🎮 Try Arithmetic Operations!")
        
        col_a1, col_a2, col_a3, col_a4 = st.columns([2, 1, 2, 2])
        
        with col_a1:
            num1 = st.number_input("First number", value=10, key="arith_num1")
        
        with col_a2:
            operator = st.selectbox("Operator", ["+", "-", "*", "/", "//", "%", "**"], key="arith_op")
        
        with col_a3:
            num2 = st.number_input("Second number", value=3, key="arith_num2")
        
        with col_a4:
            st.write("")  # spacing
            calc_btn = st.button("🔢 Calculate", use_container_width=True)
        
        if calc_btn or (num1 is not None and num2 is not None):
            try:
                if operator == "+":
                    result = num1 + num2
                    explanation = f"Add {num1} and {num2}"
                elif operator == "-":
                    result = num1 - num2
                    explanation = f"Subtract {num2} from {num1}"
                elif operator == "*":
                    result = num1 * num2
                    explanation = f"Multiply {num1} by {num2}"
                elif operator == "/":
                    result = num1 / num2
                    explanation = f"Divide {num1} by {num2}"
                elif operator == "//":
                    result = num1 // num2
                    explanation = f"Divide {num1} by {num2} and drop decimals"
                elif operator == "%":
                    result = num1 % num2
                    explanation = f"Remainder when {num1} is divided by {num2}"
                elif operator == "**":
                    result = num1 ** num2
                    explanation = f"Raise {num1} to the power of {num2}"
                
                # Display result
                col_res1, col_res2 = st.columns([1, 2])
                
                with col_res1:
                    st.markdown("### Result:")
                    st.markdown(f"## :green[{result}]")
                
                with col_res2:
                    st.info(f"""
                    **Operation:** {explanation}
                    
                    **Python Code:**
                    ```python
                    result = {num1} {operator} {num2}
                    print(result)  # {result}
                    ```
                    """)
                
                # Special explanations
                if operator == "//":
                    st.warning(f"""
                    💡 **Floor Division** gives you the whole number part only.
                    - Regular division: `{num1} / {num2}` = {num1 / num2}
                    - Floor division: `{num1} // {num2}` = {result}
                    """)
                elif operator == "%":
                    st.warning(f"""
                    💡 **Modulus (%)** gives you the remainder.
                    - {num1} ÷ {num2} = {num1 // num2} remainder **{result}**
                    - Useful for checking if a number is even/odd!
                    - Example: `10 % 2` = 0 (even), `11 % 2` = 1 (odd)
                    """)
                elif operator == "**":
                    st.warning(f"""
                    💡 **Exponent (**)** means "to the power of"
                    - `{num1} ** {num2}` = {num1} × {num1} × ... ({num2} times)
                    - Example: `2 ** 3` = 2 × 2 × 2 = 8
                    """)
                
            except ZeroDivisionError:
                st.error("❌ Cannot divide by zero!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
        
        # Order of operations
        st.markdown("---")
        st.markdown("#### 📏 Order of Operations (PEMDAS)")
        
        col_order1, col_order2 = st.columns(2)
        
        with col_order1:
            st.info("""
            **Python follows math rules:**
            1. **P**arentheses `()`
            2. **E**xponents `**`
            3. **M**ultiplication/Division `*`, `/`, `//`, `%`
            4. **A**ddition/Subtraction `+`, `-`
            
            **From left to right** if same level!
            """)
        
        with col_order2:
            st.code("""
# Without parentheses
5 + 3 * 2      # = 11 (not 16!)
# 3 * 2 first = 6
# 5 + 6 = 11

# With parentheses
(5 + 3) * 2    # = 16
# (5 + 3) first = 8
# 8 * 2 = 16
""", language="python")
    
    # ============================================
    # TAB 2: COMPARISON OPERATORS
    # ============================================
    with op_tabs[1]:
        st.markdown("### ⚖️ Comparison Operators")
        st.write("Compare values and get True or False!")
        
        # Show all comparison operators
        st.markdown("""
        | Operator | Meaning | Example | Result |
        |----------|---------|---------|--------|
        | `==` | Equal to | `5 == 5` | `True` |
        | `!=` | Not equal to | `5 != 3` | `True` |
        | `>` | Greater than | `5 > 3` | `True` |
        | `<` | Less than | `5 < 3` | `False` |
        | `>=` | Greater than or equal | `5 >= 5` | `True` |
        | `<=` | Less than or equal | `3 <= 5` | `True` |
        """)
        
        st.warning("⚠️ **Common Mistake:** Don't confuse `=` (assignment) with `==` (comparison)!")
        
        st.markdown("---")
        st.markdown("#### 🎮 Try Comparison Operations!")
        
        col_c1, col_c2, col_c3, col_c4 = st.columns([2, 1, 2, 2])
        
        with col_c1:
            comp_val1 = st.text_input("First value", value="10", key="comp_val1")
        
        with col_c2:
            comp_op = st.selectbox("Operator", ["==", "!=", ">", "<", ">=", "<="], key="comp_op")
        
        with col_c3:
            comp_val2 = st.text_input("Second value", value="5", key="comp_val2")
        
        with col_c4:
            st.write("")  # spacing
            comp_btn = st.button("⚖️ Compare", use_container_width=True)
        
        if comp_btn or (comp_val1 and comp_val2):
            try:
                # Try to convert to numbers if possible
                try:
                    v1 = float(comp_val1)
                    v2 = float(comp_val2)
                    val_type = "numbers"
                except:
                    v1 = comp_val1
                    v2 = comp_val2
                    val_type = "strings"
                
                # Perform comparison
                if comp_op == "==":
                    result = v1 == v2
                    explanation = f"Is {v1} equal to {v2}?"
                elif comp_op == "!=":
                    result = v1 != v2
                    explanation = f"Is {v1} NOT equal to {v2}?"
                elif comp_op == ">":
                    result = v1 > v2
                    explanation = f"Is {v1} greater than {v2}?"
                elif comp_op == "<":
                    result = v1 < v2
                    explanation = f"Is {v1} less than {v2}?"
                elif comp_op == ">=":
                    result = v1 >= v2
                    explanation = f"Is {v1} greater than or equal to {v2}?"
                elif comp_op == "<=":
                    result = v1 <= v2
                    explanation = f"Is {v1} less than or equal to {v2}?"
                
                # Display result
                col_cres1, col_cres2 = st.columns([1, 2])
                
                with col_cres1:
                    st.markdown("### Result:")
                    if result:
                        st.markdown(f"## :green[True] ✅")
                    else:
                        st.markdown(f"## :red[False] ❌")
                
                with col_cres2:
                    st.info(f"""
                    **Question:** {explanation}
                    
                    **Answer:** {result}
                    
                    **Python Code:**
                    ```python
                    result = {comp_val1} {comp_op} {comp_val2}
                    print(result)  # {result}
                    ```
                    
                    **Type:** Comparing {val_type}
                    """)
                
                # Show usage example
                st.success(f"""
                **💡 Use in code:**
                ```python
                if {comp_val1} {comp_op} {comp_val2}:
                    print("Condition is True!")
                else:
                    print("Condition is False!")
                ```
                """)
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
        
        # String comparison
        st.markdown("---")
        st.markdown("#### 📝 Comparing Strings")
        
        col_str1, col_str2 = st.columns(2)
        
        with col_str1:
            st.info("""
            **Strings compare alphabetically:**
            - `"apple" < "banana"` → `True`
            - `"cat" > "car"` → `True`
            - `"A" < "a"` → `True` (uppercase first)
            """)
        
        with col_str2:
            st.warning("""
            **Watch out for numbers as strings:**
            - `"10" < "5"` → `True` (text comparison!)
            - `10 < 5` → `False` (number comparison)
            - Convert first: `int("10") < int("5")`
            """)
    
    # ============================================
    # TAB 3: LOGICAL OPERATORS
    # ============================================
    with op_tabs[2]:
        st.markdown("### 🔀 Logical Operators")
        st.write("Combine conditions to make complex decisions!")
        
        # Show all logical operators
        st.markdown("""
        | Operator | Meaning | Example | Result |
        |----------|---------|---------|--------|
        | `and` | Both must be True | `True and True` | `True` |
        | `or` | At least one must be True | `True or False` | `True` |
        | `not` | Flip the value | `not True` | `False` |
        """)
        
        st.markdown("---")
        st.markdown("#### 🎮 AND Operator")
        st.write("Both conditions must be True")
        
        col_and1, col_and2, col_and3 = st.columns(3)
        
        with col_and1:
            and_val1 = st.selectbox("First value", [True, False], key="and_val1")
        
        with col_and2:
            st.markdown("### and")
        
        with col_and3:
            and_val2 = st.selectbox("Second value", [True, False], key="and_val2")
        
        and_result = and_val1 and and_val2
        
        col_and_res1, col_and_res2 = st.columns([1, 2])
        
        with col_and_res1:
            st.markdown("### Result:")
            if and_result:
                st.markdown(f"## :green[{and_result}] ✅")
            else:
                st.markdown(f"## :red[{and_result}] ❌")
        
        with col_and_res2:
            st.info(f"""
            **Truth Table for AND:**
            - `True and True` = `True` ✅
            - `True and False` = `False` ❌
            - `False and True` = `False` ❌
            - `False and False` = `False` ❌
            
            **Only True if BOTH are True!**
            """)
        
        st.code(f"""
# Example: Can you go to the party?
age = 16
has_permission = {and_val1}
can_go = age >= 13 and has_permission
print(can_go)  # {and_val1 and True}
""", language="python")
        
        st.markdown("---")
        st.markdown("#### 🎮 OR Operator")
        st.write("At least one condition must be True")
        
        col_or1, col_or2, col_or3 = st.columns(3)
        
        with col_or1:
            or_val1 = st.selectbox("First value", [True, False], key="or_val1")
        
        with col_or2:
            st.markdown("### or")
        
        with col_or3:
            or_val2 = st.selectbox("Second value", [True, False], key="or_val2")
        
        or_result = or_val1 or or_val2
        
        col_or_res1, col_or_res2 = st.columns([1, 2])
        
        with col_or_res1:
            st.markdown("### Result:")
            if or_result:
                st.markdown(f"## :green[{or_result}] ✅")
            else:
                st.markdown(f"## :red[{or_result}] ❌")
        
        with col_or_res2:
            st.info(f"""
            **Truth Table for OR:**
            - `True or True` = `True` ✅
            - `True or False` = `True` ✅
            - `False or True` = `True` ✅
            - `False or False` = `False` ❌
            
            **True if AT LEAST ONE is True!**
            """)
        
        st.code(f"""
# Example: Do you need an umbrella?
is_raining = {or_val1}
is_snowing = {or_val2}
need_umbrella = is_raining or is_snowing
print(need_umbrella)  # {or_result}
""", language="python")
        
        st.markdown("---")
        st.markdown("#### 🎮 NOT Operator")
        st.write("Flips True to False and False to True")
        
        col_not1, col_not2 = st.columns(2)
        
        with col_not1:
            not_val = st.selectbox("Value", [True, False], key="not_val")
        
        with col_not2:
            not_result = not not_val
            st.markdown("### Result:")
            if not_result:
                st.markdown(f"## :green[not {not_val} = {not_result}] ✅")
            else:
                st.markdown(f"## :red[not {not_val} = {not_result}] ❌")
        
        st.info("""
        **NOT simply flips the value:**
        - `not True` = `False`
        - `not False` = `True`
        """)
        
        st.code(f"""
# Example: Is the door closed?
is_open = {not_val}
is_closed = not is_open
print(is_closed)  # {not not_val}
""", language="python")
        
        # Combined example
        st.markdown("---")
        st.markdown("#### 🎯 Combining Logical Operators")
        
        st.code("""
# Can you ride the roller coaster?
age = 14
height = 150  # cm
has_ticket = True

can_ride = (age >= 12 and height >= 140) and has_ticket
# First check age AND height
# Then check if you have a ticket
# All must be True!

print(can_ride)  # True
""", language="python")
        
        st.warning("""
        **💡 Short-Circuit Evaluation:**
        - `and`: If first is False, don't check second (already False!)
        - `or`: If first is True, don't check second (already True!)
        
        This makes Python faster!
        """)
    
    # ============================================
    # TAB 4: ASSIGNMENT OPERATORS
    # ============================================
    with op_tabs[3]:
        st.markdown("### 🎯 Assignment Operators")
        st.write("Store values in variables and update them efficiently!")
        
        # Show all assignment operators
        st.markdown("""
        | Operator | Meaning | Example | Equivalent To |
        |----------|---------|---------|---------------|
        | `=` | Assign | `x = 5` | `x = 5` |
        | `+=` | Add and assign | `x += 3` | `x = x + 3` |
        | `-=` | Subtract and assign | `x -= 3` | `x = x - 3` |
        | `*=` | Multiply and assign | `x *= 3` | `x = x * 3` |
        | `/=` | Divide and assign | `x /= 3` | `x = x / 3` |
        | `//=` | Floor divide and assign | `x //= 3` | `x = x // 3` |
        | `%=` | Modulus and assign | `x %=  3` | `x = x % 3` |
        | `**=` | Power and assign | `x **= 3` | `x = x ** 3` |
        """)
        
        st.markdown("---")
        st.markdown("#### 🎮 Try Assignment Operators!")
        
        # Initialize session state
        if 'assign_var' not in st.session_state:
            st.session_state.assign_var = 10
        
        col_assign1, col_assign2 = st.columns(2)
        
        with col_assign1:
            st.markdown(f"### Current Value: :green[{st.session_state.assign_var}]")
        
        with col_assign2:
            reset_btn = st.button("🔄 Reset to 10")
            if reset_btn:
                st.session_state.assign_var = 10
                st.rerun()
        
        st.markdown("---")
        
        col_op1, col_op2, col_op3 = st.columns([1, 1, 1])
        
        with col_op1:
            assign_op = st.selectbox("Choose operator", ["=", "+=", "-=", "*=", "/=", "//=", "%=", "**="], key="assign_op")
        
        with col_op2:
            assign_val = st.number_input("Value", value=3, key="assign_val")
        
        with col_op3:
            st.write("")  # spacing
            apply_btn = st.button("✅ Apply", use_container_width=True)
        
        if apply_btn:
            old_value = st.session_state.assign_var
            
            try:
                if assign_op == "=":
                    st.session_state.assign_var = assign_val
                    explanation = f"Set x to {assign_val}"
                elif assign_op == "+=":
                    st.session_state.assign_var += assign_val
                    explanation = f"Add {assign_val} to x"
                elif assign_op == "-=":
                    st.session_state.assign_var -= assign_val
                    explanation = f"Subtract {assign_val} from x"
                elif assign_op == "*=":
                    st.session_state.assign_var *= assign_val
                    explanation = f"Multiply x by {assign_val}"
                elif assign_op == "/=":
                    st.session_state.assign_var /= assign_val
                    explanation = f"Divide x by {assign_val}"
                elif assign_op == "//=":
                    st.session_state.assign_var //= assign_val
                    explanation = f"Floor divide x by {assign_val}"
                elif assign_op == "%=":
                    st.session_state.assign_var %= assign_val
                    explanation = f"x modulus {assign_val}"
                elif assign_op == "**=":
                    st.session_state.assign_var **= assign_val
                    explanation = f"Raise x to power {assign_val}"
                
                st.success(f"""
                ✅ **Operation:** {explanation}
                
                **Before:** x = {old_value}
                
                **Code:** `x {assign_op} {assign_val}`
                
                **After:** x = {st.session_state.assign_var}
                """)
                
                st.rerun()
                
            except ZeroDivisionError:
                st.error("❌ Cannot divide by zero!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
        
        # Show examples
        st.markdown("---")
        st.markdown("#### 📝 Why Use Compound Operators?")
        
        col_why1, col_why2 = st.columns(2)
        
        with col_why1:
            st.info("""
            **Shorter & Cleaner:**
            ```python
            # Long way
            score = score + 10
            health = health - 5
            points = points * 2
            
            # Short way (same result!)
            score += 10
            health -= 5
            points *= 2
            ```
            """)
        
        with col_why2:
            st.success("""
            **Common Use Cases:**
            ```python
            # Counting
            count = 0
            count += 1  # Increment by 1
            
            # Accumulating
            total = 0
            total += price  # Add to total
            
            # Game stats
            lives -= 1  # Lose a life
            score *= 2  # Double points!
            ```
            """)
    
    # Final tips
    st.markdown("---")
    st.markdown("### 🎯 Key Takeaways")
    
    col_key1, col_key2 = st.columns(2)
    
    with col_key1:
        st.info("""
        **Operator Types:**
        1. **Arithmetic** - Math operations
        2. **Comparison** - True/False comparisons
        3. **Logical** - Combine conditions
        4. **Assignment** - Store and update values
        """)
    
    with col_key2:
        st.success("""
        **Remember:**
        - `=` assigns, `==` compares
        - Use `()` to control order
        - `and` needs both True
        - `or` needs one True
        - `not` flips True/False
        """)
    
    # Practice
    with st.expander("💪 Practice Exercises", expanded=False):
        st.markdown("""
        **Try these in Python:**
        
        1. **Arithmetic:**
        ```python
        # Calculate area of a rectangle
        length = 10
        width = 5
        area = length * width
        print(area)
        ```
        
        2. **Comparison:**
        ```python
        # Check voting age
        age = 16
        can_vote = age >= 18
        print(can_vote)  # False
        ```
        
        3. **Logical:**
        ```python
        # Check if number is in range
        num = 15
        in_range = num >= 10 and num <= 20
        print(in_range)  # True
        ```
        
        4. **Assignment:**
        ```python
        # Game score
        score = 0
        score += 10  # Found coin
        score += 50  # Completed level
        score *= 2   # Bonus multiplier
        print(score)  # 120
        ```
        """)

