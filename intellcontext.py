from typing import List, Optional
from haystack.document_store.memory import InMemoryDocumentStore
from haystack.query import SearchQuery
from haystack.retriever.dense import DensePassageRetriever
from haystack.reader.deep_qa_reader import DeepQAReader

def search_nav(
    documents: List[dict], 
    hovered_text: str,
    payload_range: tuple,
    source_document: dict,
    retriever: Optional[DensePassageRetriever] = None,
    reader: Optional[DeepQAReader] = None,
) -> List[dict]:
    

    results = []

    source_definition = None
    if source_document.get("symbol_locations"):
        for symbol in source_document["symbol_locations"]:
            if symbol["range"] == payload_range and symbol["kind"] == "definition":
                source_definition = symbol
                break

    for doc in documents:
        if doc["file_path"] == source_document.get("file_path"):
            continue  


        occurrences = []
        for start, end in matches:
            is_definition = (
                source_definition is None
                or source_definition["range"] != (start, end)
            )
            occurrence = {
                "range": (start, end),
                "kind": "definition" if is_definition else "reference",
            }

            if retriever and reader:
                passage = doc["content"][start:end]
                query = SearchQuery(query=hovered_text, passage=passage)
                answer = reader.predict(query=query, retriever=retriever)
                occurrence["snippet"] = answer.answers[0]["answer"]

            occurrences.append(occurrence)

        if occurrences:
            results.append({"file_path": doc["file_path"], "data": occurrences})

    return results

hovered_text = "my_function"
payload_range = (10, 20)
source_document = {"file_path": "main.py"}

results = search_nav(documents, hovered_text, payload_range, source_document)

print(results)

