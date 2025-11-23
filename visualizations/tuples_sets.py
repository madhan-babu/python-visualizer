import streamlit as st

def show():
    st.markdown('<h2 style="color: #2196F3;">🎁 Tuples & Sets Explorer</h2>', unsafe_allow_html=True)
    st.write("Learn about two more important collection types in Python!")
    
    # Overview
    with st.expander("📚 What are Tuples and Sets?", expanded=False):
        st.markdown("""
        Python has several collection types. You've learned about **lists** and **dictionaries**. 
        Now let's explore **tuples** and **sets**!
        
        **Comparison Table:**
        
        | Feature | List | Tuple | Set |
        |---------|------|-------|-----|
        | **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` |
        | **Ordered** | ✅ Yes | ✅ Yes | ❌ No |
        | **Mutable** | ✅ Yes | ❌ No | ✅ Yes |
        | **Duplicates** | ✅ Allowed | ✅ Allowed | ❌ Not allowed |
        | **Indexing** | ✅ Yes | ✅ Yes | ❌ No |
        | **Use Case** | General purpose | Immutable data | Unique items |
        
        **When to use each:**
        - **List:** When you need to modify the collection
        - **Tuple:** When data shouldn't change (coordinates, RGB colors, dates)
        - **Set:** When you need unique items or fast membership testing
        """)
    
    # Create tabs
    tabs = st.tabs(["🎯 Tuples", "🎨 Sets", "⚖️ Comparison"])
    
    # ============================================
    # TAB 1: TUPLES
    # ============================================
    with tabs[0]:
        st.markdown("### 🎯 Tuples - Immutable Sequences")
        st.write("Like lists, but you can't change them!")
        
        st.info("""
        **Tuple characteristics:**
        - Created with parentheses `()`
        - Ordered (items have a fixed position)
        - Immutable (cannot be changed after creation)
        - Allow duplicate values
        - Can be indexed like lists
        
        **Why use tuples?**
        - Protect data from accidental changes
        - Faster than lists
        - Can be used as dictionary keys
        - Return multiple values from functions
        """)
        
        st.markdown("---")
        st.markdown("#### 🎮 Creating Tuples")
        
        col_create1, col_create2 = st.columns(2)
        
        with col_create1:
            st.code("""# Create tuples
empty = ()
single = (5,)      # Note the comma!
coordinates = (10, 20)
rgb = (255, 128, 0)
mixed = (1, "hello", True)""", language="python")
        
        with col_create2:
            st.warning("""
            **⚠️ Important:**
            - Single item tuple needs comma: `(5,)`
            - Without comma: `(5)` is just a number!
            - Parentheses optional: `1, 2, 3` is also a tuple
            """)
        
        st.markdown("---")
        st.markdown("#### 🔍 Try Tuples")
        
        tuple_input = st.text_input("Enter tuple items (comma-separated):", 
                                    value="10, 20, 30",
                                    key="tuple_input")
        
        if st.button("🎯 Create Tuple", key="create_tuple_btn"):
            try:
                # Parse input
                items = [item.strip() for item in tuple_input.split(",")]
                # Try to convert to numbers where possible
                parsed_items = []
                for item in items:
                    try:
                        if '.' in item:
                            parsed_items.append(float(item))
                        else:
                            parsed_items.append(int(item))
                    except:
                        parsed_items.append(item)
                
                my_tuple = tuple(parsed_items)
                
                st.code(f"my_tuple = {my_tuple}", language="python")
                
                # Visual representation
                st.markdown("#### 📊 Tuple Structure:")
                cols = st.columns(len(my_tuple))
                for i, item in enumerate(my_tuple):
                    with cols[i]:
                        st.markdown(f"""
                        <div style='
                            border: 2px solid #9C27B0;
                            border-radius: 10px;
                            padding: 15px;
                            text-align: center;
                            background-color: rgba(156, 39, 176, 0.1);
                        '>
                            <div style='font-size: 0.8rem; color: #666;'>Index: {i}</div>
                            <div style='font-size: 1.3rem; font-weight: bold; color: #9C27B0;'>{item}</div>
                            <div style='font-size: 0.7rem; color: #999;'>({type(item).__name__})</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                st.markdown("---")
                
                col_info1, col_info2, col_info3 = st.columns(3)
                with col_info1:
                    st.metric("Length", len(my_tuple))
                with col_info2:
                    st.metric("Type", "tuple")
                with col_info3:
                    st.metric("Mutable", "No ❌")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
        
        st.markdown("---")
        st.markdown("#### 📖 Tuple Operations")
        
        demo_tuple = (10, 20, 30, 40, 50)
        st.code(f"numbers = {demo_tuple}", language="python")
        
        col_op1, col_op2 = st.columns(2)
        
        with col_op1:
            st.markdown("**✅ What You CAN Do:**")
            
            if st.button("Access by index", key="tuple_access_btn"):
                st.code(f"numbers[0] = {demo_tuple[0]}\nnumbers[-1] = {demo_tuple[-1]}", language="python")
            
            if st.button("Slice", key="tuple_slice_btn"):
                st.code(f"numbers[1:3] = {demo_tuple[1:3]}", language="python")
            
            if st.button("Count occurrences", key="tuple_count_btn"):
                st.code(f"numbers.count(20) = {demo_tuple.count(20)}", language="python")
            
            if st.button("Find index", key="tuple_index_btn"):
                st.code(f"numbers.index(30) = {demo_tuple.index(30)}", language="python")
            
            if st.button("Check membership", key="tuple_in_btn"):
                st.code(f"20 in numbers = {20 in demo_tuple}", language="python")
        
        with col_op2:
            st.markdown("**❌ What You CANNOT Do:**")
            
            st.error("""
            ```python
            numbers[0] = 99
            # ❌ Error: tuples are immutable!
            
            numbers.append(60)
            # ❌ Error: no append method!
            
            numbers.remove(20)
            # ❌ Error: no remove method!
            
            del numbers[0]
            # ❌ Error: cannot delete items!
            ```
            """)
        
        st.markdown("---")
        st.markdown("#### 🔄 Tuple Packing & Unpacking")
        
        st.info("""
        **Tuple Packing** - Create tuple without parentheses:
        ```python
        coordinates = 10, 20, 30  # This is a tuple!
        ```
        
        **Tuple Unpacking** - Assign tuple items to variables:
        ```python
        x, y, z = coordinates
        # x=10, y=20, z=30
        ```
        """)
        
        col_unpack1, col_unpack2, col_unpack3 = st.columns(3)
        
        with col_unpack1:
            unpack_x = st.number_input("X:", value=100, key="unpack_x")
        with col_unpack2:
            unpack_y = st.number_input("Y:", value=200, key="unpack_y")
        with col_unpack3:
            unpack_z = st.number_input("Z:", value=300, key="unpack_z")
        
        if st.button("📦 Pack & Unpack", key="pack_unpack_btn"):
            point = (unpack_x, unpack_y, unpack_z)
            st.code(f"""# Packing
point = {unpack_x}, {unpack_y}, {unpack_z}
print(point)  # {point}

# Unpacking
x, y, z = point
print(f"X={{x}}, Y={{y}}, Z={{z}}")
# X={unpack_x}, Y={unpack_y}, Z={unpack_z}""", language="python")
            
            st.success(f"✅ Packed: {point}")
            st.info(f"✅ Unpacked: X={unpack_x}, Y={unpack_y}, Z={unpack_z}")
        
        st.markdown("---")
        st.markdown("#### 🎯 Real-World Examples")
        
        example_choice = st.radio("Choose example:", 
                                 ["Coordinates", "RGB Color", "Date (Year, Month, Day)", "Multiple Return Values"],
                                 key="tuple_example")
        
        if example_choice == "Coordinates":
            st.code("""# Store position that shouldn't change
player_spawn = (0, 0)
checkpoint_1 = (100, 50)
checkpoint_2 = (200, 75)

# Access
x, y = player_spawn
print(f"Start at ({x}, {y})")""", language="python")
        
        elif example_choice == "RGB Color":
            st.code("""# Store RGB values
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)

# Use in function
def display_color(rgb):
    r, g, b = rgb
    print(f"RGB({r}, {g}, {b})")

display_color(purple)  # RGB(128, 0, 128)""", language="python")
        
        elif example_choice == "Date (Year, Month, Day)":
            st.code("""# Store dates
birthday = (2008, 5, 15)  # May 15, 2008
today = (2024, 11, 23)

# Unpack
year, month, day = birthday
print(f"Born in {year}")""", language="python")
        
        else:  # Multiple Return Values
            st.code("""# Function returns multiple values as tuple
def get_min_max(numbers):
    return min(numbers), max(numbers)

scores = [85, 92, 78, 95, 88]
minimum, maximum = get_min_max(scores)

print(f"Min: {minimum}, Max: {maximum}")
# Min: 78, Max: 95""", language="python")
    
    # ============================================
    # TAB 2: SETS
    # ============================================
    with tabs[1]:
        st.markdown("### 🎨 Sets - Unique Collections")
        st.write("Unordered collections of unique items")
        
        st.info("""
        **Set characteristics:**
        - Created with curly braces `{}` or `set()`
        - Unordered (no indexing!)
        - Mutable (can add/remove items)
        - No duplicate values (automatically removed)
        - Fast membership testing
        
        **Why use sets?**
        - Remove duplicates from a list
        - Fast lookup: "is this item in the collection?"
        - Mathematical set operations (union, intersection, difference)
        - Unique items only
        """)
        
        st.markdown("---")
        st.markdown("#### 🎮 Creating Sets")
        
        col_set1, col_set2 = st.columns(2)
        
        with col_set1:
            st.code("""# Create sets
empty = set()         # Not {}, that's a dict!
numbers = {1, 2, 3, 4}
colors = {"red", "blue", "green"}
mixed = {1, "hello", 3.14}

# From list (removes duplicates)
my_list = [1, 2, 2, 3, 3, 3]
my_set = set(my_list)
print(my_set)  # {1, 2, 3}""", language="python")
        
        with col_set2:
            st.warning("""
            **⚠️ Important:**
            - Empty set: `set()` not `{}`
            - `{}` creates an empty dictionary!
            - Sets automatically remove duplicates
            - Order is not guaranteed
            - Cannot contain mutable items (lists, dicts)
            """)
        
        st.markdown("---")
        st.markdown("#### 🔍 Try Sets - See Duplicates Removed!")
        
        set_input = st.text_input("Enter items (comma-separated, duplicates OK):", 
                                  value="apple, banana, apple, orange, banana, apple",
                                  key="set_input")
        
        if st.button("🎨 Create Set", key="create_set_btn"):
            try:
                items = [item.strip() for item in set_input.split(",")]
                my_set = set(items)
                
                st.markdown("#### 📊 Before (List with duplicates):")
                st.code(f"items = {items}", language="python")
                st.info(f"Count: {len(items)} items (including duplicates)")
                
                st.markdown("#### ✨ After (Set with unique items only):")
                st.code(f"my_set = set(items)\n# {my_set}", language="python")
                st.success(f"Count: {len(my_set)} unique items")
                
                # Visual representation
                st.markdown("#### 🎨 Set Contents:")
                cols = st.columns(min(len(my_set), 6))  # Max 6 columns
                for i, item in enumerate(my_set):
                    if i < 6:  # Show first 6 items
                        with cols[i]:
                            st.markdown(f"""
                            <div style='
                                border: 2px solid #FF5722;
                                border-radius: 50%;
                                padding: 20px;
                                text-align: center;
                                background-color: rgba(255, 87, 34, 0.1);
                                min-height: 80px;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                            '>
                                <div style='font-size: 1.1rem; font-weight: bold; color: #FF5722;'>{item}</div>
                            </div>
                            """, unsafe_allow_html=True)
                
                if len(my_set) > 6:
                    st.caption(f"... and {len(my_set) - 6} more items")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
        
        st.markdown("---")
        st.markdown("#### 🔧 Set Operations")
        
        demo_set = {"apple", "banana", "orange"}
        st.code(f"fruits = {demo_set}", language="python")
        
        col_setop1, col_setop2 = st.columns(2)
        
        with col_setop1:
            st.markdown("**➕ Adding Items:**")
            
            add_item = st.text_input("Item to add:", value="mango", key="set_add_item")
            if st.button("Add", key="set_add_btn"):
                new_set = demo_set.copy()
                new_set.add(add_item)
                st.code(f"fruits.add('{add_item}')\nprint(fruits)  # {new_set}", language="python")
                st.success(f"✅ Added! New set: {new_set}")
        
        with col_setop2:
            st.markdown("**❌ Removing Items:**")
            
            remove_item = st.selectbox("Item to remove:", list(demo_set), key="set_remove_item")
            if st.button("Remove", key="set_remove_btn"):
                new_set = demo_set.copy()
                new_set.remove(remove_item)
                st.code(f"fruits.remove('{remove_item}')\nprint(fruits)  # {new_set}", language="python")
                st.success(f"✅ Removed! New set: {new_set}")
        
        st.markdown("---")
        st.markdown("#### 🔍 Membership Testing (Very Fast!)")
        
        check_item = st.text_input("Check if item exists:", value="banana", key="set_check")
        if st.button("🔍 Check", key="set_check_btn"):
            exists = check_item in demo_set
            st.code(f"'{check_item}' in fruits  # {exists}", language="python")
            if exists:
                st.success(f"✅ '{check_item}' IS in the set!")
            else:
                st.error(f"❌ '{check_item}' is NOT in the set!")
        
        st.markdown("---")
        st.markdown("#### 🎯 Set Math Operations")
        
        st.info("""
        **Mathematical set operations:**
        - **Union (`|`):** Items in either set
        - **Intersection (`&`):** Items in both sets
        - **Difference (`-`):** Items in first but not second
        - **Symmetric Difference (`^`):** Items in either but not both
        """)
        
        set1_input = st.text_input("Set 1 (comma-separated):", value="1, 2, 3, 4", key="set1_math")
        set2_input = st.text_input("Set 2 (comma-separated):", value="3, 4, 5, 6", key="set2_math")
        
        if st.button("🧮 Calculate Set Operations", key="set_math_btn"):
            try:
                set1 = set([item.strip() for item in set1_input.split(",")])
                set2 = set([item.strip() for item in set2_input.split(",")])
                
                st.code(f"set1 = {set1}\nset2 = {set2}", language="python")
                
                col_math1, col_math2 = st.columns(2)
                
                with col_math1:
                    # Union
                    union = set1 | set2
                    st.markdown("**🔗 Union (|)** - All items from both")
                    st.code(f"set1 | set2 = {union}", language="python")
                    st.success(f"Result: {union}")
                    
                    st.markdown("")
                    
                    # Difference
                    diff = set1 - set2
                    st.markdown("**➖ Difference (-)** - In set1 but not set2")
                    st.code(f"set1 - set2 = {diff}", language="python")
                    st.info(f"Result: {diff}")
                
                with col_math2:
                    # Intersection
                    inter = set1 & set2
                    st.markdown("**🎯 Intersection (&)** - Common items")
                    st.code(f"set1 & set2 = {inter}", language="python")
                    st.warning(f"Result: {inter}")
                    
                    st.markdown("")
                    
                    # Symmetric Difference
                    sym_diff = set1 ^ set2
                    st.markdown("**⚡ Symmetric Diff (^)** - In either but not both")
                    st.code(f"set1 ^ set2 = {sym_diff}", language="python")
                    st.error(f"Result: {sym_diff}")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
        
        st.markdown("---")
        st.markdown("#### 💡 Real-World Set Examples")
        
        set_example = st.radio("Choose example:", 
                              ["Remove Duplicates", "Find Common Items", "Find Unique Items"],
                              key="set_example")
        
        if set_example == "Remove Duplicates":
            st.code("""# Remove duplicate scores
scores = [85, 92, 85, 78, 92, 95, 78, 88]
unique_scores = list(set(scores))
print(f"Original: {len(scores)} scores")
print(f"Unique: {len(unique_scores)} scores")
print(unique_scores)""", language="python")
        
        elif set_example == "Find Common Items":
            st.code("""# Find common interests
alice_hobbies = {"reading", "gaming", "music", "sports"}
bob_hobbies = {"gaming", "cooking", "music", "movies"}

common = alice_hobbies & bob_hobbies
print(f"Common interests: {common}")
# Common interests: {'gaming', 'music'}""", language="python")
        
        else:  # Find Unique Items
            st.code("""# Find items only in one list
class_a = {"Alice", "Bob", "Charlie", "David"}
class_b = {"Charlie", "David", "Eve", "Frank"}

only_a = class_a - class_b
only_b = class_b - class_a

print(f"Only in Class A: {only_a}")
print(f"Only in Class B: {only_b}")
# Only in Class A: {'Alice', 'Bob'}
# Only in Class B: {'Eve', 'Frank'}""", language="python")
    
    # ============================================
    # TAB 3: COMPARISON
    # ============================================
    with tabs[2]:
        st.markdown("### ⚖️ Lists vs Tuples vs Sets")
        st.write("Which one should you use?")
        
        st.markdown("#### 📊 Feature Comparison")
        
        comparison_data = {
            "Feature": ["Syntax", "Ordered", "Mutable", "Duplicates", "Indexing", "Methods", "Speed", "Use Case"],
            "List": ["`[1, 2, 3]`", "✅ Yes", "✅ Yes", "✅ Allowed", "✅ Yes", "Many (append, insert, etc.)", "⚡ Medium", "General purpose"],
            "Tuple": ["`(1, 2, 3)`", "✅ Yes", "❌ No", "✅ Allowed", "✅ Yes", "Few (count, index)", "⚡⚡ Fast", "Immutable data"],
            "Set": ["`{1, 2, 3}`", "❌ No", "✅ Yes", "❌ Not allowed", "❌ No", "Some (add, remove, math ops)", "⚡⚡⚡ Very Fast", "Unique items"]
        }
        
        for i in range(len(comparison_data["Feature"])):
            col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
            with col1:
                st.markdown(f"**{comparison_data['Feature'][i]}**")
            with col2:
                st.info(comparison_data['List'][i])
            with col3:
                st.warning(comparison_data['Tuple'][i])
            with col4:
                st.success(comparison_data['Set'][i])
        
        st.markdown("---")
        st.markdown("#### 🎯 When to Use Each?")
        
        col_when1, col_when2, col_when3 = st.columns(3)
        
        with col_when1:
            st.markdown("### 📚 Use List When:")
            st.info("""
            - Need to modify items
            - Order matters
            - Duplicates are OK
            - Need indexing
            - General collection
            
            **Examples:**
            - Todo items
            - Shopping cart
            - Student names
            - Game inventory
            """)
        
        with col_when2:
            st.markdown("### 🎯 Use Tuple When:")
            st.warning("""
            - Data shouldn't change
            - Return multiple values
            - Use as dict key
            - Faster than list
            - Protect from errors
            
            **Examples:**
            - Coordinates (x, y)
            - RGB colors
            - Date (year, month, day)
            - Database records
            """)
        
        with col_when3:
            st.markdown("### 🎨 Use Set When:")
            st.success("""
            - Need unique items only
            - Fast lookup needed
            - Mathematical operations
            - Remove duplicates
            - Order doesn't matter
            
            **Examples:**
            - Unique tags
            - Visited pages
            - Common interests
            - Valid options
            """)
        
        st.markdown("---")
        st.markdown("#### 🧪 Interactive Comparison")
        
        comp_input = st.text_input("Enter items (with duplicates):", 
                                   value="apple, banana, apple, cherry, banana",
                                   key="comp_input")
        
        if st.button("🔄 Convert to All Three", key="convert_all_btn"):
            items = [item.strip() for item in comp_input.split(",")]
            
            col_comp1, col_comp2, col_comp3 = st.columns(3)
            
            with col_comp1:
                st.markdown("### 📚 List")
                my_list = items
                st.code(f"list = {my_list}", language="python")
                st.info(f"Length: {len(my_list)}")
                st.info(f"Ordered: ✅")
                st.info(f"Mutable: ✅")
                st.info(f"Duplicates: ✅")
            
            with col_comp2:
                st.markdown("### 🎯 Tuple")
                my_tuple = tuple(items)
                st.code(f"tuple = {my_tuple}", language="python")
                st.warning(f"Length: {len(my_tuple)}")
                st.warning(f"Ordered: ✅")
                st.warning(f"Mutable: ❌")
                st.warning(f"Duplicates: ✅")
            
            with col_comp3:
                st.markdown("### 🎨 Set")
                my_set = set(items)
                st.code(f"set = {my_set}", language="python")
                st.success(f"Length: {len(my_set)}")
                st.success(f"Ordered: ❌")
                st.success(f"Mutable: ✅")
                st.success(f"Duplicates: ❌")
    
    # Key takeaways
    st.markdown("---")
    st.markdown("### 🎯 Key Takeaways")
    
    col_key1, col_key2 = st.columns(2)
    
    with col_key1:
        st.info("""
        **Tuples:**
        - Use `()` to create
        - Immutable (cannot change)
        - Ordered (can index)
        - Great for data that shouldn't change
        - Tuple unpacking: `x, y = (1, 2)`
        """)
    
    with col_key2:
        st.success("""
        **Sets:**
        - Use `{}` or `set()` to create
        - Mutable (can add/remove)
        - Unordered (cannot index)
        - Automatically removes duplicates
        - Fast membership testing
        - Set operations: `|`, `&`, `-`, `^`
        """)
    
    # Practice exercises
    with st.expander("💪 Practice Exercises", expanded=False):
        st.markdown("""
        **Try these challenges:**
        
        1. **Tuple Unpacking:**
        ```python
        # Swap two variables using tuples
        a = 10
        b = 20
        a, b = b, a
        print(a, b)  # 20 10
        ```
        
        2. **Remove Duplicates:**
        ```python
        numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        unique = list(set(numbers))
        print(unique)  # [1, 2, 3, 4]
        ```
        
        3. **Find Common Elements:**
        ```python
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        common = set(list1) & set(list2)
        print(common)  # {4, 5}
        ```
        
        4. **Return Multiple Values:**
        ```python
        def get_stats(numbers):
            return min(numbers), max(numbers), sum(numbers)
        
        scores = [85, 92, 78, 95]
        min_score, max_score, total = get_stats(scores)
        print(f"Min: {min_score}, Max: {max_score}, Total: {total}")
        ```
        
        5. **Set Operations:**
        ```python
        students_python = {"Alice", "Bob", "Charlie"}
        students_java = {"Bob", "Charlie", "David"}
        
        both = students_python & students_java
        only_python = students_python - students_java
        either = students_python | students_java
        
        print(f"Both: {both}")
        print(f"Only Python: {only_python}")
        print(f"Either: {either}")
        ```
        
        **Challenge:** Create a program that:
        - Takes two lists of numbers
        - Finds items in both lists (intersection)
        - Finds items only in first list (difference)
        - Finds all unique items combined (union)
        - Removes all duplicates from each list
        """)

