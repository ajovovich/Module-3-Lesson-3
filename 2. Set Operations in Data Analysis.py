#Task 1: Duplicate Entries Cleanup

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

unique_ids = set(customer_ids)
sorted_unique_ids = sorted(unique_ids)

print("The unique ids are as followed:", sorted_unique_ids)