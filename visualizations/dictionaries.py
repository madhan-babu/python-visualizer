import streamlit as st
import json

def show():
    st.markdown('<h2 style="color: #2196F3;">📖 Python Dictionaries Explorer</h2>', unsafe_allow_html=True)
    st.write("Learn how to store and manage key-value pairs in dictionaries!")
    
    # Overview
    with st.expander("📚 What is a Dictionary?", expanded=False):
        st.markdown("""
        **A dictionary** stores data as **key-value pairs** - like a real dictionary!
        
        Think of a dictionary like:
        - 📕 A real dictionary: word (key) → definition (value)
        - 📞 A phone book: name (key) → phone number (value)
        - 🗂️ A filing cabinet: label (key) → contents (value)
        - 🏷️ Product tags: barcode (key) → price (value)
        
        **Key Features:**
        - Keys must be **unique** (no duplicates)
        - Keys are usually strings or numbers
        - Values can be **anything** (numbers, strings, lists, even other dicts!)
        - Fast lookup by key
        - Order is preserved (Python 3.7+)
        
        **Examples:**
        ```python
        person = {"name": "Alice", "age": 15, "grade": "10th"}
        prices = {"apple": 1.50, "banana": 0.75, "orange": 2.00}
        scores = {"math": 95, "science": 87, "english": 92}
        ```
        """)
    
    # Initialize session state for the interactive dictionary
    if 'my_dict' not in st.session_state:
        st.session_state.my_dict = {"name": "Alice", "age": 15, "grade": "10th"}
    
    # Main visualization
    st.markdown("### 🎮 Interactive Dictionary Builder")
    
    # Display current dictionary
    st.markdown("#### Current Dictionary:")
    
    if len(st.session_state.my_dict) == 0:
        st.info("📭 Dictionary is empty! Add some key-value pairs below.")
    else:
        # Visual representation of the dictionary
        for key, value in st.session_state.my_dict.items():
            col1, col2, col3 = st.columns([2, 1, 2])
            
            with col1:
                st.markdown(f"""
                <div style='
                    border: 2px solid #FF9800;
                    border-radius: 10px;
                    padding: 15px;
                    background-color: rgba(255, 152, 0, 0.1);
                    text-align: center;
                '>
                    <div style='font-size: 0.8rem; color: #666;'>KEY</div>
                    <div style='font-size: 1.2rem; font-weight: bold; color: #FF9800;'>{key}</div>
                    <div style='font-size: 0.7rem; color: #999;'>({type(key).__name__})</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("<div style='text-align: center; font-size: 2rem; padding-top: 20px;'>→</div>", unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div style='
                    border: 2px solid #4CAF50;
                    border-radius: 10px;
                    padding: 15px;
                    background-color: rgba(76, 175, 80, 0.1);
                    text-align: center;
                '>
                    <div style='font-size: 0.8rem; color: #666;'>VALUE</div>
                    <div style='font-size: 1.2rem; font-weight: bold; color: #4CAF50;'>{value}</div>
                    <div style='font-size: 0.7rem; color: #999;'>({type(value).__name__})</div>
                </div>
                """, unsafe_allow_html=True)
    
    # Show Python code representation
    st.code(f"my_dict = {st.session_state.my_dict}", language="python")
    
    col_info1, col_info2, col_info3 = st.columns(3)
    with col_info1:
        st.metric("Number of Pairs", len(st.session_state.my_dict))
    with col_info2:
        st.markdown("**Keys:**")
        st.code(str(list(st.session_state.my_dict.keys())) if st.session_state.my_dict else "[]", language="python")
    with col_info3:
        st.markdown("**Values:**")
        st.code(str(list(st.session_state.my_dict.values())) if st.session_state.my_dict else "[]", language="python")
    
    st.markdown("---")
    
    # Operations tabs
    op_tabs = st.tabs(["➕ Add/Update", "🔍 Access Values", "❌ Remove Items", "📊 Dict Methods", "🔄 Iterate"])
    
    # ============================================
    # TAB 1: ADD/UPDATE ITEMS
    # ============================================
    with op_tabs[0]:
        st.markdown("### ➕ Add or Update Key-Value Pairs")
        
        st.info("""
        **Add/Update** - Use square brackets or `.update()`
        - If key exists → update value
        - If key doesn't exist → add new pair
        
        ```python
        my_dict["name"] = "Bob"      # Add or update
        my_dict.update({"age": 16})  # Add or update
        ```
        """)
        
        col_add1, col_add2, col_add3 = st.columns([2, 2, 1])
        
        with col_add1:
            new_key = st.text_input("Key", key="add_key")
        
        with col_add2:
            new_value = st.text_input("Value", key="add_value")
        
        with col_add3:
            st.write("")
            add_btn = st.button("➕ Add/Update", use_container_width=True)
        
        if add_btn and new_key and new_value:
            # Try to convert value to appropriate type
            try:
                if '.' in new_value:
                    converted_value = float(new_value)
                else:
                    converted_value = int(new_value)
            except:
                if new_value == "True":
                    converted_value = True
                elif new_value == "False":
                    converted_value = False
                else:
                    converted_value = new_value
            
            # Check if updating existing key
            if new_key in st.session_state.my_dict:
                old_value = st.session_state.my_dict[new_key]
                st.session_state.my_dict[new_key] = converted_value
                st.warning(f"✏️ Updated '{new_key}': {repr(old_value)} → {repr(converted_value)}")
                st.code(f"my_dict[{repr(new_key)}] = {repr(converted_value)}\n# Result: {st.session_state.my_dict}", language="python")
            else:
                st.session_state.my_dict[new_key] = converted_value
                st.success(f"✅ Added new pair: '{new_key}' → {repr(converted_value)}")
                st.code(f"my_dict[{repr(new_key)}] = {repr(converted_value)}\n# Result: {st.session_state.my_dict}", language="python")
            
            st.rerun()
        
        # Bulk update
        st.markdown("---")
        st.markdown("#### 🔄 Update Multiple Pairs at Once")
        
        st.info("""
        **`.update()`** method - Add/update multiple pairs
        ```python
        my_dict.update({"city": "NYC", "country": "USA"})
        ```
        """)
        
        col_bulk1, col_bulk2 = st.columns([3, 1])
        with col_bulk1:
            bulk_input = st.text_input("Enter pairs (key:value, key:value)", 
                                       placeholder="city:NYC, country:USA",
                                       key="bulk_input")
        with col_bulk2:
            st.write("")
            bulk_btn = st.button("🔄 Update", use_container_width=True)
        
        if bulk_btn and bulk_input:
            try:
                pairs = bulk_input.split(",")
                new_dict = {}
                for pair in pairs:
                    if ":" in pair:
                        k, v = pair.split(":", 1)
                        new_dict[k.strip()] = v.strip()
                
                st.session_state.my_dict.update(new_dict)
                st.success(f"✅ Updated {len(new_dict)} pairs!")
                st.code(f"my_dict.update({new_dict})\n# Result: {st.session_state.my_dict}", language="python")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    # ============================================
    # TAB 2: ACCESS VALUES
    # ============================================
    with op_tabs[1]:
        st.markdown("### 🔍 Access Values by Key")
        
        if len(st.session_state.my_dict) == 0:
            st.warning("⚠️ Dictionary is empty! Add items first.")
        else:
            st.info("""
            **Two ways to access values:**
            
            1. **Square brackets** `dict[key]` - Error if key doesn't exist
            2. **`.get()` method** `dict.get(key)` - Returns None if key doesn't exist
            
            ```python
            name = my_dict["name"]           # KeyError if "name" not found
            age = my_dict.get("age")         # Returns None if not found
            age = my_dict.get("age", 0)      # Returns 0 if not found (default)
            ```
            """)
            
            access_method = st.radio("Choose method:", 
                                    ["Square brackets []", "get() method"],
                                    horizontal=True,
                                    key="access_method")
            
            if "Square brackets" in access_method:
                st.markdown("#### 🔲 Using Square Brackets")
                
                col_sq1, col_sq2 = st.columns([3, 1])
                with col_sq1:
                    access_key = st.selectbox("Select key to access:", 
                                             list(st.session_state.my_dict.keys()),
                                             key="access_key_sq")
                with col_sq2:
                    st.write("")
                    access_btn = st.button("🔍 Access", use_container_width=True, key="access_btn_sq")
                
                if access_btn or access_key:
                    value = st.session_state.my_dict[access_key]
                    st.success(f"✅ `my_dict[{repr(access_key)}]` = {repr(value)}")
                    st.code(f"value = my_dict[{repr(access_key)}]\nprint(value)  # {repr(value)}", language="python")
                
                # Show error example
                st.markdown("---")
                st.markdown("**⚠️ What happens with a non-existent key?**")
                fake_key = st.text_input("Try a key that doesn't exist:", value="xyz", key="fake_key_sq")
                if st.button("Try It", key="try_fake_btn_sq"):
                    if fake_key in st.session_state.my_dict:
                        st.info(f"Key '{fake_key}' exists! Value: {st.session_state.my_dict[fake_key]}")
                    else:
                        st.error(f"❌ KeyError: '{fake_key}' not found in dictionary!")
                        st.code(f"value = my_dict[{repr(fake_key)}]  # KeyError!", language="python")
            
            else:  # get() method
                st.markdown("#### 🎯 Using .get() Method")
                
                col_get1, col_get2, col_get3 = st.columns([2, 2, 1])
                with col_get1:
                    get_key = st.text_input("Key to get:", key="get_key")
                with col_get2:
                    default_val = st.text_input("Default value (if not found):", value="Not Found", key="default_val")
                with col_get3:
                    st.write("")
                    get_btn = st.button("🔍 Get", use_container_width=True, key="get_btn_method")
                
                if get_btn and get_key:
                    value = st.session_state.my_dict.get(get_key, default_val)
                    
                    if get_key in st.session_state.my_dict:
                        st.success(f"✅ Found! `my_dict.get({repr(get_key)})` = {repr(value)}")
                    else:
                        st.warning(f"⚠️ Key not found. Returned default: {repr(value)}")
                    
                    st.code(f"value = my_dict.get({repr(get_key)}, {repr(default_val)})\nprint(value)  # {repr(value)}", language="python")
                
                st.info("""
                **💡 Why use .get()?**
                - Safer - no errors if key missing
                - Can provide default value
                - Good for optional data
                """)
    
    # ============================================
    # TAB 3: REMOVE ITEMS
    # ============================================
    with op_tabs[2]:
        st.markdown("### ❌ Remove Key-Value Pairs")
        
        if len(st.session_state.my_dict) == 0:
            st.warning("⚠️ Dictionary is empty! Add items first.")
        else:
            remove_method = st.radio("Choose method:", 
                                    ["pop() - Remove and return", "del - Just remove", "clear() - Remove all"],
                                    key="dict_remove_method")
            
            if "pop" in remove_method:
                st.info("""
                **`pop(key)`** - Removes key and **returns** its value
                ```python
                age = my_dict.pop("age")  # Returns value and removes
                ```
                """)
                
                col_pop1, col_pop2 = st.columns([3, 1])
                with col_pop1:
                    pop_key = st.selectbox("Key to pop:", 
                                          list(st.session_state.my_dict.keys()),
                                          key="pop_key")
                with col_pop2:
                    st.write("")
                    pop_btn = st.button("🗑️ Pop", use_container_width=True, key="dict_pop_btn")
                
                if pop_btn:
                    popped_value = st.session_state.my_dict.pop(pop_key)
                    st.success(f"✅ Popped '{pop_key}' → {repr(popped_value)}")
                    st.code(f"value = my_dict.pop({repr(pop_key)})\nprint(value)  # {repr(popped_value)}\n# Result: {st.session_state.my_dict}", language="python")
                    st.rerun()
            
            elif "del" in remove_method:
                st.info("""
                **`del`** statement - Removes key (no return value)
                ```python
                del my_dict["age"]  # Just removes it
                ```
                """)
                
                col_del1, col_del2 = st.columns([3, 1])
                with col_del1:
                    del_key = st.selectbox("Key to delete:", 
                                          list(st.session_state.my_dict.keys()),
                                          key="del_key")
                with col_del2:
                    st.write("")
                    del_btn = st.button("🗑️ Delete", use_container_width=True, key="dict_del_btn")
                
                if del_btn:
                    del st.session_state.my_dict[del_key]
                    st.success(f"✅ Deleted '{del_key}'")
                    st.code(f"del my_dict[{repr(del_key)}]\n# Result: {st.session_state.my_dict}", language="python")
                    st.rerun()
            
            elif "clear" in remove_method:
                st.warning("""
                **`clear()`** - Removes **ALL** key-value pairs
                ```python
                my_dict.clear()  # Empty dictionary
                ```
                """)
                
                clear_btn = st.button("🗑️ Clear All", type="primary", key="dict_clear_btn")
                
                if clear_btn:
                    st.session_state.my_dict.clear()
                    st.success("✅ Cleared all items from dictionary!")
                    st.code(f"my_dict.clear()\n# Result: {st.session_state.my_dict}", language="python")
                    st.rerun()
    
    # ============================================
    # TAB 4: DICT METHODS
    # ============================================
    with op_tabs[3]:
        st.markdown("### 📊 Dictionary Methods")
        
        if len(st.session_state.my_dict) == 0:
            st.warning("⚠️ Dictionary is empty! Add items first to see methods in action.")
        
        col_meth1, col_meth2 = st.columns(2)
        
        with col_meth1:
            st.markdown("#### 🔑 Keys, Values, Items")
            
            if st.session_state.my_dict:
                # Keys
                keys = list(st.session_state.my_dict.keys())
                st.code(f"my_dict.keys() = {keys}", language="python")
                st.caption("Get all keys")
                
                # Values
                values = list(st.session_state.my_dict.values())
                st.code(f"my_dict.values() = {values}", language="python")
                st.caption("Get all values")
                
                # Items
                items = list(st.session_state.my_dict.items())
                st.code(f"my_dict.items() = {items}", language="python")
                st.caption("Get all key-value pairs as tuples")
        
        with col_meth2:
            st.markdown("#### 🔍 Check & Copy")
            
            if st.session_state.my_dict:
                # Check key exists
                check_key = st.text_input("Check if key exists:", key="check_key_method")
                if check_key:
                    exists = check_key in st.session_state.my_dict
                    if exists:
                        st.success(f"✅ '{check_key}' is IN the dictionary!")
                    else:
                        st.error(f"❌ '{check_key}' is NOT in the dictionary!")
                    st.code(f"{repr(check_key)} in my_dict  # {exists}", language="python")
                
                st.markdown("---")
                
                # Copy
                if st.button("📋 Copy Dictionary", key="copy_dict_btn"):
                    copied = st.session_state.my_dict.copy()
                    st.success(f"✅ Created a copy!")
                    st.code(f"new_dict = my_dict.copy()\nprint(new_dict)  # {copied}", language="python")
        
        # Length
        st.markdown("---")
        st.markdown("#### 📏 Dictionary Length")
        st.code(f"len(my_dict) = {len(st.session_state.my_dict)}", language="python")
        st.caption("Number of key-value pairs")
    
    # ============================================
    # TAB 5: ITERATE
    # ============================================
    with op_tabs[4]:
        st.markdown("### 🔄 Loop Through Dictionary")
        
        if len(st.session_state.my_dict) == 0:
            st.warning("⚠️ Dictionary is empty! Add items first.")
        else:
            loop_type = st.radio("Choose what to loop over:", 
                                ["Keys only", "Values only", "Key-Value pairs"],
                                horizontal=True,
                                key="loop_type")
            
            if loop_type == "Keys only":
                st.info("""
                **Loop through keys:**
                ```python
                for key in my_dict:
                    print(key)
                ```
                or
                ```python
                for key in my_dict.keys():
                    print(key)
                ```
                """)
                
                if st.button("▶️ Run Loop", key="run_keys"):
                    st.markdown("#### Iteration Results:")
                    st.code(f"for key in my_dict:\n    print(key)", language="python")
                    st.markdown("---")
                    
                    for i, key in enumerate(st.session_state.my_dict, 1):
                        col1, col2 = st.columns([1, 3])
                        with col1:
                            st.markdown(f"**Iteration {i}**")
                        with col2:
                            st.code(f"key = {repr(key)}", language="python")
                        st.markdown("---")
            
            elif loop_type == "Values only":
                st.info("""
                **Loop through values:**
                ```python
                for value in my_dict.values():
                    print(value)
                ```
                """)
                
                if st.button("▶️ Run Loop", key="run_values"):
                    st.markdown("#### Iteration Results:")
                    st.code(f"for value in my_dict.values():\n    print(value)", language="python")
                    st.markdown("---")
                    
                    for i, value in enumerate(st.session_state.my_dict.values(), 1):
                        col1, col2 = st.columns([1, 3])
                        with col1:
                            st.markdown(f"**Iteration {i}**")
                        with col2:
                            st.code(f"value = {repr(value)}", language="python")
                        st.markdown("---")
            
            else:  # Key-Value pairs
                st.info("""
                **Loop through key-value pairs:**
                ```python
                for key, value in my_dict.items():
                    print(f"{key}: {value}")
                ```
                """)
                
                if st.button("▶️ Run Loop", key="run_items"):
                    st.markdown("#### Iteration Results:")
                    st.code(f"for key, value in my_dict.items():\n    print(f'{{key}}: {{value}}')", language="python")
                    st.markdown("---")
                    
                    for i, (key, value) in enumerate(st.session_state.my_dict.items(), 1):
                        col1, col2, col3 = st.columns([1, 2, 2])
                        with col1:
                            st.markdown(f"**Iter {i}**")
                        with col2:
                            st.markdown(f"**key:** :orange[{repr(key)}]")
                        with col3:
                            st.markdown(f"**value:** :green[{repr(value)}]")
                        st.markdown("---")
    
    # Reset button
    st.markdown("---")
    col_reset1, col_reset2 = st.columns([3, 1])
    with col_reset2:
        if st.button("🔄 Reset to Default", type="secondary", key="dict_reset_btn"):
            st.session_state.my_dict = {"name": "Alice", "age": 15, "grade": "10th"}
            st.rerun()
    
    # Key concepts
    st.markdown("---")
    st.markdown("### 🎯 Key Takeaways")
    
    col_key1, col_key2 = st.columns(2)
    
    with col_key1:
        st.info("""
        **Dictionary Basics:**
        - Store key-value pairs: `{"key": "value"}`
        - Keys must be unique
        - Fast lookup by key
        - Mutable (changeable)
        - Order preserved (Python 3.7+)
        """)
    
    with col_key2:
        st.success("""
        **Common Operations:**
        - `dict[key] = value` - add/update
        - `dict[key]` - access (error if missing)
        - `dict.get(key)` - safe access
        - `dict.pop(key)` - remove and return
        - `dict.keys()`, `dict.values()`, `dict.items()`
        """)
    
    # Practice exercises
    with st.expander("💪 Practice Exercises", expanded=False):
        st.markdown("""
        **Try these fun challenges:**
        
        1. **Your Profile:**
        ```python
        # Create a dictionary about yourself
        me = {
            "name": "Sam",
            "age": 12,
            "favorite_color": "blue",
            "hobby": "gaming"
        }
        
        print(f"Hi, I'm {me['name']}")
        print(f"I'm {me['age']} years old")
        print(f"I love {me['hobby']}")
        ```
        
        2. **Pet Information:**
        ```python
        # Store info about a pet
        pet = {
            "name": "Max",
            "type": "dog",
            "age": 3
        }
        
        # Add new information
        pet["color"] = "brown"
        
        # Update age (birthday!)
        pet["age"] = 4
        
        print(pet)
        ```
        
        3. **Game Character:**
        ```python
        # Create a game character
        character = {
            "name": "Hero",
            "health": 100,
            "level": 1,
            "coins": 50
        }
        
        # Character found coins!
        character["coins"] = character["coins"] + 10
        
        # Level up!
        character["level"] = character["level"] + 1
        
        print(f"{character['name']} is now level {character['level']}")
        print(f"Total coins: {character['coins']}")
        ```
        
        4. **Check What's Inside:**
        ```python
        # Check if keys exist
        scores = {"math": 95, "science": 88, "english": 92}
        
        if "math" in scores:
            print(f"Math score: {scores['math']}")
        
        if "history" in scores:
            print("Has history score")
        else:
            print("No history score yet")
        ```
        
        5. **School Locker:**
        ```python
        # What's in your locker?
        locker = {
            "books": 4,
            "pencils": 12,
            "notebook": 3
        }
        
        # Take out a notebook
        locker["notebook"] = locker["notebook"] - 1
        
        # Add more pencils
        locker["pencils"] = locker["pencils"] + 5
        
        # Check individual items
        print(f"Books: {locker['books']}")
        print(f"Pencils: {locker['pencils']}")
        print(f"Notebooks: {locker['notebook']}")
        ```
        """)

