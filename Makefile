# Set up the virtual enviroment
init:
	@python3 -m venv venv
	@. venv/bin/activate && python3 -m pip install -r requirements.txt

# Remove the virtual enviroment and pycache
clean:
	@rm -rf venv/
	@find . -type d -name "__pycache__" -exec rm -rf {} +