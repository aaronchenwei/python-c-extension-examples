# python-c-extension-examples

Examples for implementing custom Python c-extensions.

Python is an incredibly versatile and widely-used programming language, and one of its strengths is the ability to extend its functionality using C extensions. C extensions are powerful tools that allow Python code to interface with C libraries, providing a significant performance boost and making it possible to take advantage of the vast number of C libraries available.

## Prerequisites

- Python 3.x and its development package
- A C compiler (such as GCC)
- Python's setuptools package

## Examples

- 01-helloworld-distutils

```sh
$ sudo dnf install python3-devel
```

  ```
  DeprecationWarning: The distutils package is deprecated and slated for removal in Python 3.12. Use setuptools or check PEP 632 for potential alternatives
  ```

- 02-helloworld-setuptools

```sh
$ sudo dnf install python3-setuptools
```
