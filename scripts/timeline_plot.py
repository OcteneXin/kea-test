import matplotlib.pyplot as plt
import seaborn as sns

# 假设你有一个页面序列列表，例如：
pages = ['A', 'A', 'A', 'B', 'B', 'C', 'A', 'A', 'D', 'E']
unique_pages = list(set(pages))
page_to_id = {p: i for i, p in enumerate(unique_pages)}
page_ids = [page_to_id[p] for p in pages]

plt.figure(figsize=(12, 2))
sns.heatmap([page_ids], cmap="tab20", cbar=False, xticklabels=False)
plt.yticks([], [])
plt.title("Page Timeline")
plt.xlabel("Time step")
plt.show()
