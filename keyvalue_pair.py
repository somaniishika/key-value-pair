visited_list = []

def dfs(listDictionary, element, returnList):
    if element not in visited_list:
        visited_list.append(element)
        for _ in range(len(listDictionary)):
            for keyPair in listDictionary[_]:
                if keyPair == element or listDictionary[_][keyPair] == element:
                    if keyPair not in returnList:
                        returnList.append(keyPair)
                    if listDictionary[_][keyPair] not in returnList:
                        returnList.append(listDictionary[_][keyPair])
            if keyPair == element:
                dfs(listDictionary, listDictionary[_][keyPair], returnList)
            elif listDictionary[_][keyPair] == element:
                dfs(listDictionary, keyPair, returnList)
        return returnList   
    return None                         

answer = []
listDictonary = [{"Dg set": "Diesel generator"}, {"Organization": "Organisation"}, {"Group": "Organization"}, {"Orange": "Kinnu"}, {"Orange": "narangi"}]
for i in range(len(listDictonary)):
    ans = dfs(listDictonary, list(listDictonary[i].keys())[0], [])
    if ans != None:
        answer.append(ans)
print(answer)        
