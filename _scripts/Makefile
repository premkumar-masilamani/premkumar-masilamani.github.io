.PHONY: setup
setup:
	@echo "Creating virtual environment..."
	pipenv shell

.PHONY: show
show:
	@echo "Listing dependencies..."
	pipenv graph

.PHONY: check
check:
	make link
	make profanity

.PHONY: link
link:
	python3 src/link_checker.py

.PHONY: profanity
profanity:
	python3 src/profanity_checker.py

.PHONY: mp3
mp3:
	python3 src/mp3_converter.py
