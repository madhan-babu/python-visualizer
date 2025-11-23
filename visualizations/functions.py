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
        def get_stats(numbers):
            total = sum(numbers)
            average = total / len(numbers)
            return total, average  # Returns tuple
        
        t, avg = get_stats([10, 20, 30])
        print(t)    # 60
        print(avg)  # 20.0
        ```
        """)
        
        numbers_input = st.text_input("Enter numbers (comma-separated):", value="10, 20, 30, 40", key="multi_return_input")
        
        if st.button("📊 Calculate Stats", key="calc_stats_btn"):
            try:
                numbers = [float(x.strip()) for x in numbers_input.split(",")]
                total = sum(numbers)
                average = total / len(numbers)
                minimum = min(numbers)
                maximum = max(numbers)
                
                st.success("✅ Function returned 4 values!")
                
                col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
                with col_stat1:
                    st.metric("Total", total)
                with col_stat2:
                    st.metric("Average", round(average, 2))
                with col_stat3:
                    st.metric("Min", minimum)
                with col_stat4:
                    st.metric("Max", maximum)
                
                st.code(f"""def get_stats(numbers):
    return sum(numbers), sum(numbers)/len(numbers), min(numbers), max(numbers)

total, avg, min_val, max_val = get_stats({numbers})
# total = {total}, avg = {round(average, 2)}, min = {minimum}, max = {maximum}""", language="python")
            except:
                st.error("❌ Invalid input! Use numbers separated by commas.")
    
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
            def create_user(name, age, email, country):
                return {
                    "name": name,
                    "age": age,
                    "email": email,
                    "country": country
                }
            ```
            """)
            
            col_mult1, col_mult2, col_mult3, col_mult4 = st.columns(4)
            with col_mult1:
                user_name = st.text_input("Name:", value="Alice", key="user_name")
            with col_mult2:
                user_age = st.number_input("Age:", value=15, min_value=1, key="user_age")
            with col_mult3:
                user_email = st.text_input("Email:", value="alice@example.com", key="user_email")
            with col_mult4:
                user_country = st.text_input("Country:", value="USA", key="user_country")
            
            if st.button("👤 Create User", key="create_user_btn"):
                st.success(f"✅ Called: `create_user({repr(user_name)}, {int(user_age)}, {repr(user_email)}, {repr(user_country)})`")
                
                user_dict = {
                    "name": user_name,
                    "age": int(user_age),
                    "email": user_email,
                    "country": user_country
                }
                
                st.json(user_dict)
                st.code(f"user = create_user({repr(user_name)}, {int(user_age)}, {repr(user_email)}, {repr(user_country)})\nprint(user)", language="python")
        
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
                                       ["Math Functions", "String Functions", "List Functions", "Validation Functions"],
                                       key="example_category")
        
        if example_category == "Math Functions":
            st.markdown("#### 🔢 Math Functions")
            
            math_func = st.radio("Choose function:", 
                                ["calculate_circle_area", "fahrenheit_to_celsius", "is_prime"],
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
            
            elif math_func == "is_prime":
                st.code("""def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Usage:
