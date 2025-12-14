#!/bin/bash
# Harmonia Demo - Quick Start Script

set -e

echo "🔮 Harmonia Cognitive Kernel - Setup"
echo "======================================"

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.10+"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo "✓ Python $PYTHON_VERSION detected"

# Create virtual environment if not exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate
echo "✓ Virtual environment activated"

# Install dependencies
echo "📦 Installing dependencies..."
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt

# Check for .env file
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        echo "📝 Creating .env from .env.example"
        cp .env.example .env
        echo "⚠️  Edit .env to add your OPENAI_API_KEY (optional - mock mode works without it)"
    fi
fi

# Run the server
echo ""
echo "🚀 Starting Harmonia server..."
echo "   Open http://localhost:8000 in your browser"
echo ""
python -m uvicorn main:app --reload --port 8000
