import streamlit as st

def show():
    st.markdown('<h2 style="color: #2196F3;">💬 Print & Input - Talk to Your Program!</h2>', unsafe_allow_html=True)
    st.write("Learn how to display messages and get user input in Python!")
    
    # Overview
    with st.expander("📚 What are Print & Input?", expanded=False):
        st.markdown("""
        **Print and Input are Python's way of communicating:**
        
        - **print()** - Shows messages to the user (output)
        - **input()** - Asks the user for information (input)
        
        Think of it like a conversation:
        - 🗣️ **You (program):** "What's your name?" ← using print()
        - 👂 **User types:** "Sarah" ← using input()
        - 🗣️ **You (program):** "Hello Sarah!" ← using print()
        """)
    
    # Create two main sections
    print_tab, input_tab, together_tab = st.tabs(["📢 Print Function", "⌨️ Input Function", "🤝 Using Both Together"])
    
    # ============================================
    # TAB 1: PRINT FUNCTION
    # ============================================
    with print_tab:
        st.markdown("### 📢 The print() Function")
        st.write("Display text, numbers, and variables on the screen!")
        
        # Basic printing
        st.markdown("#### 🎯 Basic Printing")
        
        col_p1, col_p2 = st.columns(2)
        
        with col_p1:
            st.code("""
# Print text (use quotes)
print("Hello, World!")
print('Python is fun!')

# Print numbers (no quotes needed)
print(42)
print(3.14)

# Print variables
name = "Alice"
age = 12
print(name)
print(age)
""", language="python")
        
        with col_p2:
            st.markdown("**Output:**")
            st.text("""
Hello, World!
Python is fun!
42
3.14
Alice
12
""")
        
        st.markdown("---")
        st.markdown("#### 🎨 Try Print Yourself!")
        
        print_input = st.text_area("What do you want to print?", 
                                   value='Hello, World!',
                                   height=100,
                                   key="print_test")
        
        col_btn1, col_btn2 = st.columns([1, 4])
        with col_btn1:
            print_btn = st.button("▶️ Run", use_container_width=True)
        
        if print_btn or print_input:
            st.markdown("**Output:**")
            st.success(f"```\n{print_input}\n```")
            st.code(f'print("{print_input}")', language="python")
        
        # Print multiple things
        st.markdown("---")
        st.markdown("#### 🎯 Print Multiple Things")
        st.write("You can print several things at once, separated by commas!")
        
        col_m1, col_m2 = st.columns(2)
        
        with col_m1:
            st.code("""
# Print multiple items
name = "Bob"
age = 10

print("My name is", name)
print("I am", age, "years old")
print("Score:", 100, "points!")

# Python adds spaces automatically!
""", language="python")
        
        with col_m2:
            st.markdown("**Output:**")
            st.text("""
My name is Bob
I am 10 years old
Score: 100 points!
""")
            st.info("💡 Python automatically adds **spaces** between items!")
        
        # Special characters
        st.markdown("---")
        st.markdown("#### ✨ Special Print Tricks")
        
        col_s1, col_s2 = st.columns(2)
        
        with col_s1:
            st.code("""
# Empty line
print()

# New line with \\n
print("Line 1\\nLine 2\\nLine 3")

# Tab space with \\t
print("Name:\\tAlice")
print("Age:\\t12")
""", language="python")
        
        with col_s2:
            st.markdown("**Output:**")
            st.text("""

Line 1
Line 2
Line 3
Name:	Alice
Age:	12
""")
            st.info("""
💡 Special codes:
- `\\n` = new line
- `\\t` = tab space
""")
    
    # ============================================
    # TAB 2: INPUT FUNCTION
    # ============================================
    with input_tab:
        st.markdown("### ⌨️ The input() Function")
        st.write("Ask the user to type something and store their answer!")
        
        # Basic input
        st.markdown("#### 🎯 Basic Input")
        
        col_i1, col_i2 = st.columns(2)
        
        with col_i1:
            st.code("""
# Ask for user's name
name = input("What is your name? ")
print("Hello,", name)

# The program waits for user to type
# Then stores it in the variable
""", language="python")
        
        with col_i2:
            st.markdown("**How it works:**")
            st.info("""
1️⃣ Program shows: "What is your name? "
2️⃣ User types: "Emma"
3️⃣ Press Enter
4️⃣ "Emma" is stored in variable `name`
5️⃣ Program prints: "Hello, Emma"
""")
        
        st.markdown("---")
        st.markdown("#### 🎮 Try Input Yourself!")
        
        st.write("Simulate what input() does:")
        
        col_input1, col_input2 = st.columns([3, 2])
        
        with col_input1:
            user_prompt = st.text_input("Your question/prompt:", 
                                       value="What is your name?",
                                       key="input_prompt")
            user_response = st.text_input(f"{user_prompt} ", 
                                         value="",
                                         key="input_response",
                                         placeholder="Type your answer here...")
        
        with col_input2:
            st.markdown("**Python Code:**")
            st.code(f"""
name = input("{user_prompt} ")
print("You typed:", name)
""", language="python")
        
        if user_response:
            st.success(f"**You typed:** {user_response}")
            st.info(f"💾 This would be stored in the variable!")
        
        # Important note about input
        st.markdown("---")
        st.markdown("#### ⚠️ Important: input() Always Returns a String!")
        
        col_warn1, col_warn2 = st.columns(2)
        
        with col_warn1:
            st.markdown("**❌ Problem:**")
            st.code("""
# User types: 10
age = input("Enter your age: ")
next_year = age + 1

# Error! Can't add string and number
# age is "10" (text), not 10 (number)
""", language="python")
        
        with col_warn2:
            st.markdown("**✅ Solution:**")
            st.code("""
# Convert to integer first!
age = input("Enter your age: ")
age = int(age)
next_year = age + 1

# Or do it in one line:
age = int(input("Enter your age: "))
next_year = age + 1
""", language="python")
        
        st.warning("""
        💡 **Remember:** 
        - `input()` always gives you text (string)
        - Use `int()` to convert to whole numbers
        - Use `float()` to convert to decimals
        """)
        
        # Interactive conversion demo
        st.markdown("---")
        st.markdown("#### 🔄 Interactive Input & Conversion")
        
        col_demo1, col_demo2 = st.columns(2)
        
        with col_demo1:
            demo_input = st.text_input("Enter a number:", value="15", key="demo_num")
            convert_choice = st.radio("Convert to:", ["Keep as string", "Convert to int", "Convert to float"], key="convert_radio")
        
        with col_demo2:
            st.markdown("**Result:**")
            try:
                if convert_choice == "Keep as string":
                    result = demo_input
                    st.code(f'value = "{result}"\ntype: {type(result).__name__}')
                    st.info("✅ This is text. Good for names, not math!")
                elif convert_choice == "Convert to int":
                    result = int(demo_input)
                    st.code(f'value = {result}\ntype: {type(result).__name__}')
                    st.success(f"✅ Now you can do math: {result} + 5 = {result + 5}")
                elif convert_choice == "Convert to float":
                    result = float(demo_input)
                    st.code(f'value = {result}\ntype: {type(result).__name__}')
                    st.success(f"✅ Decimal number: {result} / 2 = {result / 2}")
            except ValueError:
                st.error("❌ Cannot convert to number!")
    
    # ============================================
    # TAB 3: USING BOTH TOGETHER
    # ============================================
    with together_tab:
        st.markdown("### 🤝 Using Print & Input Together")
        st.write("Create interactive programs that talk with users!")
        
        # Example 1: Simple greeting
        st.markdown("#### 🎯 Example 1: Personal Greeting")
        
        col_ex1_1, col_ex1_2 = st.columns(2)
        
        with col_ex1_1:
            st.code("""
# Ask for name
name = input("What's your name? ")

# Greet the user
print("Hello,", name)
print("Welcome to Python!")
""", language="python")
        
        with col_ex1_2:
            st.markdown("**Try it:**")
            ex1_name = st.text_input("What's your name? ", key="ex1_name")
            if ex1_name:
                st.text(f"Hello, {ex1_name}")
                st.text("Welcome to Python!")
        
        # Example 2: Age calculator
        st.markdown("---")
        st.markdown("#### 🎯 Example 2: Age Calculator")
        
        col_ex2_1, col_ex2_2 = st.columns(2)
        
        with col_ex2_1:
            st.code("""
# Ask for age
age = input("How old are you? ")
age = int(age)  # Convert to number!

# Calculate next year's age
next_year = age + 1

# Show result
print("Next year you'll be", next_year)
""", language="python")
        
        with col_ex2_2:
            st.markdown("**Try it:**")
            ex2_age = st.text_input("How old are you? ", key="ex2_age", value="")
            if ex2_age:
                try:
                    age_num = int(ex2_age)
                    next_year = age_num + 1
                    st.text(f"Next year you'll be {next_year}")
                except:
                    st.error("Please enter a number!")
        
        # Example 3: Multiple inputs
        st.markdown("---")
        st.markdown("#### 🎯 Example 3: All About You")
        
        col_ex3_1, col_ex3_2 = st.columns(2)
        
        with col_ex3_1:
            st.code("""
# Ask multiple questions
name = input("Name: ")
age = int(input("Age: "))
color = input("Favorite color: ")

# Print a summary
print()  # Empty line
print("=== All About You ===")
print("Name:", name)
print("Age:", age, "years old")
print("Favorite color:", color)
""", language="python")
        
        with col_ex3_2:
            st.markdown("**Try it:**")
            ex3_name = st.text_input("Name: ", key="ex3_name")
            ex3_age = st.text_input("Age: ", key="ex3_age")
            ex3_color = st.text_input("Favorite color: ", key="ex3_color")
            
            if ex3_name and ex3_age and ex3_color:
                st.text("")
                st.text("=== All About You ===")
                st.text(f"Name: {ex3_name}")
                st.text(f"Age: {ex3_age} years old")
                st.text(f"Favorite color: {ex3_color}")
    
    # Key takeaways
    st.markdown("---")
    st.markdown("### 🎯 Key Takeaways")
    
    col_key1, col_key2 = st.columns(2)
    
    with col_key1:
        st.info("""
        **print() Function:**
        - Shows information to the user
        - Can print text, numbers, variables
        - Use quotes for text: `print("Hello")`
        - Separate items with commas
        - Automatically adds spaces between items
        """)
    
    with col_key2:
        st.success("""
        **input() Function:**
        - Gets information from the user
        - Always returns a string (text)
        - Store in a variable: `name = input()`
        - Can include a question/prompt
        - Convert to numbers: `int()` or `float()`
        """)
    
    # Practice exercises
    st.markdown("---")
    with st.expander("💪 Practice Exercises", expanded=False):
        st.markdown("""
        **Try these in Python:**
        
        1. **Simple Print:**
        ```python
        # Print your name and age
        print("My name is [your name]")
        print("I am [your age] years old")
        ```
        
        2. **Using Variables:**
        ```python
        # Store and print
        name = "Your Name"
        age = 12
        print("Hello, my name is", name)
        print("I am", age, "years old")
        ```
        
        3. **Get User Input:**
        ```python
        # Ask for favorite things
        food = input("What's your favorite food? ")
        sport = input("What's your favorite sport? ")
        print("You like", food, "and", sport)
        ```
        
        4. **Math with Input:**
        ```python
        # Simple calculator
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        total = num1 + num2
        print("The sum is", total)
        ```
        """)

