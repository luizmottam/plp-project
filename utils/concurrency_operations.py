import threading

# Exemplos de funções que poderiam ser utilizadas para concorrência
def run_in_thread(target, *args):
    thread = threading.Thread(target=target, args=args)
    thread.start()
    return thread

def example_concurrent_function():
    print("This is running in a separate thread")
