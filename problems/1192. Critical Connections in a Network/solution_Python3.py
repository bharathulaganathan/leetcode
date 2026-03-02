class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        critical = list()
        def is_critical(current, remaining, target):
            for connection in remaining:
                if current in connection:
                    if target in connection:
                        return False
                    new_current = connection.copy()
                    new_current.remove(current)
                    new_remaining = remaining.copy()
                    new_remaining.remove(connection)
                    if not is_critical(new_current[0], new_remaining, target):
                        return False
            return True
        for connection in connections:
            remaining = connections.copy()
            remaining.remove(connection)
            if is_critical(connection[0], remaining, connection[1]):
                critical.append(connection)
        return critical
        