##
## EPITECH PROJECT, 2018
## Ceasar
## File description:
## Makeile for Ceasar
##

RM	= rm -f

SRCS	= challenge01.py	\
	  challenge02.py	\
	  challenge03.py	\
	  challenge04.py	\
	  challenge05.py	\
	  challenge06.py	\
	  challenge07.py	\
	  challenge08.py	\
	  challenge09.py	\

BINARIES    = $(SRCS:%.py=%)

all: $(BINARIES)

%: %.py
	chmod +x $<
	cp $< $@

clean:
	rm -f $(BINARIES)

re: clean all

.PHONY: all clean re
