import streamlit as st
import time

def show():
    st.markdown('<h2 style="color: #2196F3;">🔁 Python Loops Visualizer</h2>', unsafe_allow_html=True)
    st.write("Watch loops in action and understand how they repeat code!")
    
    # Overview
    with st.expander("📚 What are Loops?", expanded=False):
        st.markdown("""
        **Loops** let you repeat code multiple times without writing it over and over.
        
        Think of loops like:
        - 🔄 A song on repeat
        - 🏃 Running laps around a track
        - 📚 Reading each page in a book
        - 🎮 Game levels that keep going
        
        **Two types of loops in Python:**
        
        1. **`for` loop** - Repeat a specific number of times
           - Loop through a list, range, or string
           - You know how many times it will run
        
        2. **`while` loop** - Repeat while a condition is True
           - Keep going until something changes
           - You don't always know how many times it will run
        
        **Why use loops?**
        - Avoid repeating code (DRY - Don't Repeat Yourself!)
        - Process lists of data
        - Keep programs running
        - Make games, animations, and more!
        """)
    
    # Create tabs for different loop types
    loop_tabs = st.tabs(["🔄 For Loops", "⏰ While Loops", "🎮 Loop Control", "🎯 Nested Loops"])
    
    # ============================================
    # TAB 1: FOR LOOPS
    # ============================================
    with loop_tabs[0]:
        st.markdown("### 🔄 For Loops")
        st.write("Iterate over sequences (lists, strings, ranges)")
        
        # For loop type selector
        for_type = st.radio("Choose what to loop over:", 
                           ["List", "Range", "String"], 
                           horizontal=True,
                           key="for_type")
        
        if for_type == "List":
            st.info("""
            **Loop through a list** - Visit each item one by one
            ```python
            for item in my_list:
                print(item)
            ```
            """)
            
            # Input list
            list_input = st.text_input("Enter items (comma-separated):", 
                                      value="apple, banana, orange",
                                      key="for_list_input")
            items = [item.strip() for item in list_input.split(",") if item.strip()]
            
            if st.button("▶️ Run For Loop", key="run_for_list"):
                st.markdown("#### 🎬 Loop Execution:")
                
                # Create container for loop visualization
                loop_container = st.container()
                
                with loop_container:
                    st.code(f"my_list = {items}\n\nfor item in my_list:\n    print(item)", language="python")
                    
                    st.markdown("---")
                    
                    # Show each iteration
                    for i, item in enumerate(items):
                        col1, col2, col3 = st.columns([1, 2, 2])
                        
                        with col1:
                            st.markdown(f"### Iteration {i+1}")
                        
                        with col2:
                            st.markdown(f"**Current item:**")
                            st.markdown(f"### :green[{item}]")
                        
                        with col3:
                            st.code(f"item = {repr(item)}\nprint(item)  # Output: {item}", language="python")
                        
                        st.markdown("---")
                
                st.success(f"✅ Loop completed! Processed {len(items)} items.")
        
        elif for_type == "Range":
            st.info("""
            **Loop through a range** - Repeat a specific number of times
            ```python
            for i in range(5):  # 0, 1, 2, 3, 4
                print(i)
            ```
            """)
            
            col_r1, col_r2, col_r3 = st.columns(3)
            
            with col_r1:
                range_start = st.number_input("Start", value=0, key="range_start")
            with col_r2:
                range_end = st.number_input("End", value=5, key="range_end")
            with col_r3:
                range_step = st.number_input("Step", value=1, min_value=1, key="range_step")
            
            if st.button("▶️ Run For Loop", key="run_for_range"):
                st.markdown("#### 🎬 Loop Execution:")
                
                if range_start < range_end:
                    st.code(f"for i in range({int(range_start)}, {int(range_end)}, {int(range_step)}):\n    print(i)", language="python")
                    st.markdown("---")
                    
                    numbers = list(range(int(range_start), int(range_end), int(range_step)))
                    
                    # Visual representation
                    for idx, i in enumerate(numbers):
                        col1, col2, col3 = st.columns([1, 2, 2])
                        
                        with col1:
                            st.markdown(f"### Iteration {idx+1}")
                        
                        with col2:
                            st.markdown(f"**Current value:**")
                            st.markdown(f"### :blue[{i}]")
                        
                        with col3:
                            st.code(f"i = {i}\nprint(i)  # Output: {i}", language="python")
                        
                        st.markdown("---")
                    
                    st.success(f"✅ Loop completed! Ran {len(numbers)} times.")
                else:
                    st.error("❌ Start must be less than End!")
        
        elif for_type == "String":
            st.info("""
            **Loop through a string** - Visit each character
            ```python
            for char in "Hello":
                print(char)
            ```
            """)
            
            string_input = st.text_input("Enter a string:", value="Python", key="for_string_input")
            
            if st.button("▶️ Run For Loop", key="run_for_string"):
                st.markdown("#### 🎬 Loop Execution:")
                
                st.code(f"text = {repr(string_input)}\n\nfor char in text:\n    print(char)", language="python")
                st.markdown("---")
                
                for i, char in enumerate(string_input):
                    col1, col2, col3 = st.columns([1, 2, 2])
                    
                    with col1:
                        st.markdown(f"### Iteration {i+1}")
                    
                    with col2:
                        st.markdown(f"**Current char:**")
                        st.markdown(f"### :orange[{repr(char)}]")
                    
                    with col3:
                        st.code(f"char = {repr(char)}\nprint(char)  # Output: {char}", language="python")
                    
                    st.markdown("---")
                
                st.success(f"✅ Loop completed! Processed {len(string_input)} characters.")
        
        # Enumerate example
        st.markdown("---")
        st.markdown("### 🔢 For Loop with Index (enumerate)")
        
        st.info("""
        **`enumerate()`** - Get both index and value
        ```python
        for index, item in enumerate(my_list):
            print(f"{index}: {item}")
        ```
        """)
        
        enum_input = st.text_input("Enter items:", value="cat, dog, bird", key="enum_input")
        enum_items = [item.strip() for item in enum_input.split(",") if item.strip()]
        
        if st.button("▶️ Run Enumerate Loop", key="run_enum"):
            st.code(f"items = {enum_items}\n\nfor index, item in enumerate(items):\n    print(f'{{index}}: {{item}}')", language="python")
            st.markdown("---")
            
            for index, item in enumerate(enum_items):
                col1, col2, col3 = st.columns([1, 1, 3])
                
                with col1:
                    st.markdown(f"**Index:** :blue[{index}]")
                with col2:
                    st.markdown(f"**Item:** :green[{item}]")
                with col3:
                    st.code(f"print(f'{index}: {item}')\n# Output: {index}: {item}", language="python")
                
                st.markdown("---")
    
    # ============================================
    # TAB 2: WHILE LOOPS
    # ============================================
    with loop_tabs[1]:
        st.markdown("### ⏰ While Loops")
        st.write("Repeat while a condition is True")
        
        st.info("""
        **While loop** - Keeps running as long as condition is True
        ```python
        count = 0
        while count < 5:
            print(count)
            count += 1  # IMPORTANT: Update the condition!
        ```
        """)
        
        st.warning("⚠️ **Danger:** Infinite loops! Always update your condition variable!")
        
        # While loop examples
        while_example = st.radio("Choose example:", 
                                 ["Count Up", "Count Down", "Find Target"],
                                 horizontal=True,
                                 key="while_example")
        
        if while_example == "Count Up":
            st.markdown("#### 🔼 Count Up Example")
            
            col_cu1, col_cu2 = st.columns(2)
            with col_cu1:
                start_val = st.number_input("Start value", value=0, key="cu_start")
            with col_cu2:
                target_val = st.number_input("Target value", value=5, key="cu_target")
            
            if st.button("▶️ Run While Loop", key="run_while_up"):
                if start_val < target_val:
                    st.code(f"count = {int(start_val)}\nwhile count < {int(target_val)}:\n    print(count)\n    count += 1", language="python")
                    st.markdown("---")
                    
                    count = int(start_val)
                    iteration = 1
                    
                    while count < int(target_val):
                        col1, col2, col3, col4 = st.columns([1, 1, 2, 2])
                        
                        with col1:
                            st.markdown(f"**Iter {iteration}**")
                        with col2:
                            st.markdown(f"**count:** :blue[{count}]")
                        with col3:
                            st.markdown(f"**Check:** `{count} < {int(target_val)}` = :green[True]")
                        with col4:
                            st.code(f"print({count})\ncount = {count} + 1", language="python")
                        
                        count += 1
                        iteration += 1
                        st.markdown("---")
                    
                    # Final check (condition becomes False)
                    col1, col2, col3 = st.columns([1, 1, 3])
                    with col1:
                        st.markdown(f"**Final**")
                    with col2:
                        st.markdown(f"**count:** :blue[{count}]")
                    with col3:
                        st.markdown(f"**Check:** `{count} < {int(target_val)}` = :red[False] → Loop stops!")
                    
                    st.success(f"✅ Loop completed after {iteration-1} iterations!")
                else:
                    st.error("❌ Start must be less than target!")
        
        elif while_example == "Count Down":
            st.markdown("#### 🔽 Count Down Example")
            
            col_cd1, col_cd2 = st.columns(2)
            with col_cd1:
                countdown_start = st.number_input("Start value", value=5, key="cd_start")
            with col_cd2:
                countdown_end = st.number_input("Stop at", value=0, key="cd_end")
            
            if st.button("▶️ Run While Loop", key="run_while_down"):
                if countdown_start > countdown_end:
                    st.code(f"count = {int(countdown_start)}\nwhile count > {int(countdown_end)}:\n    print(count)\n    count -= 1", language="python")
                    st.markdown("---")
                    
                    count = int(countdown_start)
                    iteration = 1
                    
                    while count > int(countdown_end):
                        col1, col2, col3, col4 = st.columns([1, 1, 2, 2])
                        
                        with col1:
                            st.markdown(f"**Iter {iteration}**")
                        with col2:
                            st.markdown(f"**count:** :orange[{count}]")
                        with col3:
                            st.markdown(f"**Check:** `{count} > {int(countdown_end)}` = :green[True]")
                        with col4:
                            st.code(f"print({count})\ncount = {count} - 1", language="python")
                        
                        count -= 1
                        iteration += 1
                        st.markdown("---")
                    
                    # Final check
                    col1, col2, col3 = st.columns([1, 1, 3])
                    with col1:
                        st.markdown(f"**Final**")
                    with col2:
                        st.markdown(f"**count:** :orange[{count}]")
                    with col3:
                        st.markdown(f"**Check:** `{count} > {int(countdown_end)}` = :red[False] → Loop stops!")
                    
                    st.success(f"✅ Loop completed after {iteration-1} iterations!")
                else:
                    st.error("❌ Start must be greater than end!")
        
        elif while_example == "Find Target":
            st.markdown("#### 🎯 Find Target Example")
            st.write("Search through a list until target is found")
            
            col_ft1, col_ft2 = st.columns(2)
            with col_ft1:
                search_list = st.text_input("List (comma-separated):", value="10, 20, 30, 40, 50", key="search_list")
            with col_ft2:
                target_item = st.text_input("Target to find:", value="30", key="target_item")
            
            if st.button("▶️ Run While Loop", key="run_while_find"):
                items = [item.strip() for item in search_list.split(",")]
                
                st.code(f"""items = {items}
target = {repr(target_item)}
index = 0
found = False

while index < len(items) and not found:
    if items[index] == target:
        found = True
        print(f"Found at index {{index}}!")
    else:
        index += 1""", language="python")
                
                st.markdown("---")
                
                index = 0
                found = False
                iteration = 1
                
                while index < len(items) and not found:
                    col1, col2, col3, col4 = st.columns([1, 1, 2, 2])
                    
                    with col1:
                        st.markdown(f"**Iter {iteration}**")
                    with col2:
                        st.markdown(f"**index:** :blue[{index}]")
                    with col3:
                        st.markdown(f"**Check:** `items[{index}]` = {repr(items[index])}")
                    with col4:
                        if items[index] == target_item:
                            st.markdown(f":green[**Match!** Found '{target_item}']")
                            found = True
                        else:
                            st.markdown(f":red[No match, continue...]")
                    
                    if not found:
                        index += 1
                    iteration += 1
                    st.markdown("---")
                
                if found:
                    st.success(f"✅ Found '{target_item}' at index {index}!")
                else:
                    st.error(f"❌ '{target_item}' not found in list!")
    
    # ============================================
    # TAB 3: LOOP CONTROL
    # ============================================
    with loop_tabs[2]:
        st.markdown("### 🎮 Loop Control (break & continue)")
        st.write("Control how loops execute")
        
        control_type = st.radio("Choose control statement:", 
                               ["break - Exit loop", "continue - Skip iteration"],
                               key="control_type")
        
        if "break" in control_type:
            st.info("""
            **`break`** - Exit the loop immediately
            ```python
            for i in range(10):
                if i == 5:
                    break  # Stop the loop
                print(i)
            # Prints: 0, 1, 2, 3, 4
            ```
            """)
            
            col_br1, col_br2 = st.columns(2)
            with col_br1:
                break_range = st.number_input("Loop from 0 to:", value=10, min_value=1, key="break_range")
            with col_br2:
                break_at = st.number_input("Break at:", value=5, min_value=0, key="break_at")
            
            if st.button("▶️ Run Loop with Break", key="run_break"):
                st.code(f"for i in range({int(break_range)}):\n    if i == {int(break_at)}:\n        break\n    print(i)", language="python")
                st.markdown("---")
                
                for i in range(int(break_range)):
                    if i == int(break_at):
                        col1, col2 = st.columns([1, 3])
                        with col1:
                            st.markdown(f"### :red[i = {i}]")
                        with col2:
                            st.error(f"🛑 **BREAK!** i == {int(break_at)} → Exit loop")
                        break
                    else:
                        col1, col2, col3 = st.columns([1, 2, 2])
                        with col1:
                            st.markdown(f"**i = {i}**")
                        with col2:
                            st.markdown(f"Check: `{i} == {int(break_at)}` = False")
                        with col3:
                            st.code(f"print({i})", language="python")
                        st.markdown("---")
                
                st.success(f"✅ Loop broke at i = {int(break_at)}")
        
        elif "continue" in control_type:
            st.info("""
            **`continue`** - Skip to next iteration
            ```python
            for i in range(5):
                if i == 2:
                    continue  # Skip this iteration
                print(i)
            # Prints: 0, 1, 3, 4 (skips 2)
            ```
            """)
            
            col_co1, col_co2 = st.columns(2)
            with col_co1:
                continue_range = st.number_input("Loop from 0 to:", value=10, min_value=1, key="continue_range")
            with col_co2:
                skip_at = st.number_input("Skip at:", value=5, min_value=0, key="skip_at")
            
            if st.button("▶️ Run Loop with Continue", key="run_continue"):
                st.code(f"for i in range({int(continue_range)}):\n    if i == {int(skip_at)}:\n        continue  # Skip\n    print(i)", language="python")
                st.markdown("---")
                
                for i in range(int(continue_range)):
                    if i == int(skip_at):
                        col1, col2 = st.columns([1, 3])
                        with col1:
                            st.markdown(f"### :orange[i = {i}]")
                        with col2:
                            st.warning(f"⏭️ **CONTINUE!** i == {int(skip_at)} → Skip to next iteration")
                        st.markdown("---")
                        continue
                    
                    col1, col2, col3 = st.columns([1, 2, 2])
                    with col1:
                        st.markdown(f"**i = {i}**")
                    with col2:
                        st.markdown(f"Check: `{i} == {int(skip_at)}` = False")
                    with col3:
                        st.code(f"print({i})", language="python")
                    st.markdown("---")
                
                st.success(f"✅ Loop completed, skipped i = {int(skip_at)}")
    
    # ============================================
    # TAB 4: NESTED LOOPS
    # ============================================
    with loop_tabs[3]:
        st.markdown("### 🎯 Nested Loops")
        st.write("Loops inside loops!")
        
        st.info("""
        **Nested loops** - A loop inside another loop
        - Outer loop runs once
        - Inner loop runs completely for each outer iteration
        - Useful for 2D data (tables, grids, matrices)
        
        ```python
        for i in range(3):        # Outer loop
            for j in range(3):    # Inner loop
                print(f"({i}, {j})")
        ```
        """)
        
        nested_type = st.radio("Choose example:", 
                              ["Multiplication Table", "Grid Pattern"],
                              key="nested_type")
        
        if nested_type == "Multiplication Table":
            st.markdown("#### ✖️ Multiplication Table (Nested Loops)")
            
            col_mt1, col_mt2 = st.columns(2)
            with col_mt1:
                rows_mult = st.number_input("Numbers (rows):", value=3, min_value=1, max_value=5, key="mult_rows")
            with col_mt2:
                cols_mult = st.number_input("Multiply up to (cols):", value=3, min_value=1, max_value=5, key="mult_cols")
            
            if st.button("▶️ Generate Table", key="run_mult"):
                st.code(f"# Nested loops: outer for rows, inner for columns\nfor row in range(1, {int(rows_mult)+1}):\n    for col in range(1, {int(cols_mult)+1}):\n        result = row * col\n        print(f'{{row}} x {{col}} = {{result}}')\n    print('---')  # Separate each row", language="python")
                st.markdown("---")
                
                # Show execution
                for row in range(1, int(rows_mult)+1):
                    st.markdown(f"### 🔄 Outer Loop: row = {row}")
                    
                    for col in range(1, int(cols_mult)+1):
                        result = row * col
                        col1, col2, col3, col4 = st.columns([1, 1, 2, 2])
                        
                        with col1:
                            st.markdown(f"**Row {row}**")
                        with col2:
                            st.markdown(f"**Col {col}**")
                        with col3:
                            st.markdown(f"`{row} × {col}`")
                        with col4:
                            st.markdown(f"### :green[= {result}]")
                    
                    st.markdown("---")
                
                st.success(f"✅ Nested loops: Outer ran {int(rows_mult)} times, Inner ran {int(cols_mult)} times each = {int(rows_mult) * int(cols_mult)} total iterations!")
        
        elif nested_type == "Grid Pattern":
            st.markdown("#### 🎨 Grid Pattern")
            
            col_gp1, col_gp2 = st.columns(2)
            with col_gp1:
                rows = st.number_input("Rows:", value=3, min_value=1, max_value=5, key="grid_rows")
            with col_gp2:
                cols = st.number_input("Columns:", value=3, min_value=1, max_value=5, key="grid_cols")
            
            if st.button("▶️ Generate Grid", key="run_grid"):
                st.code(f"for row in range({int(rows)}):\n    for col in range({int(cols)}):\n        print(f'({{row}}, {{col}})', end=' ')\n    print()  # New line", language="python")
                st.markdown("---")
                
                for row in range(int(rows)):
                    cols_ui = st.columns(int(cols))
                    
                    for col in range(int(cols)):
                        with cols_ui[col]:
                            st.markdown(f"""
                            <div style='
                                border: 2px solid #2196F3;
                                border-radius: 10px;
                                padding: 20px;
                                text-align: center;
                                background-color: rgba(33, 150, 243, 0.1);
                                margin: 5px;
                            '>
                                <div style='font-weight: bold; font-size: 1.2rem;'>({row}, {col})</div>
                            </div>
                            """, unsafe_allow_html=True)
                
                st.success(f"✅ Generated {int(rows)} × {int(cols)} grid!")
    
    # Key takeaways
    st.markdown("---")
    st.markdown("### 🎯 Key Takeaways")
    
    col_key1, col_key2 = st.columns(2)
    
    with col_key1:
        st.info("""
        **For Loops:**
        - Use when you know how many times to loop
        - `for item in list:` - iterate items
        - `for i in range(5):` - repeat 5 times
        - `enumerate()` - get index + item
        """)
    
    with col_key2:
        st.success("""
        **While Loops:**
        - Use when condition determines when to stop
        - Always update condition variable!
        - `break` - exit loop early
        - `continue` - skip to next iteration
        """)
    
    # Practice exercises
    with st.expander("💪 Practice Exercises", expanded=False):
        st.markdown("""
        **Try these in Python:**
        
        1. **Sum Numbers:**
        ```python
        total = 0
        for i in range(1, 11):
            total += i
        print(total)  # 55
        ```
        
        2. **Find Even Numbers:**
        ```python
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        for num in numbers:
            if num % 2 == 0:
                print(num)  # 2, 4, 6, 8
        ```
        
        3. **Password Checker (while loop):**
        ```python
        password = ""
        while password != "secret":
            password = input("Enter password: ")
        print("Access granted!")
        ```
        
        4. **Print Each Item in a List:**
        ```python
        # Loop through list items
        friends = ["Emma", "Noah", "Olivia", "Liam"]
        
        for friend in friends:
            print(f"Hello, {friend}!")
        # Output:
        # Hello, Emma!
        # Hello, Noah!
        # Hello, Olivia!
        # Hello, Liam!
        ```
        
        5. **Loop Through Dictionary Items:**
        ```python
        # Show all key-value pairs
        prices = {
            "apple": 1.50,
            "banana": 0.75,
            "orange": 1.25
        }
        
        for fruit, price in prices.items():
            print(f"{fruit} costs ${price}")
        # Output:
        # apple costs $1.50
        # banana costs $0.75
        # orange costs $1.25
        ```
        
        6. **Count Items in Locker:**
        ```python
        # What's in your locker?
        locker = {
            "books": 4,
            "pencils": 12,
            "notebook": 3
        }
        
        print("My locker has:")
        for item, count in locker.items():
            print(f"  {item}: {count}")
        # Output:
        # My locker has:
        #   books: 4
        #   pencils: 12
        #   notebook: 3
        ```
        
        7. **Sum All Numbers in List:**
        ```python
        # Add up all numbers
        numbers = [10, 20, 30, 40, 50]
        total = 0
        
        for num in numbers:
            total = total + num
        
        print(f"Total: {total}")  # 150
        ```
        
        8. **Find Largest Number:**
        ```python
        # Find the biggest number
        numbers = [45, 23, 89, 12, 67]
        largest = numbers[0]
        
        for num in numbers:
            if num > largest:
                largest = num
        
        print(f"Largest: {largest}")  # 89
        ```
        """)

