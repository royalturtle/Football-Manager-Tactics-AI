import os
from src.AIs.env.dataloader.DataLoader_FM import DataLoaderFM


test_data = {
    'position': [
        "GK",
        "DR",
        "DCR",
        "DC",
        "DCL",
        "DL",
        "WBR",
        "DM",
        "DMCL",
        "WBL",
        "ML",
    ],
    'lineup': [
        "ZXNEM",
        "ZXNEH",
        "ZXNEK",
        "ZXNEL",
        "ZXNEI",
        "ZXNEP",
        "ZXNEB",
        "ZXNEQ",
        "ZXNEG",
        "ZXNEW",
        "ZXNEF"
    ],
    'players': 4,
    'all': [
        ("GK", "ZXNEM"),
        ("DR", "ZXNEH"),
        ("DCR", "ZXNEK"),
        ("DC", "ZXNEL"),
        ("DCL", "ZXNEI"),
        ("DL", "ZXNEP"),
        ("WBR", "ZXNEB"),
        ("DM", "ZXNEQ"),
        ("DMCL", "ZXNEG"),
        ("WBL", "ZXNEW"),
        ("ML", "ZXNEF"),
    ]
}

path = os.getcwd()[:-10] + "\\data\\"
file1 = path + "(v2.1) players stat (FD).csv"
file2 = path + "(v2.1) players stat (GK).csv"

dataloader = DataLoaderFM((file1, file2), test_data['players'])
print(dataloader.get_stats_by_nickname(test_data['lineup'], position=test_data['position'], is_only_stats=True))
