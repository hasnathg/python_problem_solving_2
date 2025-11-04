# Example 1: Subscription Overlaps
# Find common subscribers
news_sub = {"alice@mail.com", "bob@mail.com", "charlie@mail.com"}
blog_sub = {"bob@mail.com", "diana@mail.com", "alice@mail.com"}

common = news_sub.intersection(blog_sub)
only_news = news_sub - blog_sub
all_subs = news_sub.union(blog_sub)

print(f"Common subscribers: {common}")
print(f"News-only subscribers: {only_news}")
print(f"All subscribers: {all_subs}")

# Example 2: Unique Entry Filter
# Filter duplicate sensor readings
readings = [22.1, 22.5, 22.1, 23.0, 22.5, 22.1]
unique = set()
duplicates = set()

for value in readings:
    if value in unique:
        duplicates.add(value)
    else:
        unique.add(value)

print(f"Original: {len(readings)} readings")
print(f"Unique values: {unique}")
print(f"Duplicate values: {duplicates}")