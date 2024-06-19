
ProductName = str(input("Enter the Product Name: "))
StockLevel = int(input("Enter Stock Level: "))
CaseSize = 6
DesiredStockLevel = int(input("Enter Desired Stock Level: "))


def OrderCase (StockLevel, CaseSize, DesiredStockLevel, ProductName):
    stock = DesiredStockLevel - StockLevel
    if stock >= CaseSize:
        print(f"Order a Case of {ProductName}, Current Level: {StockLevel}")
    else:
        print("Stock Level Appropriate")


OrderCase(StockLevel, CaseSize, DesiredStockLevel, ProductName)