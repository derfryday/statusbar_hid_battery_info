VENV = .venv
MAIN = src/statusbar_hid_battery_info/app.py
NUITKA_OPTIONS = --macos-app-icon=src/statusbar_hid_battery_info/resources/app.icns --macos-app-mode=background --disable-console --noinclude-pytest-mode=nofollow --noinclude-setuptools-mode=nofollow --static-libpython=no --standalone --onefile --macos-create-app-bundle --macos-app-name=StatusbarHIDBattInfo --macos-signed-app-name='dev.derfryday.StatusbarHIDBattInfo' --output-filename=StatusbarHIDBattInfo --include-data-dir=src/statusbar_hid_battery_info/resources=statusbar_hid_battery_info/resources --include-data-files=Info.plist=Info.plist --product-name=StatusbarHIDBattInfo

BUILD:
	poetry install --without test,dev
	$(VENV)/bin/nuitka3 $(NUITKA_OPTIONS) $(MAIN)
