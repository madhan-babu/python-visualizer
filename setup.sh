#!/bin/bash

# Python Visualizer Setup Script
echo "🐍 Python Visualizer Setup"
echo "=========================="
echo ""

# Check Python version
echo "📋 Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ Found: $PYTHON_VERSION"
else
    echo "❌ Python 3 not found! Please install Python 3.7 or higher"
    exit 1
fi

# Check pip
echo ""
echo "📋 Checking pip..."
if command -v pip3 &> /dev/null || command -v pip &> /dev/null; then
    echo "✅ pip is available"
else
    echo "❌ pip not found! Please install pip"
    exit 1
fi

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
if python3 -m pip install -r requirements.txt; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Make run script executable
echo ""
echo "🔧 Setting up run script..."
chmod +x run.sh
echo "✅ Run script is ready"

# Success message
echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the visualizer, run:"
echo "  ./run.sh"
echo ""
echo "Or manually:"
echo "  streamlit run app.py"
echo ""
echo "The app will open at: http://localhost:8501"
echo ""

