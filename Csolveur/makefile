##########################
##### COMPILER FLAGS #####
##########################
CC=clang
CFLAGS=-Wall -Wextra -pedantic -fdiagnostics-color=always
CFLAGS+=$(CPPFLAGS) -O0 -g3 -fsanitize=address -fno-omit-frame-pointer -fno-optimize-sibling-calls
LDFLAGS+=-fsanitize=address


############################
##### FILES TO COMPILE #####
############################

# Program:
solveur_main_test: solveur_main_test.o solveur.o

# Format is:
## program_name: file_name1.o file_name2.o


# Object files
solveur_main_test.o: solveur.o solveur_main_test.c
solveur.o: solveur.h solveur.c

# Format is:
## file_name.o: <dependency.o> <header_file.h> file_name.c


##########################
##### OTHER COMMANDS #####
##########################

clean:
	rm -f *.o *_test

# For the test, replace `solveur_main_test` with your program name.
test: solveur_main_test
	./solveur_main_test

.SILENT: clean
