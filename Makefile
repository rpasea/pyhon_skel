build:
	pip install -r requirements.txt -r test-requirements.txt -e .

test:
	tox

run:
	FLASK_APP=skeleton.skeleton FLASK_DEBUG=true flask run -p 8080
