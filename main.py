from src import items

def main():
    inventario = items.Ollivanders()
    print("Hello from ollivanders!")

    elixir = items.NormalItem("Elixir of the moongose", 20, 21)

    items.Ollivanders.add_item(inventario, elixir)


    print(inventario)
if __name__ == "__main__":
    main()