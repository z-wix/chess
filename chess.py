import chess.pgn
import csv

# Specify the input PGN file and output CSV file
input_pgn_file = "/Users/Zack.Wixom/personal/chess/data/chess_com_games_2025-01-06.pgn"  # Replace with your file path
output_csv_file = "chess_games_summary.csv"

# Open the PGN file and create the CSV file
with open(input_pgn_file) as pgn, open(output_csv_file, mode="w", newline="") as csvfile:
    # Define the CSV writer and header
    fieldnames = ["Game Number", "Result", "Opening", "ECO", "Your Elo", "Opponent Elo", "Color", "Moves"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    game_number = 0
    
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None:
            break  # End of file
        
        game_number += 1
        headers = game.headers
        
        # Extract relevant data
        result = headers.get("Result", "Unknown")
        opening = headers.get("Opening", "Unknown")
        eco = headers.get("ECO", "Unknown")
        your_elo = headers.get("WhiteElo" if headers["White"] == "User" else "BlackElo", "0")
        opponent_elo = headers.get("BlackElo" if headers["White"] == "User" else "WhiteElo", "0")
        color = "White" if headers["White"] == "User" else "Black"
        moves = game.board().variation_san(game.mainline_moves())
        
        # Write to the CSV
        writer.writerow({
            "Game Number": game_number,
            "Result": result,
            "Opening": opening,
            "ECO": eco,
            "Your Elo": your_elo,
            "Opponent Elo": opponent_elo,
            "Color": color,
            "Moves": moves
        })

print(f"PGN file has been reformatted and saved to {output_csv_file}.")
