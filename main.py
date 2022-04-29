from median_heap import MedianHeap


def main() -> None:
    median_heap = MedianHeap()

    values = [1, 2, 3, 4, 5]  # Change the values here to experiment with the code

    median_heap.add_values(values)

    print(f"Current median value is: {median_heap.get_median()}")


if __name__ == "__main__":
    main()
