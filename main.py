from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue

def test_structure(structure):
    """Helper function to print a structure's current state and status flags."""
    print(structure)
    try:
        full = structure.is_full()
    except AttributeError:
        full = "N/A"
    print(f"is_empty: {structure.is_empty()}, is_full: {full}")

def application_stack_balanced():
    """Lab Exercise 5.1 Item 6a: Balanced Parentheses Check via LinkedStack"""
    def is_balanced(s):
        stack = LinkedStack()
        mapping = {')':'(', ']':'[', '}':'{'}
        for ch in s:
            if ch in '([{':
                stack.push(ch)
            elif ch in ')]}':
                if stack.is_empty() or stack.pop() != mapping[ch]:
                    return False
        return stack.is_empty()

    tests = ["{([])}", "([)]", "((()))", "{[}]", ""]
    print("\nApplication 6a: Balanced Parentheses")
    for t in tests:
        print(f"{t or 'empty'} -> {'Balanced' if is_balanced(t) else 'Not Balanced'}")

def application_queue_print():
    """Lab Exercise 5.1 Item 6b: Print Queue Spooling Simulation via LinkedQueue"""
    print("\n--- Application 6b: Print Queue Simulation (FIFO) ---")
    q = LinkedQueue()
    jobs = [("Job1", 5), ("Job2", 2), ("Job3", 10)]
    for job_id, pages in jobs:
        q.enqueue((job_id, pages))
        print(f"Enqueued {job_id} with {pages} pages. {q}")

    total_wait = 0
    while not q.is_empty():
        job_id, pages = q.dequeue()
        print(f"Printing {job_id} ({pages} pages) - Wait time before: {total_wait} pages")
        total_wait += pages

def run_error_samples():
    """Lab Exercise 5.2 Deliverable 2: Explicit error and boundary demonstrations"""
    print("\nSample Runs: Error Handling (Underflow & Overflow)")
    
    print("\n1. ArrayStack Overflow Test (capacity 2):")
    s = ArrayStack(2)
    s.push("A"); print(s)
    s.push("B"); print(s)
    try:
        s.push("C")
    except OverflowError as e:
        print(f"Caught expected overflow: {e}")

    print("\n2. ArrayStack Underflow Test:")
    s = ArrayStack(2)
    try:
        s.pop()
    except IndexError as e:
        print(f"Caught expected underflow on pop: {e}")
    try:
        s.peek()
    except IndexError as e:
        print(f"Caught expected underflow on peek: {e}")

    print("\n3. LinkedStack Underflow Test:")
    ls = LinkedStack()
    try:
        ls.pop()
    except IndexError as e:
        print(f"Caught expected underflow: {e}")

    print("\n4. ArrayQueue Overflow & Wrap-Around Demo (capacity 3):")
    q = ArrayQueue(3)
    q.enqueue("A"); q.enqueue("B"); q.enqueue("C")
    print(q)
    try:
        q.enqueue("D")
    except OverflowError as e:
        print(f"Caught expected overflow: {e}")
    print(f"Dequeued: {q.dequeue()}")
    print(f"After dequeue, front wrapped: {q}")
    q.enqueue("D")
    print(f"After enqueue D (wrap-around reused): {q}")

    print("\n5. ArrayQueue Underflow Test:")
    q2 = ArrayQueue(2)
    try:
        q2.dequeue()
    except IndexError as e:
        print(f"Caught expected underflow: {e}")

def main():
    print("Module 5: Stacks and Queues - Test Driver")
    
    print("\n1. ArrayStack Demo")
    s = ArrayStack(3)
    s.push("A"); test_structure(s)
    s.push("B"); test_structure(s)
    s.push("C"); test_structure(s)
    print(f"Popped: {s.pop()}"); test_structure(s)

    print("\n2. LinkedStack Demo")
    ls = LinkedStack()
    ls.push("X"); test_structure(ls)
    ls.push("Y"); test_structure(ls)
    print(f"Popped: {ls.pop()}"); test_structure(ls)

    print("\n3. ArrayQueue Demo")
    q = ArrayQueue(3)
    q.enqueue("A"); test_structure(q)
    q.enqueue("B"); test_structure(q)
    q.enqueue("C"); test_structure(q)
    print(f"Dequeued: {q.dequeue()}"); test_structure(q)
    q.enqueue("D"); test_structure(q)

    print("\n4. LinkedQueue Demo")
    lq = LinkedQueue()
    lq.enqueue("1"); test_structure(lq)
    lq.enqueue("2"); test_structure(lq)
    print(f"Dequeued: {lq.dequeue()}"); test_structure(lq)

    application_stack_balanced()
    application_queue_print()

    run_error_samples()

if __name__ == "__main__":
    main()
