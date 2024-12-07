import time
from Queue import Queue
from Queue_With_List import Queue_With_List

def performance_test(num_items):
    # Test Queue_With_List
    list_queue = Queue_With_List()
    start_time = time.time()
    for i in range(num_items):
        list_queue.enqueue(i)
    enqueue_time_list = time.time() - start_time
    
    start_time = time.time()
    for _ in range(num_items):
        list_queue.dequeue()
    dequeue_time_list = time.time() - start_time
    
    # Testing listing implementation
    linked_queue = Queue()
    start_time = time.time()
    for i in range(num_items):
        linked_queue.enqueue(i)
    enqueue_time_linked  = time.time() - start_time
    
    start_time = time.time()
    for _ in range(num_items):
        linked_queue.dequeue()
    dequeue_time_linked = time.time() - start_time
    
    return{ 
        "num_items": num_items,
        "enqueue_time_list": enqueue_time_list,
        "dequeue_time_list": dequeue_time_list,
        "enqueue_time_linked": enqueue_time_linked,
        "dequeue_time_linked": dequeue_time_linked,
        
    }

def main():
    test_sizes = [1000, 10000, 100000, 1000000]
    results = []
    
    for size in test_sizes:
        result = performance_test(size)
        results.append(result)
        print(f"Results for {size} items:")
        print(f"  List Queue Enqueue Time: {result['enqueue_time_list']:.6f} seconds")
        print(f"  List Queue Dequeue Time: {result['dequeue_time_list']:.6f} seconds")
        print(f"  Linked Queue Enqueue Time: {result['enqueue_time_linked']:.6f} seconds")
        print(f"  List Queue Dequeue Time: {result['dequeue_time_linked']:.6f} seconds")
        print()

if __name__ == "__main__":
    main()