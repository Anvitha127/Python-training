{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The number is less than 15\n"
     ]
    }
   ],
   "source": [
    "x=10;\n",
    "if(x<15):\n",
    "  print(\"The number is less than 15\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=10;\n",
    "if(x>15):\n",
    "  print(\"Hello\");  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Good Afternoon\n"
     ]
    }
   ],
   "source": [
    "x=10;\n",
    "if(x>15):\n",
    "  print(\"Hello Good Morning\");\n",
    "else:\n",
    "  print(\"Hello Good Afternoon\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "y is large number\n"
     ]
    }
   ],
   "source": [
    "x=10;\n",
    "y=15;\n",
    "if(x<y):\n",
    "  print(\"y is large number\");\n",
    "else:\n",
    "  print(\"y is small number\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "z is large number\n"
     ]
    }
   ],
   "source": [
    "x=10;\n",
    "y=20;\n",
    "z=30;\n",
    "if(x>y and x>z):\n",
    "  print(\"x is large number\");\n",
    "elif(y>x and y>z):\n",
    "  print(\"y is large number\");\n",
    "else:\n",
    "  print(\"z is large number\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "its zero\n"
     ]
    }
   ],
   "source": [
    "x=0;\n",
    "if(x<0):\n",
    "  print(\"its negative number\");\n",
    "elif(x>0):\n",
    "  print(\"its positive number\");\n",
    "elif(x==0):\n",
    "  print(\"its zero\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "n=1;\n",
    "while(n<=10):\n",
    "    print(n);\n",
    "    n=n+1;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "9\n",
      "8\n",
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "n=10;\n",
    "while(n>=1):\n",
    "    print(n);\n",
    "    n=n-1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n",
      "23\n",
      "24\n",
      "25\n",
      "26\n",
      "27\n",
      "28\n",
      "29\n",
      "30\n",
      "31\n",
      "32\n",
      "33\n",
      "34\n",
      "35\n",
      "36\n",
      "37\n",
      "38\n",
      "39\n",
      "40\n",
      "41\n",
      "42\n",
      "43\n",
      "44\n",
      "45\n"
     ]
    }
   ],
   "source": [
    "n=22;\n",
    "while(n<=45):\n",
    "    print(n)\n",
    "    n=n+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter lower limit1\n",
      "enter upper limit100\n",
      "2450\n"
     ]
    }
   ],
   "source": [
    "x=int(input(\"enter lower limit\"));\n",
    "y=int(input(\"enter upper limit\"));\n",
    "sum=0;\n",
    "while(x!=y):\n",
    "    if(x%2==0):\n",
    "        sum=sum+x;\n",
    "    x=x+1;\n",
    "print(sum);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number145\n",
      "5\n",
      "4\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "x=int(input(\"enter a number\"));\n",
    "while(x!=0):\n",
    "    r=x%10;\n",
    "    print(r);\n",
    "    x=x//10;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number1951\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "x=int(input(\"enter a number\"))\n",
    "sum=0\n",
    "while(x!=0):\n",
    "    r=x%10;\n",
    "    if(r%2==0):\n",
    "      sum=sum+r;\n",
    "    x=x//10;\n",
    "print(sum);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number9876543210\n",
      "zero\n",
      "one\n",
      "two\n",
      "three\n",
      "four\n",
      "five\n",
      "six\n",
      "seven\n",
      "eight\n",
      "nine\n"
     ]
    }
   ],
   "source": [
    "x=int(input(\"enter a number\"))\n",
    "while(x!=0):\n",
    "  r=x%10;\n",
    "  if(r==0):\n",
    "    print(\"zero\");\n",
    "  elif(r==1):\n",
    "    print(\"one\");\n",
    "  elif(r==2):\n",
    "    print(\"two\");\n",
    "  elif(r==3):\n",
    "    print(\"three\");\n",
    "  elif(r==4):\n",
    "    print(\"four\");\n",
    "  elif(r==5):\n",
    "    print(\"five\");\n",
    "  elif(r==6):\n",
    "    print(\"six\"); \n",
    "  elif(r==7):\n",
    "    print(\"seven\");\n",
    "  elif(r==8):\n",
    "    print(\"eight\"); \n",
    "  elif(r==9):\n",
    "    print(\"nine\");  \n",
    "  x=x//10;  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number5\n",
      "Enter Lower Limit50\n",
      "Enter Upper Limit65\n"
     ]
    }
   ],
   "source": [
    "digit=int(input(\"enter a number\"))\n",
    "l1=int(input(\"Enter Lower Limit\"))\n",
    "l2=int(input(\"Enter Upper Limit\"))\n",
    "\n",
    "cnt=0;\n",
    "\n",
    "while(l1!=l2):\n",
    "  buffer=l1;\n",
    "  while(l1!=l2):\n",
    "    r=l1%10;\n",
    "    if(r==digit):\n",
    "      cnt=cnt+1;\n",
    "    l1=l1/10;\n",
    "  l1=buffer;\n",
    "  l1=l1+1;\n",
    "    \n",
    "print(cnt);    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "x,y,z=6,60,65\n",
    "count=0\n",
    "while(y<z):\n",
    "    t=y+1\n",
    "    while t>0:\n",
    "        r=t%10\n",
    "        if r==x:\n",
    "            count=count+1\n",
    "        t=t//10\n",
    "    y=y+1\n",
    "print(count)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "x,y,z=6,60,65\n",
    "count=0\n",
    "while(y<=z):\n",
    "    t=y+1\n",
    "    while t>0:\n",
    "        r=t%10\n",
    "        if r==x:\n",
    "            count=count+1\n",
    "        t=t//10\n",
    "    y=y+1\n",
    "print(count)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 5 6 7 8 9 \n",
      "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 \n"
     ]
    }
   ],
   "source": [
    "def printNNaturalNumbers(n):\n",
    "    cnt=1;\n",
    "    while(cnt<=n):\n",
    "        print(cnt,end=\" \");\n",
    "        cnt=cnt+1;\n",
    "    print()\n",
    "    return\n",
    "printNNaturalNumbers(9);\n",
    "printNNaturalNumbers(15);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n",
      "3628800\n",
      "2432902008176640000\n"
     ]
    }
   ],
   "source": [
    "def findFact(n):\n",
    "    fact=1;\n",
    "    while(n!=0):\n",
    "        fact=fact*n;\n",
    "        n=n-1;\n",
    "    return fact;\n",
    "    \n",
    "print(findFact(5));\n",
    "print(findFact(10));\n",
    "print(findFact(20));"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def countofPalindromes(n1,n2):\n",
    "    cnt=0;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
