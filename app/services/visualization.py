import matplotlib.pyplot as plt
from io import BytesIO

def create_bar_chart(data):
    if data and isinstance(data[0], tuple):
        x, y = zip(*data) if len(data[0]) == 2 else ([], [])
    else:
        x, y = ["A", "B"], [10, 15]  # Fallback data

    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color="skyblue")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Generated Chart")
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    return buffer
