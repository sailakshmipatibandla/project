Temp <- c(
67,72,74,62,65,59,61,69,66,68,58,64,66,57,68,62,59,73,61,61,67,81,79,76,82,
90,87,82,77,72,65,73,76,84,85,81,83,83,88,92,92,89,73,81,80,81,82,84,87,85,
74,86,85,82,86,88,86,83,81,81,81,82,89,90,90,86,82,80,77,79,76,78,78,77,72,
79,81,86,97,94,96,94,91,92,93,93,87,84,80,78,75,73,81,76,77,71,71,78,67,76,
68,82,64,71,81,69,63,70,75,76,68)
ts.plot(Temp)
title("Temperature at NYC")
sm.regression.autocor(y=Temp, h.first=10, maxh=6)
