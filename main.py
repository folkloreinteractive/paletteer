import app
import sys

if len(sys.argv) != 3:
    print("Usage: python main.py <source> <target>")
    sys.exit(1)

[x, source, target] = sys.argv
app.run(source, target)