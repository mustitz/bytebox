include ../../common.mk

MODULE = sanctum
SOURCES = $(wildcard *.c)
OBJECTS = $(SOURCES:%.c=$(OBJDIR)/$(MODULE)/%.o)
DEPS = $(OBJECTS:.o=.d)
LIBRARY = $(LIBDIR)/lib$(MODULE).a
PATROL = $(CHECKDIR)/sanctum-patrol

-include $(DEPS)

build: $(LIBRARY)

$(LIBRARY): $(OBJECTS) | $(LIBDIR)
	ar rcs $@ $^

$(OBJDIR)/$(MODULE)/%.o: %.c | $(OBJDIR)/$(MODULE)
	$(CC) $(CFLAGS) -MMD -MP $(INCLUDES) -c $< -o $@

$(PATROL): test/main.c $(LIBRARY) | $(CHECKDIR)
	$(CC) $(CFLAGS) $(INCLUDES) $< -L$(LIBDIR) -l$(MODULE) -o $@

$(OBJDIR)/$(MODULE):
	mkdir -p $@

$(LIBDIR):
	mkdir -p $@

$(CHECKDIR):
	mkdir -p $@

check: $(LIBRARY) $(PATROL)
	@python3 $(SRCROOT)/debrief.py run $(PATROL)
	$(LEAVE_CHECK)

clean:
	rm -f $(OBJECTS) $(DEPS) $(LIBRARY) $(PATROL)

%-asan:
	$(eval $(file < $(SRCROOT)/asan.mk))
	$(MAKE) $*

%-tsan:
	$(eval $(file < $(SRCROOT)/tsan.mk))
	$(MAKE) $*

.PHONY: build check clean %-asan %-tsan
