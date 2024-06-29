import matplotlib.pyplot as plt
from Scrapping import search_ebay
from Scrapping import search_alibaba


def main():
    product_name = input("Enter the product name: ")
    selected_sites = {}

    # Prompt user to select sites
    print("Enter 'y' for the sites you want to search:")
    for site in ['eBay', 'Alibaba', 'Walmart']:  # Add more sites as needed
        choice = input(f"Do you want to search on {site}? (y/n): ")
        selected_sites[site] = choice.lower() == 'y'

    # Scrape product info from selected sites
    product_data = {}
    for site, selected in selected_sites.items():
        if selected:
            if site == 'eBay':
                product_data[site] = search_ebay(product_name)
            elif site == 'Alibaba':
                product_data[site] = search_alibaba(product_name)
            elif site == 'Walmart':
                product_data[site] = search_alibaba(product_name)

    # Display product info from each site
    for site, data in product_data.items():
        print(f"\n{site} Results:")
        if data:
            for product in data:
                print(f"Name: {product['name']}")
                print(f"Price: {product['price']}")
                print(f"Link: {product['link']}")
                print('-' * 30)
        else:
            print("No results found.")

    plot(product_data)


def plot(product_data):
    # Extracting site names and corresponding prices
    sites = list(product_data.keys())
    prices = [float(product['price'].replace('$', '').replace(',', '')) for products in product_data.values() for product in products]

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.bar(sites, prices, alpha=0.7)
    plt.xlabel('Site')
    plt.ylabel('Price ($)')
    plt.title('Price Comparison of Product')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(True)
    plt.tight_layout()  # Adjust layout to prevent overlapping labels
    plt.show()


if __name__ == "__main__":
    main()
