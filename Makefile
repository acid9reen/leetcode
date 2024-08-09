.PHONY: deps
deps: requirements/requirements.txt sync-venv

.PHONY: sync-venv
sync-venv: requirements/requirements.txt
	uv pip sync $<

requirements/requirements.txt: requirements/requirements.in
	uv pip compile $< --output-file $@
