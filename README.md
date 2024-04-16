# Elevator-CaseStudy - Activity II

We had worked on the following methods :

1) Cohesion and Coupling
2) Refactoring


Cohesion: 

Functional Cohesion: Classes focus on elevator control and related functionalities. For example, the Elevator class oversees elevator movements, the FloorButton class represents floor buttons, and the User class represents system users. Each class serves a clear and distinct purpose, exhibiting functional cohesiveness.

Coupling :

The coupling between classes appears to be relatively low. For example:
The User class interacts with the ElevatorController to request elevator assignment, but it doesn't directly manipulate elevator objects.
The ElevatorController interacts with elevator objects but doesn't directly manipulate user objects.
Classes interact through well-defined interfaces, rather than directly accessing each other's attributes, indicating loose coupling.

Overall, the code demonstrates functional cohesion, as each class encapsulates related functionalities, and low coupling, as there is minimal direct interaction between classes, promoting modularity and ease of maintenance.

Refactoring :

The refactoring applied in the provided code can be categorized into several types:
Encapsulation:
Attribute Encapsulation: Properties and setters are used to encapsulate class attributes, ensuring controlled access and modification.
Consistent Naming Convention:
Naming Conventions: Consistent naming conventions are followed throughout the code, such as using underscore prefixes for private attributes.
Remove Redundancy:
Elimination of Redundancy: Redundant or unnecessary code, such as redundant comments, is removed to improve clarity and conciseness.
Comments:
Documentation: Comments are added to explain the purpose of certain parts of the code, such as where coupling occurs and where refactoring was applied.
Overall:
The refactoring aims to improve readability, maintainability, and extensibility of the codebase by encapsulating attributes, following consistent naming conventions, eliminating redundancy, and adding appropriate documentation.




