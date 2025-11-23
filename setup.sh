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

# Check if venv exists
echo ""
if [ -d "venv" ]; then
    echo "📦 Virtual environment already exists"
else
    echo "📦 Creating virtual environment..."
    if python3 -m venv venv; then
        echo "✅ Virtual environment created"
    else
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
fi

# Activate virtual environment
echo ""
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "📦 Upgrading pip..."
python -m pip install --upgrade pip --quiet

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
if pip install -r requirements.txt; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    deactivate
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
echo "  source venv/bin/activate"
echo "  streamlit run app.py"
echo ""
echo "The app will open at: http://localhost:8501"
echo ""

