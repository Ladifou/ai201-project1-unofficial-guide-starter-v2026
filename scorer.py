from store import Result
from rapidfuzz import fuzz

def judge(question: str, expects: str, answer: str, results: list[Result]) -> bool:
    """Use Rapidfuzz as alternative"""
    passed = judge_with_rapidfuzz(question, expects, answer, results)
    return passed

def retrieval_hits(expects: str, results: list[Result]) -> bool:
    """Check if the expected answer is in the retrieved results"""
    for result in results:
        if expects.lower().strip() in result.text.lower().strip():
            return True
    return False

def judge_with_rapidfuzz(question: str, expects: str, answer: str, results: list[Result]) -> bool:
    """Use Rapidfuzz to check if the expected answer is in the retrieved results"""
    
    for result in results:
        if fuzz.partial_ratio(expects.lower().strip(), result.text.lower().strip()) > 80:
            return True
    return False