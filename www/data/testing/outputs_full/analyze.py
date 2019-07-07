import sys
import os
import math

def get_iou(bb1, bb2):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.

    Parameters
    ----------
    bb1 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x1, y1) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner
    bb2 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x, y) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner

    Returns
    -------
    float
        in [0, 1]
    """
    assert bb1['x1'] < bb1['x2']
    assert bb1['y1'] < bb1['y2']
    assert bb2['x1'] < bb2['x2']
    assert bb2['y1'] < bb2['y2']

    # determine the coordinates of the intersection rectangle
    x_left = max(bb1['x1'], bb2['x1'])
    y_top = max(bb1['y1'], bb2['y1'])
    x_right = min(bb1['x2'], bb2['x2'])
    y_bottom = min(bb1['y2'], bb2['y2'])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box
    intersection_area = (x_right - x_left) * (y_bottom - y_top)

    # compute the area of both AABBs
    bb1_area = (bb1['x2'] - bb1['x1']) * (bb1['y2'] - bb1['y1'])
    bb2_area = (bb2['x2'] - bb2['x1']) * (bb2['y2'] - bb2['y1'])

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
    assert iou >= 0.0
    assert iou <= 1.0
    return iou

def read_data(filename, mode):
    ''' mode 0 = truth, mode 1 = data '''
    fp = open(filename, "r")
    data = []
    for line in fp:
        if mode == 0:
            splitLine = line.replace("\r\n","").split(" ")
            splitLine = filter(None, splitLine)
            splitLine[0] = splitLine[0][:-4]
            splitLine = [float(i) for i in splitLine]
            data.append(splitLine)
        elif mode == 1:
            splitLine = line.replace("\n","").split(",")
            splitLine[0] = splitLine[0][-10:-4]
            splitLine = [float(i) for i in splitLine]
            data.append(splitLine)
    fp.close()
    return sorted(data, key=lambda x: x[0])

def get_index(subItem, data):
    for i,item in enumerate(data):
        if item[0] == subItem:
            return i
    return -1

def good_values(data):
    for v in data:
        if math.isnan(v): return False
    if (data[1] + data[2] + data[3] + data[4]) == 0: return False
    return True
        

def main():
    truth = read_data(sys.argv[1], 0)
    data = read_data(sys.argv[2], 1)
    i = get_index(data[0][0], truth)
    truth = truth[i:]


    assert len(truth) == len(data)

    c = 0
    true_positives = 0
    false_negatives = 0
    false_positives = 0
    iou_sum = 0
    while c < len(data):
        #print(truth[c][0])
        #print(data[c][0])
        if truth[c][0] == data[c][0]:
            if not good_values(data[c]):
                false_negatives += 1
                c += 1
                continue
            iou = get_iou({'x1': truth[c][1], 'x2': truth[c][1] + truth[c][3], 'y1': truth[c][2], 'y2': truth[c][2] + truth[c][4]}, {'x1': data[c][1], 'x2': data[c][1] + data[c][3], 'y1': data[c][2], 'y2': data[c][2] + data[c][4]})
            #print(iou)
            if iou > 0.5:
                true_positives += 1
                iou_sum += iou
            else: #iou == 0.0:
                false_positives += 1
        else:
            print("Error at item " + str(c) + ", these don't match: " + str(truth[c]) + ", " + str(data[c]))

        c += 1
    print("TP: " + str(true_positives))
    print("FN: " + str(false_negatives))
    print("FP: " + str(false_positives))
    print("Recall: " + str(float(true_positives)/(true_positives + false_positives)))
    print("Precision: " + str(float(true_positives)/(true_positives + false_negatives)))
    print("Avg IOU: " + str(iou_sum/true_positives))
    #print(len(truth))
    #print(len(data))
    #print(truth[0:10])
    #print(data[0:10])


main()
