{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "838b626c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Convertpostive(n,m):\n",
    "    Square = pow((n-m),2)\n",
    "    return pow(Square,0.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "7910055f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def partition(n,k,a):\n",
    "    output = {}\n",
    "    for item in n:\n",
    "        na = Convertpostive(item,a[0])\n",
    "        kgroup = 1\n",
    "        l = len(a)\n",
    "\n",
    "        for j in range(1,l):\n",
    "            na_temp = Convertpostive(item,a[j])\n",
    "            if(na_temp < na ):\n",
    "                na = na_temp\n",
    "                kgroup = j+1\n",
    "        if kgroup not in output:\n",
    "            output[kgroup] = [item]\n",
    "        else:\n",
    "            l = output[kgroup]\n",
    "            l.append(item)\n",
    "            output[kgroup] = l\n",
    "    return output\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "fdc32fb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def kclustering(n,k,a):\n",
    "    outputtable = {}\n",
    "    foutput = partition(n,k,a)\n",
    "    print(foutput)\n",
    "    outputtable[1] = foutput\n",
    "    flag = False\n",
    "    i = 1\n",
    "    while(flag == False):\n",
    "        loutput = outputtable[i]\n",
    "        a = []\n",
    "        print(\"\")\n",
    "        for key in loutput:\n",
    "            l = loutput[key]\n",
    "            a.append(sum(l)/len(l))\n",
    "        for i in range(0,len(a)):\n",
    "            print(\"m\"+str(i+1)+\": \"+str(a[i]))\n",
    "        output = partition(n,k,a)\n",
    "        print(output)\n",
    "        i = i + 1\n",
    "        outputtable[i] = output\n",
    "        flag = True\n",
    "        for key in loutput:\n",
    "            if(loutput[key] != output[key]):\n",
    "                flag = False\n",
    "                break\n",
    "        print(flag)\n",
    "    return outputtable[i]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "5bde479b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: [15, 15, 16, 19, 19, 20, 20], 3: [21, 22, 28], 2: [35, 40, 41, 42, 43, 44, 60, 61, 65]}\n",
      "\n",
      "m1: 17.714285714285715\n",
      "m2: 23.666666666666668\n",
      "m3: 47.888888888888886\n",
      "{1: [15, 15, 16, 19, 19, 20, 20], 2: [21, 22, 28, 35], 3: [40, 41, 42, 43, 44, 60, 61, 65]}\n",
      "False\n",
      "\n",
      "m1: 17.714285714285715\n",
      "m2: 26.5\n",
      "m3: 49.5\n",
      "{1: [15, 15, 16, 19, 19, 20, 20, 21, 22], 2: [28, 35], 3: [40, 41, 42, 43, 44, 60, 61, 65]}\n",
      "False\n",
      "\n",
      "m1: 18.555555555555557\n",
      "m2: 31.5\n",
      "m3: 49.5\n",
      "{1: [15, 15, 16, 19, 19, 20, 20, 21, 22], 2: [28, 35, 40], 3: [41, 42, 43, 44, 60, 61, 65]}\n",
      "False\n",
      "\n",
      "m1: 18.555555555555557\n",
      "m2: 34.333333333333336\n",
      "m3: 50.857142857142854\n",
      "{1: [15, 15, 16, 19, 19, 20, 20, 21, 22], 2: [28, 35, 40, 41, 42], 3: [43, 44, 60, 61, 65]}\n",
      "False\n",
      "\n",
      "m1: 18.555555555555557\n",
      "m2: 37.2\n",
      "m3: 54.6\n",
      "{1: [15, 15, 16, 19, 19, 20, 20, 21, 22], 2: [28, 35, 40, 41, 42, 43, 44], 3: [60, 61, 65]}\n",
      "False\n",
      "\n",
      "m1: 18.555555555555557\n",
      "m2: 39.0\n",
      "m3: 62.0\n",
      "{1: [15, 15, 16, 19, 19, 20, 20, 21, 22, 28], 2: [35, 40, 41, 42, 43, 44], 3: [60, 61, 65]}\n",
      "False\n",
      "\n",
      "m1: 19.5\n",
      "m2: 40.833333333333336\n",
      "m3: 62.0\n",
      "{1: [15, 15, 16, 19, 19, 20, 20, 21, 22, 28], 2: [35, 40, 41, 42, 43, 44], 3: [60, 61, 65]}\n",
      "True\n",
      "\n",
      " Output :  {1: [15, 15, 16, 19, 19, 20, 20, 21, 22, 28], 2: [35, 40, 41, 42, 43, 44], 3: [60, 61, 65]}\n"
     ]
    }
   ],
   "source": [
    "n=[15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]\n",
    "k = int(input(\"enter the k: \"))\n",
    "a = []\n",
    "for i in range(0,k):\n",
    "    temp = int(input(\"enter m\"+str(i+1)+\": \"))\n",
    "    a.append(temp)\n",
    "output = kclustering(n,k,a)\n",
    "\n",
    "print(\"\\n Output : \", output)"
   ]
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "7ae0aef52bef687a3c48202339f3a6d3f7667471f22019098c9e93c6041c6fc2"
  },
  "kernelspec": {
   "display_name": "Python 3.9.7 ('base')",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
