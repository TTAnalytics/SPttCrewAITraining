#!/bin/bash

# Move to the folder of the setup.sh file
cd "$(dirname "$0")"

# Setup a virtual environment with python 3.10 or the installed version of python3
if command -v python3.10 &>/dev/null; then
    echo "Using python3.10 to create virtual environment"
    python3.10 -m venv .venv
else
    echo "Using python3 to create virtual environment"
    python3 -m venv .venv
fi

# Activate the virtual environment
echo "Activating virtual environment"
source .venv/bin/activate

# Install crewAI using pip
echo "Installing crewai"
pip install crewai

# Create a crew using crewai
PARENT_DIR=$(basename "$(pwd)")
CREW_NAME=${PARENT_DIR#agentic-workflows-}
echo "Creating crew with name: $CREW_NAME"
crewai create crew $CREW_NAME

# Move all folders and files created by crewai one level above to the root folder
CREW_DIR="$PWD/$CREW_NAME"
ROOT_DIR="$(pwd)"
if [ -d "$CREW_DIR" ]; then
    echo "Moving all files and folders from $CREW_NAME to the project root directory"
    shopt -s dotglob
    for file in "$CREW_DIR"/*; do
        if [ "$(basename "$file")" != ".gitignore" ]; then
            mv "$file" "$ROOT_DIR"
        else
            rm "$file"
        fi
    done
    shopt -u dotglob
    rmdir "$CREW_DIR"
    echo "Move completed successfully"
else
    echo "Error: Crew directory $CREW_DIR does not exist"
fi

echo "Setup completed"
