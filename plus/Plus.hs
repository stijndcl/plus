plus x y | x == 1 && y == 0 = 1
         | x == 0 && y == 1 = 1
         | x == 0 && y == 0 = 0
         | x == 0 = [1..]!! plus x (y-1)
         | otherwise = [1..]!! plus (x-1) y