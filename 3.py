def difference_table(x, y, return_delta=False):
 # Table Definitions:
 n = len(x)
 dTable = np.zeros((n, n))
 dTable[:, 0] = y
 # Table Layout:
 column_names = ["Y", "△1", "△2", "△3", "△4", "△5", "△6", "△7", "△8", "△9", "△10"]
 table = PrettyTable(column_names)
 table.align = "r"
 # Generating Forward Difference Table
 for i in range(1, n):
 for j in range(0, n - i):
 dTable[j][i] = round(dTable[j + 1][i - 1] - dTable[j][i - 1], 4)
 # Output Structure
 num_columns = min(dTable.shape[1], 11)
 for row in dTable:
 row = row[:num_columns].copy()
 row.resize((11))
 table.add_row(row)
 # Returns
 if not return_delta:
 return table
 elif return_delta == "forward":
 # Returns n Forward Deltas, default=5
 n = min(dTable.shape[1], 5 + 1)
 return dTable[0, 1:n]
 elif return_delta == "backward":
 # Returns n Backward Deltas, default=5
 n = min(dTable.shape[1], 6)
 j = 1
 del_Y = []
 for i in range(dTable.shape[0] - 1, dTable.shape[0] - n, -1):
 del_Y.append(dTable[i - 1, j])
 j += 1
 return del_Y

x = np.linspace(-1, 1, 21)
y = np.exp(x).round(4)
print(difference_table(x,y))