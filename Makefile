install_deps:
	pip3 install -r ./requirements/requirements.txt

run_rests:
	cd tests; \
	PYTHONPATH=".." pytest 

prepare: install_deps run_rests

run:
	python3 src/main.py
