def similar(self, k, simularity):
    """
    Return the K most similar restuarants to SELF, using SIMILARITY for comparison.
    """
    
    others = list(Restaurant.all)
    
    others.remove(self)
    
    return sorted(others, key=lambda r: -simularity(self, r))[:k]

    