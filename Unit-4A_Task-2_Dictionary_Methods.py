# Example solution: dictionary methods
data = {"a": 90, "b": 89, "c": 30}
print("Keys:", data.keys())
print("Values:", data.values())
print("Items:", data.items())
print("get b:", data.get("b"))
print("get z:", data.get("z"))

data.update({"b": 78, "d": 47})
print("After update:", data)

removed = data.pop("a")
print("Removed:", removed)
print("After pop:", data)