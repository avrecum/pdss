This project emerged out of pure boredom during the SARS-CoV-2 pandemic. It's basically just me trying to figure out the workings of Python, Flask, Flask-restful while practicing some common data structures all at once.

# What is PDSS?
PDSS (Python Data Structure Server) is an in-memory store for simple and more complex data structures with a REST interface to perform queries on them.

## Workflow:
The user:
- requests a new instance of a data structure of their choice, which is initialized in memory and assigned a unique ID. This ID is returned upon initialization and can be used by the user to access the data structure.
- performs operations on these data structures.
- destroys the data structure after it is no longer needed.

