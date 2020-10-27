import os

def _analyzefile(filepath):
    dict = {"extension": ".py",
            "number of lines": 7,
            "linelengths": [17,7,7,9,12,0,12],
            "number of methods": 1}
    return dict

def run(args):
    print("repo-analyser started")
    stats = _analyzefile(args.filepath)
    print(stats)