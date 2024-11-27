import matplotlib.pyplot as plt
from io import BytesIO

def create_bar_chart(data):
    graphTitle = 'Generated Chart'
    data = data
    print('data:---->', data, 'Bool =>', len(data) > 0 and isinstance(data[0], tuple), 'Type of data ', type(data))
    # Check if data has valid tuples with both X and Y values
    if len(data) > 0 and isinstance(data, list):
        # Handle single-element tuples by assigning a default Y value (e.g., 1)
        print('if case : --->', len(data) > 0 and isinstance(data[0], tuple))
        if len(data[0]) == 1:
            x = [item[0] for item in data]
            y = [1] * len(data)  # Assign default Y value as 1 for all
            graphTitle = 'Data only contains labels x; default Y values applied'
        elif len(data[0]) == 2:
            x, y = zip(*data)
        else:
            x, y = [], []
            graphTitle = 'Invalid data format'
    else:
        print('Else case ---->')
        # Fallback data in case of completely invalid input
        fallback_data = [{"x_column": "A", "y_column": 10}, {"x_column": "B", "y_column": 15}]
        x = [item["x_column"] for item in fallback_data]
        y = [item["y_column"] for item in fallback_data]
        graphTitle = 'Data format is incorrect or empty'

    print('graphTitle: ', graphTitle)
    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    if x and y:  # Ensure x and y are not empty
        plt.bar(x, y, color='skyblue')
    else:
        graphTitle = 'No valid data to display'
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")
    plt.title(graphTitle)
    plt.tight_layout()

    # Save the chart to a buffer
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    return buffer

