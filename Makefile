all: dist

.PHONY: dist
dist:
	# pip freeze > requirements.txt
	python setup.py sdist bdist_wheel
	@echo Dist completed!

.PHONY: test
test:
	python -m tox
	@echo Test completed!

.PHONY: doc
doc:
	mkdir -p doc/pydoc
	cd doc/pydoc
	python -m pydoc -w sepbit.hellopy
	@echo Doc completed!

.PHONY: clean
clean:
	rm -rf .coverage build dist doc/pydoc htmlcov .tox *.egg-info 
	find . -type f -name '*.pyc' -exec rm -f {} \;
	find . -type f -name '*.pyo' -exec rm -f {} \;
	find . -type d -name '__pycache__' -exec rm -rf {} \;
	@echo Clean completed!

.PHONY: tags
tags:
	ctags -R --languages=python --python-kinds=cfmi src
	ctags -R --languages=python --python-kinds=cfmi -f tags -pipenv $(pipenv --venv)/lib/python3.7
	@echo Tags completed!
