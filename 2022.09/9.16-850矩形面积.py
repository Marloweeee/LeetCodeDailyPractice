class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        hbound = set()
        for rect in rectangles:
            # �±߽�
            hbound.add(rect[1])
            # �ϱ߽�
            hbound.add(rect[3])

        hbound = sorted(hbound)
        m = len(hbound)
        # ��˼·���㷨���֡��� length ���鲢����Ҫ��ʽ�ش洢����
        # length[i] ����ͨ�� hbound[i+1] - hbound[i] �õ�
        seg = [0] * (m - 1)

        sweep = list()
        for i, rect in enumerate(rectangles):
            # ��߽�
            sweep.append((rect[0], i, 1))
            # �ұ߽�
            sweep.append((rect[2], i, -1))
        sweep.sort()

        ans = i = 0
        while i < len(sweep):
            j = i
            while j + 1 < len(sweep) and sweep[i][0] == sweep[j + 1][0]:
                j += 1
            if j + 1 == len(sweep):
                break

            # һ���Եش����һ����������ͬ�����ұ߽�
            for k in range(i, j + 1):
                _, idx, diff = sweep[k]
                left, right = rectangles[idx][1], rectangles[idx][3]
                for x in range(m - 1):
                    if left <= hbound[x] and hbound[x + 1] <= right:
                        seg[x] += diff

            cover = 0
            for k in range(m - 1):
                if seg[k] > 0:
                    cover += (hbound[k + 1] - hbound[k])
            ans += cover * (sweep[j + 1][0] - sweep[j][0])
            i = j + 1

        return ans % (10 ** 9 + 7)

