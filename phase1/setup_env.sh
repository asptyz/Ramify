#!/bin/bash

# Script that launches a new shell with the venv activated
# Usage: ./activate_venv.sh

VENV_DIR="venv"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$SCRIPT_DIR/$VENV_DIR"

REQUIREMENT_FILE="$SCRIPT_DIR/requirement.txt"

# Check if the venv already exists
if [ ! -d "$VENV_PATH" ]; then
    echo "Creating the virtual environment..."
    python3 -m venv "$VENV_PATH"
    
    if [ $? -ne 0 ]; then
        echo "✗ Error while creating the virtual environment"
        exit 1
    fi
    echo "✓ Virtual environment created successfully"
fi

# Update pip3 to the latest version
echo "Updating pip3 to the latest version..."
"$VENV_PATH/bin/pip3" install --upgrade pip --quiet
if [ $? -eq 0 ]; then
    echo "✓ pip3 updated successfully"
else
    echo "⚠ Warning: Unable to update pip3 (continuing with current version)"
fi

# Install or update dependencies in the venv
if [ -f "$REQUIREMENT_FILE" ]; then
    echo "Installing dependencies in the venv..."
    "$VENV_PATH/bin/pip3" install -r "$REQUIREMENT_FILE"
    if [ $? -eq 0 ]; then
        echo "✓ Dependencies installed successfully"
    else
        echo "✗ Error while installing dependencies"
        exit 1
    fi
fi

# Launch a new shell with the venv activated
echo "Launching a new shell with the venv activated..."
echo "Type 'exit' to leave the shell and return to your previous shell."
echo ""

exec $SHELL -c "source '$VENV_PATH/bin/activate' && cd '$SCRIPT_DIR' && exec $SHELL"
