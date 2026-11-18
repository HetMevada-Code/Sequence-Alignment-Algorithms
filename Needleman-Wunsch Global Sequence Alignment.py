# Needleman-Wunsch: Global Sequence Alignment
s1 = "ATGC"
s2 = "ATG"
m = 2
mm = -1
g = -1

# Create score and arrow matrices
dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
ar = [[""]*(len(s2)+1) for _ in range(len(s1)+1)]

# Initialize first row and column
for i in range(len(s1)+1):
    dp[i][0] = i*g
    if i > 0:
        ar[i][0] = "↑"

for j in range(len(s2)+1):
    dp[0][j] = j*g
    if j > 0:
        ar[0][j] = "←"

# Fill matrices
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        d = dp[i-1][j-1] + (m if s1[i-1]==s2[j-1] else mm)
        u = dp[i-1][j] + g
        l = dp[i][j-1] + g

        dp[i][j] = max(d, u, l)

        if dp[i][j] == d:
            ar[i][j] = "↖"
        elif dp[i][j] == u:
            ar[i][j] = "↑"
        else:
            ar[i][j] = "←"

# Print matrix with arrows
print("Score + Arrow Matrix:")
for i in range(len(dp)):
    print([f"{dp[i][j]}{ar[i][j]}" for j in range(len(dp[0]))])

# Traceback from bottom-right
i, j = len(s1), len(s2)
a, b = "", ""

while i > 0 or j > 0:
    if ar[i][j] == "↖":
        a, b = s1[i-1]+a, s2[j-1]+b
        i, j = i-1, j-1
    elif ar[i][j] == "↑":
        a, b = s1[i-1]+a, "-"+b
        i -= 1
    else:
        a, b = "-"+a, s2[j-1]+b
        j -= 1

print("Score:", dp[-1][-1])
print("Alignment:")
print(a)
print(b)
