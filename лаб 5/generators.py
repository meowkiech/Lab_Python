def dish_generator_by_category(data, target_category):
    for line in data:
        if line.category.lower() == target_category.lower():
            yield line