import streamlit as st

def show():
    st.markdown('<h2 style="color: #2196F3;">🐍 Welcome to Python!</h2>', unsafe_allow_html=True)
    st.write("Learn about Python - one of the world's most popular programming languages!")
    
    # What is Python
    st.markdown("---")
    st.markdown("### 🌟 What is Python?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Python** is a high-level, interpreted programming language known for its simplicity and readability. 
        It's perfect for beginners and powerful enough for experts!
        
        **Key Features:**
        - 📖 **Easy to Read** - Code looks like English
        - 🚀 **Easy to Learn** - Great for beginners
        - 💪 **Powerful** - Can build anything from websites to AI
        - 🌍 **Popular** - Used by millions worldwide
        - 🆓 **Free & Open Source** - Anyone can use it
        """)
    
    with col2:
        st.info("""
        **Fun Fact!** 🎭
        
        Python is named after the British comedy group "Monty Python's Flying Circus", not the snake!
        
        Creator Guido van Rossum wanted a fun name for his language.
        """)
    
    # History
    st.markdown("---")
    st.markdown("### 📜 Python History")
    
    timeline_col1, timeline_col2 = st.columns(2)
    
    with timeline_col1:
        st.success("""
        **🎂 Birth of Python**
        - **1989**: Guido van Rossum started developing Python
        - **1991**: Python 0.9.0 released
        - **2000**: Python 2.0 released
        - **2008**: Python 3.0 released (current version)
        """)
    
    with timeline_col2:
        st.info("""
        **👨‍💻 Creator**
        
        **Guido van Rossum** from the Netherlands created Python while working at CWI (Centrum Wiskunde & Informatica).
        
        He was Python's "Benevolent Dictator For Life" (BDFL) until 2018!
        """)
    
    # Why Python
    st.markdown("---")
    st.markdown("### 💡 Why Learn Python?")
    
    col_why1, col_why2, col_why3 = st.columns(3)
    
    with col_why1:
        st.markdown("""
        **🎓 For Beginners**
        - Simple syntax
        - Less code needed
        - Fewer errors
        - Great community support
        - Lots of learning resources
        """)
    
    with col_why2:
        st.markdown("""
        **💼 For Career**
        - High demand jobs
        - Good salaries
        - Many industries use it
        - Future-proof skill
        - Remote work opportunities
        """)
    
    with col_why3:
        st.markdown("""
        **🛠️ Build Cool Stuff**
        - Websites & Apps
        - Games
        - Robots & IoT
        - AI & Machine Learning
        - Data Analysis
        """)
    
    # What can you build
    st.markdown("---")
    st.markdown("### 🚀 What Can You Build with Python?")
    
    st.markdown("""
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin-top: 20px;">
        <div style="padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
            <h4 style="margin: 0 0 10px 0;">🌐 Web Development</h4>
            <p style="margin: 0; font-size: 0.9rem;">Build websites and web applications using Django, Flask, FastAPI</p>
        </div>
        <div style="padding: 15px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white;">
            <h4 style="margin: 0 0 10px 0;">🤖 Artificial Intelligence</h4>
            <p style="margin: 0; font-size: 0.9rem;">Create smart programs, chatbots, and machine learning models</p>
        </div>
        <div style="padding: 15px; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); border-radius: 10px; color: white;">
            <h4 style="margin: 0 0 10px 0;">📊 Data Science</h4>
            <p style="margin: 0; font-size: 0.9rem;">Analyze data, create visualizations, and discover insights</p>
        </div>
        <div style="padding: 15px; background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); border-radius: 10px; color: white;">
            <h4 style="margin: 0 0 10px 0;">🎮 Game Development</h4>
            <p style="margin: 0; font-size: 0.9rem;">Make 2D and 3D games using Pygame, Panda3D</p>
        </div>
        <div style="padding: 15px; background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); border-radius: 10px; color: white;">
            <h4 style="margin: 0 0 10px 0;">🔧 Automation</h4>
            <p style="margin: 0; font-size: 0.9rem;">Automate boring tasks, web scraping, file management</p>
        </div>
        <div style="padding: 15px; background: linear-gradient(135deg, #30cfd0 0%, #330867 100%); border-radius: 10px; color: white;">
            <h4 style="margin: 0 0 10px 0;">📱 Desktop Apps</h4>
            <p style="margin: 0; font-size: 0.9rem;">Create desktop applications using Tkinter, PyQt, Kivy</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Companies using Python
    st.markdown("---")
    st.markdown("### 🏢 Big Companies Using Python")
    
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: #f8f9fa; border-radius: 10px; margin: 20px 0;">
        <p style="font-size: 1.1rem; color: #333; margin-bottom: 15px;">Python powers some of the world's biggest companies:</p>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; font-size: 1.2rem; font-weight: 600;">
            <span style="padding: 10px 20px; background: white; border-radius: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">🔍 Google</span>
            <span style="padding: 10px 20px; background: white; border-radius: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">📘 Facebook</span>
            <span style="padding: 10px 20px; background: white; border-radius: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">📺 Netflix</span>
            <span style="padding: 10px 20px; background: white; border-radius: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">🎵 Spotify</span>
            <span style="padding: 10px 20px; background: white; border-radius: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">📷 Instagram</span>
            <span style="padding: 10px 20px; background: white; border-radius: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">🚗 Uber</span>
            <span style="padding: 10px 20px; background: white; border-radius: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">🏦 Dropbox</span>
            <span style="padding: 10px 20px; background: white; border-radius: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">🛒 Amazon</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Python Resources
    st.markdown("---")
    st.markdown("### 📚 Learn More About Python")
    
    resource_col1, resource_col2 = st.columns(2)
    
    with resource_col1:
        st.markdown("""
        **🌐 Official Resources:**
        - [Python.org](https://www.python.org/) - Official Python website
        - [Python Documentation](https://docs.python.org/3/) - Official docs
        - [Python Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language)) - Python on Wikipedia
        - [Python Wiki](https://wiki.python.org/moin/) - Community wiki
        - [PEP 8](https://peps.python.org/pep-0008/) - Python style guide
        """)
    
    with resource_col2:
        st.markdown("""
        **📖 Learning Resources:**
        - [Python for Beginners](https://www.python.org/about/gettingstarted/) - Getting started guide
        - [Python Tutorial](https://docs.python.org/3/tutorial/) - Official tutorial
        - [Real Python](https://realpython.com/) - Tutorials and articles
        - [Python Tutor](https://pythontutor.com/) - Visualize code execution
        - [Codecademy Python](https://www.codecademy.com/learn/learn-python-3) - Interactive course
        """)
    
    # Getting Started
    st.markdown("---")
    st.markdown("### 🎯 Ready to Start Learning?")
    
    st.success("""
    **👉 Use the tabs above to explore Python concepts:**
    
    1. **Variables & Memory** - Learn how Python stores information
    2. **Print & Input** - Communicate with your programs
    3. **Data Types** - Understand different types of data
    4. **Operators** - Perform operations on data
    5. **And much more!**
    
    Each tab has **interactive visualizations** to help you understand concepts better!
    """)
    
    # Quote
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white; margin: 20px 0;">
        <p style="font-size: 1.5rem; font-style: italic; margin: 0;">
            "Python is an experiment in how much freedom programmers need. 
            Too much freedom and nobody can read another's code; 
            too little and expressiveness is endangered."
        </p>
        <p style="font-size: 1.1rem; margin-top: 15px; opacity: 0.9;">
            — Guido van Rossum, Creator of Python
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Fun Facts
    st.markdown("---")
    st.markdown("### 🎉 Fun Python Facts")
    
    fun_col1, fun_col2, fun_col3 = st.columns(3)
    
    with fun_col1:
        st.info("""
        **🐍 The Snake Logo**
        
        The Python logo has two intertwined snakes - representing the dual nature of Python as both simple and powerful!
        """)
    
    with fun_col2:
        st.warning("""
        **📈 Fastest Growing**
        
        Python is one of the fastest-growing programming languages in the world, especially popular for AI and data science!
        """)
    
    with fun_col3:
        st.success("""
        **🎓 Educational Choice**
        
        Python is the most commonly taught programming language in universities around the world!
        """)

