# DESCRIPTION
# This script is for parsing the gazePredictionsDone.csv generaterd by the webgazerExtractServer. 

import sys
import os
import csv
import numpy as np

EXCLUDE = ["participant_characteristics.csv"]

def parse_gaze_predictions(filename):
    if filename[-4:] != ".csv":
        print("Failed. Please provide the csv file generated by webgazerExtractServer.py")
        exit()
    with open(filename, "r") as csv_file:
        data = np.array(list(csv.reader(csv_file)))
    #fieldnames = data[0]
    #data = data[1:]
    fieldnames =  np.asarray(['participant', 'frameImageFile', 'frameTimeEpoch', 'frameNum', 'mouseMoveX', 'mouseMoveY', 'mouseClickX', 'mouseClickY', 'keyPressed', 'keyPressedX', 'keyPressedY', 'tobiiLeftScreenGazeX', 'tobiiLeftScreenGazeY', 'tobiiRightScreenGazeX', 'tobiiRightScreenGazeY', 'webGazerX', 'webGazerY', 'clmPos_0000', 'clmPos_0001', 'clmPos_0002', 'clmPos_0003', 'clmPos_0004', 'clmPos_0005', 'clmPos_0006', 'clmPos_0007', 'clmPos_0008', 'clmPos_0009', 'clmPos_0010', 'clmPos_0011', 'clmPos_0012', 'clmPos_0013', 'clmPos_0014', 'clmPos_0015', 'clmPos_0016', 'clmPos_0017', 'clmPos_0018', 'clmPos_0019', 'clmPos_0020', 'clmPos_0021', 'clmPos_0022', 'clmPos_0023', 'clmPos_0024', 'clmPos_0025', 'clmPos_0026', 'clmPos_0027', 'clmPos_0028', 'clmPos_0029', 'clmPos_0030', 'clmPos_0031', 'clmPos_0032', 'clmPos_0033', 'clmPos_0034', 'clmPos_0035', 'clmPos_0036', 'clmPos_0037', 'clmPos_0038', 'clmPos_0039', 'clmPos_0040', 'clmPos_0041', 'clmPos_0042', 'clmPos_0043', 'clmPos_0044', 'clmPos_0045', 'clmPos_0046', 'clmPos_0047', 'clmPos_0048', 'clmPos_0049', 'clmPos_0050', 'clmPos_0051', 'clmPos_0052', 'clmPos_0053', 'clmPos_0054', 'clmPos_0055', 'clmPos_0056', 'clmPos_0057', 'clmPos_0058', 'clmPos_0059', 'clmPos_0060', 'clmPos_0061', 'clmPos_0062', 'clmPos_0063', 'clmPos_0064', 'clmPos_0065', 'clmPos_0066', 'clmPos_0067', 'clmPos_0068', 'clmPos_0069', 'clmPos_0070', 'clmPos_0071', 'clmPos_0072', 'clmPos_0073', 'clmPos_0074', 'clmPos_0075', 'clmPos_0076', 'clmPos_0077', 'clmPos_0078', 'clmPos_0079', 'clmPos_0080', 'clmPos_0081', 'clmPos_0082', 'clmPos_0083', 'clmPos_0084', 'clmPos_0085', 'clmPos_0086', 'clmPos_0087', 'clmPos_0088', 'clmPos_0089', 'clmPos_0090', 'clmPos_0091', 'clmPos_0092', 'clmPos_0093', 'clmPos_0094', 'clmPos_0095', 'clmPos_0096', 'clmPos_0097', 'clmPos_0098', 'clmPos_0099', 'clmPos_0100', 'clmPos_0101', 'clmPos_0102', 'clmPos_0103', 'clmPos_0104', 'clmPos_0105', 'clmPos_0106', 'clmPos_0107', 'clmPos_0108', 'clmPos_0109', 'clmPos_0110', 'clmPos_0111', 'clmPos_0112', 'clmPos_0113', 'clmPos_0114', 'clmPos_0115', 'clmPos_0116', 'clmPos_0117', 'clmPos_0118', 'clmPos_0119', 'clmPos_0120', 'clmPos_0121', 'clmPos_0122', 'clmPos_0123', 'clmPos_0124', 'clmPos_0125', 'clmPos_0126', 'clmPos_0127', 'clmPos_0128', 'clmPos_0129', 'clmPos_0130', 'clmPos_0131', 'clmPos_0132', 'clmPos_0133', 'clmPos_0134', 'clmPos_0135', 'clmPos_0136', 'clmPos_0137', 'clmPos_0138', 'clmPos_0139', 'clmPos_0140', 'clmPos_0141', 'eyeFeatures_0000', 'eyeFeatures_0001', 'eyeFeatures_0002', 'eyeFeatures_0003', 'eyeFeatures_0004', 'eyeFeatures_0005', 'eyeFeatures_0006', 'eyeFeatures_0007', 'eyeFeatures_0008', 'eyeFeatures_0009', 'eyeFeatures_0010', 'eyeFeatures_0011', 'eyeFeatures_0012', 'eyeFeatures_0013', 'eyeFeatures_0014', 'eyeFeatures_0015', 'eyeFeatures_0016', 'eyeFeatures_0017', 'eyeFeatures_0018', 'eyeFeatures_0019', 'eyeFeatures_0020', 'eyeFeatures_0021', 'eyeFeatures_0022', 'eyeFeatures_0023', 'eyeFeatures_0024', 'eyeFeatures_0025', 'eyeFeatures_0026', 'eyeFeatures_0027', 'eyeFeatures_0028', 'eyeFeatures_0029', 'eyeFeatures_0030', 'eyeFeatures_0031', 'eyeFeatures_0032', 'eyeFeatures_0033', 'eyeFeatures_0034', 'eyeFeatures_0035', 'eyeFeatures_0036', 'eyeFeatures_0037', 'eyeFeatures_0038', 'eyeFeatures_0039', 'eyeFeatures_0040', 'eyeFeatures_0041', 'eyeFeatures_0042', 'eyeFeatures_0043', 'eyeFeatures_0044', 'eyeFeatures_0045', 'eyeFeatures_0046', 'eyeFeatures_0047', 'eyeFeatures_0048', 'eyeFeatures_0049', 'eyeFeatures_0050', 'eyeFeatures_0051', 'eyeFeatures_0052', 'eyeFeatures_0053', 'eyeFeatures_0054', 'eyeFeatures_0055', 'eyeFeatures_0056', 'eyeFeatures_0057', 'eyeFeatures_0058', 'eyeFeatures_0059', 'eyeFeatures_0060', 'eyeFeatures_0061', 'eyeFeatures_0062', 'eyeFeatures_0063', 'eyeFeatures_0064', 'eyeFeatures_0065', 'eyeFeatures_0066', 'eyeFeatures_0067', 'eyeFeatures_0068', 'eyeFeatures_0069', 'eyeFeatures_0070', 'eyeFeatures_0071', 'eyeFeatures_0072', 'eyeFeatures_0073', 'eyeFeatures_0074', 'eyeFeatures_0075', 'eyeFeatures_0076', 'eyeFeatures_0077', 'eyeFeatures_0078', 'eyeFeatures_0079', 'eyeFeatures_0080', 'eyeFeatures_0081', 'eyeFeatures_0082', 'eyeFeatures_0083', 'eyeFeatures_0084', 'eyeFeatures_0085', 'eyeFeatures_0086', 'eyeFeatures_0087', 'eyeFeatures_0088', 'eyeFeatures_0089', 'eyeFeatures_0090', 'eyeFeatures_0091', 'eyeFeatures_0092', 'eyeFeatures_0093', 'eyeFeatures_0094', 'eyeFeatures_0095', 'eyeFeatures_0096', 'eyeFeatures_0097', 'eyeFeatures_0098', 'eyeFeatures_0099', 'eyeFeatures_0100', 'eyeFeatures_0101', 'eyeFeatures_0102', 'eyeFeatures_0103', 'eyeFeatures_0104', 'eyeFeatures_0105', 'eyeFeatures_0106', 'eyeFeatures_0107', 'eyeFeatures_0108', 'eyeFeatures_0109', 'eyeFeatures_0110', 'eyeFeatures_0111', 'eyeFeatures_0112', 'eyeFeatures_0113', 'eyeFeatures_0114', 'eyeFeatures_0115', 'eyeFeatures_0116', 'eyeFeatures_0117', 'eyeFeatures_0118', 'eyeFeatures_0119'])
    return fieldnames, data.T

