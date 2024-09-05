import time


def data_stream():
    """Simulate a data stream."""
    for i in range(10):
        time.sleep(1)  # Simulate data arriving every second
        yield i


def stream_processor(data_stream):
    """Process data from the stream."""
    for data in data_stream:
        processed_data = data * 2  # Example processing step
        yield processed_data


# Usage
stream = data_stream()
processed_stream = stream_processor(stream)
for data in processed_stream:
    print(data)
