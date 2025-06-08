override BUILDDIR = $(SRCROOT)/build/asan
override CFLAGS += -fsanitize=address -fsanitize=undefined -fno-omit-frame-pointer -g

override LIBDIR = $(BUILDDIR)/lib
override OBJDIR = $(BUILDDIR)/obj
override CHECKDIR = $(BUILDDIR)/check
$(shell mkdir -p $(LIBDIR) $(OBJDIR) $(CHECKDIR))
