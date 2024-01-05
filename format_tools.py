
with open('tools.txt', 'r+') as f:
    tools = ['"' + line.rstrip()[1:-3] + '"' for line in f]
    f.seek(0)
    for tool in tools:
        f.write(f"{tool},\n")
    f.truncate()

