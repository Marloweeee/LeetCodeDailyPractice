# 1 (rand_X() - 1) �� Y + rand_Y() ==> ���Եȸ��ʵ�����[1, X * Y]��Χ�����������rand_XY()
# 2 ��M��N�ı�������rand_M()%N+1���Բ���[1,N]��Χ�������
# 3 ��M����N�ı���ʱ�����þܾ��������������ж�M=(rand_N()-1)*N+rand_N()�Ƿ���N�ı�����Χ�ڣ����򷵻�M%N+1


# The rand7() API is already defined for you.
def rand7():
    pass
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num=(rand7()-1)*7+rand7()# [1,49]
            if num<=40:
                return num%10+1
        