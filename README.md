# repo-analyser

Small tool to analyse repos and their development over time. Some potential questions to answer with this tool:

* Total lines of code
* Lines of code per file and file type
* Average line length

This data should be persistable to either flat files or a database. The application is structured with a cli and a database repository that both depend on the business logic. Should filepath->open file also be abstracted out of main so it can take a socket or stream instead of actual file?

Project requirements so far should just be pytest. Then pylint, pipx for development requirements.