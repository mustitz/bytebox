override BUILDDIR = $(SRCROOT)/build/tsan
override CFLAGS += -fsanitize=thread -fno-omit-frame-pointer -g

override LIBDIR = $(BUILDDIR)/lib
override OBJDIR = $(BUILDDIR)/obj
override CHECKDIR = $(BUILDDIR)/check
$(shell mkdir -p $(LIBDIR) $(OBJDIR) $(CHECKDIR))
