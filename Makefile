test:
	python3 -m unittest
coverage_test:
	coverage run -m unittest test_rpn
	coverage report

.PHONY: test
