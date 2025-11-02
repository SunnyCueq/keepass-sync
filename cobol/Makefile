# Makefile for COBOL KeePass Sync
# Requires GnuCOBOL (formerly OpenCOBOL)

COBOL = cobc
COBOL_FLAGS = -x -std=default -free
TARGET = keepass-sync
SOURCE = sync.cbl

all: $(TARGET)

$(TARGET): $(SOURCE)
	$(COBOL) $(COBOL_FLAGS) $(SOURCE) -o $(TARGET)

clean:
	rm -f $(TARGET) *.o

install: $(TARGET)
	cp $(TARGET) /usr/local/bin/

.PHONY: all clean install

