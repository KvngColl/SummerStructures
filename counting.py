#counting the most common school names

schools = ['Ashesi', 'KNUST', 'Ashesi', 'UCC', 'KNUST', 'UPSA', 'Ashesi']
from collections import Counter
school_counts = Counter(schools)
top_school = school_counts.most_common(2)
print(top_school)
