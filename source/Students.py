webdev = set(["venkatesh", "vivek", "nithin", "avinash"])
python = set(["venkatesh", "nithin", "sowmith"])
print (webdev.intersection(python))
common = webdev.intersection(python)
only_web = webdev.difference(common)
only_pyth = python.difference(common)
no_common = only_pyth | only_web
print(no_common)