PYLINTRC='./.pylintrc'
TEST_PYLINTRC='./test/.pylintrc'
VERSION=$(shell python lib.py version)

# developer
DEFAULT_TEST_PORT="8002"
DEFAULT_CALL_URL="http://127.0.0.1:$(DEFAULT_TEST_PORT)/bot"
DEFAULT_CALL_ID="172862922"
DEFAULT_CALL_TEXT="test"

PYVERSION=$(shell which python3.5 || echo python)

ifneq ('$(PYVERSION)','python')
	PYVERSION='python3.5'
endif

ifeq ('$(DEV_CALL_ID)','')
	DEV_CALL_ID=$(DEFAULT_CALL_ID)
endif

ifeq ('$(DEV_CALL_URL)','')
	DEV_CALL_URL=$(DEFAULT_CALL_URL)
endif

ifeq ('$(CALL_TEXT)','')
	CALL_TEXT=$(DEFAULT_CALL_TEXT)
endif

ifeq ('$(SEMVER)','')
	SEMVER='patch'
endif

ifeq ('$(PUSH)','')
	PUSH='false'
endif

NEXT='$(shell python lib.py $(SEMVER) next-version)'

lint:
	pylint --rcfile=$(PYLINTRC) bobot
	pylint --rcfile=$(TEST_PYLINTRC) test

publish-test:
	echo 'Publishing into PYPITEST $(SEMVER) release with version: $(VERSION)'
	./tasks/publish.sh pypitest $(VERSION) $(PUSH) true

publish:
	echo 'Publishing into PYPI $(SEMVER) release with version: $(VERSION)'
	./tasks/publish.sh pypi $(VERSION) $(PUSH) true

release-test:
	echo 'Publishing into PYPITEST $(SEMVER) release with version: $(NEXT) (Update from: $(VERSION))'
	./tasks/publish.sh pypitest $(NEXT) $(PUSH) true

release:
	echo 'Publishing into PYPI $(SEMVER) release with version: $(NEXT) (Update from: $(VERSION))'
	./tasks/publish.sh pypi $(NEXT) $(PUSH) true

register-test:
	python setup.py register -r pypitest

register:
	python setup.py register -r pypi

commit-release:
	echo 'Commiting $(SEMVER) release with version: $(NEXT) (Update from: $(VERSION))'
	./tasks/publish.sh pypitest $(NEXT) $(PUSH) false

call:
	./tasks/call.sh $(DEV_CALL_URL) $(DEV_CALL_ID) "$(CALL_TEXT)"

tests:
	$(PYVERSION) ./test/testrunner.py

run-test-server:
	python3.5 test/testserver.py debug