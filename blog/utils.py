from .models import Blog
def get_result(res):
    """get result for take 50 char of description(a field on blog model)"""
    result = {}
    for r in res:
        result[r.id] = r.description[:50]
    return result
