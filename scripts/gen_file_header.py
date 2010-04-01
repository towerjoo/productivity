# coding: utf-8

class Writer:
    def __init__(self, skeleton, data):
        self.skeleton = skeleton
        self.data = data

    def read_skeleton(self):
        f = open(self.skeleton, "r")
        cont = f.read()
        f.close()
        return cont

    def write_to_dest(self, output):
        f = open(output, "w")
        cont = self.read_skeleton()
        self.data.update({"filename" : output})
        out = cont % self.data
        f.write(out)
        f.close()


def opt_parser(data):
    from optparse import OptionParser
    parser = OptionParser()
    parser.version = get_current_version()
    parser.add_option("-s", "--skeleton", dest="skeleton", help="specify the skeleton file")
    parser.add_option("-o", "--output", dest="output", help="specify the output file")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="show more detailed information")
    (options, args) = parser.parse_args()
    if options.skeleton and options.output:
        if options.verbose:
            print "Generate %s from skeleton file %s (if the specified skeleton file can't be found, it will be searched in skeleton directory in the current working directory)..." % (options.output, options.skeleton)
        import os,sys
        if os.path.isfile(options.skeleton):
            writer = Writer(options.skeleton, data)
        elif os.path.isfile(os.path.join("skeleton", options.skeleton)):
            writer = Writer(os.path.join("skeleton", options.skeleton), data)
        else:
            print "skeleton file you specified (%s) not found." % options.skeleton
            return
        if options.output in os.listdir(os.getcwd()):
            print "output file you specified (%s) has existed already." % options.output
            return
        else:
            writer.write_to_dest(options.output)
            if options.verbose:
                print "The generating process is done successfully."
    else:
        parser.print_usage()


def get_current_format_date():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_current_version():
    return "%prog 0.1"


if __name__ == "__main__":
    data = {
            "author" : "Tower Joo", 
            "email" : "zhutao.iscas@gmail.com",
            "date" : get_current_format_date()
            }
    opt_parser(data)


