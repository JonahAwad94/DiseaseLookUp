# DiseaseLookUp
 Disease Look Up based on Hetionet's Database
 
 Collaborators:
 Jonah Alexander-Awad
 
 Eric Benjamin 


Prequisites to run:
- Python
- Py2neo
- Neo4j community edition with your data loaded. If you want to use HetioNet, visit:
- https://github.com/hetio/hetionet/tree/master/hetnet/neo4j (make sure "dbms.allow_upgrade" is uncommented and set to true in the "conf" folder in your neo4j installation

Instructions:
- Place nodes.tsv and edges.tsv in same directory as main.py
- Run "net start neo4j" in bin folder of your neo4j to start up neo4j service
- Create password if first time in neo4j browser
- Change "neo4jPassword" variable at the top of main.py to whatever password you created
- Run main.py
