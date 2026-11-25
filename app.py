tasks = ["Learn Git branching", "Resolve a merge conflict"]

def main():
    print("=== MY DAILY TASKS ===")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

if __name__ == "__main__":
    main()
    print("All tasks listed successfully.")
