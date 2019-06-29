{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def isPalindrome(s):\n",
    "    if s==s[::-1]:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "    \n",
    "print(isPalindrome(\"python\"))\n",
    "print(isPalindrome(\"jalaj\"))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def countOfChars(str):\n",
    "    return len(str)\n",
    "countOfChars(\"Application\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def countDigits(n):\n",
    "    return len(n)\n",
    "countDigits(\"25410\")"
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
      "1\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "def countUpperCase(str):\n",
    "    cnt=0\n",
    "    lst=list(str)\n",
    "    for x in range(len(lst)):\n",
    "        if ord(lst[x])>=65 and ord(lst[x])<=90:\n",
    "            cnt=cnt+1\n",
    "    return cnt\n",
    "\n",
    "print(countUpperCase(\"Application\"))\n",
    "print(countUpperCase(\"TeST\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "item is found\n"
     ]
    }
   ],
   "source": [
    "def binarysearch(a,lindex,rindex,tarItem):\n",
    "    while(lindex<=rindex):\n",
    "        mid=lindex+(rindex-lindex)//2\n",
    "        if a[mid]==tarItem:\n",
    "            return mid\n",
    "        if a[mid]>tarItem:\n",
    "            rindex=mid-1\n",
    "        else:\n",
    "            lindex=mid+1\n",
    "    return -1\n",
    "\n",
    "list=[1,4,9,15,25,45,57,88,98]\n",
    "res=binarysearch(list,0,8,45)\n",
    "if(res!=-1):\n",
    "    print(\"item is found\")\n",
    "else:\n",
    "    print(\"item is not found\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 3 6 18 19 25 "
     ]
    }
   ],
   "source": [
    "def bubblesort(a):\n",
    "    for i in range(len(a)-1):\n",
    "        for j in range(len(a)-1):\n",
    "            if(a[j]>a[j+1]):\n",
    "                a[j],a[j+1]=a[j+1],a[j]\n",
    "    for i in range(len(a)):\n",
    "        print(a[i],end=\" \")\n",
    "       \n",
    "list=[19,1,25,6,18,3]        \n",
    "bubblesort(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "application\n",
      "application\n",
      "applicaton test\n",
      "        working\n",
      "        completed\n",
      "        list\n",
      "        strings\n",
      "        python\n"
     ]
    }
   ],
   "source": [
    "str=\"application\"\n",
    "print(str)\n",
    "str1='application'\n",
    "print(str1)\n",
    "str2=\"\"\"applicaton test\n",
    "        working\n",
    "        completed\n",
    "        list\n",
    "        strings\n",
    "        python\"\"\"\n",
    "print(str2)"
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
      "application\n",
      "str[0] = a\n",
      "str[1] = p\n",
      "str[-1] = n\n",
      "str[-3] = i\n",
      "str[1:5] = ppli\n",
      "str[:5] = appli\n",
      "str[:-5] = applic\n",
      "str[5:-2] = cati\n",
      "str[::-1] = noitacilppa\n"
     ]
    }
   ],
   "source": [
    "str=\"application\"\n",
    "print(str)\n",
    "print(\"str[0] =\",str[0])\n",
    "print(\"str[1] =\",str[1])\n",
    "print(\"str[-1] =\",str[-1])\n",
    "print(\"str[-3] =\",str[-3])\n",
    "print(\"str[1:5] =\",str[1:5])\n",
    "print(\"str[:5] =\",str[:5])\n",
    "print(\"str[:-5] =\",str[:-5])\n",
    "print(\"str[5:-2] =\",str[5:-2])\n",
    "print(\"str[::-1] =\",str[::-1])\n"
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
      "1 8 8 9 None\n",
      "1 5 2 0 None\n"
     ]
    }
   ],
   "source": [
    "def printDigits(str):\n",
    "    lst=list(str)\n",
    "    for x in range(len(lst)):\n",
    "        if ord(lst[x])>=48 and ord(lst[x])<=57:\n",
    "            print(lst[x],end=\" \")\n",
    "    \n",
    "print(printDigits(\"Application1889\"))\n",
    "print(printDigits(\"Te1520st\"))"
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
      "26\n"
     ]
    }
   ],
   "source": [
    "def sumofDigits(str):\n",
    "    sum=0\n",
    "    lst=list(str)\n",
    "    for x in range(len(lst)):\n",
    "        if ord(lst[x])>=48 and ord(lst[x])<=57:\n",
    "             sum=sum+ord(lst[x])-48\n",
    "    return sum\n",
    "print(sumofDigits(\"Application1889\"))"
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
      "16\n"
     ]
    }
   ],
   "source": [
    "def sumOnlyEvenDigits(str):\n",
    "    sum=0\n",
    "    lst=list(str)\n",
    "    for x in range(len(lst)):\n",
    "        if ord(lst[x])>=48 and ord(lst[x])<=57:\n",
    "            ac=ord(lst[x])-48\n",
    "            if(ac%2==0):\n",
    "                sum=sum+ac\n",
    "    return sum\n",
    "print(sumOnlyEvenDigits(\"application1889\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
