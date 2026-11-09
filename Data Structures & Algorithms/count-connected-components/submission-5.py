class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph_dic = defaultdict(list)
        for edge in edges:
            graph_dic[edge[0]].append(edge[1])
            graph_dic[edge[1]].append(edge[0])

        visited = set()
        count = 0

        def recurse(children):
            for node in children:
                if node not in visited:
                    visited.add(node)
                    new_children = graph_dic[node]
                    if not new_children:
                        continue
                    else:
                        recurse(new_children)
            

        for edge in edges:
            if edge[0] not in visited:
                print(edge)
                count += 1
                recurse([edge[0]])

        count += n - len(visited)

        # print(visited)

        return count
        