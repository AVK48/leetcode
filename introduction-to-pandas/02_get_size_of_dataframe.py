import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    v,p = players.shape
    return[v,p]
