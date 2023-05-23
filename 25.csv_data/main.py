import pandas as pd

squirrel = pd.read_csv("2018_Squirrel_Data.csv")
color = squirrel["Primary Fur Color"]
# print(color.head(50))
gray_nmb = len(color[color == "Gray"])
red_nmb = len(color[color == "Cinnamon"])
black_nmb = len(color[color == "Black"])


squirrel_count = pd.DataFrame(
    {
        "Fur Color": ["grey", "red", "black"],
        "Count": [gray_nmb, red_nmb, black_nmb]
    }
)

squirrel_count.to_csv("squirrel_count.csv")


