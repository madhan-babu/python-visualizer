#!/bin/bash

# Quick start script for Python Visualizer
# Make executable with: chmod +x run.sh

echo "🐍 Python Concepts Visualizer"
echo "=============================="
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run setup.sh first:"
    echo "  ./setup.sh"
    echo ""
    exit 1
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Check if streamlit is installed in venv
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit not found in virtual environment"
    echo "Please run setup.sh to install dependencies:"
    echo "  ./setup.sh"
    echo ""
    deactivate
    exit 1
fi

echo "🚀 Starting visualizer..."
echo "📱 Opening in browser at http://localhost:8501"
echo ""
echo "💡 Press Ctrl+C to stop"
echo ""

streamlit run app.py

# Deactivate venv when streamlit exits
deactivate