def calc_gaze_error(tobiiLeftX, tobiiLeftY, tobiiRightX, tobiiRightY, webGazerX, webGazerY):
    i = 0
    error_x = 0
    error_y = 0
    valid = 0
    while i < len(webGazerX):
        vals = [tobiiLeftX[i], tobiiLeftY[i], tobiiRightX[i], tobiiRightY[i], webGazerX[i], webGazerY[i]]
        if [val for val in vals if val in ['-1','']]:
            i += 1
            continue
        average_true_x = (float(vals[0]) + float(vals[2]))/2
        average_true_y = (float(vals[1]) + float(vals[3]))/2
        error_x += abs(average_true_x - float(vals[4]))
        error_y += abs(average_true_y - float(vals[5]))
        valid += 1
        i += 1
    return error_x/valid, error_y/valid

def run_for_file(filename):
    fieldnames, data = parse_gaze_predictions(filename)
    error_x, error_y = calc_gaze_error(data[np.where(fieldnames == "tobiiLeftScreenGazeX")[0][0]],
                                       data[np.where(fieldnames == "tobiiLeftScreenGazeY")[0][0]],
                                       data[np.where(fieldnames == "tobiiRightScreenGazeX")[0][0]],
                                       data[np.where(fieldnames == "tobiiRightScreenGazeY")[0][0]],
                                       data[np.where(fieldnames == "webGazerX")[0][0]],
                                       data[np.where(fieldnames == "webGazerY")[0][0]])
    return [error_x, error_y]


def parse(filename):
    fp = open(filename, "r")
    names = []
    for l in fp:
        names.append(l.split(","))
    fp.close()
    return names

def main():
    csv_count, error_x, error_y = [0, 0, 0]
    processed = parse("log.csv")
    fp = open("log.csv", "a")
    for path, subdirs, files in os.walk(sys.argv[1]):
        for name in files:
            if name not in processed and name[-4:] == ".csv" and name not in EXCLUDE:
                print(name)
		try:
                    x, y = run_for_file(path + "/" + name)
		except:
		    x = None
		    y = None
		fp.write(name + "," + str(x) + "," + str(y) + "\n")
		print(name + "," + str(x) + "," + str(y))
		if x != None:
                    error_x += x
                    error_y += y
                    csv_count += 1
    fp.close()
    error_x = error_x/csv_count
    error_y = error_y/csv_count
    print([error_x, error_y])

if __name__ == "__main__":
    main()
