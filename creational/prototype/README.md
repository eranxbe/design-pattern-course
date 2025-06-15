Prototype is a creational design pattern that is used when the type of objects to create is determined by a prototypical instance, which is cloned to produce new objects. 

This is useful when the cost of creating an object is more expensive than cloning it.

There are 2 main components:
- prototype interface that will contain an abstract method to clone the prototype object
- the concrete prototype class that implements the interface

This is good for examples like:
- Prototype Registry
- Avoid subclasses
- Preload and caching
- Clone Webdriver
- Clone Page Objects
