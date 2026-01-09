import pandas as pd
import matplotlib.pyplot as plt


DATA_FILE = "Immovable-monuments-by-voivodeship.xlsx"

# 1. Loads data from an Excel file and returns a DataFrame
def load_monuments_data(filepath: str) -> pd.DataFrame:
    df = pd.read_excel(filepath)
    df.columns = [col.strip() for col in df.columns]
    return df

# 2. Returns voivodeships that in 2025 have a higher number of monuments than in 2016 and 2024.
def voivodeships_with_increase(df: pd.DataFrame) -> pd.DataFrame:
    mask = (
        (df["YEAR 2025"] > df["YEAR 2016"]) &
        (df["YEAR 2025"] > df["YEAR 2024"])
    )
    return df[mask]

# 3. Calculates the growth in the number of monuments between 2016 and 2025 and returns it as a numerical array. The order corresponds to the order of voivodeships in the DataFrame.
def compute_growth_array(df: pd.DataFrame,
                         year_start: str = "YEAR 2016",
                         year_end: str = "YEAR 2025"):

    growth = df[year_end] - df[year_start]
    return growth.to_numpy()

# 4. Creates a bar plot of the number of monuments for the specified years.
# 'years' – a list of column names, e.g., ['YEAR 2016', 'YEAR 2024', 'YEAR 2025'].
def plot_monuments_by_year(df: pd.DataFrame,
                           years: list,
                           title: str = "Immovable monuments by voivodeship"):

    x_labels = df["VOIVODESHIP"].tolist()
    x_positions = range(len(x_labels))

    plt.figure(figsize=(12, 6))
    bar_width = 0.25
    offset = 0

    for year in years:
        plt.bar(
            [x + offset for x in x_positions],
            df[year].values,
            width=bar_width,
            label=year
        )
        offset += bar_width

    plt.xticks(
        [x + bar_width for x in x_positions],
        x_labels,
        rotation=45,
        ha="right"
    )
    plt.ylabel("Number of monuments")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    # 1. Load data
    df = load_monuments_data(DATA_FILE)

    # 2. Voivodeships with more monuments in 2025 than in 2016 and 2024
    increased_df = voivodeships_with_increase(df)
    print("Voivodeships with more monuments in 2025 than in 2016 and 2024:")
    for name in increased_df["VOIVODESHIP"]:
        print("-", name)

    # 3. Growth in the number of monuments 2016–2025
    growth_array = compute_growth_array(df, "YEAR 2016", "YEAR 2025")
    print("\nIncrease in the number of monuments 2016–2025 (in voivodeship order):")
    print(growth_array)

    # 4. Bar plot for years 2016, 2024, and 2025
    years_to_plot = ["YEAR 2016", "YEAR 2024", "YEAR 2025"]
    plot_monuments_by_year(df, years_to_plot,
                           title="Immovable monuments in Poland by voivodeship")


if __name__ == "__main__":
    main()