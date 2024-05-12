def hanoi(n, source, target, auxiliary, moves):
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target, moves)
    moves.append(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source, moves)


#Setting the game
n = 3
moves = []
hanoi(n, 'A', 'C', 'B', moves)
for i, move in enumerate(moves, 1):
    print(f"step {i}: {move}")
