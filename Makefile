# Compiler
CC = python3

# Test folder
TEST = $(wildcard tests)

# Flags for unittest
UFLAGS = -m unittest discover $(TEST)

# Flags for fail fast unittest
FFLAGS = -m unittest discover -f $(TEST)

# Name of executable
NAME = $(wildcard console.py)

# Source code: all python files
SRC = $(shell find ./ -iname "*.py")

# Cache files
CACHE = "__pycache__"

# Source code checker
CHECKER = pycodestyle


# Essential files: wildcard is evaluated once
ESS_FILES := "$(wildcard README.md)"

# Vim temporary files
VIM_TMP = $(wildcard *.swp)

# Emacs temporary files
EMACS_TMP = $(wildcard *~)


# Rules

# makefile should not compile if Essential files are missing

ifneq ($(strip $(ESS_FILES)), "")

all: # Execute the program
	$(CC) $(NAME)

.PHONY: clean check cclean fclean re test fast_test ready

clean:	# Delete all temporary files and executable
	$(RM) $(VIM_TMP) $(EMACS_TMP)

cclean: #delete only the cache directories
	find ./ -type d -name $(CACHE) -exec rm -rf {} +;

fclean: cclean clean # delete all temporary files and cache directories

re:	fclean all # Forcefully recompile all the source files \
	and execute the program

check: # Ensure source codes are $(CHECKER) compliant
	$(CHECKER) $(SRC)

test: # Run the complete unittest
	$(CC) $(UFLAGS)

fast_test: # Run the unittest but stop execution at first failure encountered
	$(CC) $(FFLAGS)

ready: test check re # Ensure file is ready to be submitted

else
$(info "README.md missing")

endif
