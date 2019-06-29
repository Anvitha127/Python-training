{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "file is created successfully and data is written\n"
     ]
    }
   ],
   "source": [
    "def createfile(filename):\n",
    "    f=open(filename,\"w\")\n",
    "    for i in range(10):\n",
    "        f.write(\"This is %d line\\n\"%i)\n",
    "    print(\"file is created successfully and data is written\")\n",
    "    f.close()\n",
    "    return\n",
    "createfile(\"file.txt\")"
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
      "this is 0 line\n",
      "this is 1 line\n",
      "this is 2 line\n",
      "this is 3 line\n",
      "this is 4 line\n",
      "this is 5 line\n",
      "this is 6 line\n",
      "this is 7 line\n",
      "this is 8 line\n",
      "this is 9 line\n",
      "\n"
     ]
    }
   ],
   "source": [
    "def readfile(filename):\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        print(x)\n",
    "    f.close()\n",
    "    return\n",
    "readfile(\"file.txt\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "150\n"
     ]
    }
   ],
   "source": [
    "def countcharacter(filename):\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        lst=list(x)\n",
    "    return len(lst)\n",
    "print(countcharacter(\"file.txt\"))"
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
      "0\n"
     ]
    }
   ],
   "source": [
    "def dataanalysiswordcount(filename,word):\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        lst=x.split()\n",
    "    cnt=lst.count(word)\n",
    "    return cnt\n",
    "print(dataanalysiswordcount(\"file.txt\",\"rest\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def uppercasecount(filename):\n",
    "    cntupper=0\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        lst=list(x)\n",
    "    for i in lst:\n",
    "        if i.isupper():\n",
    "            cntupper+=1\n",
    "    return cntupper\n",
    "uppercasecount(\"file.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['This is 0 line',\n",
       " 'This is 1 line',\n",
       " 'This is 2 line',\n",
       " 'This is 3 line',\n",
       " 'This is 4 line',\n",
       " 'This is 5 line',\n",
       " 'This is 6 line',\n",
       " 'This is 7 line',\n",
       " 'This is 8 line',\n",
       " 'This is 9 line',\n",
       " '']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def countoflines(filename):\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        lst=x.split(\"\\n\")\n",
    "    return lst\n",
    "countoflines(\"file.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def countoflines(filename):\n",
    "    f=open(filename,\"r\")\n",
    "    if f.mode==\"r\":\n",
    "        x=f.read()\n",
    "        lst=x.split(\"\\n\")\n",
    "    return len(lst)\n",
    "countoflines(\"file.txt\")"
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
      "This is 0 line\r\n",
      "This is 1 line\r\n",
      "This is 2 line\r\n",
      "This is 3 line\r\n",
      "This is 4 line\r\n",
      "This is 5 line\r\n",
      "This is 6 line\r\n",
      "This is 7 line\r\n",
      "This is 8 line\r\n",
      "This is 9 line\r\n"
     ]
    }
   ],
   "source": [
    "cat file.txt\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "def phonenumbervalidate(phone):\n",
    "    pattern='[6-9][0-9]{9}$'\n",
    "    phone=str(phone)\n",
    "    if re.match(pattern,phone):\n",
    "        return True\n",
    "    return False\n",
    "print(phonenumbervalidate(9966335588))\n",
    "print(phonenumbervalidate(99663355))\n",
    "\n",
    "    "
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
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "def validaterollnumber(number):\n",
    "        number=str(number)\n",
    "        pattern=\"^[1][5][2][U][1][A][0][1-9][0-9]$\"\n",
    "        if re.match(pattern,number):\n",
    "            return True\n",
    "        return False\n",
    "print(validaterollnumber(\"152U1A0555\"))\n",
    "print(validaterollnumber(\"152U1A0485\"))\n",
    "\n",
    "    "
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
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "def validatepassword(s):\n",
    "    pattern=\"^[a-zA-Z0-9!@#$]{6,15}$\"\n",
    "    if re.match(pattern,s):\n",
    "        return True\n",
    "    return False\n",
    "print(validatepassword(\"Anil1889@21#M\"))\n",
    "print(validatepassword(\"$anil.1889@21#M1111111222222\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "def validateemailid(email):\n",
    "    pattern=\"\"\"[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}\"\"\"\n",
    "    if re.match(pattern,email):\n",
    "        return True\n",
    "    return False\n",
    "print(validateemailid(\"anil.1889@gmail.com\"))\n",
    "print(validateemailid(\"$anil.1889@gmail.com\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
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
