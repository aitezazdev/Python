def compute_final_score(scores):
    # Remove the two lowest scores
    sorted_scores = sorted(scores)
    adjusted_scores = sorted_scores[2:]
    
    # Sum up the adjusted scores
    final_score = sum(adjusted_scores)
    
    return final_score

# Example scores
scores = [8, 4, 7, 8.5, 9.5, 7, 5, 10]

# Compute the final score
final_score = compute_final_score(scores)
print("Final Score:", final_score)
