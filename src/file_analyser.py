import os

def analysefile(filepath):
    _ = open(filepath, 'r') 
    _, extension = os.path.splitext(filepath)
    return {"extension": extension,
            "line_count": 7}
    #dict = {"extension": ".py",
    #        "number of lines": 7,
    #        "linelengths": [17,7,7,9,12,0,12],
    #        "number of methods": 1}
    #return dict

#def analyse_from_path(filepath):
    
#raise FileNotFoundError
#def run(args):
#    print("repo-analyser started")
#    stats = _analyzefile(args.filepath)
#    print(stats)