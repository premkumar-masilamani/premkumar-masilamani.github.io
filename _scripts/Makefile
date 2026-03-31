.PHONY: setup
setup:
	@echo "Creating virtual environment..."
	python3 -m venv .venv
	@echo "Virtual environment created in .venv"
	@echo "Installing dependencies..."
	./.venv/bin/pip install -r requirements.txt
	@echo "To activate the virtual environment, run: source .venv/bin/activate"

.PHONY: show
show:
	@echo "Listing dependencies..."
	./.venv/bin/pip list

.PHONY: check
check:
	make link
	make profanity

.PHONY: link
link:
	./.venv/bin/python3 src/link_checker.py

.PHONY: profanity
profanity:
	./.venv/bin/python3 src/profanity_checker.py

.PHONY: files
files:
	./.venv/bin/python3 src/files_checker.py ../

.PHONY: mp3
mp3:
	./.venv/bin/python3 src/convert_mp3.py
