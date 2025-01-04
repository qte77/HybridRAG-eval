import pytest
from unittest.mock import Mock
from llm_api import LLM
from vector_db import VectorDB
from databases.KnowledgeGraph import KnowledgeGraph
from databases.GraphRAG import GraphRAG
from databases.HybridRAG import HybridRAG
from databases.VectorRAG import VectorRAG

@pytest.fixture
def mock_graph_db():
    return Mock(spec=KnowledgeGraph)

@pytest.fixture
def mock_vector_db():
    return Mock(spec=VectorDB)

@pytest.fixture
def mock_llm():
    return Mock(spec=LLM)

@pytest.mark.parametrize("rag_class, db_fixture", [
    (GraphRAG, "mock_graph_db"),
    (VectorRAG, "mock_vector_db"),
    (HybridRAG, "mock_vector_db")
])
def test_all_rag_query(rag_class, db_fixture, mock_graph_db, mock_vector_db, mock_llm, request):
    rag = rag_class()
    db = request.getfixturevalue(db_fixture)
    
    if isinstance(rag, HybridRAG):
        rag.vector_db = mock_vector_db
        rag.kg = mock_graph_db
    else:
        setattr(rag, db_fixture.split('_')[1], db)
    
    rag.llm = mock_llm
    
    db.retrieve.return_value = "Sample context"
    mock_llm.generate.return_value = "Sample answer"
    
    question = "What is the capital of France?"
    answer, runtime = rag.query(question)
    
    assert answer == "Sample answer"
    assert isinstance(runtime, float)
    
    if isinstance(rag, HybridRAG):
        mock_vector_db.retrieve.assert_called_once_with(question)
        mock_graph_db.retrieve.assert_called_once_with(question)
        mock_llm.generate.assert_called_once()
    else:
        db.retrieve.assert_called_once_with(question)
        mock_llm.generate.assert_called_once_with(question, "Sample context")

    if isinstance(rag, HybridRAG):
        assert hasattr(rag, 'combine_contexts'), "HybridRAG should have a combine_contexts method"
