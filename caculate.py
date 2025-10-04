def paginate(data: list, page: int = 1, per_page: int = 10):
    """
    Paginate a list of items.
    """
    total = len(data)
    start = (page - 1) * per_page
    end = start + per_page
    items = data[start:end]

    return {
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": (total + per_page - 1) // per_page,
        "items": items
    }


# Example usage
data = list(range(1, 51))  # 50 items
result = paginate(data, page=2, per_page=10)
print(result)
