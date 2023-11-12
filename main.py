from src.ui import get_initial_state, print_initial_state, menu

def main():
    initial_state = get_initial_state()
    print_initial_state(initial_state)
    selected_option = menu()

    print(selected_option)

if __name__ == "__main__":
    main()
