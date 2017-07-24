import re

# Open file
class FileRead:
    def __init__(self, file):
        self.f = None;
        self.bridges = [];
        try:
            f = open(file)
        except FileNotFoundError:
            print("%s Not Found!" % file)
            f = None

        if f is not None:
            l = f.readline()
            while l != "":
                self.bridges.append(l)
                l = f.readline()

    def getBridgesList(self):
        return self.bridges

    def getBridge(self):
        i = 0
        while i < len(self.bridges):
            # Contains dictionary of nodes, list of trusses, and dictionary of forces, all in strings
            bridge = {'nodes': {}, 'trusses': [], 'forces': {}}
            elements = self.bridges[i].replace('\\n', '').split(', ')
            nodes = {}
            trusses = []
            forces = []
            # Match nodes
            for l in elements:
                nodeMatch = re.search('(^\S+?)\((-?\d+\.?\d*)\s(-?\d+\.?\d*)\)', l)
                trussMatch = re.search('^\((\S+)\s(\S+)\)', l)
                forceMatch = re.search('(^\S+?)\((\d+\.?\d*)<(\d+\.?\d*)\)', l)

                if nodeMatch is not None:
                    nodes[nodeMatch.group(1)] = [nodeMatch.group(2), nodeMatch.group(3)]
                if trussMatch is not None:
                    trusses.append([trussMatch.group(1), trussMatch.group(2)])
                if forceMatch is not None:
                    forces.append([forceMatch.group(1), [forceMatch.group(2), forceMatch.group(3)]])

            bridge['nodes'] = nodes
            bridge['trusses'] = trusses
            bridge['forces'] = forces

            yield bridge
            i += 1












