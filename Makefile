UI_DIR = ui
SRC_DIR = src
VENVDIR = venv
PYUIC = $(VENVDIR)/bin/pyuic6
PYTHON = $(VENVDIR)/bin/python
DESIGN_APP = $(VENVDIR)/bin/pyqt6-tools
MAIN_SCRIPT = $(SRC_DIR)/main.py

UI_FILES = $(wildcard $(UI_DIR)/*.ui)
PY_FILES = $(patsubst $(UI_DIR)/%.ui, $(SRC_DIR)/%.py, $(UI_FILES))

all: $(PY_FILES)

$(SRC_DIR)/%.py: $(UI_DIR)/%.ui
	@mkdir -p $(SRC_DIR)
	@if [ "$@" == "$(SRC_DIR)/main.py" ]; then \
	    $(PYUIC) -x $< -o $@; \
	else \
	    $(PYUIC) $< -o $@; \
	fi
	@echo "Converted $< -> $@"

design:
	@if [ -f $(DESIGN_APP) ]; then \
	    $(DESIGN_APP) designer;\
	else \
	    echo "Error: $(DESIGN_APP) not found."; \
	fi

run:
	@if [ -f $(MAIN_SCRIPT) ]; then \
	    $(PYTHON) $(MAIN_SCRIPT); \
	else \
	    echo "Error: $(MAIN_SCRIPT) not found."; \
	fi