def consolidate_data(name, data):
    # Consolidate data by gender
    consolidated = {}
    for entry in data:
        gender = entry.get("gender", "unknown").lower()
        usages = entry.get("usages", [])
        if gender not in consolidated:
            consolidated[gender] = []
        consolidated[gender].extend([usage["usage_full"] for usage in usages])

    # Format the consolidated result
    result = [
        f"Name: {name.capitalize()}\nGender: {gender}\nUsage: {', '.join(sorted(set(usages)))}"
        for gender, usages in consolidated.items()
    ]

    return "\n\n".join(result)
