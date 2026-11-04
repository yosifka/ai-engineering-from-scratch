def process_data(items: list[int]) -> list[int]:
    results = []
    for item in items:
        # We want to inspect what happens here
        doubled = item * 2
        results.append(doubled)
    return results


data = [10, 20, 30]
final_output = process_data(data)
print(f"Done: {final_output}")
