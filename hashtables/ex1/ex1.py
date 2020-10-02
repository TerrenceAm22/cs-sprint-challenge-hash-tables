def get_indices_of_item_weights(weights, length, limit):
    """
    Function to get
    item weights
    """
    # Your code here
    if limit < 0 or len(weights) < 2 or length < 2:
        return None

    weightsDict = {}
    for index in range(length):
        weightsDict[weights[index]] = index

    i = 0
    for weight in weights:
        if weightsDict.get(limit - weight):
            return (weightsDict.get(limit - weight), i)
        i += 1


    return None
