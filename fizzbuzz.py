{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "48448fac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nhap so 2 so bat ki:5 25\n",
      "['5', '25']\n",
      "Buzz\n",
      "Fizz\n",
      "khong thuoc truong hop tren:gt bien lap la:  7\n",
      "khong thuoc truong hop tren:gt bien lap la:  8\n",
      "Fizz\n",
      "Buzz\n",
      "khong thuoc truong hop tren:gt bien lap la:  11\n",
      "Fizz\n",
      "khong thuoc truong hop tren:gt bien lap la:  13\n",
      "khong thuoc truong hop tren:gt bien lap la:  14\n",
      "FizzBuzz\n",
      "khong thuoc truong hop tren:gt bien lap la:  16\n",
      "khong thuoc truong hop tren:gt bien lap la:  17\n",
      "Fizz\n",
      "khong thuoc truong hop tren:gt bien lap la:  19\n",
      "Buzz\n",
      "Fizz\n",
      "khong thuoc truong hop tren:gt bien lap la:  22\n",
      "khong thuoc truong hop tren:gt bien lap la:  23\n",
      "Fizz\n",
      "Buzz\n"
     ]
    }
   ],
   "source": [
    "number=input(\"nhap so 2 so bat ki:\")\n",
    "\n",
    "num_split=number.split()\n",
    "startnum=int(num_split[0])\n",
    "endnum=int(num_split[1])\n",
    "print(num_split)\n",
    "\n",
    "\n",
    "\n",
    "if startnum> endnum:\n",
    "    \n",
    "    print(\" so bat dau phai nho hon so ket thuc\")\n",
    "else :\n",
    "   \n",
    "    for i in range(startnum,endnum+1):\n",
    "   \n",
    "        if i%3==0 and i%5==0:\n",
    "            print(\"FizzBuzz\")\n",
    "        elif i%3==0:\n",
    "            print(\"Fizz\")\n",
    "        elif i%5==0:\n",
    "            print(\"Buzz\")\n",
    "        else:\n",
    "            print(\"khong thuoc truong hop tren:gt bien lap la: \",i)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88715351",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c29d561",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
