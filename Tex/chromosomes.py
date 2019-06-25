range_index = int(df['Length'].mean())
df = df.sort_values("Start")
df = df.reset_index(drop=True)

pd.options.mode.chained_assignment = None
# g = 0 for the first file
# for the rest of them, g is appended
g = g+1
df.iloc[0, df.columns.get_loc('depMapID')] = g
start_old = df["Start"][0]
n = len(df.index)
for i in range(1,n):
    start_new = df["Start"][i]
    if start_new != start_old and not (start_new < start_old + range_index):
        g = g + 1
        start_old = start_new
    df.iloc[i, df.columns.get_loc('depMapID')] = "g
