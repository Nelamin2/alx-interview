def pascal_triangle(n):
    """ a fungtion that calculates the apscal traiangel's value for a given n

    """"
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row [1]
    
    for i in range(1, n):
        row = [1]  # Start each row with 1
        # Compute the interior values of the row
        for j in range(1, i):
            # Each interior value is the sum of the two values above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)  # Add the completed row to the triangle
    
    return triangle

# Example usage:
n = 5
print(pascal_triangle(n))
