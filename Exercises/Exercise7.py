li = [20, 16, 12, 14, 14, 15, 17, 17, 7, 13]


# Insertion Sort
[[20],16, 12, 14, 14, 15, 17, 17, 7, 13] #first assume first element is a sorted sublist of length 1

[[16, 20], 12, 14, 14, 15, 17, 17, 7, 13] # add the next item (16) to the appropriate place in the sub list
                                            # so that sublist grows by one

[[12, 16, 20], 14, 14, 15, 17, 17, 7, 13]   # add the next item (12) to the appropriate place in the sub list
                                            # so that sublist grows by one                      

[[12, 14, 16, 20], 14, 15, 17, 17, 7, 13]    # add the next item (14) to the appropriate place in the sub list
                                            # so that sublist grows by one 

[[12, 14, 14, 16, 20], 15, 17, 17, 7, 13]   # add the next item (14) to the appropriate place in the sub list
                                            # so that sublist grows by one

[[12, 14, 14, 15, 16, 20], 17, 17, 7, 13]   # add the next item (15) to the appropriate place in the sub list
                                            # so that sublist grows by one

[[12, 14, 14, 15, 16, 17, 20], 17, 7, 13]   # add the next item (17) to the appropriate place in the sub list
                                            # so that sublist grows by one

[[12, 14, 14, 15, 16, 17, 17, 20], 7, 13]   # add the next item (17) to the appropriate place in the sub list
                                            # so that sublist grows by one


[[7, 12, 14, 14, 15, 16, 17, 17, 20], 13]   # add the next item (7) to the appropriate place in the sub list
                                            # so that sublist grows by one

[[7, 12, 13, 14, 14, 15, 16, 17, 17, 20]]   # add the next item (13) to the appropriate place in the sub list
                                            # so that sublist grows by one

[7, 12, 13, 14, 14, 15, 16, 17, 17, 20]     #the sublist is now the whole list, but ordered!!




# QuickSort
li = [20, 16, 12, 14, 14, 15, 17, 17, 7, 13]

