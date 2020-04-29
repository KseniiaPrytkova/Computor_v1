
#!/bin/sh	



# python3 checker.py

# echo "------------- sample"
# echo "The equation to solve: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
# python3 checker.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
# echo "-------------"

# echo "-------------"
# echo "The equation to solve: 5 * X^0 + 4 * X^1 = 4 * X^0"
# python3 checker.py "5 * X^0 + 4 * X^1 = 4 * X^0"
# echo "-------------"

# echo "-------------"
# echo "The equation to solve: 8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
# python3 checker.py "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
# echo "-------------"

# echo "------------- correction form"
# echo "The equation to solve: 5 * X^0 = 5 * X^0"
# python3 checker.py "5 * X^0 = 5 * X^0"
# echo "-------------"

# echo "\n-------------"
# echo "The equation to solve: 4 * X^0 = 8"
# python3 checker.py "4 * X^0 = 8"
# echo "-------------"


# echo "\n-------------"
# echo "The equation to solve: 5 * X^0 = 4 * X^0 + 7 * X^1"
# python3 checker.py "5 * X^0 = 4 * X^0 + 7 * X^1"
# echo "-------------"

# echo "\n-------------"
# echo "The equation to solve: 5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1"
# python3 checker.py "5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1"
# echo "-------------"

# echo "\n-------------"
# echo "The equation to solve: 6 * X^0 + 11 * x^1 + 5 * x^2 = 1 * X^0 + 1 * X^1"
# python3 checker.py "6 * X^0 + 11 * x^1 + 5 * x^2 = 1 * X^0 + 1 * X^1"
# echo "-------------"

# echo "\n-------------"
# echo "The equation to solve: 5 * X^0 + 3 * x^1 + 3 * x^2 = 1 * X^0 + 0 * X^1"
# python3 checker.py "5 * X^0 + 3 * x^1 + 3 * x^2 = 1 * X^0 + 0 * X^1"
# echo "-------------"

# echo "------------- others"
# echo "The equation to solve: 20*X^0 = 0"
# python3 checker.py "20*X^0 = 0"

# echo "-------------"
# echo "The equation to solve: 20*X^0 = 20"
# python3 checker.py "20*X^0 = 20"

# echo "-------------"
# echo "The equation to solve: 20*X^0 = 20*x"
# python3 checker.py "20*X^0 = 20*x"

# echo "-------------"
# echo "The equation to solve: 20*X^0 = 20*x^0"
# python3 checker.py "20*X^0 = 20*x^0"

# echo "-------------"
# echo "The equation to solve: 20*X^0 = -20*x^0"
# python3 checker.py "20*X^0 = -20*x^0"

# echo "-------------"
# echo "The equation to solve: 20*X^0 + 2*X^0 = -20*x^0"
# python3 checker.py "20*X^0 + 2*X^0 = -20*x^0"

# echo "-------------"
# echo "The equation to solve: 20*X^0 - 2*X^0 = -20*x^0"
# python3 checker.py "20*X^0 - 2*X^0 = -20*x^0"

# echo "-------------"
# echo "The equation to solve: 20*X^1  - 2*X^0 = -20*x^0"
# python3 checker.py "20*X^1  - 2*X^0 = -20*x^0"

# echo "-------------"
# echo "The equation to solve: 20*X^1 + 5* - 2*X^0 = -20*x^0"
# python3 checker.py "20*X^1 + 5* - 2*X^0 = -20*x^0"

echo "-------------"
echo "The equation to solve: 20*X^1 + 5*X^1 - 2*X^0 = -20*x^0"
python3 checker.py "20*X^1 + 5*X^1 - 2*X^0 = -20*x^0 "

echo "-------------"
echo "The equation to solve: 20*X^1 + 5*X^1 - 2*X^0 = -20*x^0 - 8*X^1 "
python3 checker.py "20*X^1 + 5*X^1 - 2*X^0 = -20*x^0 - 8*X^1 "

