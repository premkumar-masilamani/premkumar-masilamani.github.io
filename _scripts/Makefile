# Define variables
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Default target
all: run

# Create virtual environment
$(VENV):
	python3 -m venv $(VENV)

# Install dependencies
deps: $(VENV)
	$(PIP) install -r requirements.txt

# Run the script inside the virtual environment
run: deps
	$(PYTHON) link_checker.py
	$(PYTHON) profanity_checker.py

# Clean the virtual environment
clean:
	rm -rf $(VENV)

# Recreate virtual environment and run
rebuild: clean all
