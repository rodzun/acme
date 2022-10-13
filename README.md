# README
This is my implementation for ioet, acme challenge. It was implemented with Object-Oriented Programming Paradigm in mind. 

It contains one main class (*ACME*) with the necessary methods in order to work with the strings containing the data (*nameDaysSplitter, daysSplitter, dayNameTimesSplitter, hoursSplitter* methods), calculate the payment per person (*personPayment* method) and print the total payment for all the people in the data file (*totalPayments* method).

The solution has the following files:
- ***acme_solution.py***: File containing the logic that solves the problem and shows the solution required.
- ***constants.py***: File containing constant data used by the class ACME. It helps for future maintenance and scalability purposes, as well if days, time intervals or fees change.
- ***test_acme.py***: File containing test cases using [*unittest*](https://docs.python.org/3/library/unittest.html).
- ***data.txt***: File containing data. In this particular case used *by acme_solution.py* and *test_acme.py*. Contains five persons data.
- ***README.md***: This file, containing general information about the solution presented.


## Requirements
The solution was developed with, and is required to have installed locally or via virtual environments the following:
- Python 3.8.10

## Usage
- To run the main solution (*acme_solution.py*) use the following:
    ```shell
    $ python acme_solution.py
    ```
- To run all test cases use the following:
    ```shell
    $ python test_acme.py
    ```
    or 
    ```shell
    $ python -m unittest
    ```
    or 
    ```shell
    $ python -m unittest -v
    ```
    for a more verbosed output with names on each testcase tested.