echo "-------------"
echo "The equation to solve: 20*X^1 + 5*X^2 - 2*X^0 = -20*x^0 - 8*X^1 "
python3 checker.py "20*X^1 + 5*X^2 - 2*X^0 = -20*x^0 - 8*X^1 "

echo "-------------"
echo "The equation to solve: 20*X^1 + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
python3 checker.py "20*X^1 + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "

# echo "-------------"
# echo "The equation to solve: 20*X^-1 + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# python3 checker.py "20*X^-1 + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# echo "-------------"
# echo "The equation to solve: 20*X^1 54df6h54ds56h + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# python3 checker.py "20*X^1 54df6h54ds56h + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# echo "-------------"
# echo "The equation to solve: 20*X^1.2  + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# python3 checker.py "20*X^1.2  + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# echo "-------------"
# echo "The equation to solve: 20*X^1.2  + 5*X^2 + 2*X^0 = 20*x^1.2 - 8*X^1 "
# python3 checker.py "20*X^1.2  + 5*X^2 + 2*X^0 = 20*x^1.2 - 8*X^1 "
# echo "-------------"
# echo "The equation to solve: 0*X^1  + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# python3 checker.py "0*X^1  + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# echo "-------------"
# echo "The equation to solve: 4  5 4  5  0*X^1  + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1"
# python3 checker.py "4  5 4  5  0*X^1  + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# echo "-------------"
# echo "The equation to solve: 45450*X^1  + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1"
# python3 checker.py "45450*X^1  + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# echo "-------------"
# echo "The equation to solve: 45450*X^1  + 5*X^-2 + 2*X^0 = -20*x^0 - 8*X^1 "
# python3 checker.py "45450*X^1  + 5*X^-2 + 2*X^0 = -20*x^0 - 8*X^1 "
# echo "-------------"
# echo "The equation to solve: 45450*X^1  + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# python3 checker.py "45450*X^1  + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# echo "-------------"
# echo "The equation to solve: 45450*X^1  + 5*X^2.2 + 2*X^0 = -20*x^0 - 8*X^1 "
# python3 checker.py "45450*X^1  + 5*X^2.2 + 2*X^0 = -20*x^0 - 8*X^1 "
# echo "-------------"
# echo "The equation to solve: 45450*X^1  + 5*X^2. + 2*X^0 = -20*x^0 - 8*X^1 "
# python3 checker.py "45450*X^1  + 5*X^2. + 2*X^0 = -20*x^0 - 8*X^1 "
# echo "-------------"
# echo "The equation to solve: 45450*X^1  + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# python3 checker.py "45450*X^1  + 5*X^2 + 2*X^0 = -20*x^0 - 8*X^1 "
# echo "--------------------------------------------------------------"
# echo "Test cepalle:"
# echo "--------------------------------------------------------------"
# echo "The equation to solve: 0=0"
# python3 checker.py "0=0"
# echo "-------------"
# echo "The equation to solve: 0*X^0=0*X^0"
# python3 checker.py "0*X^0=0*X^0"
# echo "-------------"
# echo "The equation to solve: 5 * X^0 = 5 * X^0"
# python3 checker.py "5 * X^0 = 5 * X^0"
# echo "-------------"
# echo "The equation to solve: 4 * X^0 = 8 *X^0"
# python3 checker.py "4 * X^0 = 8 *X^0"
# echo "-------------"
# echo "The equation to solve: 5.5 * X^0 = 4 * X^0 + 7.2 * X^1"
# python3 checker.py "5.5 * X^0 = 4 * X^0 + 7.2 * X^1"
# echo "-------------"
# echo "The equation to solve: 5.5 * X^0 + 7.2*X ^ 1= 4 * X^0 + 7.2 * X^1"
# python3 checker.py "5.5 * X^0 + 7.2*X ^ 1= 4 * X^0 + 7.2 * X^1"
# echo "-------------"
# echo "The equation to solve: 5.5 * X^0 + 7.2*X ^1= 4 * X^0 + 7.2 * X^1"
# python3 checker.py "5.5 * X^0 + 7.2*X ^1= 4 * X^0 + 7.2 * X^1"
# echo "-------------"
# echo "The equation to solve: 5.5 * X^0 + 7.2*X^1= 4 * X^0 + 7.2 * X^1"
# python3 checker.py "5.5 * X^0 + 7.2*X^1= 4 * X^0 + 7.2 * X^1"
# echo "-------------"
# echo "The equation to solve: 5.5 * X^0 + 7.2*X^1= 4 * X^0"
# python3 checker.py "5.5 * X^0 + 7.2*X^1= 4 * X^0"
# echo "-------------"
# echo "The equation to solve: 6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1"
# python3 checker.py "6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1"
# echo "-------------"
# echo "The equation to solve: 5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1"
# python3 checker.py "5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1"
# echo "-------------"
# echo "The equation to solve: 5 * X^0 + 3 * X^1= 1 * X^0 + 0 * X^1 - 3 * X^2"
# python3 checker.py "5 * X^0 + 3 * X^1= 1 * X^0 + 0 * X^1 - 3 * X^2"
# echo "-------------"
# echo "The equation to solve: 3 * X^1= 1 * X^0 + 0 * X^1 - 3 * X^2"
# python3 checker.py "3 * X^1= 1 * X^0 + 0 * X^1 - 3 * X^2"
# echo "-------------"
# echo "The equation to solve: 3 * X^1= 1 * X^0 - 3 * X^2"
# python3 checker.py "3 * X^1= 1 * X^0 - 3 * X^2"
# echo "-------------"
# echo "The equation to solve: 1*X^-1 = 1*X^-1"
# python3 checker.py "1*X^-1 = 1*X^-1"
# echo "-------------"
# echo "The equation to solve: 1*X^1.5=1*X^1.5"
# python3 checker.py "1*X^1.5=1*X^1.5"
# echo "-------------"
# echo "The equation to solve: 1*X^1.5=1*X^1.a5"
# python3 checker.py "1*X^1.5=1*X^1.a5"
# echo "-------------"
# echo "The equation to solve: 1*X^1.5=1*X^1.5               "
# python3 checker.py "1*X^1.5=1*X^1.5               "
# echo "-------------"
# echo "The equation to solve: 1*X^1=1*X^1"
# python3 checker.py "1*X^1=1*X^1"
# echo "-------------"
# echo "The equation to solve: 1*X^1=1*X^1"
# python3 checker.py "1*X^1=1*X^1"
# echo "-------------"
# echo "The equation to solve: 1*X^1 -0 +0=1*X^1"
# python3 checker.py "1*X^1 -0 +0=1*X^1"
# echo "-------------"
# echo "The equation to solve: 1*X^1-0+0=1*X^1"
# python3 checker.py "1*X^1-0+0=1*X^1"
# echo "-------------"
# echo "The equation to solve: 1*X^1--0*X^0=1*X^1"
# python3 checker.py "1*X^1--0*X^0=1*X^1"
# echo "-------------"
# echo "The equation to solve: 1*X^1+++0*X^0=1*X^1"
# python3 checker.py "1*X^1+++0*X^0=1*X^1"
# echo "-------------"
# echo "The equation to solve: "
# python3 checker.py ""
# echo "-------------"
# echo "The equation to solve: ="
# python3 checker.py "="
# echo "-------------"
# echo "The equation to solve: ====="
# python3 checker.py "====="
# echo "-------------"
# echo "The equation to solve: 0*X^0=5*X^0="
# python3 checker.py "0*X^0=5*X^0="
# echo "-------------"
# echo "The equation to solve: 0*X^0=5*X^0"
# python3 checker.py "0*X^0=5*X^0"
