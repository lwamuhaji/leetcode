

def solution(tickets):
    def adjacencies(node):
        return [i for i in range(len(tickets)) if tickets[node][1] == tickets[i][0]]
        
    def dfs(node, visited, routes):
        if len(routes) == len(tickets):
            result.append([tickets[routes[0]][0]] + [tickets[ticket][1] for ticket in routes])
            
        for next_node in adjacencies(node):
            if not visited[next_node]:
                visited_temp = visited[:]
                visited_temp[next_node] = True
                routes_temp = routes[:]
                routes_temp.append(next_node)
                dfs(next_node, visited_temp, routes_temp)
    
    result = []
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            visited = [False for n in range(len(tickets))]
            visited[i] = True
            routes = [i]
            dfs(i, visited, routes)
    return sorted(result)[0]
    
    