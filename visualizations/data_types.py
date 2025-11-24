import streamlit as st

def show():
    st.markdown('<h2 style="color: #2196F3;">🎨 Python Data Types Explorer</h2>', unsafe_allow_html=True)
    st.write("Discover different types of data in Python and how to use them!")
    
    # Overview section
    with st.expander("📚 What are Data Types?", expanded=False):
        st.markdown("""
        **Data types** tell Python what kind of information you're storing.
        
        Think of data types like **containers**:
        - 📦 Different containers for different things
        - 🥤 You wouldn't put milk in a paper bag!
        - 🎒 Each container has special features
        
        **Why does it matter?**
        - Different operations work with different types
        - `"3" + "5"` gives `"35"` (text joining)
        - `3 + 5` gives `8` (math addition)
        - Same `+` symbol, different behavior!
        """)
    
    # Main data types overview
    st.markdown("### 🎯 Main Data Types in Python")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🔢 Numbers")
        st.info("""
        **int** (Integer)
        - Whole numbers
        - Examples: 5, -10, 1000
        
        **float** (Decimal)
        - Numbers with decimals
        - Examples: 3.14, -0.5, 2.0
        """)
    
    with col2:
        st.markdown("#### 📝 Text")
        st.success("""
        **str** (String)
        - Text/words
        - Use quotes: " " or ' '
        - Examples: "Hello", 'Python', "123"
        """)
    
    with col3:
        st.markdown("#### ✅ Logic")
        st.warning("""
        **bool** (Boolean)
        - True or False only
        - Used for decisions
        - Examples: True, False
        
        **NoneType**
        - Represents "nothing"
        - Only value: None
        """)
    
    # Interactive type checker
    st.markdown("---")
    st.markdown("### 🔍 Type Checker - Try It Out!")
    
    col_input1, col_input2 = st.columns([2, 1])
    
    with col_input1:
        test_value = st.text_input("Enter any value (try: 42, 3.14, Hello, True)", 
                                   value="42", 
                                   key="type_test")
    
    with col_input2:
        st.write("")  # spacing
        check_btn = st.button("🔍 Check Type", use_container_width=True)
    
    if check_btn or test_value:
        st.markdown("#### 🎯 Analysis Results:")
        
        col_res1, col_res2, col_res3 = st.columns(3)
        
        # Determine the type
        python_type = None
        type_name = None
        type_color = None
        actual_value = None
        
        # Try to evaluate the value
        try:
            # Check for boolean first
            if test_value == "True":
                actual_value = True
                python_type = bool
                type_name = "bool (Boolean)"
                type_color = "orange"
            elif test_value == "False":
                actual_value = False
                python_type = bool
                type_name = "bool (Boolean)"
                type_color = "orange"
            elif test_value == "None":
                actual_value = None
                python_type = type(None)
                type_name = "NoneType"
                type_color = "gray"
            # Try as int
            elif test_value.lstrip('-').isdigit():
                actual_value = int(test_value)
                python_type = int
                type_name = "int (Integer)"
                type_color = "blue"
            # Try as float
            elif test_value.replace('.', '', 1).replace('-', '', 1).isdigit():
                actual_value = float(test_value)
                python_type = float
                type_name = "float (Decimal)"
                type_color = "green"
            else:
                # It's a string
                actual_value = test_value
                python_type = str
                type_name = "str (String)"
                type_color = "purple"
        except:
            actual_value = test_value
            python_type = str
            type_name = "str (String)"
            type_color = "purple"
        
        with col_res1:
            st.markdown(f"**Your Input:**")
            st.code(f"{test_value}")
        
        with col_res2:
            st.markdown(f"**Python Type:**")
            if type_color == "blue":
                st.markdown(f":{type_color}[{type_name}]")
            elif type_color == "green":
                st.markdown(f":{type_color}[{type_name}]")
            elif type_color == "purple":
                st.markdown(f":{type_color}[{type_name}]")
            elif type_color == "orange":
                st.markdown(f":{type_color}[{type_name}]")
            else:
                st.markdown(f"{type_name}")
        
        with col_res3:
            st.markdown(f"**Python Code:**")
            st.code(f"type({test_value})")
        
        # Show what you can do with this type
        st.markdown("#### 🎮 What Can You Do With This Type?")
        
        if python_type == int or python_type == float:
            st.success(f"""
            **✅ Math Operations:**
            - Addition: `{actual_value} + 5` = {actual_value + 5}
            - Multiplication: `{actual_value} * 2` = {actual_value * 2}
            - Division: `{actual_value} / 2` = {actual_value / 2}
            - Power: `{actual_value} ** 2` = {actual_value ** 2}
            """)
        elif python_type == str:
            st.success(f"""
            **✅ String Operations:**
            - Length: `len("{actual_value}")` = {len(actual_value)}
            - Uppercase: `"{actual_value}".upper()` = "{actual_value.upper()}"
            - Repeat: `"{actual_value}" * 3` = "{actual_value * 3}"
            - Join: `"{actual_value}" + " World"` = "{actual_value} World"
            """)
        elif python_type == bool:
            st.success(f"""
            **✅ Boolean Operations:**
            - NOT: `not {actual_value}` = {not actual_value}
            - AND: `{actual_value} and True` = {actual_value and True}
            - OR: `{actual_value} or False` = {actual_value or False}
            - Used in: if statements, while loops
            """)
        elif actual_value is None:
            st.success("""
            **✅ None Usage:**
            - Represents "no value" or "empty"
            - Often used as default value
            - Check with: `if value is None:`
            """)
    
    # Type conversion section
    st.markdown("---")
    st.markdown("### 🔄 Type Conversion (Casting)")
    st.write("You can convert between types using special functions!")
    
    col_conv1, col_conv2, col_conv3 = st.columns(3)
    
    with col_conv1:
        st.markdown("#### 🔢 Convert to Integer")
        st.code("""
# String to int
int("42")      # → 42
int("3.7")     # → Error!
int(3.7)       # → 3

# Float to int (cuts decimal)
int(9.9)       # → 9
int(-2.5)      # → -2
""", language="python")
    
    with col_conv2:
        st.markdown("#### 📝 Convert to String")
        st.code("""
# Number to string
str(42)        # → "42"
str(3.14)      # → "3.14"
str(True)      # → "True"

# Everything can be string!
str(None)      # → "None"
""", language="python")
    
    with col_conv3:
        st.markdown("#### 🔢 Convert to Float")
        st.code("""
# String to float
float("3.14")  # → 3.14
float("42")    # → 42.0

# Int to float
float(5)       # → 5.0
float(-10)     # → -10.0
""", language="python")
    
    # Interactive conversion
    st.markdown("#### 🎯 Try Type Conversion")
    
    col_try1, col_try2, col_try3 = st.columns([2, 1, 2])
    
    with col_try1:
        conv_value = st.text_input("Enter a value to convert", value="42", key="conv_input")
    
    with col_try2:
        conv_type = st.selectbox("Convert to:", ["int", "float", "str"], key="conv_type")
    
    with col_try3:
        st.write("")  # spacing
        convert_btn = st.button("🔄 Convert", use_container_width=True)
    
    if convert_btn or (conv_value and conv_type):
        try:
            if conv_type == "int":
                result = int(float(conv_value))  # float first to handle "3.7"
                st.success(f"✅ Result: `{result}` (type: {type(result).__name__})")
                st.code(f"int({conv_value}) = {result}", language="python")
            elif conv_type == "float":
                result = float(conv_value)
                st.success(f"✅ Result: `{result}` (type: {type(result).__name__})")
                st.code(f"float({conv_value}) = {result}", language="python")
            elif conv_type == "str":
                result = str(conv_value)
                st.success(f"✅ Result: `\"{result}\"` (type: {type(result).__name__})")
                st.code(f"str({conv_value}) = \"{result}\"", language="python")
        except Exception as e:
            st.error(f"❌ Cannot convert '{conv_value}' to {conv_type}")
            st.caption(f"Error: {str(e)}")
    
    # Common mistakes section
    st.markdown("---")
    st.markdown("### ⚠️ Common Mistakes & Type Errors")
    
    col_err1, col_err2 = st.columns(2)
    
    with col_err1:
        st.markdown("#### ❌ Mixing Types (Wrong)")
        st.code("""
# Can't add string and number
"3" + 5        # ❌ Error!

# Can't multiply string by string
"Hi" * "3"     # ❌ Error!

# Can't compare different types
"10" > 5       # ❌ Unexpected!
""", language="python")
    
    with col_err2:
        st.markdown("#### ✅ Correct Way")
        st.code("""
# Convert first!
int("3") + 5          # ✅ = 8
"3" + str(5)          # ✅ = "35"

# Convert to number
"Hi" * 3              # ✅ = "HiHiHi"

# Convert to same type
int("10") > 5         # ✅ = True
"10" > "5"            # ✅ = False (text!)
""", language="python")
    
    # Key concepts
    st.markdown("---")
    st.markdown("### 🎯 Key Takeaways")
    
    col_key1, col_key2 = st.columns(2)
    
    with col_key1:
        st.info("""
        **Remember:**
        1. Every value has a type
        2. Type determines what you can do
        3. Use `type(value)` to check type
        4. Convert with `int()`, `float()`, `str()`
        5. Strings need quotes, numbers don't
        """)
    
    with col_key2:
        st.success("""
        **Quick Reference:**
        - `42` → int (whole number)
        - `3.14` → float (decimal)
        - `"Hello"` → str (text, needs quotes)
        - `True/False` → bool (logic)
        - `None` → NoneType (nothing/empty)
        """)
    
    # Practice suggestions
    st.markdown("---")
    with st.expander("💪 Practice Exercises", expanded=False):
        st.markdown("""
        **Try these in Python:**
        
        1. **Type Checking:**
        ```python
        print(type(42))
        print(type("42"))
        print(type(4.2))
        print(type(True))
        ```
        
        2. **Type Conversion:**
        ```python
        age = "15"
        next_year = int(age) + 1
        print("Next year I'll be", next_year)
        ```
        
        3. **Common Error - Fix It:**
        ```python
        # This has an error - fix it!
        num = "10"
        result = num + 5
        print(result)
        ```
        
        4. **String or Number?**
        ```python
        a = "5" + "3"    # What is a?
        b = 5 + 3        # What is b?
        c = "5" * 3      # What is c?
        d = 5 * 3        # What is d?
        ```
        """)

