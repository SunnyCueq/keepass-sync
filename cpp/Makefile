# Makefile for KeePass Sync (C++)
# Supports Linux, macOS, and Windows (with MinGW/MSYS2)

CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra -O2
TARGET = keepass-sync
SOURCES = sync.cpp

# Platform detection
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
    PLATFORM = linux
endif
ifeq ($(UNAME_S),Darwin)
    PLATFORM = darwin
endif
ifdef OS
    PLATFORM = windows
    TARGET = keepass-sync.exe
endif

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SOURCES)

clean:
	rm -f $(TARGET) $(TARGET).exe *.o

install: $(TARGET)
	cp $(TARGET) /usr/local/bin/

.PHONY: all clean install

