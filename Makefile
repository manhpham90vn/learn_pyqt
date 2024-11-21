UI_DIR = ui
SRC_DIR = src
VENV_DIR = venv
PYUIC = $(VENV_DIR)/bin/pyuic6
PYTHON = $(VENV_DIR)/bin/python
TOOLS_APP = $(VENV_DIR)/bin/pyqt6-tools
MAIN_SCRIPT = $(SRC_DIR)/main.py

UI_FILES = $(wildcard $(UI_DIR)/*.ui)
PY_FILES = $(patsubst $(UI_DIR)/%.ui, $(SRC_DIR)/%.py, $(UI_FILES))

all: $(PY_FILES)

init:
	@if [ ! -d $(VENV_DIR) ]; then \
	    echo "Creating virtual environment..."; \
	    python -m venv $(VENV_DIR); \
	else \
	    echo "Virtual environment already exists."; \
	fi

install:
	@echo "Installing dependencies..."
	@$(VENV_DIR)/bin/pip install -r requirements.txt

freeze:
	@echo "Freezing dependencies..."
	@$(VENV_DIR)/bin/pip freeze > requirements.txt

design:
	$(TOOLS_APP) designer

$(SRC_DIR)/%.py: $(UI_DIR)/%.ui
	@mkdir -p $(SRC_DIR)
	@if [ "$@" = "$(MAIN_SCRIPT)" ]; then \
	    $(PYUIC) -x $< -o $@ || { echo "Failed to convert $<"; exit 1; }; \
	else \
	    $(PYUIC) $< -o $@ || { echo "Failed to convert $<"; exit 1; }; \
	fi
	@echo "Converted $< -> $@"

run:
	$(PYTHON) $(MAIN_SCRIPT);