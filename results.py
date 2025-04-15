import os
import matplotlib.pyplot as plt

############################################
# Part 1: Stacked Horizontal Bar Chart
############################################

# Define segment sizes (in bytes)
segments = {
    '__TEXT': 16384,
    '__DATA_CONST': 16384,
    '__DATA': 16384,
    '__LINKEDIT': 10720,
}

# Colors for the segments
colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B2']

# Create a horizontal bar (stacked chart)
fig1, ax1 = plt.subplots(figsize=(10, 2))
start = 0
for i, (seg, size) in enumerate(segments.items()):
    ax1.barh(0, size, left=start, height=0.4, label=seg, color=colors[i % len(colors)])
    # Add a label in the middle of each segment
    ax1.text(start + size / 2, 0, f"{seg}\n{size} bytes",
             ha='center', va='center', color='white', fontsize=9)
    start += size

ax1.set_xlim(0, sum(segments.values()))
ax1.set_yticks([])
ax1.set_xlabel("Size (bytes)")
ax1.set_title("Memory Layout (Selected Segments) for -O0")
ax1.legend(loc='upper right')
plt.tight_layout()
plt.savefig("diagrams/memory_layout.png")

############################################
# Part 2: Side-by-Side Bar Chart Comparison
############################################
sections = ['__text']
size_O0 = [3112]  # Size for -O0
size_O2 = [1120]  # Size for -O2

fig2, ax2 = plt.subplots()
x = range(len(sections))
width = 0.35  # Width of the bars

ax2.bar(x, size_O0, width, label='-O0', color='blue')
ax2.bar([p + width for p in x], size_O2, width, label='-O2', color='orange')

ax2.set_xticks([p + width/2 for p in x])
ax2.set_xticklabels(sections)
ax2.set_ylabel('Section size (bytes)')
ax2.set_title('Comparison of __text Section Size: -O0 vs -O2')
ax2.legend()
plt.tight_layout()
plt.savefig("diagrams/text_size_comparison.png")

# Display both figures
plt.show()
