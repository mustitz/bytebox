include common.mk

build:
	$(MAKE) -C src build

clean:
	rm -rf $(BUILDDIR)

%:
	$(ENTER_CHECK)
	$(MAKE) -C src $@
	$(LEAVE_CHECK)

.PHONY: build clean