print(is_prime(17))  # True
print(is_prime(20))  # False""", language="python")
                
                check_num = st.number_input("Number to check:", value=17, min_value=1, key="prime_num")
                if st.button("🔍 Check Prime", key="check_prime_btn"):
                    if check_num < 2:
                        is_prime_result = False
                    else:
                        is_prime_result = True
                        for i in range(2, int(check_num ** 0.5) + 1):
                            if check_num % i == 0:
                                is_prime_result = False
                                break
                    
                    if is_prime_result:
                        st.success(f"✅ {int(check_num)} is a prime number!")
                    else:
                        st.error(f"❌ {int(check_num)} is NOT a prime number")
        
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
        
        elif example_category == "List Functions":
            st.markdown("#### 📚 List Functions")
            
            st.code("""def find_max(numbers):
    return max(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def remove_duplicates(items):
    return list(set(items))""", language="python")
            
            list_input = st.text_input("Enter numbers (comma-separated):", value="5, 10, 15, 10, 20, 5", key="list_func_input")
            
            if st.button("📊 Analyze List", key="analyze_list_btn"):
                try:
                    numbers = [float(x.strip()) for x in list_input.split(",")]
                    
                    col_list1, col_list2, col_list3 = st.columns(3)
                    
                    with col_list1:
                        st.metric("Maximum", max(numbers))
                    with col_list2:
                        st.metric("Average", round(sum(numbers) / len(numbers), 2))
                    with col_list3:
                        unique = list(set(numbers))
                        st.metric("Unique Count", len(unique))
                    
                    st.code(f"Original: {numbers}\nUnique: {unique}", language="python")
                except:
                    st.error("Invalid input!")
        
        elif example_category == "Validation Functions":
            st.markdown("#### ✅ Validation Functions")
            
            st.code("""def is_valid_email(email):
    return "@" in email and "." in email

def is_strong_password(password):
    if len(password) < 8:
        return False
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    return has_digit and has_upper

def is_adult(age):
    return age >= 18""", language="python")
            
            val_func = st.radio("Choose validator:", 
                              ["Email", "Password", "Age"],
                              horizontal=True,
                              key="val_func_choice")
            
            if val_func == "Email":
                email = st.text_input("Email:", value="user@example.com", key="email_val")
                if st.button("✅ Validate Email", key="val_email_btn"):
                    is_valid = "@" in email and "." in email
                    if is_valid:
                        st.success(f"✅ '{email}' is a valid email format")
                    else:
                        st.error(f"❌ '{email}' is NOT a valid email format")
            
            elif val_func == "Password":
                password = st.text_input("Password:", value="MyPass123", type="password", key="pass_val")
                if st.button("✅ Validate Password", key="val_pass_btn"):
                    checks = {
                        "Length ≥ 8": len(password) >= 8,
                        "Has digit": any(char.isdigit() for char in password),
                        "Has uppercase": any(char.isupper() for char in password)
                    }
                    
                    all_valid = all(checks.values())
                    
                    for check, passed in checks.items():
                        if passed:
                            st.success(f"✅ {check}")
                        else:
                            st.error(f"❌ {check}")
                    
                    if all_valid:
                        st.success("🎉 Strong password!")
                    else:
                        st.warning("⚠️ Weak password")
            
            elif val_func == "Age":
                age = st.number_input("Age:", value=15, min_value=0, max_value=120, key="age_val")
                if st.button("✅ Check Age", key="val_age_btn"):
                    is_adult = age >= 18
                    if is_adult:
                        st.success(f"✅ Age {int(age)} is adult (≥18)")
                    else:
                        st.info(f"ℹ️ Age {int(age)} is minor (<18)")
    
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
        **Try these challenges:**
        
        1. **Temperature Converter:**
        ```python
        def convert_temperature(temp, from_unit, to_unit):
            # Convert between F, C, K
            pass
        ```
        
        2. **Grade Calculator:**
        ```python
        def calculate_grade(score):
            # Return letter grade (A, B, C, D, F)
            if score >= 90:
                return "A"
            # ... complete it!
        ```
        
        3. **List Statistics:**
        ```python
        def get_stats(numbers):
            # Return min, max, average, median
            return min_val, max_val, avg, median
        ```
        
        4. **Password Generator:**
        ```python
        def generate_password(length, include_numbers=True, include_symbols=False):
            # Generate random password with options
            pass
        ```
        
        5. **Shopping Cart Total:**
        ```python
        def calculate_total(prices, tax_rate=0.08, discount=0):
            # Calculate total with tax and discount
            subtotal = sum(prices)
            tax = subtotal * tax_rate
            total = subtotal + tax - discount
            return total
        ```
        """)

