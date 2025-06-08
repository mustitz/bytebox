ifndef COMMON_MK_INCLUDED
COMMON_MK_INCLUDED := 1

SRCROOT := $(realpath $(dir $(lastword $(MAKEFILE_LIST))))

BUILD ?= build
DEBUG ?= 0
CC ?= gcc
CFLAGS ?= -Wall -Wextra -std=c99 -fPIC

ifeq ($(DEBUG),1)
    CFLAGS += -g -O0 -DDEBUG
else
    CFLAGS += -O2 -DNDEBUG
endif

INCLUDES = -I$(SRCROOT)/include
BUILDDIR = $(SRCROOT)/$(BUILD)
LIBDIR = $(BUILDDIR)/lib
OBJDIR = $(BUILDDIR)/obj
CHECKDIR = $(BUILDDIR)/check
TMPDIR = $(BUILDDIR)/tmp
$(shell rm -r -f $(TMPDIR))

ENTER_CHECK = @python3 $(SRCROOT)/debrief.py enter $(BUILDDIR) $(MAKECMDGOALS)
LEAVE_CHECK = @python3 $(SRCROOT)/debrief.py leave $(BUILDDIR) $(MAKECMDGOALS)

export

endif # COMMON_MK_INCLUDED
