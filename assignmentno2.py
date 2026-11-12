{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b5128cc9-4212-4645-8549-3703cadcabf1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[24, 25, 26, 27, 28]\n",
      "['Asha', 'Ravi', 'Meera', 'Arjun', 'Priya']\n"
     ]
    }
   ],
   "source": [
    "age_list = [24, 25, 26, 27, 28]\n",
    "name_list = [\"Asha\", \"Ravi\", \"Meera\", \"Arjun\", \"Priya\"]\n",
    "\n",
    "print(age_list)\n",
    "print(name_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "a7bcc681-c0ea-473e-bba7-b3671ea42e58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Asha', 'Ravi', 'Meera', 'Arjun', 'priya', 'Yazhini']\n"
     ]
    }
   ],
   "source": [
    "name_list.append(\"Yazhini\")\n",
    "print(name_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "282136f8-5fa8-44d3-97f0-5536fcc200ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[30, 30, 30, 30, 30, 30, 30, 29, 29, 27, 26, 26, 26, 25]\n"
     ]
    }
   ],
   "source": [
    "age_list.insert(1, 30)\n",
    "print(age_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "8c1c585b-7327-4817-8f29-567bc0b4360f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Asha', 'Ravi', 'Meera', 'Arjun', 'priya']\n"
     ]
    }
   ],
   "source": [
    "name_list.remove(\"Yazhini\")\n",
    "print(name_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "569451c3-6ced-4dbc-8ab5-72f688183042",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24\n"
     ]
    }
   ],
   "source": [
    "popped=age_list.pop()\n",
    "print(popped)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "3b498eef-b378-4e23-b6bc-68b2416308aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[30, 30, 30, 30, 30, 29, 27, 26, 26, 25, 29, 30, 26]\n"
     ]
    }
   ],
   "source": [
    "age_list.extend([29, 30, 26])\n",
    "print(age_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "849b05fc-df50-430f-b596-8ab0987f1bb3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[30, 30, 30, 30, 30, 30, 29, 29, 27, 26, 26, 26, 25]\n"
     ]
    }
   ],
   "source": [
    "age_list.sort(reverse=True)\n",
    "print(age_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "9952609a-d695-46ec-be56-ad219b798bf4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "minimum age 25\n",
      "maximum age 30\n",
      "368\n"
     ]
    }
   ],
   "source": [
    "minimum_age=min(age_list)\n",
    "print('minimum age',minimum_age)\n",
    "maximum_age=max(age_list)\n",
    "print('maximum age',maximum_age)\n",
    "sum_of_all_ages=sum(age_list)\n",
    "print(sum_of_all_ages)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d047b4a-1600-4c7b-b320-293ffde9a529",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "ee82fbca-a50e-473e-ae2f-0997f1494763",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Asha', 'Ravi', 'Meera', 'Arjun', 'priya']\n"
     ]
    }
   ],
   "source": [
    "print(name_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "7cf99ee9-3bf8-4f21-883f-721796fa7a83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "priya\n"
     ]
    }
   ],
   "source": [
    "print(name_list[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "9553e426-760b-498c-8b3e-59d8ec430ad1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Meera', 'Arjun']\n"
     ]
    }
   ],
   "source": [
    "print(name_list[2:4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "f2c046a6-648f-46ca-9cd5-f3787f9b4ce0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['priya', 'Arjun', 'Meera', 'Ravi', 'Asha']\n"
     ]
    }
   ],
   "source": [
    "print(name_list[::-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "333dc8fb-e333-46cb-b446-087318f9b39a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "52490cbc-4b5a-497c-8524-09924c0f7434",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Asha': 85, 'Ravi': 78, 'Meera': 92, 'Arjun': 67, 'Priya': 88}\n"
     ]
    }
   ],
   "source": [
    "student_marks = {\"Asha\": 85, \"Ravi\": 78, \"Meera\": 92, \"Arjun\": 67, \"Priya\": 88}\n",
    "print(student_marks)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "0307e137-622a-431d-88ea-f29767a52598",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Meera's mark: 92\n"
     ]
    }
   ],
   "source": [
    "print(\"Meera's mark:\", student_marks[\"Meera\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "33071795-9f51-4b06-a17e-8b0e13ae56fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Asha': 85, 'Ravi': 78, 'Meera': 92, 'Arjun': 67, 'Priya': 88, 'Janani': 80}\n"
     ]
    }
   ],
   "source": [
    "student_marks[\"Janani\"] = 80\n",
    "print(student_marks)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "a3468e57-7526-44b1-9fec-84e177d78a62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Asha': 85, 'Ravi': 82, 'Meera': 92, 'Arjun': 67, 'Priya': 88, 'Janani': 80}\n"
     ]
    }
   ],
   "source": [
    "student_marks[\"Ravi\"] = 82\n",
    "print(student_marks)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "46762ae3-7f67-4708-9f84-26b4a77b17da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['Asha', 'Ravi', 'Meera', 'Arjun', 'Priya', 'Janani'])\n"
     ]
    }
   ],
   "source": [
    "print(student_marks.keys())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "7190f5d0-a9ca-440a-807f-61190c11c20f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_values([85, 82, 92, 67, 88, 80])\n"
     ]
    }
   ],
   "source": [
    "print(student_marks.values())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "e401b9c5-b8c5-4836-b4d6-80d6f276f968",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_items([('Asha', 85), ('Ravi', 82), ('Meera', 92), ('Arjun', 67), ('Priya', 88), ('Janani', 80)])\n"
     ]
    }
   ],
   "source": [
    "print(student_marks.items())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "841b5adf-1f8a-4d0d-b1b4-4dff176697bf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "b49a0a32-b100-43e3-aa9d-38e026210001",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'o', 'e', 'a', 'i', 'u'}\n"
     ]
    }
   ],
   "source": [
    "my_set=set([\"a\",\"e\",\"i\",\"o\",\"u\",\"a\",\"a\",\"i\"])\n",
    "print(my_set)\n",
    "#### In case of sets duplicate values are dropped from the set which gives more precise data ."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "d327be18-d734-44f6-a1e1-9e96d52c1807",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'set' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[64]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m my_set[\u001b[32m4\u001b[39m] = \u001b[33m's'\u001b[39m\n\u001b[32m      2\u001b[39m print(my_set)\n\u001b[32m      3\u001b[39m \u001b[38;5;66;03m#### As sets are unordered , it doesn't have an index.so it is impossible to do indexing and slicing in the set\u001b[39;00m\n",
      "\u001b[31mTypeError\u001b[39m: 'set' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "my_set[4] = 's'\n",
    "print(my_set)\n",
    "#### As sets are unordered , it doesn't have an index.so it is impossible to do indexing and slicing in the set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "25edb739-1ce6-40ec-89db-634267707038",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 3, 5, 7, 9}\n",
      "{2, 3, 5, 8, 10}\n"
     ]
    }
   ],
   "source": [
    "set1 = {1, 3, 5, 7, 9}\n",
    "set2 = {2, 3, 5, 8, 10}\n",
    "print(set1)\n",
    "print(set2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "ce4037ac-23eb-4bbc-ade6-55cc17fa1bc8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 5, 7, 8, 9, 10}\n"
     ]
    }
   ],
   "source": [
    "print(set1.union(set2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "9c081eee-bb2d-4f9c-81c0-5d8ed408dc07",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your score (0 to 10):  9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Performance Category: Above Average\n",
      "Excellent work! Keep up the great performance.\n"
     ]
    }
   ],
   "source": [
    "score = float(input(\"Enter your score (0 to 10): \"))\n",
    "\n",
    "if score < 0 or score > 10:\n",
    "    print(\"Invalid score. Please enter a value between 0 and 10.\")\n",
    "\n",
    "elif score > 7:\n",
    "    print(\"Performance Category: Above Average\")\n",
    "    print(\"Excellent work! Keep up the great performance.\")\n",
    "\n",
    "elif score >= 4 and score <= 7:\n",
    "    print(\"Performance Category: Average\")\n",
    "    print(\"Good effort! A little more focus can take you to the next level.\")\n",
    "\n",
    "else:\n",
    "    print(\"Performance Category: Below Average\")\n",
    "    print(\"Need to improve your performance, consistent practice will lead to better results.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47ba3c08-8793-47c1-8935-8526fc1109ed",
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
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
