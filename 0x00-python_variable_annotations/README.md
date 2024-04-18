# Python Variable Annotations

This repository contains Python scripts with variable annotations. These scripts demonstrate various concepts related to type annotations in Python 3.

## Table of Contents

1. [Basic Annotations - Add](#basic-annotations---add)
2. [Basic Annotations - Concat](#basic-annotations---concat)
3. [Basic Annotations - Floor](#basic-annotations---floor)
4. [Basic Annotations - To String](#basic-annotations---to-string)
5. [Define Variables](#define-variables)
6. [Complex Types - List of Floats](#complex-types---list-of-floats)
7. [Complex Types - Mixed List](#complex-types---mixed-list)
8. [Complex Types - String and Int/Float to Tuple](#complex-types---string-and-intfloat-to-tuple)
9. [Complex Types - Functions](#complex-types---functions)
10. [Let's Duck Type an Iterable Object](#lets-duck-type-an-iterable-object)
11. [Duck Typing - First Element of a Sequence](#duck-typing---first-element-of-a-sequence)
12. [More Involved Type Annotations](#more-involved-type-annotations)
13. [Type Checking](#type-checking)

## Basic Annotations - Add

Function `add` takes two float arguments and returns their sum as a float.

## Basic Annotations - Concat

Function `concat` takes two string arguments and returns their concatenation.

## Basic Annotations - Floor

Function `floor` takes a float argument and returns its floor as an integer.

## Basic Annotations - To String

Function `to_str` takes a float argument and returns its string representation.

## Define Variables

Variables `a`, `pi`, `i_understand_annotations`, and `school` are defined with their respective types and values.

## Complex Types - List of Floats

Function `sum_list` takes a list of floats and returns their sum as a float.

## Complex Types - Mixed List

Function `sum_mixed_list` takes a list of integers and floats and returns their sum as a float.

## Complex Types - String and Int/Float to Tuple

Function `to_kv` takes a string and an int or float, and returns a tuple with the string and the square of the int/float.

## Complex Types - Functions

Function `make_multiplier` takes a float multiplier and returns a function that multiplies a float by the multiplier.

## Let's Duck Type an Iterable Object

Function `element_length` takes an iterable object and returns a list of tuples containing each element and its length.

## Duck Typing - First Element of a Sequence

Function `safe_first_element` returns the first element of a sequence or `None` if the sequence is empty.

## More Involved Type Annotations

Function `safely_get_value` takes a dictionary, a key, and an optional default value, and

returns the value associated with the key or the default value if the key is not found.

## Type Checking

Function `zoom_array` takes a tuple and an optional factor, and returns a list. It has been annotated and type-checked with `mypy`.

---

Feel free to use these scripts for learning and practice purposes.

