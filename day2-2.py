lines = []
with open('day2-2_input.txt') as f:
    lines = f.readlines()

listOfGames = (list(map(lambda x : x.replace("\n",""), lines)))
# qualifier = {
#     'red'   : 12,
#     'green' : 13,
#     'blue'  : 14
# }
qualifiedGamePower = []
for game in listOfGames : 
    gameDetail = game.split(":")
    gameID = int(gameDetail[0].replace('Game ',""))
    games = list(map(lambda x : x.split(', '),(gameDetail[1]).strip().split("; ")))
    # isQualified = True
    minCubes = {
        'red'   : 1,
        'green' : 1,
        'blue'  : 1
    }
    for cubes in games :
        for cube in cubes :
            cubeDetails = (cube.split())
            if(minCubes.get(cubeDetails[1]) < int(cubeDetails[0])):
                minCubes[cubeDetails[1]] = int(cubeDetails[0])
    qualifiedGamePower.append( minCubes.get("red") * minCubes.get("blue") * minCubes.get("green")  )
print(qualifiedGamePower)
print(sum(qualifiedGamePower))