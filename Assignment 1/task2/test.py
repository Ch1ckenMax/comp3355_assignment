from __future__ import print_function

from copy import copy
import json
import short_key

class Tester:
    def __init__(self):
        with open("./students_number.txt", "r") as f:
            self.student_ids = list()
            for line in f.readlines():
                self.student_ids.append(line.strip())
        
        with open("./student_pub_keys.json", "r") as f:
            self.pub_keys = json.load(f)

        with open("./student_priv_keys.json", "r") as f:
            self.priv_keys = json.load(f)

    def test_one_student(self):
        student_id = short_key.get_student_number()

        if student_id not in self.student_ids:
            print("Your student id is not valid!")
            return -1
        
        tmp_N = int(self.pub_keys[student_id]["N"], 16)
        tmp_e = int(self.pub_keys[student_id]["e"], 16)

        tmp_p, tmp_q = short_key.get_factors(tmp_N)
        print("Your p and q are: p -> {}, q -> {}".format(hex(tmp_p), hex(tmp_q)))

        p_and_q = [int(self.priv_keys[student_id]["p"], 16), int(self.priv_keys[student_id]["q"], 16)]
        
        if tmp_p not in p_and_q or \
                tmp_q not in p_and_q:

            print("The p & q are wrong!")
            print("The correct ones should be: p -> {}, q -> {}".format( \
                self.priv_keys[student_id]["p"], \
                self.priv_keys[student_id]["q"]))
            return 0

        print("The p & q are correct!\n")
        tmp_d = short_key.get_private_key_from_p_q_e(tmp_p, tmp_q, tmp_e)
        print("The private key is: {}".format(tmp_d))
        if tmp_d != int(self.priv_keys[student_id]["d"], 16):
            print("The private key is wrong!")
            print("The correct one should be: {}".format(self.priv_keys[student_id]["d"]))
            return 1
        print("The private key is correct!\n")
        return 2

if __name__ == "__main__":
    test = Tester() 
    test.test_one_student()

