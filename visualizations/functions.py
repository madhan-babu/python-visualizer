import streamlit as st

def show():
    st.markdown('<h2 style="color: #2196F3;">🔧 Python Functions Explorer</h2>', unsafe_allow_html=True)
    st.write("Learn how to create and use functions - reusable blocks of code!")
    
    # Overview
    with st.expander("📚 What is a Function?", expanded=False):
        st.markdown("""
        **A function** is a reusable block of code that performs a specific task.
        
        Think of functions like:
        - 🔧 A tool in your toolbox - use it whenever you need it
        - 📦 A vending machine - put something in (input), get something out (output)
        - 🎮 A game power-up - predefined action you can trigger
        - 🍳 A recipe - follow the steps to get the result
        
        **Why use functions?**
        - **Reusability**: Write once, use many times
        - **Organization**: Break big problems into smaller pieces
        - **Readability**: Give descriptive names to actions
        - **Maintainability**: Fix bugs in one place
        - **DRY Principle**: Don't Repeat Yourself!
        
        **Function Anatomy:**
        ```python
        def function_name(parameters):
            # Function body
            # Do something
            return result
        ```
        """)
    
    # Create tabs for different function concepts
    func_tabs = st.tabs(["📝 Define Functions", "📞 Call Functions", "🎁 Return Values", "⚙️ Parameters", "🎯 Examples"])
    
    # ============================================
    # TAB 1: DEFINE FUNCTIONS
    # ============================================
    with func_tabs[0]:
        st.markdown("### 📝 Defining Functions")
        st.write("Learn how to create your own functions")
        
        st.info("""
        **Basic function syntax:**
        ```python
        def function_name():
            # Code here
            print("Hello!")
        ```
        
        **Parts of a function:**
        1. `def` - keyword to define a function
        2. `function_name` - what you call it (use descriptive names!)
        3. `()` - parentheses for parameters (empty if none)
        4. `:` - colon to start the function body
        5. Indented code - the function body (what it does)
        """)
        
        st.markdown("---")
        st.markdown("#### 🎮 Create Your Own Function")
        
        col_def1, col_def2 = st.columns(2)
        
        with col_def1:
            func_name = st.text_input("Function name:", value="greet", key="func_name_def")
        
        with col_def2:
            func_action = st.selectbox("What should it do?", 
                                      ["Print a message", "Calculate sum", "Check even/odd"],
                                      key="func_action")
        
        # Generate function based on selection
        if func_action == "Print a message":
            message = st.text_input("Message to print:", value="Hello, World!", key="func_message")
            
            st.markdown("#### 📄 Your Function:")
            function_code = f"""def {func_name}():
    print("{message}")"""
            st.code(function_code, language="python")
            
            if st.button("▶️ Test Function", key="test_simple_func"):
                st.success(f"✅ Calling `{func_name}()`...")
                st.info(f"Output: {message}")
                st.code(f"{func_name}()  # Call the function\n# Output: {message}", language="python")
        
        elif func_action == "Calculate sum":
            st.markdown("#### 📄 Your Function:")
            function_code = f"""def {func_name}(a, b):
    result = a + b
    return result"""
            st.code(function_code, language="python")
            
            col_test1, col_test2 = st.columns(2)
            with col_test1:
                test_a = st.number_input("First number:", value=5, key="sum_a")
            with col_test2:
                test_b = st.number_input("Second number:", value=3, key="sum_b")
            
            if st.button("▶️ Test Function", key="test_sum_func"):
                result = test_a + test_b
                st.success(f"✅ Calling `{func_name}({test_a}, {test_b})`...")
                st.info(f"Result: {result}")
                st.code(f"result = {func_name}({test_a}, {test_b})\nprint(result)  # {result}", language="python")
        
        elif func_action == "Check even/odd":
            st.markdown("#### 📄 Your Function:")
            function_code = f"""def {func_name}(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd" """
            st.code(function_code, language="python")
            
            test_num = st.number_input("Number to check:", value=7, key="check_num")
            
            if st.button("▶️ Test Function", key="test_even_func"):
                result = "Even" if test_num % 2 == 0 else "Odd"
                st.success(f"✅ Calling `{func_name}({int(test_num)})`...")
                st.info(f"Result: {result}")
                st.code(f"result = {func_name}({int(test_num)})\nprint(result)  # {result}", language="python")
        
        st.markdown("---")
        st.markdown("#### 🎨 Function Naming Rules")
        
        col_naming1, col_naming2 = st.columns(2)
        
        with col_naming1:
            st.success("""
            **✅ Good Names:**
            - `calculate_average()`
            - `get_user_input()`
            - `is_valid()`
            - `convert_to_celsius()`
            - Use descriptive names!
            - Use snake_case
            """)
        
        with col_naming2:
            st.error("""
            **❌ Bad Names:**
            - `func()` - too vague
            - `x()` - not descriptive
            - `doStuff()` - camelCase (not Python style)
            - `my-function()` - hyphens not allowed
            - Reserved words like `print()`, `list()`
            """)
    
    # ============================================
    # TAB 2: CALL FUNCTIONS
    # ============================================
    with func_tabs[1]:
        st.markdown("### 📞 Calling Functions")
        st.write("How to use functions after defining them")
        
        st.info("""
        **Defining vs Calling:**
        
        **Define** (create the function):
        ```python
        def greet():
            print("Hello!")
        ```
        
        **Call** (use the function):
        ```python
        greet()  # Actually runs the code
        ```
        
        **Key Point:** Defining a function doesn't run it! You must call it.
        """)
        
        st.markdown("---")
        st.markdown("#### 🎯 Interactive Function Calls")
        
        # Example functions to call
        example_func = st.radio("Choose a function to call:", 
                               ["say_hello()", "square(n)", "repeat_text(text, times)"],
                               key="example_func_call")
        
        if example_func == "say_hello()":
            st.code("""def say_hello():
    return "Hello from the function!"
    
# Call it:
message = say_hello()
print(message)""", language="python")
            
            if st.button("📞 Call say_hello()", key="call_hello"):
                st.success("✅ Function called!")
                st.info("Output: Hello from the function!")
                
                col_flow1, col_flow2, col_flow3 = st.columns(3)
                with col_flow1:
                    st.markdown("**1. Define** ✏️")
                    st.caption("Create the function")
                with col_flow2:
                    st.markdown("**2. Call** 📞")
                    st.caption("say_hello()")
                with col_flow3:
                    st.markdown("**3. Execute** ⚡")
                    st.caption("Code runs!")
        
        elif example_func == "square(n)":
            st.code("""def square(n):
    return n * n
    
# Call it with different values:
result = square(5)
print(result)  # 25""", language="python")
            
            call_input = st.number_input("Enter a number to square:", value=5, key="square_input")
            
            if st.button(f"📞 Call square({int(call_input)})", key="call_square"):
                result = int(call_input) ** 2
                st.success(f"✅ Function called with argument: {int(call_input)}")
                st.info(f"Output: {result}")
                
                # Show execution flow
                st.markdown("**Execution Flow:**")
                st.code(f"""1. Call: square({int(call_input)})
2. Parameter n receives value {int(call_input)}
3. Calculate: {int(call_input)} * {int(call_input)} = {result}
4. Return: {result}""", language="python")
        
        elif example_func == "repeat_text(text, times)":
            st.code("""def repeat_text(text, times):
    return text * times
    
# Call it:
result = repeat_text("Hi! ", 3)
print(result)  # Hi! Hi! Hi! """, language="python")
            
            col_rep1, col_rep2 = st.columns(2)
            with col_rep1:
                text_input = st.text_input("Text:", value="Hi! ", key="repeat_text")
            with col_rep2:
                times_input = st.number_input("Times:", value=3, min_value=1, max_value=10, key="repeat_times")
            
            if st.button(f'📞 Call repeat_text("{text_input}", {int(times_input)})', key="call_repeat"):
                result = text_input * int(times_input)
                st.success(f"✅ Function called!")
                st.info(f"Output: {result}")
        
        st.markdown("---")
        st.markdown("#### 🔁 Multiple Calls")
        
        st.warning("""
        **Functions can be called multiple times!**
        
        ```python
        def add_five(n):
            return n + 5
        
        result1 = add_five(10)  # 15
        result2 = add_five(20)  # 25
        result3 = add_five(7)   # 12
        ```
        
        Same function, different inputs → different outputs!
        """)
    
    # ============================================
    # TAB 3: RETURN VALUES
    # ============================================
    with func_tabs[2]:
        st.markdown("### 🎁 Return Values")
        st.write("Get results back from your functions")
        
        st.info("""
        **`return` statement:**
        - Sends a value back to the caller
        - Exits the function immediately
        - Without `return`, function returns `None`
        
        ```python
        def add(a, b):
            return a + b  # Send result back
        
        result = add(3, 5)  # result = 8
        ```
        """)
        
        st.markdown("---")
        st.markdown("#### 🆚 With vs Without Return")
        
        col_ret1, col_ret2 = st.columns(2)
        
        with col_ret1:
            st.markdown("**❌ Without `return`**")
            st.code("""def greet(name):
    message = f"Hello, {name}!"
    print(message)
    # No return!

result = greet("Alice")
print(result)  # None""", language="python")
            
            st.caption("Function does something but doesn't give back a value")
        
        with col_ret2:
            st.markdown("**✅ With `return`**")
            st.code("""def greet(name):
    message = f"Hello, {name}!"
    return message

result = greet("Alice")
print(result)  # "Hello, Alice!" """, language="python")
            
            st.caption("Function gives back a value you can use")
        
        st.markdown("---")
        st.markdown("#### 🎮 Try It: Return Values")
        
        return_demo = st.selectbox("Choose function type:", 
                                   ["Print only (no return)", "Return value"],
                                   key="return_demo")
        
        name_input = st.text_input("Enter a name:", value="Alice", key="return_name")
        
        if return_demo == "Print only (no return)":
            st.code(f"""def greet(name):
    print(f"Hello, {{name}}!")
    # No return statement

greet("{name_input}")""", language="python")
            
            if st.button("▶️ Run", key="run_no_return"):
                st.markdown("**Output to console:**")
                st.info(f"Hello, {name_input}!")
                st.markdown("**Returned value:**")
                st.code("None", language="python")
                st.caption("⚠️ Can't save the greeting to use later!")
        
        else:
            st.code(f"""def greet(name):
    return f"Hello, {{name}}!"

result = greet("{name_input}")
print(result)
print(result.upper())  # Can use the result!""", language="python")
            
            if st.button("▶️ Run", key="run_with_return"):
                result = f"Hello, {name_input}!"
                st.markdown("**Returned value:**")
                st.code(f'"{result}"', language="python")
                st.markdown("**Can use it multiple ways:**")
                st.success(f"Original: {result}")
                st.success(f"Uppercase: {result.upper()}")
                st.success(f"Length: {len(result)} characters")
        
        st.markdown("---")
        st.markdown("#### 🔢 Returning Multiple Values")
        
        st.info("""
        **Return multiple values using a tuple:**
        ```python
        def get_name_and_age():
            name = "Alice"
            age = 12
            return name, age  # Returns two values
        
        person_name, person_age = get_name_and_age()
        print(person_name)  # Alice
        print(person_age)   # 12
        ```
        """)
        
        st.markdown("**Example: Calculate Rectangle Dimensions**")
        st.code("""def rectangle_info(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

# Use it:
a, p = rectangle_info(5, 3)
print(f"Area: {a}, Perimeter: {p}")""", language="python")
        
        col_rect1, col_rect2 = st.columns(2)
        with col_rect1:
            rect_width = st.number_input("Width:", value=5, min_value=1, key="rect_width")
        with col_rect2:
            rect_height = st.number_input("Height:", value=3, min_value=1, key="rect_height")
        
        if st.button("📊 Calculate", key="calc_rect_btn"):
            area = rect_width * rect_height
            perimeter = 2 * (rect_width + rect_height)
            
            st.success("✅ Function returned 2 values!")
            
            col_result1, col_result2 = st.columns(2)
            with col_result1:
                st.metric("Area", area)
            with col_result2:
                st.metric("Perimeter", perimeter)
            
            st.code(f"""area, perimeter = rectangle_info({int(rect_width)}, {int(rect_height)})
# area = {int(area)}, perimeter = {int(perimeter)}""", language="python")
    
    # ============================================
    # TAB 4: PARAMETERS
    # ============================================
    with func_tabs[3]:
        st.markdown("### ⚙️ Parameters & Arguments")
        st.write("Pass information into your functions")
        
        st.info("""
        **Parameters vs Arguments:**
        
        **Parameters** = Variables in function definition
        ```python
        def greet(name):  # 'name' is a parameter
            return f"Hello, {name}!"
        ```
        
        **Arguments** = Actual values passed when calling
        ```python
        greet("Alice")  # "Alice" is an argument
        ```
        """)
        
        st.markdown("---")
        st.markdown("#### 📊 Types of Parameters")
        
        param_type = st.radio("Choose parameter type:", 
                             ["Required", "Default", "Multiple"],
                             horizontal=True,
                             key="param_type")
        
        if param_type == "Required":
            st.markdown("#### ✅ Required Parameters")
            st.info("""
            **Must be provided when calling the function**
            ```python
            def greet(name):
                return f"Hello, {name}!"
            
            greet("Alice")  # ✅ Works
            greet()         # ❌ Error: missing required argument
            ```
            """)
            
            st.code("""def calculate_area(length, width):
    return length * width""", language="python")
            
            col_req1, col_req2 = st.columns(2)
            with col_req1:
                length = st.number_input("Length:", value=5, key="area_length")
            with col_req2:
                width = st.number_input("Width:", value=3, key="area_width")
            
            if st.button("📐 Calculate Area", key="calc_area_btn"):
                area = length * width
                st.success(f"✅ Called: `calculate_area({length}, {width})`")
                st.info(f"Result: {area}")
                st.code(f"area = calculate_area({length}, {width})\nprint(area)  # {area}", language="python")
        
        elif param_type == "Default":
            st.markdown("#### 🎯 Default Parameters")
            st.info("""
            **Optional parameters with default values**
            ```python
            def greet(name="Guest"):  # Default value
                return f"Hello, {name}!"
            
            greet("Alice")  # Hello, Alice!
            greet()         # Hello, Guest! (uses default)
            ```
            """)
            
            st.code("""def power(base, exponent=2):  # exponent defaults to 2
    return base ** exponent""", language="python")
            
            col_pow1, col_pow2 = st.columns(2)
            with col_pow1:
                base = st.number_input("Base:", value=5, key="power_base")
            with col_pow2:
                use_default = st.checkbox("Use default exponent (2)", value=True, key="use_default_exp")
                if not use_default:
                    exponent = st.number_input("Exponent:", value=3, key="power_exp")
                else:
                    exponent = 2
            
            if st.button("🔢 Calculate Power", key="calc_power_btn"):
                result = base ** exponent
                if use_default:
                    st.success(f"✅ Called: `power({base})` - using default exponent")
                else:
                    st.success(f"✅ Called: `power({base}, {exponent})`")
                st.info(f"Result: {result}")
        
        elif param_type == "Multiple":
            st.markdown("#### 🔢 Multiple Parameters")
            st.info("""
            **Functions can have many parameters**
            ```python
            def introduce_student(name, age, grade, favorite_subject):
                message = f"Hi! I'm {name}, {age} years old."
                message += f" I'm in grade {grade}."
                message += f" My favorite subject is {favorite_subject}!"
                return message
            ```
            """)
            
            col_mult1, col_mult2, col_mult3, col_mult4 = st.columns(4)
            with col_mult1:
                student_name = st.text_input("Name:", value="Alice", key="student_name")
            with col_mult2:
                student_age = st.number_input("Age:", value=12, min_value=5, max_value=18, key="student_age")
            with col_mult3:
                student_grade = st.number_input("Grade:", value=7, min_value=1, max_value=12, key="student_grade")
            with col_mult4:
                student_subject = st.text_input("Favorite Subject:", value="Math", key="student_subject")
            
            if st.button("👤 Introduce Student", key="introduce_student_btn"):
                st.success(f"✅ Called: `introduce_student({repr(student_name)}, {int(student_age)}, {int(student_grade)}, {repr(student_subject)})`")
                
                intro_message = f"Hi! I'm {student_name}, {int(student_age)} years old. "
                intro_message += f"I'm in grade {int(student_grade)}. "
                intro_message += f"My favorite subject is {student_subject}!"
                
                st.info(intro_message)
                st.code(f"""def introduce_student(name, age, grade, subject):
    message = f"Hi! I'm {{name}}, {{age}} years old."
    message += f" I'm in grade {{grade}}."
    message += f" My favorite subject is {{subject}}!"
    return message

intro = introduce_student("{student_name}", {int(student_age)}, {int(student_grade)}, "{student_subject}")
print(intro)""", language="python")
        
        st.markdown("---")
        st.markdown("#### 🎨 Parameter Best Practices")
        
        col_bp1, col_bp2 = st.columns(2)
        
        with col_bp1:
            st.success("""
            **✅ Good:**
            - Use descriptive parameter names
            - Keep number of parameters reasonable (< 5)
            - Put required parameters first
            - Use defaults for optional parameters
            """)
        
        with col_bp2:
            st.error("""
            **❌ Avoid:**
            - Single-letter names (except in math)
            - Too many parameters (hard to remember)
            - Inconsistent order
            - Confusing default values
            """)
    
    # ============================================
    # TAB 5: EXAMPLES
    # ============================================
    with func_tabs[4]:
        st.markdown("### 🎯 Real-World Function Examples")
        
        example_category = st.selectbox("Choose category:", 
                                       ["Math Functions", "String Functions", "Validation Functions"],
                                       key="example_category")
        
        if example_category == "Math Functions":
            st.markdown("#### 🔢 Math Functions")
            
            math_func = st.radio("Choose function:", 
                                ["calculate_circle_area", "fahrenheit_to_celsius", "double_number"],
                                key="math_func_choice")
            
            if math_func == "calculate_circle_area":
                st.code("""def calculate_circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area

# Usage:
area = calculate_circle_area(5)
print(f"Area: {area}")""", language="python")
                
                radius = st.number_input("Radius:", value=5.0, min_value=0.1, key="circle_radius")
                if st.button("📐 Calculate", key="calc_circle_btn"):
                    area = 3.14159 * radius ** 2
                    st.success(f"Area of circle with radius {radius}: {area:.2f}")
            
            elif math_func == "fahrenheit_to_celsius":
                st.code("""def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Usage:
temp_c = fahrenheit_to_celsius(98.6)
print(f"{temp_c}°C")""", language="python")
                
                temp_f = st.number_input("Temperature (°F):", value=98.6, key="temp_f")
                if st.button("🌡️ Convert", key="convert_temp_btn"):
                    temp_c = (temp_f - 32) * 5/9
                    st.success(f"{temp_f}°F = {temp_c:.2f}°C")
            
            elif math_func == "double_number":
                st.code("""def double_number(num):
    # Multiply any number by 2
    result = num * 2
    return result

def triple_number(num):
    # Multiply any number by 3
    result = num * 3
    return result

# Usage:
x = 7
doubled = double_number(x)
tripled = triple_number(x)
print(f"{x} doubled is {doubled}")
print(f"{x} tripled is {tripled}")""", language="python")
                
                test_num = st.number_input("Enter a number:", value=7, key="double_num")
                if st.button("🔢 Calculate", key="calc_double_btn"):
                    doubled = test_num * 2
                    tripled = test_num * 3
                    
                    col_d1, col_d2 = st.columns(2)
                    with col_d1:
                        st.metric("Doubled", doubled)
                    with col_d2:
                        st.metric("Tripled", tripled)
                    
                    st.success(f"{test_num} × 2 = {doubled}")
                    st.success(f"{test_num} × 3 = {tripled}")
        
        elif example_category == "String Functions":
            st.markdown("#### 📝 String Functions")
            
            st.code("""def count_words(text):
    words = text.split()
    return len(words)

def reverse_string(text):
    return text[::-1]

def capitalize_words(text):
    return text.title()""", language="python")
            
            string_input = st.text_area("Enter text:", value="hello world from python", key="string_func_input")
            
            col_str1, col_str2, col_str3 = st.columns(3)
            
            with col_str1:
                if st.button("📊 Count Words", key="count_words_btn"):
                    count = len(string_input.split())
                    st.metric("Word Count", count)
            
            with col_str2:
                if st.button("🔄 Reverse", key="reverse_str_btn"):
                    reversed_text = string_input[::-1]
                    st.info(f"{reversed_text}")
            
            with col_str3:
                if st.button("🔤 Capitalize", key="cap_words_btn"):
                    capitalized = string_input.title()
                    st.info(f"{capitalized}")
        
        elif example_category == "Validation Functions":
            st.markdown("#### ✅ Validation Functions")
            
            st.code("""def is_valid_email(email):
    # Check if email has @ and .
    return "@" in email and "." in email

def is_long_enough(password):
    # Check if password is at least 8 characters
    return len(password) >= 8

def is_teenager(age):
    # Check if age is between 13 and 19
    return age >= 13 and age <= 19""", language="python")
            
            val_func = st.radio("Choose validator:", 
                              ["Email", "Password Length", "Teenager Check"],
                              horizontal=True,
                              key="val_func_choice")
            
            if val_func == "Email":
                email = st.text_input("Email:", value="user@example.com", key="email_val")
                if st.button("✅ Validate Email", key="val_email_btn"):
                    has_at = "@" in email
                    has_dot = "." in email
                    is_valid = has_at and has_dot
                    
                    st.info(f"Has @ symbol: {has_at}")
                    st.info(f"Has . symbol: {has_dot}")
                    
                    if is_valid:
                        st.success(f"✅ '{email}' looks like a valid email!")
                    else:
                        st.error(f"❌ '{email}' is missing @ or .")
            
            elif val_func == "Password Length":
                password = st.text_input("Password:", value="MyPass123", type="password", key="pass_val")
                if st.button("✅ Check Length", key="val_pass_btn"):
                    length = len(password)
                    is_long = length >= 8
                    
                    st.info(f"Password length: {length} characters")
                    
                    if is_long:
                        st.success(f"✅ Password is long enough (≥8 characters)")
                    else:
                        st.error(f"❌ Password too short! Need at least 8 characters")
                        st.caption(f"You need {8 - length} more character(s)")
            
            elif val_func == "Teenager Check":
                age = st.number_input("Age:", value=15, min_value=0, max_value=120, key="age_val")
                if st.button("✅ Check Age", key="val_age_btn"):
                    is_teenager = age >= 13 and age <= 19
                    
                    if is_teenager:
                        st.success(f"✅ Age {int(age)} is a teenager (13-19)")
                    else:
                        st.info(f"ℹ️ Age {int(age)} is not a teenager")
                        if age < 13:
                            st.caption("Too young to be a teenager")
                        else:
                            st.caption("Too old to be a teenager")
    
    # Key takeaways
    st.markdown("---")
    st.markdown("### 🎯 Key Takeaways")
    
    col_key1, col_key2 = st.columns(2)
    
    with col_key1:
        st.info("""
        **Function Essentials:**
        - Define with `def function_name():`
        - Call with `function_name()`
        - Use `return` to send values back
        - Parameters pass information in
        - Default parameters are optional
        """)
    
    with col_key2:
        st.success("""
        **Best Practices:**
        - Use descriptive names
        - Keep functions focused (one task)
        - Document with docstrings
        - Return values when needed
        - Test your functions!
        """)
    
    # Practice exercises
    with st.expander("💪 Practice Exercises", expanded=False):
        st.markdown("""
        **Try these fun challenges:**
        
        1. **Make a Greeter:**
        ```python
        def greet_person(name, age):
            # Create a greeting message
            return f"Hi {name}, you are {age} years old!"
        
        # Test it:
        print(greet_person("Emma", 10))
        ```
        
        2. **Calculate Pizza Cost:**
        ```python
        def pizza_cost(num_slices, price_per_slice=3):
            # Calculate total cost of pizza slices
            total = num_slices * price_per_slice
            return total
        
        # Test it:
        print(pizza_cost(4))      # Uses default $3 per slice
        print(pizza_cost(4, 2.5)) # Custom price $2.50 per slice
        ```
        
        3. **Check if Even or Odd:**
        ```python
        def is_even(number):
            # Return True if even, False if odd
            if number % 2 == 0:
                return True
            else:
                return False
        
        # Test it:
        print(is_even(10))  # True
        print(is_even(7))   # False
        ```
        
        4. **Make a Rectangle:**
        ```python
        def draw_rectangle(width, height, symbol="*"):
            # Print a rectangle pattern
            for i in range(height):
                print(symbol * width)
        
        # Test it:
        draw_rectangle(5, 3)
        # Output:
        # *****
        # *****
        # *****
        ```
        
        5. **Convert Minutes to Hours:**
        ```python
        def minutes_to_hours(minutes):
            # Convert minutes to hours and remaining minutes
            hours = minutes // 60
            remaining_minutes = minutes % 60
            return hours, remaining_minutes
        
        # Test it:
        h, m = minutes_to_hours(150)
        print(f"{h} hours and {m} minutes")  # 2 hours and 30 minutes
        ```
        """)

