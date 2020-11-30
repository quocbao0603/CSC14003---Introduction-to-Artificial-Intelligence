
def merge_bindings(first_bindings_map, second_bindings_map):

    if first_bindings_map is None or second_bindings_map is None:
        return None

    merged_bindings = {}

        # Process our first bindings map and add the variable bindings to our merged map
    for variable, value in first_bindings_map.items():
        merged_bindings[variable] = value

        # Process our second bindings map and verify that the bindings contain in
        # this map align with the bindings from our first binding map. If any
        # variable bindings do not align, we return None. Otherwise, we process any
        # matching items and continue iterating through our binding map adding each
        # binding to our merged map.
    for variable, value in second_bindings_map.items():
        merged_bindings[variable] = value

    return merged_bindings