lines = []
with open('day2-1_input.txt') as f:
    lines = f.readlines()

listOfGames = (list(map(lambda x : x.replace("\n",""), lines)))
qualifier = {
    'red'   : 12,
    'green' : 13,
    'blue'  : 14
}
qualifiedGameIds = []
for game in listOfGames : 
    gameDetail = game.split(":")
    gameID = int(gameDetail[0].replace('Game ',""))
    games = list(map(lambda x : x.split(', '),(gameDetail[1]).strip().split("; ")))
    isQualified = True
    for cubes in games :
        for cube in cubes :
            cubeDetails = (cube.split())
            # print(cubeDetails)
            # print(qualifier.get(cubeDetails[1]))
            # print(int(cubeDetails[0]))
            # print(qualifier.get(cubeDetails[1]) < int(cubeDetails[0]))
            if(qualifier.get(cubeDetails[1]) < int(cubeDetails[0])):
                isQualified = False
    if(isQualified) : 
        qualifiedGameIds.append(gameID)
print(qualifiedGameIds)
print(sum(qualifiedGameIds))