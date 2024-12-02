# import chromadb

# # Client chromaDB
# chromadb_client = chromadb.Client()

# # Créer une collection
# collection = chromadb_client.create_collection(name="Personne")

# # Créer un document

# collection.add(

#         documents=[
#             "Salut, les amis de la Data !",
#             "J'aime la Data Science."
#         ],

#         ids=["id1", "id2"]

# )

# # Interroger la collection
# results = collection.query(

#     query_texts=["Data"],
#     n_results=1
# )

# print(results)
# print(results['documents'][0][0])

# print(collection.name)
# print(collection.json())
# print(collection.count())
# print(collection.get(ids=["id2"]))

# Projet 1

# import chromadb

# client_chroma = chromadb.Client()

# col = client_chroma.get_or_create_collection(name="books")

# col.upsert(

#     documents=[
#             "Livre Python à 50 €",
#             "Livre R à 15 €",
#             "Livre Java 49 €",
#             "Livre JavaScript à 18 €"
#     ],

#     ids=["id1", "id2", "id3", "id4"]
# )

# text = input("Tapez votre requête en langage naturel: ")

# results = col.query(

#     query_texts=text,
#     n_results=1

# )

# print(results['documents'][0][0])
# print(col.count())
# print(col.name)

# Lancement d'un client Chroma persistant
# import chromadb

# client = chromadb.PersistentClient()

# coll = client.get_or_create_collection(name="voitures")

# text_user = input("Que voulez-vous ?")

# coll.upsert(

#     documents=[
#         "DavRos",
#         "BMW",
#         "VX",
#         "RAV4"
#     ],

#     ids=["id1", "id2", "id3", "id4"]
# )

# results = coll.query(
#     query_texts=text_user,
#     n_results=1
# )

# print(results["documents"][0][0])

# Projet 3

# import chromadb

# client_db = chromadb.HttpClient(host='localhost', port=8000)


# Projet final

import chromadb
import csv

client = chromadb.PersistentClient()

col = client.get_or_create_collection(name="diamonds")

csv_file_path = "population.csv"

documents = []
ids = []

with open(csv_file_path, mode="r", encoding="ISO-8859-1") as file:
    csv_reader = csv.DictReader(file, delimiter=",")
    print("CSV columns: ", csv_reader.fieldnames)

    for idx, row in enumerate(csv_reader):
        # Concaténer les colonnes en une seule chaîne de texte
        # document = f"Carat: {row['carat']}, Cut: {row['cut']}, Color: {row['color']}, Clarity: {row['clarity']}, Depth: {row['depth']}, Table: {row['table']}, Price: {row['price']}, Dimensions: ({row['x']} x {row['y']} x {row['z']})"
        document = f"Country: {row['Country']}, Population: {row['Population']}"
        documents.append(document)
        ids.append(f"id_{idx}")  # Génère un ID unique pour chaque ligne

# Insérez les données dans la collection
col.upsert(
    documents=documents,
    ids=ids
)

# Effectuez une requête
results = col.query(
    query_texts=["Donne-moi la population de la Chine."],
    n_results=2
)

print(results['documents'][0][0])