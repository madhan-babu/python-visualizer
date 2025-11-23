import streamlit as st

def show():
    st.markdown('<h2 style="color: #2196F3;">🔀 Conditional Statements (If-Elif-Else)</h2>', unsafe_allow_html=True)
    st.write("Learn how to make decisions in your code!")
    
    # Overview
    with st.expander("📚 What are Conditional Statements?", expanded=False):
        st.markdown("""
        **Conditional statements** let your program make decisions based on conditions.
        
        Think of conditionals like:
        - 🚦 Traffic lights - different actions for red, yellow, green
        - 🌡️ Thermostat - if too cold, heat up; if too hot, cool down
        - 🎮 Game rules - if score > 100, you win; else, keep playing
        - 🏪 Store discounts - if age < 12, kid price; elif age >= 65, senior price; else, regular price
        
        **Types of conditional statements:**
        
        1. **`if`** - Do something only if condition is True
        2. **`if-else`** - Do one thing or another
        3. **`if-elif-else`** - Choose between multiple options
        
        **Why use conditionals?**
        - Make your program respond to different situations
        - Control the flow of your code
        - Create interactive programs
        - Validate user input
        """)
    
    # Create tabs for different conditional types
    cond_tabs = st.tabs(["✅ Simple If", "🔀 If-Else", "🎯 If-Elif-Else", "🔗 Nested Conditions", "💡 Examples"])
    
    # ============================================
    # TAB 1: SIMPLE IF
    # ============================================
    with cond_tabs[0]:
        st.markdown("### ✅ Simple If Statement")
        st.write("Execute code only when a condition is True")
        
        st.info("""
        **Syntax:**
        ```python
        if condition:
            # Code runs only if condition is True
            print("Condition is True!")
        ```
        
        **Key Points:**
        - Condition must result in `True` or `False`
        - Code is indented (4 spaces or 1 tab)
        - If condition is False, code is skipped
        """)
        
        st.markdown("---")
        st.markdown("#### 🎮 Try It: Simple If")
        
        col_if1, col_if2, col_if3 = st.columns([2, 1, 2])
        
        with col_if1:
            if_value = st.number_input("Enter a number:", value=15, key="simple_if_value")
        
        with col_if2:
            if_operator = st.selectbox("Operator:", [">", "<", ">=", "<=", "==", "!="], key="simple_if_op")
        
        with col_if3:
            if_compare = st.number_input("Compare to:", value=10, key="simple_if_compare")
        
        if st.button("▶️ Run If Statement", key="run_simple_if"):
            # Evaluate condition
            if if_operator == ">":
                condition_result = if_value > if_compare
                condition_text = f"{if_value} > {if_compare}"
            elif if_operator == "<":
                condition_result = if_value < if_compare
                condition_text = f"{if_value} < {if_compare}"
            elif if_operator == ">=":
                condition_result = if_value >= if_compare
                condition_text = f"{if_value} >= {if_compare}"
            elif if_operator == "<=":
                condition_result = if_value <= if_compare
                condition_text = f"{if_value} <= {if_compare}"
            elif if_operator == "==":
                condition_result = if_value == if_compare
                condition_text = f"{if_value} == {if_compare}"
            else:  # !=
                condition_result = if_value != if_compare
                condition_text = f"{if_value} != {if_compare}"
            
            # Show the code
            st.code(f"""if {condition_text}:
    print("Condition is True!")
    print("This code runs!")""", language="python")
            
            st.markdown("---")
            
            # Visual flow
            col_flow1, col_flow2, col_flow3 = st.columns([1, 1, 2])
            
            with col_flow1:
                st.markdown("**Condition:**")
                st.code(condition_text)
            
            with col_flow2:
                st.markdown("**Result:**")
                if condition_result:
                    st.markdown("### :green[True] ✅")
                else:
                    st.markdown("### :red[False] ❌")
            
            with col_flow3:
                st.markdown("**Execution:**")
                if condition_result:
                    st.success("✅ Condition is True - Code inside 'if' runs!")
                    st.info("Output: Condition is True!\nOutput: This code runs!")
                else:
                    st.warning("⚠️ Condition is False - Code inside 'if' is skipped!")
                    st.caption("No output")
        
        st.markdown("---")
        st.markdown("#### 📊 Real Example: Age Check")
        
        age_input = st.number_input("Enter age:", value=16, min_value=0, max_value=120, key="age_simple_if")
        
        if st.button("🎂 Check Age", key="check_age_simple"):
            st.code(f"""age = {int(age_input)}

if age >= 18:
    print("You are an adult!")
    print("You can vote!")""", language="python")
            
            if age_input >= 18:
                st.success("✅ Condition is True (age >= 18)")
                st.info("Output: You are an adult!\nOutput: You can vote!")
            else:
                st.warning("⚠️ Condition is False (age < 18)")
                st.caption("No output - if block is skipped")
    
    # ============================================
    # TAB 2: IF-ELSE
    # ============================================
    with cond_tabs[1]:
        st.markdown("### 🔀 If-Else Statement")
        st.write("Do one thing or another - always one path is taken")
        
        st.info("""
        **Syntax:**
        ```python
        if condition:
            # Code runs if condition is True
            print("True path!")
        else:
            # Code runs if condition is False
            print("False path!")
        ```
        
        **Key Points:**
        - One of the two blocks ALWAYS runs
        - Like a fork in the road - must choose one path
        - `else` doesn't need a condition
        """)
        
        st.markdown("---")
        st.markdown("#### 🎮 Interactive If-Else")
        
        col_ifelse1, col_ifelse2 = st.columns(2)
        
        with col_ifelse1:
            number_check = st.number_input("Enter a number:", value=7, key="ifelse_number")
        
        with col_ifelse2:
            st.write("")
            st.write("")
            check_btn = st.button("🔍 Check Even or Odd", key="check_even_odd", use_container_width=True)
        
        if check_btn:
            is_even = number_check % 2 == 0
            
            st.code(f"""number = {int(number_check)}

if number % 2 == 0:
    print("The number is EVEN")
else:
    print("The number is ODD")""", language="python")
            
            st.markdown("---")
            st.markdown("#### 🎯 Execution Flow:")
            
            # Visual flowchart
            col_flow1, col_flow2 = st.columns(2)
            
            with col_flow1:
                st.markdown("**If Branch (condition: number % 2 == 0)**")
                if is_even:
                    st.success("✅ **THIS PATH EXECUTED**")
                    st.code("print('The number is EVEN')")
                else:
                    st.markdown("⚪ *Skipped*")
                    st.code("# Not executed")
            
            with col_flow2:
                st.markdown("**Else Branch (condition is False)**")
                if not is_even:
                    st.success("✅ **THIS PATH EXECUTED**")
                    st.code("print('The number is ODD')")
                else:
                    st.markdown("⚪ *Skipped*")
                    st.code("# Not executed")
            
            st.markdown("---")
            
            if is_even:
                st.info(f"**Result:** {int(number_check)} % 2 = 0 → EVEN")
                st.success(f"Output: The number is EVEN")
            else:
                st.info(f"**Result:** {int(number_check)} % 2 = 1 → ODD")
                st.success(f"Output: The number is ODD")
        
        st.markdown("---")
        st.markdown("#### 🌡️ Temperature Example")
        
        temp = st.slider("Temperature (°C):", min_value=-20, max_value=45, value=25, key="temp_slider")
        
        if st.button("🌡️ Check Temperature", key="check_temp_btn"):
            st.code(f"""temperature = {temp}

if temperature >= 25:
    print("It's HOT! 🔥")
    print("Drink water!")
else:
    print("It's COLD! ❄️")
    print("Wear a jacket!")""", language="python")
            
            if temp >= 25:
                st.success(f"✅ Condition True: {temp}°C >= 25°C")
                st.info("Output: It's HOT! 🔥\nOutput: Drink water!")
            else:
                st.warning(f"❌ Condition False: {temp}°C < 25°C")
                st.info("Output: It's COLD! ❄️\nOutput: Wear a jacket!")
    
    # ============================================
    # TAB 3: IF-ELIF-ELSE
    # ============================================
    with cond_tabs[2]:
        st.markdown("### 🎯 If-Elif-Else Statement")
        st.write("Choose between multiple conditions")
        
        st.info("""
        **Syntax:**
        ```python
        if condition1:
            # Runs if condition1 is True
        elif condition2:
            # Runs if condition1 is False AND condition2 is True
        elif condition3:
            # Runs if condition1 and condition2 are False AND condition3 is True
        else:
            # Runs if all conditions are False
        ```
        
        **Key Points:**
        - Checks conditions from top to bottom
        - Stops at first True condition
        - Can have multiple `elif` statements
        - `else` is optional (catches all other cases)
        """)
        
        st.markdown("---")
        st.markdown("#### 📝 Grade Calculator")
        
        score = st.slider("Enter score (0-100):", min_value=0, max_value=100, value=85, key="grade_score")
        
        if st.button("📊 Calculate Grade", key="calc_grade_btn"):
            # Determine grade
            if score >= 90:
                grade = "A"
                message = "Excellent! 🌟"
                color = "green"
            elif score >= 80:
                grade = "B"
                message = "Great job! 👍"
                color = "blue"
            elif score >= 70:
                grade = "C"
                message = "Good work! 👌"
                color = "orange"
            elif score >= 60:
                grade = "D"
                message = "Needs improvement 📚"
                color = "red"
            else:
                grade = "F"
                message = "Study harder! 📖"
                color = "red"
            
            st.code(f"""score = {score}

if score >= 90:
    grade = "A"
    print("Excellent! 🌟")
elif score >= 80:
    grade = "B"
    print("Great job! 👍")
elif score >= 70:
    grade = "C"
    print("Good work! 👌")
elif score >= 60:
    grade = "D"
    print("Needs improvement 📚")
else:
    grade = "F"
    print("Study harder! 📖")
    
print(f"Your grade: {{grade}}")""", language="python")
            
            st.markdown("---")
            st.markdown("#### 🔍 Condition Check Order:")
            
            # Show which conditions were checked
            conditions = [
                ("score >= 90", score >= 90, "A"),
                ("score >= 80", score >= 80, "B"),
                ("score >= 70", score >= 70, "C"),
                ("score >= 60", score >= 60, "D"),
                ("else", True, "F")
            ]
            
            found = False
            for cond_text, cond_result, grade_val in conditions:
                col_cond1, col_cond2, col_cond3 = st.columns([2, 1, 2])
                
                with col_cond1:
                    st.code(cond_text)
                
                with col_cond2:
                    if not found and cond_result:
                        st.markdown("### :green[True] ✅")
                    elif not found:
                        st.markdown("### :red[False] ❌")
                    else:
                        st.markdown("⚪ *Skipped*")
                
                with col_cond3:
                    if not found and cond_result:
                        st.success(f"✅ **EXECUTED** → Grade: {grade_val}")
                        found = True
                    elif not found:
                        st.caption("Continue to next condition...")
                    else:
                        st.caption("Not checked (already found True)")
            
            st.markdown("---")
            st.markdown(f"### Final Result: Grade {grade} - {message}")
        
        st.markdown("---")
        st.markdown("#### 🎟️ Ticket Price Calculator")
        
        age_ticket = st.number_input("Enter age:", value=25, min_value=0, max_value=120, key="ticket_age")
        
        if st.button("💰 Calculate Price", key="calc_price_btn"):
            if age_ticket < 5:
                price = 0
                category = "Free (Under 5)"
            elif age_ticket < 18:
                price = 10
                category = "Child (5-17)"
            elif age_ticket < 65:
                price = 20
                category = "Adult (18-64)"
            else:
                price = 15
                category = "Senior (65+)"
            
            st.code(f"""age = {int(age_ticket)}

if age < 5:
    price = 0
    print("Free (Under 5)")
elif age < 18:
    price = 10
    print("Child (5-17)")
elif age < 65:
    price = 20
    print("Adult (18-64)")
else:
    price = 15
    print("Senior (65+)")
    
print(f"Ticket price: ${{price}}")""", language="python")
            
            st.success(f"🎫 Category: {category}")
            st.info(f"💵 Ticket Price: ${price}")
    
    # ============================================
    # TAB 4: NESTED CONDITIONS
    # ============================================
    with cond_tabs[3]:
        st.markdown("### 🔗 Nested Conditions")
        st.write("Put if statements inside other if statements")
        
        st.info("""
        **Nested conditionals** = if statements inside if statements
        
        ```python
        if condition1:
            if condition2:
                # Runs only if BOTH conditions are True
                print("Both True!")
            else:
                # Runs if condition1 is True but condition2 is False
                print("Only first True!")
        else:
            print("First False!")
        ```
        
        **When to use:**
        - Multiple related conditions
        - More complex decision logic
        - When you need AND relationships
        """)
        
        st.markdown("---")
        st.markdown("#### 🎮 Game Access Checker")
        
        col_nest1, col_nest2 = st.columns(2)
        
        with col_nest1:
            age_game = st.number_input("Your age:", value=16, min_value=0, max_value=120, key="game_age")
        
        with col_nest2:
            has_permission = st.checkbox("Have parent permission?", value=True, key="has_permission")
        
        if st.button("🎮 Check Game Access", key="check_game_access"):
            st.code(f"""age = {int(age_game)}
has_permission = {has_permission}

if age >= 13:
    if has_permission:
        print("✅ You can play the game!")
        print("Have fun!")
    else:
        print("⚠️ You need parent permission")
        print("Ask your parents!")
else:
    print("❌ Sorry, you're too young")
    print("Minimum age is 13")""", language="python")
            
            st.markdown("---")
            st.markdown("#### 🔍 Decision Flow:")
            
            # First condition
            st.markdown("**Step 1: Check age >= 13**")
            if age_game >= 13:
                st.success(f"✅ True ({int(age_game)} >= 13)")
                
                # Second condition (nested)
                st.markdown("**Step 2: Check parent permission**")
                if has_permission:
                    st.success("✅ True (has permission)")
                    st.markdown("---")
                    st.success("🎉 **RESULT:** You can play the game!\nHave fun!")
                else:
                    st.error("❌ False (no permission)")
                    st.markdown("---")
                    st.warning("⚠️ **RESULT:** You need parent permission\nAsk your parents!")
            else:
                st.error(f"❌ False ({int(age_game)} < 13)")
                st.caption("Step 2 is skipped")
                st.markdown("---")
                st.error("❌ **RESULT:** Sorry, you're too young\nMinimum age is 13")
        
        st.markdown("---")
        st.markdown("#### 💡 Alternative: Using 'and' Operator")
        
        st.warning("""
        **You can often replace nested if with 'and':**
        
        ```python
        # Nested if
        if age >= 13:
            if has_permission:
                print("Can play!")
        
        # Same using 'and'
        if age >= 13 and has_permission:
            print("Can play!")
        ```
        
        Use `and` when both conditions must be True!
        """)
    
    # ============================================
    # TAB 5: EXAMPLES
    # ============================================
    with cond_tabs[4]:
        st.markdown("### 💡 Real-World Examples")
        
        example_cat = st.selectbox("Choose example:", 
                                   ["Password Validator", "BMI Calculator", "Time of Day Greeter", "Number Classifier"],
                                   key="example_category_cond")
        
        if example_cat == "Password Validator":
            st.markdown("#### 🔐 Password Strength Checker")
            
            password = st.text_input("Enter password:", value="MyPass123", type="password", key="password_validator")
            
            if st.button("✅ Validate Password", key="validate_pass_btn"):
                length = len(password)
                has_digit = any(char.isdigit() for char in password)
                has_upper = any(char.isupper() for char in password)
                has_lower = any(char.islower() for char in password)
                
                st.code(f"""password = "{password}"

# Check conditions
length = len(password)  # {length}
has_digit = any(char.isdigit() for char in password)  # {has_digit}
has_upper = any(char.isupper() for char in password)  # {has_upper}
has_lower = any(char.islower() for char in password)  # {has_lower}

if length < 6:
    strength = "Too Short"
elif length < 8:
    strength = "Weak"
elif has_digit and has_upper and has_lower:
    strength = "Strong"
elif has_digit or has_upper:
    strength = "Medium"
else:
    strength = "Weak"
    
print(f"Password strength: {{strength}}")""", language="python")
                
                # Determine strength
                if length < 6:
                    strength = "Too Short"
                    color = "red"
                    icon = "❌"
                elif length < 8:
                    strength = "Weak"
                    color = "orange"
                    icon = "⚠️"
                elif has_digit and has_upper and has_lower:
                    strength = "Strong"
                    color = "green"
                    icon = "✅"
                elif has_digit or has_upper:
                    strength = "Medium"
                    color = "blue"
                    icon = "🔵"
                else:
                    strength = "Weak"
                    color = "orange"
                    icon = "⚠️"
                
                st.markdown(f"### {icon} Password Strength: {strength}")
                
                # Show checks
                col_check1, col_check2, col_check3, col_check4 = st.columns(4)
                with col_check1:
                    if length >= 8:
                        st.success(f"✅ Length: {length}")
                    else:
                        st.error(f"❌ Length: {length}")
                with col_check2:
                    if has_digit:
                        st.success("✅ Has digit")
                    else:
                        st.error("❌ No digit")
                with col_check3:
                    if has_upper:
                        st.success("✅ Has uppercase")
                    else:
                        st.error("❌ No uppercase")
                with col_check4:
                    if has_lower:
                        st.success("✅ Has lowercase")
                    else:
                        st.error("❌ No lowercase")
        
        elif example_cat == "BMI Calculator":
            st.markdown("#### ⚖️ BMI Calculator with Categories")
            
            col_bmi1, col_bmi2 = st.columns(2)
            with col_bmi1:
                weight = st.number_input("Weight (kg):", value=70.0, min_value=1.0, key="bmi_weight")
            with col_bmi2:
                height = st.number_input("Height (m):", value=1.75, min_value=0.1, key="bmi_height")
            
            if st.button("📊 Calculate BMI", key="calc_bmi_btn"):
                bmi = weight / (height ** 2)
                
                if bmi < 18.5:
                    category = "Underweight"
                    advice = "Consider eating more nutritious foods"
                elif bmi < 25:
                    category = "Normal weight"
                    advice = "Great! Keep it up!"
                elif bmi < 30:
                    category = "Overweight"
                    advice = "Consider more exercise and balanced diet"
                else:
                    category = "Obese"
                    advice = "Consult with a healthcare provider"
                
                st.code(f"""weight = {weight}
height = {height}
bmi = weight / (height ** 2)  # {bmi:.2f}

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
    
print(f"BMI: {{bmi:.2f}}")
print(f"Category: {{category}}")""", language="python")
                
                st.metric("Your BMI", f"{bmi:.2f}")
                st.info(f"**Category:** {category}")
                st.success(f"**Advice:** {advice}")
        
        elif example_cat == "Time of Day Greeter":
            st.markdown("#### 👋 Time-Based Greeting")
            
            hour = st.slider("Hour (0-23):", min_value=0, max_value=23, value=14, key="hour_slider")
            
            if st.button("👋 Get Greeting", key="get_greeting_btn"):
                if hour < 6:
                    greeting = "Good night"
                    icon = "🌙"
                    advice = "Time to sleep!"
                elif hour < 12:
                    greeting = "Good morning"
                    icon = "🌅"
                    advice = "Have a great day ahead!"
                elif hour < 17:
                    greeting = "Good afternoon"
                    icon = "☀️"
                    advice = "Keep up the good work!"
                elif hour < 21:
                    greeting = "Good evening"
                    icon = "🌆"
                    advice = "Time to relax!"
                else:
                    greeting = "Good night"
                    icon = "🌙"
                    advice = "Time to rest!"
                
                st.code(f"""hour = {hour}

if hour < 6:
    greeting = "Good night 🌙"
elif hour < 12:
    greeting = "Good morning 🌅"
elif hour < 17:
    greeting = "Good afternoon ☀️"
elif hour < 21:
    greeting = "Good evening 🌆"
else:
    greeting = "Good night 🌙"
    
print(greeting)""", language="python")
                
                st.markdown(f"## {icon} {greeting}!")
                st.info(advice)
        
        elif example_cat == "Number Classifier":
            st.markdown("#### 🔢 Number Classifier")
            
            num_classify = st.number_input("Enter a number:", value=0, key="num_classify")
            
            if st.button("🔍 Classify Number", key="classify_num_btn"):
                classifications = []
                
                # Check multiple properties
                if num_classify == 0:
                    classifications.append("Zero")
                elif num_classify > 0:
                    classifications.append("Positive")
                else:
                    classifications.append("Negative")
                
                if num_classify % 2 == 0:
                    classifications.append("Even")
                else:
                    classifications.append("Odd")
                
                if num_classify % 5 == 0:
                    classifications.append("Divisible by 5")
                
                if num_classify % 10 == 0:
                    classifications.append("Divisible by 10")
                
                st.code(f"""number = {int(num_classify)}

# Check sign
if number == 0:
    print("Zero")
elif number > 0:
    print("Positive")
else:
    print("Negative")

# Check even/odd
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Check divisibility
if number % 5 == 0:
    print("Divisible by 5")
    
if number % 10 == 0:
    print("Divisible by 10")""", language="python")
                
                st.markdown("### 📊 Classifications:")
                for classification in classifications:
                    st.success(f"✅ {classification}")
    
    # Key takeaways
    st.markdown("---")
    st.markdown("### 🎯 Key Takeaways")
    
    col_key1, col_key2 = st.columns(2)
    
    with col_key1:
        st.info("""
        **Conditional Basics:**
        - `if` - execute if condition is True
        - `if-else` - choose one of two paths
        - `if-elif-else` - choose among many paths
        - Conditions checked top to bottom
        - Stops at first True condition
        """)
    
    with col_key2:
        st.success("""
        **Best Practices:**
        - Use comparison operators (==, !=, <, >, <=, >=)
        - Combine with logical operators (and, or, not)
        - Indent code properly (4 spaces)
        - Order conditions from specific to general
        - Use `elif`, not multiple separate `if`s
        """)
    
    # Practice exercises
    with st.expander("💪 Practice Exercises", expanded=False):
        st.markdown("""
        **Try these challenges:**
        
        1. **Voting Eligibility:**
        ```python
        age = int(input("Enter your age: "))
        
        if age >= 18:
            print("You can vote!")
        else:
            years_left = 18 - age
            print(f"You can vote in {years_left} years")
        ```
        
        2. **Traffic Light:**
        ```python
        light = input("Traffic light color: ")
        
        if light == "red":
            print("STOP")
        elif light == "yellow":
            print("SLOW DOWN")
        elif light == "green":
            print("GO")
        else:
            print("Invalid color")
        ```
        
        3. **Grade with Remarks:**
        ```python
        score = int(input("Enter score: "))
        
        if score >= 90:
            print("Grade: A - Excellent!")
        elif score >= 80:
            print("Grade: B - Very Good!")
        elif score >= 70:
            print("Grade: C - Good!")
        elif score >= 60:
            print("Grade: D - Pass")
        else:
            print("Grade: F - Fail")
        ```
        
        4. **Number Sign Checker:**
        ```python
        num = float(input("Enter a number: "))
        
        if num > 0:
            print("Positive number")
        elif num < 0:
            print("Negative number")
        else:
            print("Zero")
        ```
        
        **Challenge:** Create a simple calculator that:
        - Takes two numbers and an operator (+, -, *, /)
        - Uses if-elif-else to perform the right operation
        - Handles division by zero
        - Shows the result
        """)

