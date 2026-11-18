
# Smith-Waterman Local alignment
# ↑ ↖ ←
s1 = "ATGC"
s2 = "ATG"
m = 2
mm = -1
g = -1

# Create score matrix
dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

# Create arrow matrix
ar = [[""]*(len(s2)+1) for _ in range(len(s1)+1)]

# No initialization needed (already zero)

# Fill Matrix
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        d = dp[i-1][j-1] + (m if s1[i-1] == s2[j-1] else mm)
        u = dp[i-1][j] + g
        l = dp[i][j-1] + g

        dp[i][j] = max(0,d,u,l)
        # add 0 
        if dp[i][j] == 0:
            ar[i][j] = ""
        elif dp[i][j] == d:
            ar[i][j] = "↖"
        elif dp[i][j] == u:
            ar[i][j] = "↑"
        else:
            ar[i][j] = "←"

# Print score with arrow matrix
print("Score + Arrow Matrix:")
for i in range(len(dp)):
    print([f"{dp[i][j]}{ar[i][j]}" for j in range(len(dp[0]))])

# Traceback from maximum score cell
i, j = max(((i,j) for i in range(len(dp))
            for j in range(len(dp[0]))),
            key=lambda x: dp[x[0]][x[1]])
a, b = "", ""

while i > 0 and j > 0 and dp[i][j] > 0:
    if ar[i][j] == "↖":
        a, b = s1[i-1]+a, s2[j-1]+b
        i, j = i-1, j-1
    elif ar[i][j] == "↑":
        a, b = s1[i-1]+a, "-"+b
        i -= 1
    elif ar[i][j] == "←":
        a, b = "-"+a, s2[j-1]+b
        j -= 1
    else:
        break

print("Local Alignment Score:", max(map(max,dp)))
print("Alignment:")
print(a)
print(b)
