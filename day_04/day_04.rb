require_relative "../aocutils/aocutils"
require "set"

$grid = readFile(4)
$cross = ["MAS", "SAM"]
$dirs = [-1, 0, 1].product([-1, 0, 1]).select{|x, y| x != 0 || y != 0}

def traverse(i, j, dir, accum)
    if accum == "XMAS"
      return 1
    elsif accum.length > 4 || out_of_bounds(i, j, 0, 0, $grid.length - 1, $grid[0].length - 1)
      return 0
    end
    return traverse(i + dir[0], j + dir[1], dir, accum + $grid[i][j])
end

def is_cross(i, j)
    if i > $grid.length - 3 || j > $grid.length - 3
      return 0
    end
    set1 = $grid[i][j] + $grid[i + 1][j + 1] + $grid[i + 2][j + 2]
    set2 = $grid[i + 2][j] + $grid[i + 1][j + 1] + $grid[i][j + 2]
    if $cross.include?(set1) && $cross.include?(set2)
      return 1
    end
    return 0
end

total1, total2 = 0, 0
(0..$grid.length).each do |i|
  (0..$grid[0].length).each do |j|
      $dirs.each do |dir|
        total1 += traverse(i, j, dir, "")
      end
      total2 += is_cross(i, j)
    end
end

puts "Part 1: #{total1}"
puts "Part 2: #{total2}"