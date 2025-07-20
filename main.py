from Bio import Entrez

Entrez.email = "mylarulakshmidevi@gmail.com"  

def search_papers(query):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=5)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]

if __name__ == "__main__":
    query = input("Enter your search query: ")
    ids = search_papers(query)
    print("Found PubMed IDs:", ids)
