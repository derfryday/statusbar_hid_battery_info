VENV = .venv
MAIN = src/statusbar_hid_battery_info/app.py
#NUITKA = $(VENV)/bin/nuitka3
NUITKA_OPTIONS = --static-libpython=no --standalone --onefile --macos-create-app-bundle --macos-app-name=StatusbarHIDBattInfo --macos-signed-app-name='dev.derfryday.StatusbarHIDBattInfo' --output-filename=StatusbarHIDBattInfo --include-data-dir=src/statusbar_hid_battery_info/resources --product-name=StatusbarHIDBattInfo

BUILD:
	poetry install --no-root
	$(VENV)/bin/nuitka3 $(NUITKA_OPTIONS) $(MAIN)
