# Centauri Prime
# Output = Case #x: K is ruled by Y.
# 1 <= x <= 300
# K = Kingdom name
# Y = Alice, Bob, nobody


def get_ruler(Kingdom):
    V = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    if Kingdom[0].isupper():
        if Kingdom[-1] in V:
            ruler = "Alice"  # Alice likes V
        elif (Kingdom[-1] not in V) and (Kingdom[-1].lower() != "y"):
            ruler = "Bob"  # Bob dislikes V
        else:
            ruler = "nobody"  # Likes "y"
        return ruler


def main():
    T = int(input())  # Test Case
    if (1 <= T) or (T >= 300):  # Limits
        for t in range(T):  # Loop through Kingdoms
            Kingdom = str(input())
            print(
                "Case #%d: %s is ruled by %s."
                % (t + 1, Kingdom, get_ruler(Kingdom))
            )


if __name__ == "__main__":
    main()
