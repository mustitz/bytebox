include ../common.mk

build:
	$(MAKE) -C sanctum build

%:
	$(ENTER_CHECK)
	$(MAKE) -C sanctum $@
	$(LEAVE_CHECK)
