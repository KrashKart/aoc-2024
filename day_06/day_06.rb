require_relative "../aocutils/aocutils"

@grid = readFile(6)

@h, @w = @grid.length, @grid[0].length

@grid.each_with_index do |g, idx|
  if g.include?("^")
    @starti, @startj = idx, g.find_index("^")
  end
end

def traverse(i, j, di = -1, dj = 0, isPart1=true)
  total = 0
  moves = 0
  while (!out_of_bounds(i, j, 0, 0, @h - 1, @w - 1) and moves <= @h * @w)
      if @grid[i][j] == "#"
          i, j = i - di, j - dj
          di, dj = dj, -di
      elsif @grid[i][j] == "."
          @grid[i][j] = "X"
          total += 1
      end
      i, j = i + di, j + dj
      moves += 1
  end
  return isPart1 ? total : moves
end

total1 = traverse(@starti, @startj) + 1

total2 = 0
(0..@h - 1).each do |x|
  (0..@w - 1).each do |y|
      if @grid[x][y] != "#"
        @grid[x][y] = "#"
        if traverse(@starti, @startj, -1, 0, false) > @h * @w
          total2 += 1
        end
        @grid[x][y] = "."
      end
  end
end

printParts(total1, total2)