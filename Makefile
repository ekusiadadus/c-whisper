.phony:

venv:
	python3 -m venv .venv

setup: venv
	.venv/bin/pip install -r requirements.txt
