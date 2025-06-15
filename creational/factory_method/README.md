Factory Method is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.

This is useful when there is a neeed to encapsulate the instantiation process of a product, making a class independent of how its objects are created, composed and represented.
To put simply, it detaches the creation and usage processes.

There are 2 main components:
- creator abstract class with 2 functions:
    * fatory_method - builds the product
    * action - public function that executes the factory_method
- product being created from factory

