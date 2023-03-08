#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import images


def recursive1(database, image_list, position, bg_color, color_list, count = 0):
    try:
        color = database[position]
    except:
        return 1
    color_list.append(color)
    image1_2 = []
    image2_2 = []
    image3_2 = []
    image4_2 = []
    image1 = []
    image2 = []
    image3 = []
    image4 = []
    limit_y_axis = len(image_list)
    limit_x_axis = len(image_list[0])
    flag_y = True
    for xe in range(limit_y_axis):
        try:
            if image_list[xe][0] == color:
                for row1 in range(limit_y_axis):
                    if flag_y:
                        if image3 != []:
                            image4_2.append(image4)
                            image3_2.append(image3)
                    else:
                        if image2 != []:
                            image1_2.append(image1)
                            image2_2.append(image2)
                    image1 = []
                    image2 = []
                    image3 = []
                    image4 = []
                    flag_x = True
                    if row1 == xe:
                        flag_y = False
                        continue
                    for pixel1 in range(limit_x_axis):
                        if image_list[row1][pixel1] == color:
                            flag_x = False
                            continue
                        elif flag_y and flag_x:
                           image4.append(image_list[row1][pixel1])
                        elif flag_y and not flag_x:
                           image3.append(image_list[row1][pixel1])
                        elif not flag_y and flag_x:
                           image2.append(image_list[row1][pixel1]) 
                        elif not flag_y and not flag_x:
                           image1.append(image_list[row1][pixel1])            
                image1_2.append(image1)
                image2_2.append(image2)
                break
        except:
                continue
    list1 = [image1_2, image2_2, image3_2, image4_2]
    for element in list1:
        breaker = False
        for row in element:
            for pixel in row:
                if pixel != bg_color:
                    count += recursive1(database, element, position + 1, bg_color, color_list)
                    breaker = True
                    break
            if breaker:
                break
        if not breaker:
            count += 1
    return count


def ex1(input_file, output_file):
    image_list = images.load(input_file)
    bg_color = image_list[0][0]
    database = {}
    temp_database = {}
    count = 0
    position = 0
    color_list = [bg_color]
    for row in image_list:
        for curr_pixel, nxt_pixel in zip(row, row[1:]):
            if nxt_pixel != bg_color:
                if nxt_pixel == curr_pixel:
                    if nxt_pixel not in database:
                        database[nxt_pixel] = 1
                        temp_database[nxt_pixel] = 1
                    else:
                        temp_database[nxt_pixel] += 1
                        if temp_database[nxt_pixel] > database[nxt_pixel]:
                            database[nxt_pixel] = temp_database[nxt_pixel]
                else:
                    temp_database[nxt_pixel] = 1
    database = sorted(database.items(),key = lambda x: x[1], reverse=True)
    database = [i[0] for i in database]
    print(database)
    result = recursive1(database, image_list, position, bg_color, color_list, count)
    color_list2 = [color_list]
    images.save(color_list2,output_file)
    return result
