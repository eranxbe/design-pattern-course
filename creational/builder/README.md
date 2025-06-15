Builder is a creational design pattern for constructing complex objects step by step.
like making a sandwich (SANDWICH BAR CARMEL)

useful when an object needs to be created with many configurations and parameters,
some of which can be optional.

This is good for examples like:
- sandwich
- house
- computer
- configuration file
- sql query builder
- serialization object
- test data object

There are 4 main components:
- product - represents the complex object being constructed.
- concrete_builder - constructs parts of the product and assembles them.
- builder - interface for concrete_builder.
- director - controls the building process using a builder instance.