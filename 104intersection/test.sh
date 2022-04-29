echo "\n\n\033[1;33mSTART OF TEST\n"

echo "\n\033[1;31m==========Test 1=========="
echo "\n\033[1;36mGot:\033[1;0m\n"
./104intersection 1 0 0 2 1 1 0 1
echo "\n\033[1;36mExpected:\033[1;0m\n"
echo "Sphere of radius 1"
echo "Line passing through the point (0, 0, 2) and parallel to the vector (1, 1, 0)"
echo "No intersection point\n"

echo "\n\033[1;31m==========Test 2=========="
echo "\n\033[1;36mGot:\033[1;0m\n"
./104intersection 1 4 0 3 0 0 -2 4
echo "\n\033[1;36mExpected:\033[1;0m\n"
echo "Sphere of radius 4"
echo "Line passing through the point (4, 0, 3) and parallel to the vector (0, 0, -2)"
echo "1 intersection point:"
echo "(4.000, 0.000, 0.000)"

echo "\n\033[1;31m==========Test 3=========="
echo "\n\033[1;36mGot:\033[1;0m\n"
./104intersection 2 0 0 2 1 1 0 1
echo "\n\033[1;36mExpected:\033[1;0m\n"
echo "Cylinder of radius 1"
echo "Line passing through the point (0, 0, 2) and parallel to the vector (1, 1, 0)"
echo "2 intersection points:"
echo "(0.707, 0.707, 2.000)"
echo "(-0.707, -0.707, 2.000)"

echo "\n\033[1;31m==========Test 4=========="
echo "\n\033[1;36mGot:\033[1;0m\n"
./104intersection 3 -1 -1 -1 1 1 5 30
echo "\n\033[1;36mExpected:\033[1;0m\n"
echo "Cone with a 30 degree angle"
echo "Line passing through the point (-1, -1, -1) and parallel to the vector (1, 1, 5)"
echo "2 intersection points:"
echo "(-1.568, -1.568, -3.842)"
echo "(-0.537, -0.537, 1.315)"

echo "\n\033[1;31m==========Test 5=========="
echo "\n\033[1;36mGot:\033[1;0m\n"
./104intersection 2 1 0 0 0 0 1 1
echo "\n\033[1;36mExpected:\033[1;0m\n"
echo "Cylinder of radius 1"
echo "Line passing through the point (1, 0, 0) and parallel to the vector (0, 0, 1)"
echo "There is an infinite number of intersection points."

echo "\n\n\033[1;33mEND OF TEST\n"