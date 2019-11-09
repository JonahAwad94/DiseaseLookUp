import csv
import sys
from os import system, name
from collections import defaultdict
from py2neo import Graph, Database, cypher, NodeMatcher, Relationship

    # Clear screen function for windows and unix systems
def clearScreen():
    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for unix
    else: 
        _ = system('clear')

clearScreen()
print("Loading...")
print("[----------]")

# get disease names and codes from 'nodes.tsv'
# diseaseCode{'DiseaseName' : 'DiseaseCode'}
def fetchDiseaseCode():
    d={}
    with open('nodes.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
        # append dictionary
            if (row['kind'] == 'Disease'):
                d[row['name']] = row['id']
    return d
diseaseCodeList = fetchDiseaseCode()

clearScreen()
print("Loading...")
print("[#---------]")

# Create a dictionary with compound names
# compoundNames {'compoundCode':'compoundName'}
def fetchCompoundNameList():
    d={}
    with open('nodes.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
        # append dictionary
            if (row['kind'] == 'Compound'):
                d[row['id']] = row['name']
    return d
compoundNameList = fetchCompoundNameList()

clearScreen()
print("Loading...")
print("[##--------]")


# Create a dictionary with anatomy names
# anatomyNames {'anatomyCode':'anatomyName'}
def fetchAnatomyNameList():
    d={}
    with open('nodes.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
        # append dictionary
            if (row['kind'] == 'Anatomy'):
                d[row['id']] = row['name']
    return d
anatomyNameList = fetchAnatomyNameList()

clearScreen()
print("Loading...")
print("[###-------]")


# Create a dictionary with Gene names
# GeneNames {'geneCode':'GeneName'}
def fetchGeneNameList():
    d={}
    with open('nodes.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
        # append dictionary
            if (row['kind'] == 'Gene'):
                d[row['id']] = row['name']
    return d
geneNameList = fetchGeneNameList()

clearScreen()
print("Loading...")
print("[####------]")

# Create Compound palliates Disease dictionary
# CpD {'DiseaseCode' : 'CompoundCode'}
def fetchCpD():
    d = defaultdict(list)
    with open('edges.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
        # append dictionary
            if (row['metaedge'] == 'CpD'):
                d[row['target']].append(row['source'])
    return d
CpD = fetchCpD()

clearScreen()
print("Loading...")
print("[#####-----]")


# Create Compound treats Disease Dictionary
# CtD {'DiseaseCode':'CompoundCode'}
def fetchCtD():
    d= defaultdict(list)
    with open('edges.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
        # append dictionary
            if (row['metaedge'] == 'CtD'):
                d[row['target']].append(row['source'])
    return d
CtD = fetchCtD()

clearScreen()
print("Loading...")
print("[######----]")


# Create Disease associated with Gene Dictionary
# DaG {'DiseaseCode':'GeneCode'}
def fetchDaG():
    d = defaultdict(list)
    with open('edges.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
        # append dictionary
            if (row['metaedge'] == 'DaG'):
                d[row['source']].append(row['target'])
    return d
DaG = fetchDaG()

clearScreen()
print("Loading...")
print("[#######---]")


# Create Disease upregulates with Gene Dictionary
# DuG {'DiseaseCode':'GeneCode'}
def fetchDuG():
    d= defaultdict(list)
    with open('edges.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
        # append dictionary
            if (row['metaedge'] == 'DuG'):
                d[row['source']].append(row['target'])
    return d
DuG = fetchDuG()

clearScreen()
print("Loading...")
print("[########--]")

# Create Disease downregulates with Gene Dictionary
# DdG {'DiseaseCode':'GeneCode'}
def fetchDdG():
    d= defaultdict(list)
    with open('edges.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
        # append dictionary
            if (row['metaedge'] == 'DdG'):
                d[row['source']].append(row['target'])
    return d
DdG = fetchDdG()

clearScreen()
print("Loading...")
print("[#########-]")


# Create Disease downregulates with Gene Dictionary
# DlA {'DiseaseCode':'AnatomyCode'}
def fetchDlA():
    d= defaultdict(list)
    with open('edges.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
        # append dictionary
            if (row['metaedge'] == 'DlA'):
                d[row['source']].append(row['target'])
    return d
DlA = fetchDlA()

clearScreen()
print("Complete.")

def query1():
    disease = input("Enter Disease name. ")

    # get disease code
    if disease in diseaseCodeList:
        diseaseCode = diseaseCodeList[disease]
    else:
        print(disease + " is not a known disease. Please check your spelling. ")
        start()

    # get compound that palliates disease name
    if diseaseCode in CpD:
        compoundPalliateCodeList = CpD[diseaseCode] #CpD returns a list of compounds that palliate user's disease

        compoundPalliateNameList = []
        for i in compoundPalliateCodeList:
            compoundPalliateNameList.append(compoundNameList[i])

        print("The following compounds palliate " + disease + ":\n")
        print(*compoundPalliateNameList, sep = ", ")
    else:
        print("There are no compounds that palliate " + disease)



    # get compound that treats disease name
    if diseaseCode in CtD:
        compoundTreatCodeList = CtD[diseaseCode]

        compoundTreatNameList = []
        for i in compoundTreatCodeList:
            compoundTreatNameList.append(compoundNameList[i])

        print("\n\nThe following compounds treat " + disease + ":\n")
        print(*compoundTreatNameList, sep = ", ")
    else:
        print("\n\nThere are no compounds that treat " + disease)


    # get Gene Associated with disease
    if diseaseCode in DaG:
        geneAssociationCodeList = DaG[diseaseCode]

        geneAssociationNameList = []

        #check if empty
        if geneAssociationCodeList != []:
            for i in geneAssociationCodeList:
                geneAssociationNameList.append(geneNameList[i])

            print("\n\nThe following genes are associated with " + disease + ":\n")
            print(*geneAssociationNameList, sep = ", ")
    else:
        print("\n\nThere are no genes associated with " + disease)


    # get Gene upregulates disease
    if diseaseCode in DuG:
        geneUpregulateCodeList = DuG[diseaseCode]

        geneUpregulateNameList = []

        if geneUpregulateCodeList != []:
            for i in geneUpregulateCodeList:
                geneUpregulateNameList.append(geneNameList[i])

            print("\n\nThe following genes upregulate " + disease + ":\n")
            print(*geneUpregulateNameList, sep = ", ")
    else:
        print("\n\nThere are no genes that upregulate " + disease)


    # get Gene downregulates disease
    if diseaseCode in DdG:
        geneDownregulateCodeList = DdG[diseaseCode]

        geneDownregulateNameList = []

        if geneDownregulateCodeList != []:
            for i in geneDownregulateCodeList:  
                geneDownregulateNameList.append(geneNameList[i])

            print("\n\nThe following genes downregulates " + disease + ":\n")
            print(*geneDownregulateNameList, sep = ", ")

    else:
        print("\n\nThere are no genes that downregulate " + disease)
    


    # get disease location
    if diseaseCode in DlA:
        diseaseLocationCodeList = DlA[diseaseCode]

        diseaseLocationNameList = []

        if diseaseLocationCodeList != []:
            for i in diseaseLocationCodeList:  
                diseaseLocationNameList.append(anatomyNameList[i])

            print("\n\n" + disease + " is usually located at the following locations:\n")
            print(*diseaseLocationNameList, sep = ", ")

    else:
        print("\n\nThere are no genes that downregulate " + disease)
    
    print("\n\n")
    start()



def query2():
    db = Database("bolt://localhost:7687")
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "firstproject"))

    # Query Limits set to 100 (25x4), to increase number of disease / compounds pairs, set "LIMIT" to higher value for the following 4 queries:

    query2List = graph.run("MATCH p=(compound:Compound)-[RESEMBLES]->(:Compound)-[u:UPREGULATES_CuG]->(gene:Gene)<-[DOWNREGULATES_AdG]-(:Anatomy)<-[LOCALIZES_DlA]-(disease:Disease) RETURN compound.name,disease.name LIMIT 25").data()

    query2List.append(graph.run("MATCH p=(compound:Compound)-[RESEMBLES]->(:Compound)-[DOWNREGULATES_CdG]->(gene:Gene)<-[UPREGULATES_AuG]-(:Anatomy)<-[LOCALIZES_DlA]-(disease:Disease) RETURN compound.name,disease.name LIMIT 25").data())

    query2List.append(graph.run("MATCH p=(compound:Compound)-[DOWNREGULATES_CdG]->(gene:Gene)<-[UPREGULATES_AuG]-(:Anatomy)<-[LOCALIZES_DlA]-(disease:Disease) RETURN compound.name,disease.name LIMIT 25").data())

    query2List.append(graph.run("MATCH p=(compound:Compound)-[UPREGULATES_CuG]->(gene:Gene)<-[DOWNREGULATES_AdG]-(:Anatomy)<-[LOCALIZES_DlA]-(disease:Disease) RETURN compound.name,disease.name LIMIT 25").data())

    # query2List = list( dict.fromkeys(query2List) )

    print("The following compounds may treat their respective diseases and should be researched more.\n\n")
    print(query2List)

    start()



def start():
    
    userInput = input('\nSelect an Option:\nLookup Disease Information (Press 1)\nLookup undiscovered treatments for diseases (Press 2)\nExit program (Press 3).')

    if userInput == "1":
        clearScreen() 
        query1()

    if userInput == "2":
        clearScreen()    
        query2()

    else:
        sys.exit()


# initial run
start()