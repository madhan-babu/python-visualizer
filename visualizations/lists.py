import streamlit as st
import json

def show():
    st.markdown('<h2 style="color: #2196F3;">📚 Python Lists Explorer</h2>', unsafe_allow_html=True)
    st.write("Learn how to store and manage multiple values in a list!")
    
    # Overview
    with st.expander("📚 What is a List?", expanded=False):
        st.markdown("""
        **A list** is a container that can hold multiple values in order.
        
        Think of a list like a **train** 🚂:
        - Each car holds one item
        - Cars are in a specific order
        - You can add/remove cars
        - You can check what's in each car
        - Each car has a number (index)
        
        **Why use lists?**
        - Store multiple related items together
        - Keep items in order
        - Easy to add, remove, or change items
        - Can loop through all items
        
        **Examples:**
        ```python
        fruits = ["apple", "banana", "orange"]
        scores = [95, 87, 92, 78]
        mixed = [1, "hello", True, 3.14]  # Can mix types!
        ```
        """)
    
    # Initialize session state for the interactive list
    if 'my_list' not in st.session_state:
        st.session_state.my_list = ["apple", "banana", "orange"]
    
    if 'list_history' not in st.session_state:
        st.session_state.list_history = []
    
    # Main visualization
    st.markdown("### 🎮 Interactive List Builder")
    
    # Display current list
    st.markdown("#### Current List:")
    
    if len(st.session_state.my_list) == 0:
        st.info("📭 List is empty! Add some items below.")
    else:
        # Visual representation of the list
        cols = st.columns(len(st.session_state.my_list))
        
        for i, item in enumerate(st.session_state.my_list):
            with cols[i]:
                # Determine color based on type
                item_type = type(item).__name__
                if isinstance(item, int):
                    color = "blue"
                elif isinstance(item, str):
                    color = "green"
                elif isinstance(item, float):
                    color = "orange"
                elif isinstance(item, bool):
                    color = "red"
                else:
                    color = "gray"
                
                st.markdown(f"""
                <div style='
                    border: 2px solid #{color if color != "green" else "4CAF50"};
                    border-radius: 10px;
                    padding: 10px;
                    margin: 5px;
                    text-align: center;
                    background-color: rgba(33, 150, 243, 0.1);
                '>
                    <div style='font-size: 0.8rem; color: #666;'>Index: {i}</div>
                    <div style='font-size: 1.2rem; font-weight: bold; color: #333; margin: 5px 0;'>{item}</div>
                    <div style='font-size: 0.7rem; color: #999;'>({item_type})</div>
                </div>
                """, unsafe_allow_html=True)
    
    # Show Python code representation
    st.code(f"my_list = {st.session_state.my_list}", language="python")
    
    col_info1, col_info2, col_info3 = st.columns(3)
    with col_info1:
        st.metric("Length", len(st.session_state.my_list))
    with col_info2:
        st.metric("First Index", 0 if st.session_state.my_list else "N/A")
    with col_info3:
        st.metric("Last Index", len(st.session_state.my_list) - 1 if st.session_state.my_list else "N/A")
    
    st.markdown("---")
    
    # Operations tabs
    op_tabs = st.tabs(["➕ Add Items", "❌ Remove Items", "🔍 Access Items", "✏️ Modify Items", "📊 List Methods"])
    
    # ============================================
    # TAB 1: ADD ITEMS
    # ============================================
    with op_tabs[0]:
        st.markdown("### ➕ Add Items to List")
        
        add_method = st.radio("Choose method:", ["append() - Add to end", "insert() - Add at position", "extend() - Add multiple"], key="add_method")
        
        if "append" in add_method:
            st.info("""
            **`append(item)`** - Adds an item to the **end** of the list
            - Simplest way to add items
            - List grows by 1
            """)
            
            col_app1, col_app2 = st.columns([3, 1])
            with col_app1:
                append_item = st.text_input("Item to append", key="append_item")
            with col_app2:
                st.write("")
                append_btn = st.button("➕ Append", use_container_width=True)
            
            if append_btn and append_item:
                # Try to convert to number if possible
                try:
                    if '.' in append_item:
                        item_to_add = float(append_item)
                    else:
                        item_to_add = int(append_item)
                except:
                    if append_item == "True":
                        item_to_add = True
                    elif append_item == "False":
                        item_to_add = False
                    else:
                        item_to_add = append_item
                
                st.session_state.my_list.append(item_to_add)
                st.success(f"✅ Added '{item_to_add}' to end of list!")
                st.code(f"my_list.append({repr(item_to_add)})\n# Result: {st.session_state.my_list}", language="python")
                st.rerun()
        
        elif "insert" in add_method:
            st.info("""
            **`insert(index, item)`** - Adds an item at a **specific position**
            - All items after move right
            - List grows by 1
            """)
            
            col_ins1, col_ins2, col_ins3 = st.columns([2, 2, 1])
            with col_ins1:
                insert_index = st.number_input("Index position", min_value=0, max_value=len(st.session_state.my_list), value=0, key="insert_index")
            with col_ins2:
                insert_item = st.text_input("Item to insert", key="insert_item")
            with col_ins3:
                st.write("")
                insert_btn = st.button("➕ Insert", use_container_width=True)
            
            if insert_btn and insert_item:
                try:
                    if '.' in insert_item:
                        item_to_add = float(insert_item)
                    else:
                        item_to_add = int(insert_item)
                except:
                    if insert_item == "True":
                        item_to_add = True
                    elif insert_item == "False":
                        item_to_add = False
                    else:
                        item_to_add = insert_item
                
                st.session_state.my_list.insert(int(insert_index), item_to_add)
                st.success(f"✅ Inserted '{item_to_add}' at index {insert_index}!")
                st.code(f"my_list.insert({insert_index}, {repr(item_to_add)})\n# Result: {st.session_state.my_list}", language="python")
                st.rerun()
        
        elif "extend" in add_method:
            st.info("""
            **`extend(list)`** - Adds **multiple items** at once
            - Combines two lists
            - List grows by number of items added
            """)
            
            col_ext1, col_ext2 = st.columns([3, 1])
            with col_ext1:
                extend_items = st.text_input("Items to add (comma-separated)", placeholder="dog, cat, bird", key="extend_items")
            with col_ext2:
                st.write("")
                extend_btn = st.button("➕ Extend", use_container_width=True)
            
            if extend_btn and extend_items:
                items_to_add = [item.strip() for item in extend_items.split(",")]
                st.session_state.my_list.extend(items_to_add)
                st.success(f"✅ Added {len(items_to_add)} items to list!")
                st.code(f"my_list.extend({items_to_add})\n# Result: {st.session_state.my_list}", language="python")
                st.rerun()
    
    # ============================================
    # TAB 2: REMOVE ITEMS
    # ============================================
    with op_tabs[1]:
        st.markdown("### ❌ Remove Items from List")
        
        if len(st.session_state.my_list) == 0:
            st.warning("⚠️ List is empty! Add items first.")
        else:
            remove_method = st.radio("Choose method:", ["pop() - Remove by index", "remove() - Remove by value", "clear() - Remove all"], key="remove_method")
            
            if "pop" in remove_method:
                st.info("""
                **`pop(index)`** - Removes and **returns** item at index
                - Default: removes last item (if no index given)
                - Returns the removed item
                - List shrinks by 1
                """)
                
                col_pop1, col_pop2 = st.columns([3, 1])
                with col_pop1:
                    pop_index = st.number_input("Index to remove", min_value=0, max_value=len(st.session_state.my_list)-1, value=len(st.session_state.my_list)-1, key="pop_index")
                with col_pop2:
                    st.write("")
                    pop_btn = st.button("🗑️ Pop", use_container_width=True)
                
                if pop_btn:
                    popped_item = st.session_state.my_list.pop(int(pop_index))
                    st.success(f"✅ Removed '{popped_item}' from index {pop_index}!")
                    st.code(f"item = my_list.pop({pop_index})\nprint(item)  # {repr(popped_item)}\n# Result: {st.session_state.my_list}", language="python")
                    st.rerun()
            
            elif "remove" in remove_method:
                st.info("""
                **`remove(value)`** - Removes the **first occurrence** of a value
                - Searches for the value
                - Removes only the first match
                - Error if value not found
                """)
                
                col_rem1, col_rem2 = st.columns([3, 1])
                with col_rem1:
                    remove_value = st.selectbox("Value to remove", st.session_state.my_list, key="remove_value")
                with col_rem2:
                    st.write("")
                    remove_btn = st.button("🗑️ Remove", use_container_width=True)
                
                if remove_btn:
                    st.session_state.my_list.remove(remove_value)
                    st.success(f"✅ Removed '{remove_value}' from list!")
                    st.code(f"my_list.remove({repr(remove_value)})\n# Result: {st.session_state.my_list}", language="python")
                    st.rerun()
            
            elif "clear" in remove_method:
                st.warning("""
                **`clear()`** - Removes **ALL** items from the list
                - List becomes empty
                - Cannot be undone!
                """)
                
                clear_btn = st.button("🗑️ Clear All", type="primary")
                
                if clear_btn:
                    st.session_state.my_list.clear()
                    st.success("✅ Cleared all items from list!")
                    st.code(f"my_list.clear()\n# Result: {st.session_state.my_list}", language="python")
                    st.rerun()
    
    # ============================================
    # TAB 3: ACCESS ITEMS
    # ============================================
    with op_tabs[2]:
        st.markdown("### 🔍 Access Items in List")
        
        if len(st.session_state.my_list) == 0:
            st.warning("⚠️ List is empty! Add items first.")
        else:
            st.info("""
            **Indexing** - Access items by their position (index)
            - Indexes start at **0** (first item)
            - Negative indexes count from the end
            - `list[0]` gets first item
            - `list[-1]` gets last item
            """)
            
            # Show positive and negative indexes
            col_idx1, col_idx2 = st.columns(2)
            
            with col_idx1:
                st.markdown("#### Positive Indexes (from start)")
                for i, item in enumerate(st.session_state.my_list):
                    st.code(f"my_list[{i}] = {repr(item)}", language="python")
            
            with col_idx2:
                st.markdown("#### Negative Indexes (from end)")
                for i, item in enumerate(st.session_state.my_list):
                    neg_idx = i - len(st.session_state.my_list)
                    st.code(f"my_list[{neg_idx}] = {repr(item)}", language="python")
            
            st.markdown("---")
            st.markdown("#### 🎯 Try Accessing an Item")
            
            col_acc1, col_acc2 = st.columns([3, 1])
            with col_acc1:
                access_index = st.number_input("Index to access", min_value=-len(st.session_state.my_list), max_value=len(st.session_state.my_list)-1, value=0, key="access_index")
            with col_acc2:
                st.write("")
                access_btn = st.button("🔍 Access", use_container_width=True)
            
            if access_btn or access_index is not None:
                try:
                    accessed_item = st.session_state.my_list[int(access_index)]
                    st.success(f"✅ `my_list[{int(access_index)}]` = {repr(accessed_item)}")
                    st.code(f"item = my_list[{int(access_index)}]\nprint(item)  # {repr(accessed_item)}", language="python")
                except IndexError:
                    st.error(f"❌ Index {int(access_index)} is out of range!")
            
            # Slicing
            st.markdown("---")
            st.markdown("#### ✂️ List Slicing - Get Multiple Items")
            
            st.info("""
            **Slicing** - Get a portion of the list
            - `list[start:end]` - from start to end-1
            - `list[:3]` - first 3 items
            - `list[2:]` - from index 2 to end
            - `list[-3:]` - last 3 items
            """)
            
            col_slice1, col_slice2, col_slice3 = st.columns([2, 2, 1])
            with col_slice1:
                slice_start = st.number_input("Start index", min_value=0, max_value=len(st.session_state.my_list), value=0, key="slice_start")
            with col_slice2:
                slice_end = st.number_input("End index", min_value=0, max_value=len(st.session_state.my_list), value=len(st.session_state.my_list), key="slice_end")
            with col_slice3:
                st.write("")
                slice_btn = st.button("✂️ Slice", use_container_width=True)
            
            if slice_btn or (slice_start is not None and slice_end is not None):
                sliced = st.session_state.my_list[int(slice_start):int(slice_end)]
                st.success(f"✅ `my_list[{int(slice_start)}:{int(slice_end)}]` = {sliced}")
                st.code(f"sliced = my_list[{int(slice_start)}:{int(slice_end)}]\nprint(sliced)  # {sliced}", language="python")
    
    # ============================================
    # TAB 4: MODIFY ITEMS
    # ============================================
    with op_tabs[3]:
        st.markdown("### ✏️ Modify Items in List")
        
        if len(st.session_state.my_list) == 0:
            st.warning("⚠️ List is empty! Add items first.")
        else:
            st.info("""
            **Modify by Index** - Change the value at a specific position
            - Use assignment: `list[index] = new_value`
            - List stays same size
            """)
            
            col_mod1, col_mod2, col_mod3 = st.columns([2, 2, 1])
            with col_mod1:
                modify_index = st.number_input("Index to modify", min_value=0, max_value=len(st.session_state.my_list)-1, value=0, key="modify_index")
            with col_mod2:
                new_value = st.text_input("New value", key="new_value")
            with col_mod3:
                st.write("")
                modify_btn = st.button("✏️ Modify", use_container_width=True)
            
            if modify_btn and new_value:
                old_value = st.session_state.my_list[int(modify_index)]
                
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
                
                st.session_state.my_list[int(modify_index)] = converted_value
                st.success(f"✅ Changed index {int(modify_index)} from '{old_value}' to '{converted_value}'!")
                st.code(f"my_list[{int(modify_index)}] = {repr(converted_value)}\n# Result: {st.session_state.my_list}", language="python")
                st.rerun()
            
            # Show current values
            st.markdown("#### Current Values:")
            for i, item in enumerate(st.session_state.my_list):
                st.text(f"Index {i}: {repr(item)}")
    
    # ============================================
    # TAB 5: LIST METHODS
    # ============================================
    with op_tabs[4]:
        st.markdown("### 📊 Useful List Methods")
        
        if len(st.session_state.my_list) == 0:
            st.warning("⚠️ List is empty! Add items first to see methods in action.")
        
        col_meth1, col_meth2 = st.columns(2)
        
        with col_meth1:
            st.markdown("#### 📏 Information Methods")
            
            # Length
            st.code(f"len(my_list) = {len(st.session_state.my_list)}", language="python")
            st.caption("Number of items in list")
            
            # Count
            if st.session_state.my_list:
                count_value = st.selectbox("Count occurrences of:", list(set(st.session_state.my_list)), key="count_value")
                count = st.session_state.my_list.count(count_value)
                st.code(f"my_list.count({repr(count_value)}) = {count}", language="python")
                st.caption("How many times value appears")
            
            # Index
            if st.session_state.my_list:
                try:
                    index_value = st.selectbox("Find index of:", st.session_state.my_list, key="index_value")
                    idx = st.session_state.my_list.index(index_value)
                    st.code(f"my_list.index({repr(index_value)}) = {idx}", language="python")
                    st.caption("First index where value appears")
                except:
                    pass
        
        with col_meth2:
            st.markdown("#### 🔄 Modification Methods")
            
            # Reverse
            reverse_btn = st.button("🔄 Reverse List")
            if reverse_btn:
                st.session_state.my_list.reverse()
                st.success("✅ List reversed!")
                st.rerun()
            st.caption("Reverse the order of items")
            
            # Sort (only for comparable items)
            sort_btn = st.button("📊 Sort List")
            if sort_btn:
                try:
                    st.session_state.my_list.sort()
                    st.success("✅ List sorted!")
                    st.rerun()
                except:
                    st.error("❌ Cannot sort mixed types!")
            st.caption("Sort items in ascending order")
            
            # Copy
            if st.button("📋 Copy List"):
                copied = st.session_state.my_list.copy()
                st.success(f"✅ Created a copy: {copied}")
                st.code(f"new_list = my_list.copy()\nprint(new_list)  # {copied}", language="python")
            st.caption("Create an independent copy")
        
        st.markdown("---")
        
        # Check membership
        st.markdown("#### 🔍 Check if Item Exists")
        check_value = st.text_input("Check if value exists:", key="check_value")
        if check_value:
            # Try to convert
            try:
                if '.' in check_value:
                    check_val = float(check_value)
                else:
                    check_val = int(check_value)
            except:
                check_val = check_value
            
            exists = check_val in st.session_state.my_list
            if exists:
                st.success(f"✅ '{check_val}' is IN the list!")
            else:
                st.error(f"❌ '{check_val}' is NOT in the list!")
            
            st.code(f"{repr(check_val)} in my_list  # {exists}", language="python")
    
    # Reset button
    st.markdown("---")
    col_reset1, col_reset2 = st.columns([3, 1])
    with col_reset2:
        if st.button("🔄 Reset to Default", type="secondary"):
            st.session_state.my_list = ["apple", "banana", "orange"]
            st.rerun()
    
    # Key concepts
    st.markdown("---")
    st.markdown("### 🎯 Key Takeaways")
    
    col_key1, col_key2 = st.columns(2)
    
    with col_key1:
        st.info("""
        **Lists Basics:**
        - Store multiple items: `[1, 2, 3]`
        - Indexes start at 0
        - Use `[]` to access items
        - Lists are **mutable** (changeable)
        - Can contain mixed types
        """)
    
    with col_key2:
        st.success("""
        **Common Operations:**
        - `append()` - add to end
        - `pop()` - remove by index
        - `remove()` - remove by value
        - `len()` - get size
        - `in` - check if exists
        """)
    
    # Practice exercises
    with st.expander("💪 Practice Exercises", expanded=False):
        st.markdown("""
        **Try these fun challenges:**
        
        1. **My Favorite Things:**
        ```python
        # Create a list of your favorite things
        favorites = ["pizza", "games", "Python"]
        print("My first favorite:", favorites[0])
        print("My last favorite:", favorites[-1])
        print("Total favorites:", len(favorites))
        ```
        
        2. **Shopping List:**
        ```python
        # Start with some items
        shopping = ["milk", "eggs", "bread"]
        print("Original list:", shopping)
        
        # Add more items
        shopping.append("cheese")
        shopping.append("apples")
        print("After shopping:", shopping)
        ```
        
        3. **High Scores:**
        ```python
        # Keep track of game scores
        scores = [100, 250, 180, 320]
        print("All scores:", scores)
        print("Highest score:", max(scores))
        print("Lowest score:", min(scores))
        print("Total points:", sum(scores))
        ```
        
        4. **Remove Items:**
        ```python
        # Start with a to-do list
        tasks = ["homework", "clean room", "practice", "read"]
        print("To-do:", tasks)
        
        # Complete a task (remove it)
        tasks.remove("homework")
        print("After homework:", tasks)
        
        # Complete last task
        tasks.pop()
        print("After reading:", tasks)
        ```
        
        5. **Check if Item Exists:**
        ```python
        # See if something is in your list
        colors = ["red", "blue", "green", "yellow"]
        
        if "blue" in colors:
            print("We have blue!")
        
        if "purple" not in colors:
            print("We don't have purple")
        ```
        """)

