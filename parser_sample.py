from optparse import OptionParser
import sys, re
usage= sys.argv[0] + """ -i input_file -n ncbi_tree  -o <output file>"""

parser = None
def createParser():
    global parser
    epilog = """
     this code computes the coreness of each pathways, i.e., for each pathway what is the 
     percentage of samples it is present in"""

    epilog = re.sub(r'[ \t\f\v]+',' ', epilog)

    parser = OptionParser(usage=usage, epilog=epilog)

    parser.add_option("-a", "--annot_filee", dest="annot_file",
                      help='the annotation file [REQUIRED]')

    parser.add_option("-s", "--sample", dest="sample_file",
                      help='the sample file with annotaiton [REQUIRED]')

def main(argv, errorlogger = None, runstatslogger = None):
    global parser
    (opts, args) = parser.parse_args(argv)

if __name__ == "__main__":
    createParser()
    main(sys.argv[1:])




