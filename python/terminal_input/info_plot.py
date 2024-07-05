import matplotlib.pyplot as plt
import numpy as np

def display_info(choice):
    info_dict = {
        1: 'This is information for option 1.',
        2: 'This is information for option 2. This will also plot an image automatically.',
        3: 'This is information for option 3.'
    }
    
    return info_dict.get(choice, 'No information available for the selected option.')

def plot_image():
    # Generate a simple plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.plot(x, y)
    plt.title('Sample Plot')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.grid(True)
    plt.show()

def main():
    print("Enter your choice (1, 2, 3):")
    try:
        choice = int(input().strip())
    except ValueError:
        print("Invalid input. Please enter a number (1, 2, 3).")
        return

    if choice not in [1, 2, 3]:
        print("Invalid choice. Please enter a valid option (1, 2, 3).")
        return

    if choice == 2:
        # Automatically plot if option 2 is selected
        info = display_info(choice)
        print(info)
        plot_image()
    else:
        info = display_info(choice)
        print(info)
        
        print("Would you like to plot an image? (yes/no):")
        plot_choice = input().strip().lower()
        
        if plot_choice == 'yes':
            plot_image()

if __name__ == "__main__":
    main()
