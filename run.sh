#!/bin/bash

# Quick start script for Python Visualizer
# Make executable with: chmod +x run.sh

echo "🐍 Python Concepts Visualizer"
echo "=============================="
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit not found. Installing dependencies..."
    pip install -r requirements.txt
    echo ""
fi

echo "🚀 Starting visualizer..."
echo "📱 Opening in browser at http://localhost:8501"
echo ""
echo "💡 Press Ctrl+C to stop"
echo ""

streamlit run app.py

