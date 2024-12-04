def readFile(day)
  padded_day = day.to_s() 
  if day.to_s.length == 1
        padded_day = "0" + padded_day
  end
  fstring = "day_%s/day_%s.txt" % [padded_day, padded_day]
  
  f = File.read(fstring).split
  return f
end

def out_of_bounds(i, j, iMin, jMin, iMax, jMax)
  return i < iMin || i > iMax || j < jMin || j > jMax
end

def printParts(part1, part2)
    puts "Part 1: " + part1.to_s
    puts "Part 2: " + part2.to_s
end