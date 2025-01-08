class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        import math
        
        # Factor out 2,3,5,7 from t.
        def factor_2_3_5_7(x):
            """Return (a,b,c,d, ok) where
               x = 2^a * 3^b * 5^c * 7^d * (possibly other prime factors).
               ok = False if there is a prime factor outside {2,3,5,7}.
            """
            a = b = c = d = 0
            for p, cnt in [(2,0), (3,0), (5,0), (7,0)]:
                while x % p == 0:
                    x //= p
                    if p == 2: a += 1
                    elif p == 3: b += 1
                    elif p == 5: c += 1
                    else: d += 1
            return (a, b, c, d, (x == 1))
        
        a, b, c, d, ok = factor_2_3_5_7(t)
        if not ok:
            return "-1"
        
        if t == 1:
            candidate = self._make_zero_free_ge(num)
            return candidate if candidate is not None else "-1"
            
        #    For convenience, store them in a small table.
        digit_factors = {
            1: (0,0,0,0),
            2: (1,0,0,0),
            3: (0,1,0,0),
            4: (2,0,0,0),  # 2^2
            5: (0,0,1,0),
            6: (1,1,0,0),  # 2 * 3
            7: (0,0,0,1),
            8: (3,0,0,0),  # 2^3
            9: (0,2,0,0),  # 3^2
        }
        
        min_len_factors = max(
            math.ceil(a/3),
            math.ceil(b/2),
            c,
            d
        )
        
        L_num = len(num)
        
        def can_cover(A, B, C, D, remain):
            # quick bounding: if we need A twos but each digit can supply at most 3 => 3*remain < A => can't do
            if 3*remain < A: return False
            if 2*remain < B: return False
            if 1*remain < C: return False
            if 1*remain < D: return False
            return True
        
        def dfs_build(i, L, A, B, C, D, prefix_ge, prefix_str, num_str):

            # If we used up all positions:
            if i == L:
                # if we have used up all prime-factor needs, we have a solution
                # "used up" means A<=0, B<=0, C<=0, D<=0.
                if A<=0 and B<=0 and C<=0 and D<=0:
                    return prefix_str
                else:
                    return None
            
            # Positions remaining (including i):
            remaining = L - i
            
            # Prune if even the best digits can't cover A,B,C,D in the remaining slots
            if not can_cover(A, B, C, D, remaining):
                return None
            
            # Decide the range of digits to try at this position
            low_digit = 1
            if (L == L_num) and (not prefix_ge) and (i < L_num):
                # Must be >= num_str[i]
                low_digit = max(low_digit, int(num_str[i]))
            
            for d in range(low_digit, 10):
                # Skip if d == 0 (not allowed anyway).
                # Sub-prime coverage:
                da, db, dc, dd = digit_factors[d]
                
                # New needs
                A2 = A - da
                B2 = B - db
                C2 = C - dc
                D2 = D - dd
                
                # We only need them to be >= 0 at the end, so it's okay if e.g. A2 < 0 mid-way
                # as that just means we've "over-covered" factor 2, which is fine. We'll check final.
                
                # Next prefix_ge?
                # We become prefix_ge if we place a digit > num_str[i] 
                # (and i < len(num_str), L==L_num).
                new_prefix_ge = prefix_ge
                if (not prefix_ge) and (L == L_num) and (i < L_num):
                    nd = int(num_str[i])
                    if d > nd:
                        new_prefix_ge = True
                
                # Recurse
                candidate = dfs_build(i+1, L, A2, B2, C2, D2, new_prefix_ge,
                                      prefix_str + str(d), num_str)
                if candidate is not None:
                    return candidate
            
            return None
        
        candidate_start = self._make_zero_free_ge(num)
        if candidate_start is None:
            # That means it's impossible to even find the next zero-free integer (all 9's etc.)
            return "-1"
        
        start_len = len(candidate_start)
        L_begin = max(start_len, min_len_factors)
        
        def solve_for_length(L, base_str):
            """
            If L == len(base_str), we must produce a zero-free number >= base_str.
            If L > len(base_str), no prefix constraint (we are definitely bigger).
            We'll do a standard DFS build with the prime coverage.
            """
            if L == len(base_str):
                # We must ensure result >= base_str
                return dfs_build(0, L, a, b, c, d, prefix_ge=False, prefix_str="", num_str=base_str)
            else:
                # No constraint from base_str => prefix_ge = True from start
                return dfs_build(0, L, a, b, c, d, prefix_ge=True, prefix_str="", num_str="")        
        
        # Try lengths from L_begin up to something like L_begin+50 
        # (in practice, you'd want to calibrate or find a reasoning to stop earlier).
        # If everything fails, return "-1".
        
        for length in range(L_begin, L_begin+60):
            # If length is huge, there's also a risk we can't do it, but let's just try.
            ans = solve_for_length(length, candidate_start)
            if ans is not None:
                return ans
        
        return "-1"
    
    def _make_zero_free_ge(self, s: str) -> str:
        """
        Given a decimal string s (no leading zeros guaranteed),
        return the smallest "zero-free" (digits 1..9) integer >= s as a string,
        or None if we cannot find one (e.g. s="999999...0" might push us to length+1).
        
        Basic approach:
         - scan from left to right;
         - if we see a '0', we have to increment some previous non-'9' digit 
           and set all subsequent digits to '1'.
         - watch out for carry over if everything was '9'.
        """
        arr = list(s)
        n = len(arr)
        
        # Step 1: If there's no '0', s is already zero-free => return s
        if '0' not in arr:
            return s
        
        # Step 2: Otherwise, find the leftmost '0' and try to fix it
        i = 0
        while i < n and arr[i] != '0':
            i += 1
        
        if i == n:
            # No zero found (redundant check, but safe)
            return s
        
        # We found the leftmost '0' at index i.
        # We need to increment some digit to the left of i that is < '9'.
        j = i - 1
        while j >= 0 and arr[j] == '9':
            j -= 1
        
        if j < 0:
            return "1" + ("1"*n)
        
        # Now arr[j] < '9'. So we can do arr[j] += 1, and all subsequent positions => '1'
        arr[j] = str(int(arr[j]) + 1)
        
        # For positions k in range(j+1, n), set them to '1'
        for k in range(j+1, n):
            arr[k] = '1'
        
        candidate = "".join(arr)
        
        if '0' in candidate:
            # Re-run recursively until no zeros
            return self._make_zero_free_ge(candidate)
        
        return candidate
        
