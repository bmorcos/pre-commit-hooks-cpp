# pre-commit hooks for cpp tools

This provides [pre-commit](https://pre-commit.com/) hooks for
[clang-format](https://clang.llvm.org/docs/ClangFormat.html),
[cpplint](https://github.com/cpplint/cpplint), and
[cppcheck](http://cppcheck.sourceforge.net/).

## Usage

To use these hooks, simply place the following in you `.pre-commit-config.yaml`
(more details below):

```yaml
repos:
-   repo: https://github.com/bmorcos/pre-commit-hooks-cpp
    rev: master
    hooks:
    -   id: clang-format
    -   id: cpplint
    -   id: cppcheck
```

## clang-format

This requires clang-format to be installed, e.g. `sudo apt install
clang-format`. The default setup uses the Google style guide and will format all
C/C++ files and headers found in the repo, however other arguments and
particular files can specified.

```yaml
-   repo: https://github.com/bmorcos/pre-commit-hooks-cpp
    rev: master
    hooks:
    -   id: clang-format
    #   args: [--option1, -option2=abc]
    #   files: my_file.cpp|my_other_file.cpp

```

## cpplint

This requires cpplint to be installed, e.g. `pip install cpplint`. The default
setup uses the `--verbose=3` flag and will check all C/C++ files and headers
found in the repo, however other arguments and particular files can specified.

```yaml
-   repo: https://github.com/bmorcos/pre-commit-hooks-cpp
    rev: master
    hooks:
    -   id: cpplint
    #   args: [--option1, -option2=abc]
    #   files: my_file.cpp|my_other_file.cpp

```

## cppcheck

This requires cppcheck to be installed, e.g. `sudo apt install cppcheck`. The
default setup enables warnings to be displayed and will check all C/C++ files
and headers found in the repo, however other arguments and particular files can
specified.

```yaml
-   repo: https://github.com/bmorcos/pre-commit-hooks-cpp
    rev: master
    hooks:
    -   id: cppcheck
    #   args: [--option1, -option2=abc]
    #   files: my_file.cpp|my_other_file.cpp

```
