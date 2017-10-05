import sys
import yaml
from datetime import datetime


def parseFile(inputFile):
    f = open(inputFile, 'r')
    parsedDataList = []

    for each_line in f:
        newline = each_line
        if each_line.startswith('# Weeks with no progress'):
            endChar = len(each_line)
            newline = 'Inactive:'

        elif each_line.startswith('#'):
            endChar = len(each_line)
            newline = each_line[2:endChar-1] + ':'

        elif each_line.startswith('*'):
            newline = '-' + each_line[1:]

        newline = newline.replace('\t', '    ')
        parsedDataList.append(newline)

    return ''.join(parsedDataList)


def yamlToDict(parsedData):
    yamlData = yaml.dump(yaml.load(parsedData))
    print "Yaml representation of data:"
    print yamlData
    finalData = {}
    for key, value in yaml.load(yamlData).iteritems():
        finalData[key] = value

    return finalData


# Check if all 6 sections are present in notebook.md:
def checkSections(finalData):
    reqdSections = ['Meetings', 'Inactive', 'Logistic', 'Theory', 'Practice', 'Writing']
    presentSections = list(finalData.keys())
    return list(set(reqdSections) - set(presentSections))


# Return the meetings attended by the student:
def getDates(meetings):
    dates = []
    for meeting in meetings:
        date = datetime.strptime(meeting[:8], '%m/%d/%y')
        dates.append(date)
    return dates


def main():
    parsedData = parseFile(sys.argv[1])
    # parsedData = parseFile('notebook.md')
    finalData = yamlToDict(parsedData)
    missingSections = checkSections(finalData)
    print "Below section(s) not present in notebook.md:"
    if missingSections:
        print missingSections
    else:
        print "None"

    if 'Meetings' not in missingSections:
        dates = getDates(finalData['Meetings'])
        print "\nStudent attended the below classes:"
        for i in range(len(dates)):
            print dates[i]


if __name__ == '__main__':
    main()
