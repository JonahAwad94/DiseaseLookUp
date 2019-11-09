# DiseaseLookup
 Disease Look Up based on Hetionet's Database
 
 # Collaborators:
 
 Jonah Alexander-Awad
 
 Eric Benjamin 


# Prequisites to run:
- Python
- Py2neo
- Neo4j community edition with your data loaded. If you want to use HetioNet, visit:
- https://github.com/hetio/hetionet/tree/master/hetnet/neo4j (make sure "dbms.allow_upgrade" is uncommented and set to true in the "conf" folder in your neo4j installation

# Instructions:
- Place nodes.tsv and edges.tsv in same directory as main.py
- Run "net start neo4j" in bin folder of your neo4j to start up neo4j service
- Create password if first time in neo4j browser
- Change "neo4jPassword" variable at the top of main.py to whatever password you created
- Run main.py

- Option 1 - Lookup Disease Information
  - Select 1, type in name of disease you wish to lookup. If disease is found in database, it will return the following:
    - Compounds that palliate the disease
    - Compounds that treat the disease
    - Genes associated with the disease
    - Genes that upregulate the disease
    - Genes that downregulate the disease
    - Anatomy the disease is typically located on
- Option 2 - Lookup undiscovered treatments for diseases
  - Select 2, a list of compounds and disease that they may be able to treat will be queried


# Disease Lookup Example - Migraine
<img src="/migraine-example.jpg">
