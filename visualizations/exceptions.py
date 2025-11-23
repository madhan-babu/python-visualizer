import streamlit as st

def show():
    st.markdown('<h2 style="color: #2196F3;">🛡️ Exception Handling (Try-Except)</h2>', unsafe_allow_html=True)
    st.write("Learn how to handle errors gracefully in your programs!")
    
    # Overview
    with st.expander("📚 What is Exception Handling?", expanded=False):
        st.markdown("""
        **Exception Handling** lets your program deal with errors without crashing.
        
        Think of exceptions like:
        - 🎮 Game saves before crash - don't lose progress!
        - 🏥 Safety net - catch problems before they break things
        - 🚨 Fire alarm - detect problems and respond appropriately
        - 🛡️ Shield - protect your program from unexpected situations
        
        **Without Exception Handling:**
        ```python
        age = int(input("Enter age: "))  # User types "hello"
        # Program crashes with ValueError! ❌
        ```
        
        **With Exception Handling:**
        ```python
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Please enter a number!")
            age = 0
        # Program continues running! ✅
        ```
        
        **Why use try-except?**
        - Prevent crashes
        - Provide helpful error messages
        - Handle user mistakes
        - Make programs robust and professional
        """)
    
    # Create tabs
    tabs = st.tabs(["🎯 Basic Try-Except", "🔍 Specific Exceptions", "🎨 Multiple Except", "✨ Else & Finally", "💡 Real Examples"])
    
    # ============================================
    # TAB 1: BASIC TRY-EXCEPT
    # ============================================
    with tabs[0]:
        st.markdown("### 🎯 Basic Try-Except")
        st.write("Catch errors and handle them gracefully")
        
        st.info("""
        **Try-Except Structure:**
        ```python
        try:
            # Code that might cause an error
            risky_operation()
        except:
            # Code to run if error occurs
            print("Something went wrong!")
        ```
        
        **How it works:**
        1. Python tries to run code in `try` block
        2. If error occurs, jumps to `except` block
        3. If no error, skips `except` block
        4. Program continues running!
        """)
        
        st.markdown("---")
        st.markdown("#### 🎮 Try It: Division by Zero")
        
        col_div1, col_div2 = st.columns(2)
        
        with col_div1:
            numerator = st.number_input("Numerator:", value=10, key="num_basic")
        
        with col_div2:
            denominator = st.number_input("Denominator:", value=0, key="denom_basic")
        
        col_demo1, col_demo2 = st.columns(2)
        
        with col_demo1:
            st.markdown("**❌ Without Try-Except:**")
            if st.button("Run (Will Crash!)", key="no_try_btn"):
                st.code(f"""result = {numerator} / {denominator}
print(result)""", language="python")
                
                if denominator == 0:
                    st.error("""
                    💥 **ZeroDivisionError:**
                    division by zero
                    
                    ❌ Program crashed!
                    """)
                else:
                    result = numerator / denominator
                    st.success(f"Result: {result}")
        
        with col_demo2:
            st.markdown("**✅ With Try-Except:**")
            if st.button("Run (Safe!)", key="with_try_btn"):
                st.code(f"""try:
    result = {numerator} / {denominator}
    print(result)
except:
    print("Cannot divide by zero!")""", language="python")
                
                try:
                    result = numerator / denominator
                    st.success(f"✅ Result: {result}")
                except:
                    st.warning("⚠️ Cannot divide by zero!\n\n✅ Program still running!")
        
        st.markdown("---")
        st.markdown("#### 🔄 Execution Flow")
        
        st.info("""
        **When error occurs:**
        ```
        1. Start try block ✅
        2. Error happens! 💥
        3. Jump to except block ⚡
        4. Handle error ✅
        5. Continue program ✅
        ```
        
        **When no error:**
        ```
        1. Start try block ✅
        2. Code runs successfully ✅
        3. Skip except block ⏭️
        4. Continue program ✅
        ```
        """)
        
        st.markdown("---")
        st.markdown("#### 🎯 Interactive Example")
        
        user_input = st.text_input("Enter a number:", value="42", key="basic_input")
        
        if st.button("🔍 Convert to Integer", key="convert_int_btn"):
            col_flow1, col_flow2 = st.columns(2)
            
            with col_flow1:
                st.markdown("**Code:**")
                st.code(f"""try:
    number = int("{user_input}")
    print(f"Success! {{number}}")
except:
    print("That's not a number!")""", language="python")
            
            with col_flow2:
                st.markdown("**Result:**")
                try:
                    number = int(user_input)
                    st.success(f"✅ Success! {number}")
                    st.info(f"Type: {type(number).__name__}")
                except:
                    st.error(f'❌ "{user_input}" is not a valid number!')
                    st.warning("⚠️ Handled error gracefully!")
    
    # ============================================
    # TAB 2: SPECIFIC EXCEPTIONS
    # ============================================
    with tabs[1]:
        st.markdown("### 🔍 Catching Specific Exceptions")
        st.write("Handle different errors differently")
        
        st.info("""
        **Common Exception Types:**
        
        | Exception | When It Occurs | Example |
        |-----------|----------------|---------|
        | `ValueError` | Invalid value for conversion | `int("hello")` |
        | `ZeroDivisionError` | Division by zero | `10 / 0` |
        | `TypeError` | Wrong type of operation | `"5" + 5` |
        | `IndexError` | Invalid list index | `[1,2,3][10]` |
        | `KeyError` | Invalid dictionary key | `dict["missing"]` |
        | `FileNotFoundError` | File doesn't exist | `open("missing.txt")` |
        
        **Why specify exception type?**
        - Different messages for different errors
        - Handle some errors, let others through
        - More precise error handling
        """)
        
        st.markdown("---")
        st.markdown("#### 🎮 Try Different Exception Types")
        
        exception_demo = st.radio("Choose operation:", 
                                  ["Convert to Integer", "Divide Numbers", "Access List Item", "Get Dict Value"],
                                  key="exception_demo")
        
        if exception_demo == "Convert to Integer":
            st.markdown("**ValueError Demo:**")
            
            convert_input = st.text_input("Enter value:", value="hello", key="convert_input")
            
            if st.button("🔄 Convert", key="convert_btn"):
                st.code(f"""try:
    number = int("{convert_input}")
    print(f"Converted: {{number}}")
except ValueError:
    print("ValueError: Cannot convert to integer!")""", language="python")
                
                try:
                    number = int(convert_input)
                    st.success(f"✅ Converted: {number}")
                except ValueError:
                    st.error("❌ ValueError: Cannot convert to integer!")
                    st.info("💡 Caught ValueError specifically!")
        
        elif exception_demo == "Divide Numbers":
            st.markdown("**ZeroDivisionError Demo:**")
            
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                div_a = st.number_input("Numerator:", value=100, key="div_a")
            with col_d2:
                div_b = st.number_input("Denominator:", value=0, key="div_b")
            
            if st.button("➗ Divide", key="divide_btn"):
                st.code(f"""try:
    result = {div_a} / {div_b}
    print(f"Result: {{result}}")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero!")""", language="python")
                
                try:
                    result = div_a / div_b
                    st.success(f"✅ Result: {result}")
                except ZeroDivisionError:
                    st.error("❌ ZeroDivisionError: Cannot divide by zero!")
                    st.info("💡 Caught ZeroDivisionError specifically!")
        
        elif exception_demo == "Access List Item":
            st.markdown("**IndexError Demo:**")
            
            demo_list = [10, 20, 30]
            st.code(f"my_list = {demo_list}", language="python")
            
            index_input = st.number_input("Enter index:", value=5, min_value=-10, max_value=10, key="index_input")
            
            if st.button("🔍 Access", key="access_btn"):
                st.code(f"""try:
    value = my_list[{int(index_input)}]
    print(f"Value: {{value}}")
except IndexError:
    print("IndexError: Index out of range!")""", language="python")
                
                try:
                    value = demo_list[int(index_input)]
                    st.success(f"✅ Value: {value}")
                except IndexError:
                    st.error(f"❌ IndexError: Index {int(index_input)} out of range!")
                    st.info(f"💡 Valid range: 0 to {len(demo_list)-1}")
        
        else:  # Get Dict Value
            st.markdown("**KeyError Demo:**")
            
            demo_dict = {"name": "Alice", "age": 15, "grade": "10th"}
            st.code(f"student = {demo_dict}", language="python")
            
            key_input = st.text_input("Enter key:", value="email", key="key_input")
            
            if st.button("🔑 Get Value", key="getval_btn"):
                st.code(f"""try:
    value = student["{key_input}"]
    print(f"Value: {{value}}")
except KeyError:
    print("KeyError: Key not found!")""", language="python")
                
                try:
                    value = demo_dict[key_input]
                    st.success(f"✅ Value: {value}")
                except KeyError:
                    st.error(f"❌ KeyError: '{key_input}' not found!")
                    st.info(f"💡 Available keys: {list(demo_dict.keys())}")
    
    # ============================================
    # TAB 3: MULTIPLE EXCEPT
    # ============================================
    with tabs[2]:
        st.markdown("### 🎨 Multiple Except Blocks")
        st.write("Handle different errors with different messages")
        
        st.info("""
        **Multiple except blocks:**
        ```python
        try:
            # Risky code
            operation()
        except ValueError:
            print("Invalid value!")
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        except TypeError:
            print("Wrong type!")
        except:
            print("Some other error!")
        ```
        
        **How it works:**
        - Python checks each except block in order
        - Runs the first matching except block
        - Skips remaining except blocks
        - Generic `except:` catches anything not caught above
        """)
        
        st.markdown("---")
        st.markdown("#### 🎮 Calculator with Multiple Exceptions")
        
        col_calc1, col_calc2, col_calc3 = st.columns([2, 1, 2])
        
        with col_calc1:
            calc_input1 = st.text_input("First value:", value="10", key="calc1")
        
        with col_calc2:
            calc_op = st.selectbox("Operation:", ["+", "-", "*", "/"], key="calc_op")
        
        with col_calc3:
            calc_input2 = st.text_input("Second value:", value="0", key="calc2")
        
        if st.button("🔢 Calculate", key="calc_btn"):
            st.code(f"""try:
    a = float("{calc_input1}")
    b = float("{calc_input2}")
    
    if "{calc_op}" == "+":
        result = a + b
    elif "{calc_op}" == "-":
        result = a - b
    elif "{calc_op}" == "*":
        result = a * b
    else:
        result = a / b
    
    print(f"Result: {{result}}")
    
except ValueError:
    print("ValueError: Invalid number format!")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {{e}}")""", language="python")
            
            try:
                a = float(calc_input1)
                b = float(calc_input2)
                
                if calc_op == "+":
                    result = a + b
                elif calc_op == "-":
                    result = a - b
                elif calc_op == "*":
                    result = a * b
                else:
                    result = a / b
                
                st.success(f"✅ Result: {result}")
                
            except ValueError as e:
                st.error(f"❌ ValueError: Invalid number format!")
                st.warning(f"Make sure both inputs are numbers")
                
            except ZeroDivisionError:
                st.error(f"❌ ZeroDivisionError: Cannot divide by zero!")
                st.warning("Change the second number to non-zero")
                
            except Exception as e:
                st.error(f"❌ Unexpected error: {e}")
        
        st.markdown("---")
        st.markdown("#### 📊 Error Flow Diagram")
        
        st.code("""
Try Block
    ↓
Error? ──No──→ Continue
    ↓
   Yes
    ↓
ValueError? ──Yes──→ Handle ValueError
    ↓
   No
    ↓
ZeroDivisionError? ──Yes──→ Handle ZeroDivisionError
    ↓
   No
    ↓
Other Exception? ──Yes──→ Handle Generic Error
    ↓
Continue Program
        """, language="text")
    
    # ============================================
    # TAB 4: ELSE & FINALLY
    # ============================================
    with tabs[3]:
        st.markdown("### ✨ Else & Finally Blocks")
        st.write("Advanced exception handling")
        
        st.info("""
        **Complete try-except structure:**
        ```python
        try:
            # Code that might fail
            risky_operation()
        except ExceptionType:
            # Handle specific error
            print("Error occurred!")
        else:
            # Runs only if NO error
            print("Success!")
        finally:
            # ALWAYS runs (error or not)
            print("Cleanup!")
        ```
        
        **When to use:**
        - **else:** Code to run only on success
        - **finally:** Cleanup code (close files, connections, etc.)
        """)
        
        st.markdown("---")
        st.markdown("#### 🎮 Try the Complete Structure")
        
        complete_input = st.text_input("Enter a number:", value="42", key="complete_input")
        
        if st.button("🔍 Process Number", key="complete_btn"):
            st.code(f"""try:
    number = int("{complete_input}")
    print(f"Converted: {{number}}")
except ValueError:
    print("Error: Not a valid number!")
else:
    print("Success: No errors occurred!")
    squared = number ** 2
    print(f"Squared: {{squared}}")
finally:
    print("Finally: This always runs!")""", language="python")
            
            st.markdown("---")
            st.markdown("#### 📊 Execution Log:")
            
            log_msgs = []
            
            # Try block
            st.info("🔷 **Try Block:** Attempting conversion...")
            log_msgs.append("Try: Attempting conversion...")
            
            try:
                number = int(complete_input)
                st.success(f"✅ Converted: {number}")
                log_msgs.append(f"Try: Successfully converted to {number}")
                error_occurred = False
                
            except ValueError:
                st.error(f"❌ Error: '{complete_input}' is not a valid number!")
                log_msgs.append(f"Except: ValueError caught")
                error_occurred = True
            
            else:
                if not error_occurred:
                    st.success("✅ **Else Block:** No errors, continuing...")
                    squared = number ** 2
                    st.info(f"Squared: {squared}")
                    log_msgs.append(f"Else: Calculated {number}² = {squared}")
            
            # Finally block
            st.warning("⚠️ **Finally Block:** This always runs!")
            log_msgs.append("Finally: Cleanup complete")
            
            st.markdown("---")
            st.code("\n".join(log_msgs), language="text")
        
        st.markdown("---")
        st.markdown("#### 📁 File Handling Example")
        
        st.code("""try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: No permission to read!")
else:
    print("Success: File read successfully!")
finally:
    # Always close the file!
    if 'file' in locals():
        file.close()
        print("File closed")""", language="python")
        
        st.info("""
        **Why use finally?**
        - Ensures cleanup happens
        - Closes files, connections
        - Releases resources
        - Runs even if error occurs
        """)
    
    # ============================================
    # TAB 5: REAL EXAMPLES
    # ============================================
    with tabs[4]:
        st.markdown("### 💡 Real-World Examples")
        
        example_choice = st.selectbox("Choose example:", 
                                     ["Age Input Validator", "List Access Safety", "Dictionary Lookup", "Number Converter"],
                                     key="example_choice")
        
        if example_choice == "Age Input Validator":
            st.markdown("#### 🎂 Age Input Validator")
            
            age_input = st.text_input("Enter your age:", value="15", key="age_val_input")
            
            if st.button("✅ Validate Age", key="validate_age_btn"):
                st.code(f"""try:
    age = int("{age_input}")
    
    if age < 0:
        print("Error: Age cannot be negative!")
    elif age > 150:
        print("Error: Age seems unrealistic!")
    else:
        print(f"Valid age: {{age}}")
        
except ValueError:
    print("Error: Please enter a number!")""", language="python")
                
                try:
                    age = int(age_input)
                    
                    if age < 0:
                        st.error("❌ Error: Age cannot be negative!")
                    elif age > 150:
                        st.error("❌ Error: Age seems unrealistic!")
                    else:
                        st.success(f"✅ Valid age: {age}")
                        
                        # Age category
                        if age < 13:
                            category = "Child"
                        elif age < 20:
                            category = "Teenager"
                        elif age < 65:
                            category = "Adult"
                        else:
                            category = "Senior"
                        
                        st.info(f"Category: {category}")
                
                except ValueError:
                    st.error("❌ Error: Please enter a valid number!")
        
        elif example_choice == "List Access Safety":
            st.markdown("#### 📚 Safe List Access")
            
            demo_list = ["Python", "Java", "C++", "JavaScript"]
            st.code(f"languages = {demo_list}", language="python")
            
            list_index = st.number_input("Enter index:", value=0, min_value=-10, max_value=10, key="list_safe_index")
            
            if st.button("🔍 Get Language", key="get_lang_btn"):
                st.code(f"""try:
    language = languages[{int(list_index)}]
    print(f"Language: {{language}}")
except IndexError:
    print("Error: Index out of range!")
    print(f"Valid range: 0 to {{len(languages)-1}}")""", language="python")
                
                try:
                    language = demo_list[int(list_index)]
                    st.success(f"✅ Language: {language}")
                    st.info(f"Position: {int(list_index) + 1} of {len(demo_list)}")
                except IndexError:
                    st.error(f"❌ Error: Index {int(list_index)} is out of range!")
                    st.warning(f"Valid range: 0 to {len(demo_list)-1}")
        
        elif example_choice == "Dictionary Lookup":
            st.markdown("#### 📖 Safe Dictionary Lookup")
            
            grades = {"Alice": 95, "Bob": 87, "Charlie": 92}
            st.code(f"grades = {grades}", language="python")
            
            student_name = st.text_input("Enter student name:", value="Alice", key="student_lookup")
            
            if st.button("🔍 Get Grade", key="get_grade_btn"):
                st.code(f"""try:
    grade = grades["{student_name}"]
    print(f"{{"{student_name}"}}'s grade: {{grade}}")
except KeyError:
    print("Error: Student not found!")
    print(f"Available students: {{list(grades.keys())}}")""", language="python")
                
                try:
                    grade = grades[student_name]
                    st.success(f"✅ {student_name}'s grade: {grade}")
                    
                    if grade >= 90:
                        letter = "A"
                    elif grade >= 80:
                        letter = "B"
                    elif grade >= 70:
                        letter = "C"
                    else:
                        letter = "D"
                    
                    st.info(f"Letter grade: {letter}")
                    
                except KeyError:
                    st.error(f"❌ Error: '{student_name}' not found!")
                    st.warning(f"Available students: {list(grades.keys())}")
        
        else:  # Number Converter
            st.markdown("#### 🔢 Multi-Format Number Converter")
            
            num_input = st.text_input("Enter value:", value="42", key="num_convert")
            
            if st.button("🔄 Convert", key="num_convert_btn"):
                st.code(f"""value = "{num_input}"

# Try multiple conversions
try:
    # Try integer first
    num = int(value)
    print(f"Integer: {{num}}")
except ValueError:
    try:
        # Try float
        num = float(value)
        print(f"Float: {{num}}")
    except ValueError:
        print("Error: Not a valid number!")
        num = None

if num is not None:
    print(f"Doubled: {{num * 2}}")""", language="python")
                
                try:
                    # Try integer first
                    num = int(num_input)
                    st.success(f"✅ Integer: {num}")
                    st.info(f"Type: {type(num).__name__}")
                    st.info(f"Doubled: {num * 2}")
                    
                except ValueError:
                    try:
                        # Try float
                        num = float(num_input)
                        st.success(f"✅ Float: {num}")
                        st.info(f"Type: {type(num).__name__}")
                        st.info(f"Doubled: {num * 2}")
                        
                    except ValueError:
                        st.error(f"❌ Error: '{num_input}' is not a valid number!")
    
    # Key takeaways
    st.markdown("---")
    st.markdown("### 🎯 Key Takeaways")
    
    col_key1, col_key2 = st.columns(2)
    
    with col_key1:
        st.info("""
        **Exception Handling Basics:**
        - `try:` - Code that might fail
        - `except:` - Handle the error
        - Prevents crashes
        - Makes programs robust
        - Provides helpful error messages
        """)
    
    with col_key2:
        st.success("""
        **Best Practices:**
        - Catch specific exceptions when possible
        - Provide helpful error messages
        - Use finally for cleanup
        - Don't catch exceptions silently
        - Test error cases
        """)
    
    # Practice exercises
    with st.expander("💪 Practice Exercises", expanded=False):
        st.markdown("""
        **Try these challenges:**
        
        1. **Safe Division:**
        ```python
        def safe_divide(a, b):
            try:
                return a / b
            except ZeroDivisionError:
                return "Cannot divide by zero!"
        
        print(safe_divide(10, 2))   # 5.0
        print(safe_divide(10, 0))   # Cannot divide by zero!
        ```
        
        2. **List Access with Default:**
        ```python
        def get_item(my_list, index, default=None):
            try:
                return my_list[index]
            except IndexError:
                return default
        
        fruits = ["apple", "banana"]
        print(get_item(fruits, 0))      # apple
        print(get_item(fruits, 10))     # None
        print(get_item(fruits, 10, "N/A"))  # N/A
        ```
        
        3. **Input Validator:**
        ```python
        def get_positive_number():
            while True:
                try:
                    num = int(input("Enter positive number: "))
                    if num > 0:
                        return num
                    else:
                        print("Must be positive!")
                except ValueError:
                    print("Must be a number!")
        
        result = get_positive_number()
        print(f"You entered: {result}")
        ```
        
        4. **Dictionary with Default:**
        ```python
        settings = {"theme": "dark", "font": "12"}
        
        def get_setting(key):
            try:
                return settings[key]
            except KeyError:
                return "default"
        
        print(get_setting("theme"))     # dark
        print(get_setting("language"))  # default
        ```
        
        **Challenge:** Create a calculator that:
        - Takes two numbers and an operation
        - Handles ValueError (invalid numbers)
        - Handles ZeroDivisionError (division by zero)
        - Handles invalid operations
        - Keeps running until user types "quit"
        """)

