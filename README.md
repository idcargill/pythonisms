# Pythonisms

[Lab 42](https://canvas.instructure.com/courses/3826570/assignments/26339126?return_to=https%3A%2F%2Fcanvas.instructure.com%2Fcalendar%23view_name%3Dmonth%26view_start%3D2022-04-26)

## The Associator

A class for grouping items with any value attribute and associated items. 
An iterable graph like class structure.  Iterable through item names. Items can be referenced through getter methods.

### Attributes

An Empty class will return False

### Methods

- add: add an item with optional value.
- get_item: returns a single item: takes a string arg
- get_items: returns a list of item names.
- add_associate: associates a name with an item already entered in class storage
- next(instance): will return the next item name in storage
- an empty class will return False
- contains: returns Bool if item is present. Takes a string
- get_associates: returns a list of associates of a specified item
- size: return the size of the class instance

### Decorator Function

> timing_decorator_delay

This function will delay a function for 2 seconds and time the decorated function with the added 2 seconds. It's basically worthless.
