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
      "0    1\n",
      "1    3\n",
      "2    4\n",
      "3    5\n",
      "4    6\n",
      "5    7\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "a=pd.Series([1,3,4,5,6,7])\n",
    "print(a)"
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
      "0    1.0\n",
      "1    2.0\n",
      "2    3.0\n",
      "3    4.0\n",
      "4    NaN\n",
      "5    5.0\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a1=pd.Series([1,2,3,4,np.nan,5])\n",
    "print(a1)"
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
      "DatetimeIndex(['2019-06-01', '2019-06-02', '2019-06-03', '2019-06-04',\n",
      "               '2019-06-05', '2019-06-06', '2019-06-07', '2019-06-08',\n",
      "               '2019-06-09', '2019-06-10', '2019-06-11', '2019-06-12',\n",
      "               '2019-06-13', '2019-06-14', '2019-06-15', '2019-06-16',\n",
      "               '2019-06-17', '2019-06-18', '2019-06-19', '2019-06-20'],\n",
      "              dtype='datetime64[ns]', freq='D')\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "dates=pd.date_range('20190601',periods=20)\n",
    "print(dates)"
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
      "     A          B    c  D      E    F\n",
      "0  1.0 2019-06-01  1.0  3   test  foo\n",
      "1  1.0 2019-06-01  1.0  3  train  foo\n",
      "2  1.0 2019-06-01  1.0  3   test  foo\n",
      "3  1.0 2019-06-01  1.0  3  train  foo\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "a3=pd.DataFrame({'A':1.,\n",
    "                 'B':pd.Timestamp('20190601'),\n",
    "                 'c':pd.Series(1,index=list(range(4)),dtype='float32'),\n",
    "                 'D':np.array([3]*4,dtype='int32'),\n",
    "                 'E':pd.Categorical([\"test\",\"train\",\"test\",\"train\"]),\n",
    "                 'F':'foo'})\n",
    "print(a3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "a1=tt.Turtle()\n",
    "tt.forward(100)\n",
    "tt.done()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "a1=tt.Turtle()\n",
    "a1.forward(150)\n",
    "a1.right(90)\n",
    "a1.forward(150)\n",
    "a1.right(90)\n",
    "a1.forward(150)\n",
    "a1.right(90)\n",
    "a1.forward(150)\n",
    "a1.right(90)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "a1=tt.Turtle()\n",
    "a1.backward(150)\n",
    "a1.left(90)\n",
    "a1.backward(150)\n",
    "a1.left(90)\n",
    "a1.backward(150)\n",
    "a1.left(90)\n",
    "a1.backward(150)\n",
    "a1.left(90)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "a1=tt.Turtle()\n",
    "for x in range(40):\n",
    "    a1.forward(50)\n",
    "    a1.right(144)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "a1=tt.Turtle()\n",
    "for i in range(40):\n",
    "    a1.forward(i*10)\n",
    "    a1.right(144)\n",
    "\n",
    "tt.done()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "c1=tt.Turtle()\n",
    "c1.pencolor(\"blue\")\n",
    "for i in range(50):\n",
    "    c1.forward(50)\n",
    "    c1.left(123)\n",
    "c1.pencolor(\"red\")\n",
    "for i in range(50):\n",
    "    c1.forward(100)\n",
    "    c1.left(123)\n",
    "tt.done()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "colors=['red','blue','orange','green','yellow','purple']\n",
    "a1=tt.Turtle()\n",
    "for x in range(360):\n",
    "    a1.pencolor(colors[x%6])\n",
    "    a1.width(x/100+1)\n",
    "    a1.forward(x)\n",
    "    a1.left(59)\n",
    "tt.done()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tt\n",
    "a1=tt.Turtle()\n",
    "colors=['red','blue','orange','green','yellow','purple']\n",
    "dot_distance=10\n",
    "width=10\n",
    "height=15\n",
    "a1.penup()\n",
    "for x in range(height):\n",
    "    a1.pencolor(colors[x%6])\n",
    "    for i in range(width):\n",
    "        a1.dot()\n",
    "        a1.forward(dot_distance)\n",
    "    a1.forward(dot_distance*width)\n",
    "    a1.right(90)\n",
    "    a1.forward(dot_distance)\n",
    "    a1.left(90)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "ename": "Terminator",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTerminator\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-56-04ebb806db82>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m6\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 15\u001b[0;31m         \u001b[0mcircle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcircle_size\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     16\u001b[0m         \u001b[0mleft\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m60\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36mcircle\u001b[0;34m(radius, extent, steps)\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36mcircle\u001b[0;34m(self, radius, extent, steps)\u001b[0m\n\u001b[1;32m   1988\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_rotate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mw2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1989\u001b[0m         \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msteps\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1990\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mspeed\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mspeed\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1991\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_go\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ml\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1992\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mspeed\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36mspeed\u001b[0;34m(self, speed)\u001b[0m\n\u001b[1;32m   2172\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2173\u001b[0m             \u001b[0mspeed\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2174\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mspeed\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mspeed\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2175\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2176\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mcolor\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36mpen\u001b[0;34m(self, pen, **pendict)\u001b[0m\n\u001b[1;32m   2457\u001b[0m             self._shapetrafo = ( scx*ca, scy*(shf*ca + sa),\n\u001b[1;32m   2458\u001b[0m                                 -scx*sa, scy*(ca - shf*sa))\n\u001b[0;32m-> 2459\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_update\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2460\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2461\u001b[0m \u001b[0;31m## three dummy methods to be implemented by child class:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36m_update\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   2658\u001b[0m             \u001b[0;32mreturn\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2659\u001b[0m         \u001b[0;32melif\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_tracing\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2660\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_update_data\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2661\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_drawturtle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2662\u001b[0m             \u001b[0mscreen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_update\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m                  \u001b[0;31m# TurtleScreenBase\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36m_update_data\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   2644\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2645\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_update_data\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2646\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscreen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_incrementudc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2647\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscreen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_updatecounter\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2648\u001b[0m             \u001b[0;32mreturn\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36m_incrementudc\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   1290\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mTurtleScreen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_RUNNING\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1291\u001b[0m             \u001b[0mTurtleScreen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_RUNNING\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1292\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mTerminator\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1293\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_tracing\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1294\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_updatecounter\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTerminator\u001b[0m: "
     ]
    }
   ],
   "source": [
    "from turtle import *\n",
    "import random\n",
    "for n in range(50):\n",
    "    penup()\n",
    "    goto (random.randint(-400,400),random.randint(-400,400))\n",
    "    pendown()\n",
    "    red_amount=random.randint(0,30)/100.0\n",
    "    blue_amount=random.randint(50,100)/100.0\n",
    "    green_amount=random.randint(0,30)/100.0\n",
    "    pencolor((red_amount,blue_amount,green_amount))\n",
    "    circle_size=random.randint(10,40)\n",
    "    pensize(random.randint(4,6))\n",
    "     \n",
    "    for i in range(6):\n",
    "        circle(circle_size)\n",
    "        left(60)\n",
    "    \n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "from turtle import *\n",
    "def main():\n",
    "    colors=['red','orange','yellow','seagreen4','orchid4','royalblue1','dodgerblue']\n",
    "    reset()\n",
    "    Screen()\n",
    "    up()\n",
    "    goto(-320,-195)\n",
    "    width(90)\n",
    "    for pcolor in colors:\n",
    "        color(pcolor)\n",
    "        down()\n",
    "        forward(640)\n",
    "        up()\n",
    "        backward(640)\n",
    "        left(90)\n",
    "        forward(66)\n",
    "        right(90)\n",
    "       \n",
    "    width(55)\n",
    "    color('white')\n",
    "    goto(0,-170)\n",
    "    down()\n",
    "   \n",
    "    circle(170)\n",
    "    left(90)\n",
    "    forward(340)\n",
    "    up()\n",
    "    left(180)\n",
    "    forward(170)\n",
    "    right(45)\n",
    "    down()\n",
    "    forward(170)\n",
    "    up()\n",
    "    backward(170)\n",
    "    left(90)\n",
    "    down()\n",
    "    forward(170)\n",
    "    up()\n",
    "    goto(0,300)\n",
    "   \n",
    "if __name__=='__main__':\n",
    "    main()\n",
    "    mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "from turtle import *\n",
    "\n",
    "N=80\n",
    "\n",
    "def f(x):\n",
    "    return 3.9*x*(1-x)\n",
    "\n",
    "def g(x):\n",
    "    return 3.9*(x-x**2)\n",
    "\n",
    "def h(x):\n",
    "    return 3.9*x-3.9*x*x\n",
    "\n",
    "def jumpto(x,y):\n",
    "    penup()\n",
    "    goto(x,y)\n",
    "   \n",
    "def line(x1,y1,x2,y2):\n",
    "    jumpto(x1,y1)\n",
    "    pendown()\n",
    "    jumpto(x2,y2)\n",
    "   \n",
    "def coosys() :\n",
    "    line(-1,0,N+1,0)\n",
    "    line(0,-0-1,0,1.1)\n",
    "\n",
    "def plot(fun,start,color):\n",
    "    pencolor(color)\n",
    "    x=start\n",
    "    jumpto(0,x)\n",
    "    pendown()\n",
    "    dot(5)\n",
    "    for i in range(N):\n",
    "        x=fun(x)\n",
    "        goto(i+1,x)\n",
    "        dot(5)\n",
    "def main():\n",
    "    reset()\n",
    "    setworldcoordinates(-1.0,-1.0,N+1,1.1)\n",
    "    speed(0)\n",
    "    hideturtle()\n",
    "    coosys()\n",
    "    plot(f,0.35,\"blue\")\n",
    "    plot(g,0.35,\"green\")\n",
    "    plot(h,0.35,\"red\")\n",
    "   \n",
    "   \n",
    "    for s in range(100):\n",
    "        setworldcoordinates(0.5*s,-0.1,N+1,1.1)\n",
    "    return \"Done!!\"\n",
    "if __name__==\"__main__\":\n",
    "    main()\n",
    "    mainloop()\n",
    "    "
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
