import GeneratePlots
import random
import time

def main():
    Plot_functions = [
        GeneratePlots.lineplot_code,
        GeneratePlots.scatterplot_code,
        GeneratePlots.Barchart_code,
        GeneratePlots.Barcharthorizontal_code,
        GeneratePlots.Histogram_code,
        GeneratePlots.Boxplot_code,
        GeneratePlots.Piechart_code,
        GeneratePlots.AreaPlot_code,
        GeneratePlots.StackedBarChart_code,
        GeneratePlots.Heatmap_code,
        GeneratePlots.Contour_code,
        GeneratePlots.Three_d_plot_code
    ]

    while True:
        # Displaying the menu
        print("\nSelect a plot to display:")
        for i, func in enumerate(Plot_functions, start=1):
            print(f"{i}. {func.__name__}")  # Display function names with numbers
        print(f"{len(Plot_functions) + 1}. Random Continuous")
        print("0. Exit")

        # User input
        choice = input("Enter your choice (number): ").strip()

        # Execute based on choice
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                break  # Exit the program
            elif choice == len(Plot_functions) + 1:
                try:
                    while True:  # Continuous loop for random plots
                        random.choice(Plot_functions)()  # Execute a random plot function
                        time.sleep(1)  # Adjust as needed, delay between plots
                except KeyboardInterrupt:
                    print("\nRandom continuous display stopped by user.")
            elif 1 <= choice <= len(Plot_functions):
                Plot_functions[choice - 1]()  # Execute the chosen plot function
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
