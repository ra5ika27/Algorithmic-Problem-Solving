class Solution(object):
    def isRectangleCover(self, rectangles):
        corners = {}
        L, B, R, T, area = float('inf'), float('inf'), -float('inf'), -float('inf'), 0
        # L-left R-right B-bottom T-top

        def add_corner(point):
            if point in corners:
                corners[point] += 1
            else:
                corners[point] = 1

        for rectangle in rectangles:
            L, B, R, T = min(L, rectangle[0]), min(B, rectangle[1]), max(R, rectangle[2]), max(T, rectangle[3])
            x1, y1, x2, y2 = rectangle[:]
            area += (x2 - x1) * (y2 - y1)
            map(add_corner, [(x1, y1), (x2, y2), (x1, y2), (x2, y1)])

        temp_area = (T - B) * (R - L)
        if area != temp_area:
            return False

        regions = [(L, B), (R, T), (L, T), (R, B)]

        for region in regions:
            if region not in corners or corners[region] != 1:
                return False

        for corner in corners:
            if corners[corner] % 2 and corner not in regions:
                return False

        return True
