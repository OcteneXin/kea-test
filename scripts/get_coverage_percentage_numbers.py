import sys
import os
from xml.dom import minidom
from xml.parsers.expat import ExpatError


def read_coverage_jacoco(jacoco_report_file):
    if not os.path.isfile(jacoco_report_file):
        return False, 0, 0, 0, 0

    try:
        # see the format of coverage report generated by Jacoco in xml
        xmldoc = minidom.parse(jacoco_report_file)
        counters = xmldoc.getElementsByTagName('counter')

        line_coverage = 0
        branch_coverage = 0
        method_coverage = 0
        class_coverage = 0

        for counter in counters:
            type_name = counter.getAttribute('type')
            missed_items = int(counter.getAttribute('missed'))
            covered_items = int(counter.getAttribute('covered'))

            if type_name == 'LINE':
                line_coverage = covered_items * 100.0 / (missed_items + covered_items)
                print("#Lines: %d" % (missed_items + covered_items))

            if type_name == 'BRANCH':
                branch_coverage = covered_items * 100.0 / (missed_items + covered_items)

            if type_name == 'METHOD':
                method_coverage = covered_items * 100.0 / (missed_items + covered_items)

            if type_name == 'CLASS':
                class_coverage = covered_items * 100.0 / (missed_items + covered_items)

        print("-----------")
        print("Line: " + str(line_coverage) + ", Branch: " + str(branch_coverage) + ", Method: " + str(method_coverage)
              + ", Class: " + str(class_coverage))
        print("-----------")
        return True, float("{:.2f}".format(line_coverage)), float("{:.2f}".format(branch_coverage)), \
               float("{:.2f}".format(method_coverage)), float("{:.2f}".format(class_coverage))
    except ExpatError:
        print("*****Parse xml error, catch it!********")
        return False, 0, 0, 0, 0


if __name__ == '__main__':
    read_coverage_jacoco(sys.argv[1])
