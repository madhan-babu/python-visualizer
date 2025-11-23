import streamlit as st

def show():
    st.markdown('<h2 style="color: #2196F3;">📝 Python Strings Explorer</h2>', unsafe_allow_html=True)
    st.write("Master string manipulation - one of Python's most powerful features!")
    
    # Overview
    with st.expander("📚 What are Strings?", expanded=False):
        st.markdown("""
        **Strings** are sequences of characters - text data in Python.
        
        Think of strings like:
        - 📖 A sentence in a book
        - 💬 A text message
        - 🏷️ A label or name
        - 📧 An email address
        
        **Creating strings:**
        ```python
        name = "Alice"          # Double quotes
        message = 'Hello!'      # Single quotes
        text = '''Multiple
        lines'''                # Triple quotes for multi-line
        ```
        
        **Why are strings important?**
        - Store names, messages, and text
        - Display information to users
        - Process text data (files, web pages, etc.)
        - One of the most commonly used data types
        """)
    
    # Create tabs for different string concepts
    str_tabs = st.tabs(["✨ Creating Strings", "🔍 Accessing Characters", "✂️ Slicing", "🔧 Methods", "➕ Concatenation", "🎨 Formatting"])
    
    # ============================================
    # TAB 1: CREATING STRINGS
    # ============================================
    with str_tabs[0]:
        st.markdown("### ✨ Creating Strings")
        st.write("Different ways to create strings in Python")
        
        st.info("""
        **Three ways to create strings:**
        
        1. **Single quotes:** `'Hello'`
        2. **Double quotes:** `"Hello"`
        3. **Triple quotes:** `'''Hello'''` or `\"\"\"Hello\"\"\"`
        
        **All three work the same way!** Use what's convenient.
        """)
        
        st.markdown("---")
        st.markdown("#### 🎮 Try Creating Strings")
        
        quote_type = st.radio("Choose quote type:", 
                             ["Single quotes (')", "Double quotes (\")", "Triple quotes (''')"],
                             horizontal=True,
                             key="quote_type")
        
        string_input = st.text_area("Enter your text:", value="Hello, World!", key="create_string_input")
        
        if st.button("✨ Create String", key="create_str_btn"):
            if "Single" in quote_type:
                display = f"'{string_input}'"
                code = f"text = '{string_input}'"
            elif "Double" in quote_type:
                display = f'"{string_input}"'
                code = f'text = "{string_input}"'
            else:
                display = f"'''{string_input}'''"
                code = f"text = '''{string_input}'''"
            
            st.code(code, language="python")
            st.success(f"✅ Created string: {display}")
            st.info(f"Length: {len(string_input)} characters")
        
        st.markdown("---")
        st.markdown("#### 💡 When to Use Each Type")
        
        col_use1, col_use2, col_use3 = st.columns(3)
        
        with col_use1:
            st.markdown("**Single Quotes**")
            st.code("'It\\'s Python!'", language="python")
            st.caption("Good for strings with double quotes inside")
        
        with col_use2:
            st.markdown("**Double Quotes**")
            st.code("\"He said 'Hi'\"", language="python")
            st.caption("Good for strings with single quotes inside")
        
        with col_use3:
            st.markdown("**Triple Quotes**")
            st.code('"""Line 1\nLine 2\nLine 3"""', language="python")
            st.caption("Good for multi-line strings")
        
        st.markdown("---")
        st.markdown("#### 🔤 Special Characters (Escape Sequences)")
        
        st.info("""
        **Common escape sequences:**
        - `\\n` - New line
        - `\\t` - Tab
        - `\\'` - Single quote
        - `\\"` - Double quote
        - `\\\\` - Backslash
        
        Example: `"Hello\\nWorld"` displays as:
        ```
        Hello
        World
        ```
        """)
        
        escape_demo = st.text_input("Try escape sequences:", value="Hello\\nWorld\\t!", key="escape_demo")
        if st.button("👀 Preview", key="preview_escape"):
            st.code(f'text = "{escape_demo}"', language="python")
            st.markdown("**Output:**")
            st.text(escape_demo)
    
    # ============================================
    # TAB 2: ACCESSING CHARACTERS
    # ============================================
    with str_tabs[1]:
        st.markdown("### 🔍 Accessing Characters")
        st.write("Strings are sequences - you can access individual characters!")
        
        st.info("""
        **Indexing** - Access characters by position
        - Indexes start at 0 (first character)
        - Negative indexes count from the end
        - `string[0]` - first character
        - `string[-1]` - last character
        
        Example: `"Python"[0]` → `"P"`
        """)
        
        st.markdown("---")
        
        text_for_index = st.text_input("Enter text:", value="Python", key="text_for_index")
        
        if text_for_index:
            # Show all characters with indexes
            st.markdown("#### 📊 Character Index Map")
            
            # Positive indexes
            st.markdown("**Positive indexes (from start):**")
            cols_pos = st.columns(len(text_for_index))
            for i, char in enumerate(text_for_index):
                with cols_pos[i]:
                    st.markdown(f"""
                    <div style='
                        border: 2px solid #4CAF50;
                        border-radius: 5px;
                        padding: 10px;
                        text-align: center;
                        background-color: rgba(76, 175, 80, 0.1);
                    '>
                        <div style='font-size: 0.8rem; color: #666;'>Index: {i}</div>
                        <div style='font-size: 1.5rem; font-weight: bold;'>{char}</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("")
            
            # Negative indexes
            st.markdown("**Negative indexes (from end):**")
            cols_neg = st.columns(len(text_for_index))
            for i, char in enumerate(text_for_index):
                neg_idx = i - len(text_for_index)
                with cols_neg[i]:
                    st.markdown(f"""
                    <div style='
                        border: 2px solid #FF9800;
                        border-radius: 5px;
                        padding: 10px;
                        text-align: center;
                        background-color: rgba(255, 152, 0, 0.1);
                    '>
                        <div style='font-size: 0.8rem; color: #666;'>Index: {neg_idx}</div>
                        <div style='font-size: 1.5rem; font-weight: bold;'>{char}</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("---")
            st.markdown("#### 🎯 Try Accessing a Character")
            
            col_acc1, col_acc2 = st.columns([3, 1])
            
            with col_acc1:
                index_input = st.number_input("Enter index:", 
                                             min_value=-len(text_for_index), 
                                             max_value=len(text_for_index)-1,
                                             value=0,
                                             key="index_access")
            
            with col_acc2:
                st.write("")
                st.write("")
                access_btn = st.button("🔍 Access", use_container_width=True, key="access_char_btn")
            
            if access_btn or index_input is not None:
                try:
                    char = text_for_index[int(index_input)]
                    st.success(f'✅ `"{text_for_index}"[{int(index_input)}]` = `"{char}"`')
                    st.code(f'text = "{text_for_index}"\nchar = text[{int(index_input)}]\nprint(char)  # "{char}"', language="python")
                except IndexError:
                    st.error(f"❌ Index {int(index_input)} is out of range!")
    
    # ============================================
    # TAB 3: SLICING
    # ============================================
    with str_tabs[2]:
        st.markdown("### ✂️ String Slicing")
        st.write("Get a portion of a string using slices")
        
        st.info("""
        **Slicing syntax:** `string[start:end:step]`
        - `start` - beginning index (inclusive)
        - `end` - ending index (exclusive)
        - `step` - jump/stride (optional, default=1)
        
        **Examples:**
        - `"Python"[0:3]` → `"Pyt"`
        - `"Python"[2:]` → `"thon"`
        - `"Python"[:4]` → `"Pyth"`
        - `"Python"[::2]` → `"Pto"` (every 2nd character)
        - `"Python"[::-1]` → `"nohtyP"` (reverse!)
        """)
        
        st.markdown("---")
        
        slice_text = st.text_input("Enter text to slice:", value="Programming", key="slice_text")
        
        if slice_text:
            st.markdown("#### 🎮 Interactive String Slicer")
            
            col_slice1, col_slice2, col_slice3 = st.columns(3)
            
            with col_slice1:
                start_idx = st.number_input("Start index:", 
                                           min_value=0, 
                                           max_value=len(slice_text),
                                           value=0,
                                           key="start_slice")
            
            with col_slice2:
                end_idx = st.number_input("End index:", 
                                         min_value=0, 
                                         max_value=len(slice_text),
                                         value=len(slice_text),
                                         key="end_slice")
            
            with col_slice3:
                step_val = st.number_input("Step:", 
                                          min_value=1, 
                                          max_value=5,
                                          value=1,
                                          key="step_slice")
            
            if st.button("✂️ Slice String", key="slice_btn"):
                try:
                    result = slice_text[int(start_idx):int(end_idx):int(step_val)]
                    
                    st.code(f'text = "{slice_text}"\nsliced = text[{int(start_idx)}:{int(end_idx)}:{int(step_val)}]\nprint(sliced)  # "{result}"', language="python")
                    
                    st.success(f'✅ Result: "{result}"')
                    st.info(f"Length: {len(result)} characters")
                    
                    # Visual representation
                    st.markdown("#### 📊 Visual Representation:")
                    cols = st.columns(len(slice_text))
                    for i, char in enumerate(slice_text):
                        with cols[i]:
                            if i >= start_idx and i < end_idx and (i - start_idx) % step_val == 0:
                                # This character is included
                                st.markdown(f"""
                                <div style='
                                    border: 3px solid #4CAF50;
                                    border-radius: 5px;
                                    padding: 8px;
                                    text-align: center;
                                    background-color: rgba(76, 175, 80, 0.3);
                                '>
                                    <div style='font-size: 0.7rem;'>{i}</div>
                                    <div style='font-size: 1.2rem; font-weight: bold;'>{char}</div>
                                    <div style='color: green; font-size: 0.8rem;'>✓</div>
                                </div>
                                """, unsafe_allow_html=True)
                            else:
                                # This character is not included
                                st.markdown(f"""
                                <div style='
                                    border: 1px solid #ddd;
                                    border-radius: 5px;
                                    padding: 8px;
                                    text-align: center;
                                    background-color: rgba(0, 0, 0, 0.05);
                                    opacity: 0.4;
                                '>
                                    <div style='font-size: 0.7rem;'>{i}</div>
                                    <div style='font-size: 1.2rem;'>{char}</div>
                                    <div style='color: #999; font-size: 0.8rem;'>✗</div>
                                </div>
                                """, unsafe_allow_html=True)
                
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
            
            st.markdown("---")
            st.markdown("#### 🎯 Quick Slice Patterns")
            
            col_pat1, col_pat2 = st.columns(2)
            
            with col_pat1:
                if st.button(f"🔄 Reverse: {slice_text[::-1]}", key="reverse_btn", use_container_width=True):
                    st.code(f'"{slice_text}"[::-1] = "{slice_text[::-1]}"', language="python")
            
            with col_pat2:
                if st.button(f"📍 First 3: {slice_text[:3]}", key="first3_btn", use_container_width=True):
                    st.code(f'"{slice_text}"[:3] = "{slice_text[:3]}"', language="python")
            
            col_pat3, col_pat4 = st.columns(2)
            
            with col_pat3:
                if st.button(f"📍 Last 3: {slice_text[-3:]}", key="last3_btn", use_container_width=True):
                    st.code(f'"{slice_text}"[-3:] = "{slice_text[-3:]}"', language="python")
            
            with col_pat4:
                if st.button(f"🎲 Every 2nd: {slice_text[::2]}", key="every2_btn", use_container_width=True):
                    st.code(f'"{slice_text}"[::2] = "{slice_text[::2]}"', language="python")
    
    # ============================================
    # TAB 4: STRING METHODS
    # ============================================
    with str_tabs[3]:
        st.markdown("### 🔧 String Methods")
        st.write("Powerful built-in methods to manipulate strings")
        
        st.info("""
        **Common string methods:**
        - `upper()` - Convert to uppercase
        - `lower()` - Convert to lowercase
        - `capitalize()` - First letter uppercase
        - `title()` - Capitalize Each Word
        - `strip()` - Remove whitespace from ends
        - `replace()` - Replace substring
        - `split()` - Split into list
        - `startswith()` / `endswith()` - Check beginning/end
        - `find()` / `count()` - Search and count
        """)
        
        st.markdown("---")
        
        method_text = st.text_input("Enter text for methods:", value="  hello world  ", key="method_text")
        
        st.markdown("#### 🎨 Case Methods")
        
        col_case1, col_case2, col_case3, col_case4 = st.columns(4)
        
        with col_case1:
            if st.button("🔤 upper()", key="upper_btn"):
                result = method_text.upper()
                st.code(f'"{method_text}".upper()\n# "{result}"', language="python")
                st.success(f'"{result}"')
        
        with col_case2:
            if st.button("🔡 lower()", key="lower_btn"):
                result = method_text.lower()
                st.code(f'"{method_text}".lower()\n# "{result}"', language="python")
                st.success(f'"{result}"')
        
        with col_case3:
            if st.button("Ⓐ capitalize()", key="cap_btn"):
                result = method_text.capitalize()
                st.code(f'"{method_text}".capitalize()\n# "{result}"', language="python")
                st.success(f'"{result}"')
        
        with col_case4:
            if st.button("🎩 title()", key="title_btn"):
                result = method_text.title()
                st.code(f'"{method_text}".title()\n# "{result}"', language="python")
                st.success(f'"{result}"')
        
        st.markdown("---")
        st.markdown("#### ✂️ Trimming & Replacement")
        
        col_trim1, col_trim2 = st.columns(2)
        
        with col_trim1:
            if st.button("🧹 strip() - Remove spaces", key="strip_btn"):
                result = method_text.strip()
                st.code(f'"{method_text}".strip()\n# "{result}"', language="python")
                st.info(f'Original length: {len(method_text)}\nAfter strip: {len(result)}')
                st.success(f'"{result}"')
        
        with col_trim2:
            old_word = st.text_input("Replace:", value="world", key="replace_old")
            new_word = st.text_input("With:", value="Python", key="replace_new")
            if st.button("🔄 replace()", key="replace_btn"):
                result = method_text.replace(old_word, new_word)
                st.code(f'"{method_text}".replace("{old_word}", "{new_word}")\n# "{result}"', language="python")
                st.success(f'"{result}"')
        
        st.markdown("---")
        st.markdown("#### 🔍 Searching & Checking")
        
        search_text = st.text_input("Text to search/check:", value="Python Programming", key="search_text")
        
        col_search1, col_search2 = st.columns(2)
        
        with col_search1:
            find_word = st.text_input("Find word:", value="Pro", key="find_word")
            if st.button("🔎 find()", key="find_btn"):
                index = search_text.find(find_word)
                if index != -1:
                    st.success(f'✅ Found at index {index}')
                else:
                    st.error(f'❌ Not found (returns -1)')
                st.code(f'"{search_text}".find("{find_word}")\n# {index}', language="python")
        
        with col_search2:
            count_char = st.text_input("Count character:", value="a", key="count_char")
            if st.button("🔢 count()", key="count_btn"):
                count = search_text.count(count_char)
                st.info(f'Found {count} times')
                st.code(f'"{search_text}".count("{count_char}")\n# {count}', language="python")
        
        st.markdown("---")
        st.markdown("#### ✅ Boolean Methods (True/False)")
        
        check_text = st.text_input("Text to check:", value="Hello123", key="check_text")
        
        col_bool1, col_bool2, col_bool3 = st.columns(3)
        
        with col_bool1:
            if st.button("🔤 isalpha()", key="isalpha_btn"):
                result = check_text.isalpha()
                st.code(f'"{check_text}".isalpha()\n# {result}', language="python")
                if result:
                    st.success("✅ All letters")
                else:
                    st.error("❌ Has non-letters")
        
        with col_bool2:
            if st.button("🔢 isdigit()", key="isdigit_btn"):
                result = check_text.isdigit()
                st.code(f'"{check_text}".isdigit()\n# {result}', language="python")
                if result:
                    st.success("✅ All digits")
                else:
                    st.error("❌ Has non-digits")
        
        with col_bool3:
            if st.button("🔤🔢 isalnum()", key="isalnum_btn"):
                result = check_text.isalnum()
                st.code(f'"{check_text}".isalnum()\n# {result}', language="python")
                if result:
                    st.success("✅ Letters & digits only")
                else:
                    st.error("❌ Has special chars")
    
    # ============================================
    # TAB 5: CONCATENATION
    # ============================================
    with str_tabs[4]:
        st.markdown("### ➕ String Concatenation")
        st.write("Combine strings together")
        
        st.info("""
        **Three ways to combine strings:**
        
        1. **`+` operator:** `"Hello" + " " + "World"`
        2. **Repetition `*`:** `"Hi! " * 3`
        3. **`.join()` method:** `" ".join(["Hello", "World"])`
        """)
        
        st.markdown("---")
        st.markdown("#### ➕ Using + Operator")
        
        col_concat1, col_concat2, col_concat3 = st.columns([2, 1, 2])
        
        with col_concat1:
            str1 = st.text_input("First string:", value="Hello", key="concat_str1")
        
        with col_concat2:
            st.write("")
            st.write("")
            st.markdown("### `+`")
        
        with col_concat3:
            str2 = st.text_input("Second string:", value="World", key="concat_str2")
        
        if st.button("➕ Concatenate", key="concat_btn"):
            result = str1 + " " + str2
            st.code(f'result = "{str1}" + " " + "{str2}"\nprint(result)  # "{result}"', language="python")
            st.success(f'✅ Result: "{result}"')
        
        st.markdown("---")
        st.markdown("#### ✖️ Repetition with * Operator")
        
        col_rep1, col_rep2 = st.columns([3, 1])
        
        with col_rep1:
            rep_str = st.text_input("String to repeat:", value="Python! ", key="rep_str")
        
        with col_rep2:
            rep_count = st.number_input("Times:", value=3, min_value=1, max_value=10, key="rep_count")
        
        if st.button("✖️ Repeat", key="repeat_btn"):
            result = rep_str * int(rep_count)
            st.code(f'result = "{rep_str}" * {int(rep_count)}\nprint(result)  # "{result}"', language="python")
            st.success(f'"{result}"')
        
        st.markdown("---")
        st.markdown("#### 🔗 Join Multiple Strings")
        
        st.info("""
        **`.join()` method** - Join list of strings with a separator
        ```python
        words = ["Python", "is", "awesome"]
        sentence = " ".join(words)
        # Result: "Python is awesome"
        ```
        """)
        
        join_words = st.text_input("Enter words (comma-separated):", value="Python, is, awesome", key="join_words")
        join_sep = st.text_input("Separator:", value=" ", key="join_sep")
        
        if st.button("🔗 Join", key="join_btn"):
            words_list = [w.strip() for w in join_words.split(",")]
            result = join_sep.join(words_list)
            st.code(f'words = {words_list}\nresult = "{join_sep}".join(words)\nprint(result)  # "{result}"', language="python")
            st.success(f'"{result}"')
    
    # ============================================
    # TAB 6: STRING FORMATTING
    # ============================================
    with str_tabs[5]:
        st.markdown("### 🎨 String Formatting")
        st.write("Insert values into strings")
        
        st.info("""
        **Three main ways to format strings:**
        
        1. **f-strings (Python 3.6+):** `f"Hello {name}"`
        2. **`.format()` method:** `"Hello {}".format(name)`
        3. **% operator (old):** `"Hello %s" % name`
        
        **f-strings are recommended!** They're faster and more readable.
        """)
        
        st.markdown("---")
        st.markdown("#### 🔥 f-Strings (Modern Way)")
        
        col_f1, col_f2, col_f3 = st.columns(3)
        
        with col_f1:
            name_f = st.text_input("Name:", value="Alice", key="name_f")
        
        with col_f2:
            age_f = st.number_input("Age:", value=15, key="age_f")
        
        with col_f3:
            grade_f = st.text_input("Grade:", value="10th", key="grade_f")
        
        if st.button("🎨 Format with f-string", key="fstring_btn"):
            result = f"My name is {name_f}, I'm {age_f} years old, and I'm in {grade_f} grade."
            
            st.code(f'''name = "{name_f}"
age = {age_f}
grade = "{grade_f}"

message = f"My name is {{name}}, I'm {{age}} years old, and I'm in {{grade}} grade."
print(message)''', language="python")
            
            st.success(f'✅ Result: "{result}"')
        
        st.markdown("---")
        st.markdown("#### 🧮 Formatting Numbers")
        
        number_val = st.number_input("Enter a number:", value=3.14159265, key="format_num")
        
        col_num1, col_num2, col_num3 = st.columns(3)
        
        with col_num1:
            if st.button("2 decimals", key="2dec_btn"):
                result = f"{number_val:.2f}"
                st.code(f'f"{{number:.2f}}" = "{result}"', language="python")
                st.success(f'"{result}"')
        
        with col_num2:
            if st.button("4 decimals", key="4dec_btn"):
                result = f"{number_val:.4f}"
                st.code(f'f"{{number:.4f}}" = "{result}"', language="python")
                st.success(f'"{result}"')
        
        with col_num3:
            if st.button("Percentage", key="percent_btn"):
                result = f"{number_val:.1%}"
                st.code(f'f"{{number:.1%}}" = "{result}"', language="python")
                st.success(f'"{result}"')
        
        st.markdown("---")
        st.markdown("#### 📊 Alignment & Padding")
        
        pad_text = st.text_input("Text to align:", value="Python", key="pad_text")
        width = st.slider("Width:", min_value=10, max_value=30, value=20, key="pad_width")
        
        col_align1, col_align2, col_align3 = st.columns(3)
        
        with col_align1:
            if st.button("◀️ Left", key="left_btn"):
                result = f"{pad_text:<{width}}"
                st.code(f'f"{{text:<{width}}}" = "{result}"', language="python")
                st.info(f'`|{result}|`')
        
        with col_align2:
            if st.button("🎯 Center", key="center_btn"):
                result = f"{pad_text:^{width}}"
                st.code(f'f"{{text:^{width}}}" = "{result}"', language="python")
                st.info(f'`|{result}|`')
        
        with col_align3:
            if st.button("▶️ Right", key="right_btn"):
                result = f"{pad_text:>{width}}"
                st.code(f'f"{{text:>{width}}}" = "{result}"', language="python")
                st.info(f'`|{result}|`')
    
    # Key takeaways
    st.markdown("---")
    st.markdown("### 🎯 Key Takeaways")
    
    col_key1, col_key2 = st.columns(2)
    
    with col_key1:
        st.info("""
        **String Basics:**
        - Strings are sequences of characters
        - Use `' '`, `" "`, or `''' '''` to create
        - Access with indexes: `text[0]`
        - Slice with `[start:end:step]`
        - Strings are immutable (can't change)
        """)
    
    with col_key2:
        st.success("""
        **Common Operations:**
        - `.upper()`, `.lower()`, `.title()`
        - `.strip()`, `.replace()`
        - `.split()`, `.join()`
        - `.find()`, `.count()`
        - Concatenate with `+`
        - Format with f-strings: `f"{var}"`
        """)
    
    # Practice exercises
    with st.expander("💪 Practice Exercises", expanded=False):
        st.markdown("""
        **Try these challenges:**
        
        1. **Name Formatter:**
        ```python
        first = "john"
        last = "DOE"
        
        # Format as "John Doe"
        full_name = first.capitalize() + " " + last.capitalize()
        print(full_name)
        ```
        
        2. **Palindrome Checker:**
        ```python
        word = "racecar"
        is_palindrome = word == word[::-1]
        print(is_palindrome)  # True
        ```
        
        3. **Email Validator:**
        ```python
        email = "user@example.com"
        
        has_at = "@" in email
        has_dot = "." in email
        is_valid = has_at and has_dot
        
        print(f"Valid: {is_valid}")
        ```
        
        4. **Word Counter:**
        ```python
        sentence = "Python is fun and Python is powerful"
        words = sentence.split()
        python_count = sentence.lower().count("python")
        
        print(f"Total words: {len(words)}")
        print(f"'Python' appears: {python_count} times")
        ```
        
        5. **Acronym Generator:**
        ```python
        phrase = "Laugh Out Loud"
        words = phrase.split()
        acronym = "".join([word[0] for word in words])
        print(acronym.upper())  # LOL
        ```
        
        **Challenge:** Create a program that:
        - Takes a full name (first, middle, last)
        - Converts to title case
        - Creates username (first 3 letters of first name + last name, lowercase)
        - Example: "john william smith" → Username: "johsmith"
        """)

