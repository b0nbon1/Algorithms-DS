def minMeetingRooms(intervals):
  start = sorted([i[0] for i in intervals])
  end = sorted([i[1] for i in intervals])

  res, count = 0, 0
  s, e = 0, 0
  while s < len(intervals):
    if start[s] < end[e]:
      s += 1
      count += 1
    else:
      e += 1
      count -= 1
    res = max(res, count)
  return res

print(minMeetingRooms([[7,10],[2,4]]))
